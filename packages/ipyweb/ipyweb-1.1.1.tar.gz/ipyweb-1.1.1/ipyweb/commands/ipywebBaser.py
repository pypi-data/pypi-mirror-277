import os, subprocess, click
from ipyweb.app import app
from ipyweb.config import config
from ipyweb.ipyweb import ipyweb


@click.command(help='ipyweb ver')
@click.argument('name', nargs=1, default='', type=str)
def ver(name=''):
    if not name:
        click.echo(f'ipyweb version: {app.ver}')
    else:
        app.setName(name)  # 动态设置应用名称
        ipyweb.bootBaser(True)
        click.echo(f'{name} version: {config.get("app.ver", "no set")} ')
