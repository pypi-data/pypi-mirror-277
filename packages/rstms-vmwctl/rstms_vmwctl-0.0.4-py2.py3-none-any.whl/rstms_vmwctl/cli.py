"""Console script for rstms_vmwctl."""

import sys
import json
from pathlib import Path

import click
import click.core

from .exception_handler import ExceptionHandler
from .shell import _shell_completion
from .version import __timestamp__, __version__

from .vmware_workstation import Client


header = f"vmctl v{__version__} {__timestamp__}"


def _ehandler(ctx, option, debug):
    ctx.obj = dict(ehandler=ExceptionHandler(debug))
    ctx.obj["debug"] = debug

def fail(msg):
    click.echo(f"vmwctl: {msg}", err=True)
    sys.exit(-1)

def output(obj, exit=0):
    click.echo(json.dumps(obj, indent=2))
    sys.exit(exit)


@click.group("vmctl", context_settings={"auto_envvar_prefix": "VMWCTL"})
@click.version_option(message=header)
@click.option("-d", "--debug", is_eager=True, is_flag=True, callback=_ehandler, help="debug mode")
@click.option('-h', '--host', envvar='VMCTL_HOST')
@click.option('-u', '--url', envvar='VMCTL_URL')
@click.option('-U', '--username', envvar='VMCTL_USERNAME')
@click.option('-P', '--password', envvar='VMCTL_PASSWORD')
@click.option('-r', '--router', envvar='VMCTL_ROUTER')
@click.option('--path', default='/cygdrive/h/vmware', envvar='VMCTL_PATH')
@click.option('-v', '--verbose', is_flag=True)
@click.option(
    "--shell-completion",
    is_flag=False,
    flag_value="[auto]",
    callback=_shell_completion,
    help="configure shell completion",
)
@click.pass_context
def cli(ctx, debug, shell_completion, host, url, username, password, verbose, path, router):
    """vmctl top-level help"""
    ctx.obj=Client(host, url, username, password, verbose, path, router)

@cli.command('list')
@click.pass_obj
def _list(ctx):
    """list VMs"""
    vms = ctx.get_vms()
    if not ctx.verbose:
        vms = list(vms.keys())
    output(vms)

@cli.command
@click.argument('name')
@click.pass_obj
def settings(ctx, name):
    """VM settings"""
    if not ctx.vm:
        ctx.get_vms()
    vm = ctx.vm.get(name, None)
    if not vm:
        fail(f"unknown VM '{name}'")

    config = ctx.get(f"vms/{vm['id']}")
    output(config)

@cli.command
@click.argument('name')
@click.pass_obj
def params(ctx, name):
    """VM params"""
    if not ctx.vm:
        ctx.get_vms()
    vm = ctx.vm.get(name, None)
    if not vm:
        fail(f"unknown VM '{name}'")

    config = ctx.get(f"vms/{vm['id']}/params")
    output(config)

@cli.command
@click.argument('name')
@click.pass_obj
def detail(ctx, name):
    """output VM detail"""
    if not ctx.vm:
        ctx.get_vms()
    vm = ctx.vm.get(name, None)
    if not vm:
        fail(f"unknown VM '{name}'")

    config = ctx.get(f"vms/{vm['id']}/restrictions")
    output(config)

@cli.command
@click.argument('name')
@click.pass_obj
def ip(ctx, name):
    """output VM IP address"""
    output(ctx.get_vm_ip(name))

@cli.command
@click.argument('name')
@click.pass_obj
def shutdown(ctx, name):
    """request VM shutdown"""
    output(ctx.set_power(name, 'shutdown'))

@cli.command
@click.argument('name')
@click.pass_obj
def poweroff(ctx, name):
    """request VM hard power off"""
    output(ctx.set_power(name, 'off'))

@cli.command
@click.argument('name')
@click.pass_obj
def start(ctx, name):
    """request VM start"""
    output(ctx.set_power(name, 'on'))

@cli.command
@click.argument('name')
@click.pass_obj
def state(ctx, name):
    """get VM power state"""
    output(ctx.get_power(name))



@cli.command
@click.option('-c', '--cpu', type=int, default=1, help='cpu count')
@click.option('-r', '--ram', type=int, default=4096, help='RAM in MB')
@click.option('-d', '--disk', type=int, default=8192, help='disk size in MB')
@click.option('-i', '--iso', envvar='VMCTL_ISO', help='remote ISO path')
@click.argument('name')
@click.pass_obj
def create(ctx, cpu, ram, disk, name, iso):
    """create VM"""
    output(ctx.create(name, cpu, ram, disk, iso))


@cli.command
@click.option('-f', '--force', is_flag=True, help='bypass confirmation')
@click.argument('name')
@click.pass_obj
def destroy(ctx, name, force):
    """destroy VM"""
    state = ctx.get_power(name)['power_state']
    if state != 'poweredOff':
        fail('power off first')
    if not force:
        click.confirm(f"Confirm IRRECOVERABLE DESTRUCTION of VMWare Workstation '{name}' on '{ctx.host}'", abort=True) 
    output(ctx.destroy(name))


if __name__ == "__main__":
    sys.exit(cli())  # pragma: no cover
