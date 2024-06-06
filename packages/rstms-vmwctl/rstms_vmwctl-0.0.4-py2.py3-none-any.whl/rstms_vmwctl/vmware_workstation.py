import requests
import subprocess
import tempfile
import json
from pathlib import Path

class Client():
    def __init__(self, host, url, username, password, verbose, vm_path, router): 
        self.host = host
        self.url = url
        self.username = username
        self.password = password
        self.verbose = verbose
        self.router = router 
        self.vm = {}
        self.vm_path = vm_path

    def _result(self, result):
        result.raise_for_status()
        if result.text:
            ret = result.json()
        else:
            ret = None
        return ret

    def run(self, cmd):
        proc = subprocess.run(['ssh', self.host] + cmd, text=True, check=True, capture_output=True)
        return proc.stdout.strip()

    def get(self, path):
        return self._result(requests.get(f"{self.url}/api/{path}", auth=(self.username, self.password)))

    def delete(self, path):
        return self._result(requests.delete(f"{self.url}/api/{path}", auth=(self.username, self.password)))

    def put(self, path, data):
        return self._result(requests.put(
            f"{self.url}/api/{path}", 
            auth=(self.username, self.password), 
            headers={'Content-Type': 'application/vnd.vmware.vmw.rest-v1+json'},
            data=data.encode()
            ))

    def post(self, path, data):
        return self._result(requests.post(
            f"{self.url}/api/{path}", 
            auth=(self.username, self.password), 
            headers={'Content-Type': 'application/vnd.vmware.vmw.rest-v1+json'},
            json=data
            ))

    def get_vms(self, vm_name=None):
        self.vm = {}
        vms = self.get('vms')
        for vm in vms:
            name, _, _ = vm['path'].split('\\')[-1].partition('.')
            self.vm[name] = vm
        if vm_name:
            return self.vm[vm_name]
        return self.vm

    def get_vm_id(self, name):
        vm = self.get_vms(name)
        return vm['id']

    def set_power(self, name, operation):
        vid = self.get_vm_id(name)
        return self.put(f"vms/{vid}/power", operation)

    def get_power(self, name):
        vid = self.get_vm_id(name)
        return self.get(f"vms/{vid}/power")

    def get_vm_ip(self, name):
        vid = self.get_vm_id(name)
        ret = self.get(f"vms/{vid}/nic")
        mac = ret['nics'][0]['macAddress']
        arp_table = subprocess.run(['ssh', self.router, 'arp', '-an'], text=True, capture_output=True, check=True).stdout.strip().split('\n')
        if mac:
            for arp in arp_table:
                if mac in arp:
                    address, _, _ = arp.partition(' ')
                    return address
            raise RuntimeError(f"mac address {mac} not found in ARP table on {self.router}")
        else:
            return None


    def create(self, name, cpu_count, ram_size, disk_size, iso_path):
        self.get_vms()
        if name in self.vm:
            raise RuntimeError(f"VM '{name}' exists")
        ret = {}
        dirs = []
        for dir in self.run(['find', self.vm_path, '-type', 'd', '-maxdepth', '1']).split('\n'):
            dirs.append(Path(dir).name)
        if name in dirs:
            raise RuntimeError('vm directory exists')
        self.run(['mkdir', f"{ self.vm_path }/{ name }"])
        with tempfile.NamedTemporaryFile() as vmxtemp:
            vmxfile = Path(vmxtemp.name)
            vmxfile.write_text(f"""config.version = "8"
virtualHW.version = "12"
numvcpus = "{ cpu_count }"
memsize = "{ ram_size }"
ide0:0.present = "TRUE"
ide0:0.fileName = "{name}.vmdk"
ide1:0.present = "TRUE"
ide1:0.fileName = "{ iso_path }"
ide1:0.deviceType = "cdrom-image"
ethernet0.present = "TRUE"
ethernet0.displayName = "VMnet0"
ethernet0.connectionType = "custom"
ethernet0.vnet = "VMnet0"
displayName = "{ name }"
guestOS = "debian11-64"
"""
            )
            dest=f"{self.host}:{self.vm_path}/{name}/{name}.vmx"
            subprocess.run(['scp', str(vmxfile), dest], check=True, capture_output=True)
        self.run(["sh", "-c", f"'cd {self.vm_path}/{name} && vmware-vdiskmanager -c -s {disk_size}MB -a ide -t 0 {name}.vmdk'"])
        self.get_vms()
        if not name in self.vm:
            ret = self.post("vms/registration", data=dict(name=name, path=f"H:\\vmware\\{name}\\{name}.vmx"))
        return ret

    def destroy(self, name):
        vid = self.get_vm_id(name)
        ret = self.delete(f'/vms/{vid}')
        self.run(["sh", "-c", f"'cd {self.vm_path} && rm -rf {name}'"])
        return ret
