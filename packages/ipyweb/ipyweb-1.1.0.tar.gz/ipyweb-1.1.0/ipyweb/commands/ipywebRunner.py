import os, click, subprocess
from ipyweb.app import app
from ipyweb.ipyweb import ipyweb
from ipyweb.utils import utils


@click.command(help='ipyweb run [appName]')
@click.argument('name', nargs=1, default='', type=str)
def run(name=os.environ.get('appName')):
    if name == '':
        click.echo(f'please input app name.')
        return
    click.echo(f'[{name}] ready ipyweb backend running...')
    # app.setName(name)  # 动态设置应用名称
    # ipyweb.bootBaser(True)
    command = ['python', 'cli.py', 'runcli', name]
    subprocess.run(command, shell=utils.isWin(), check=True, text=True)


@click.command(help='python cli.py runcli [appName]')
@click.argument('name', nargs=1, default='', type=str)
def runcli(name=os.environ.get('appName')):
    if name == '':
        click.echo(f'please input app name.')
        return
    app.setName(name)  # 动态设置应用名称
    ipyweb.boot(name)


@click.command(help='ipyweb frun [appName] [background]')
@click.argument('name', nargs=1, default='', type=str)
@click.argument('background', nargs=1, default='', type=str)
def frun(name=os.environ.get('appName'), background=''):
    if name == '':
        click.echo(f'please input app name.')
        return
    click.echo(f'[{name}] ready ipyweb fontend running...')
    app.setName(name)  # 动态设置应用名称
    ipyweb.bootBaser(True)

    directory = app.path(f'app/{name}/{app.frontendName}', True)
    os.chdir(directory)
    command = ['npm', 'run', 'dev']
    if background == 'd':
        command = ['start', '/b', 'npm', 'run', 'dev'] if utils.os() == 'win' else ['npm', 'run', 'dev', '&']
    subprocess.run(command, shell=utils.isWin(), check=True, text=True)
    # with subprocess.Popen(command, cwd=directory, shell=utils.isWin()) as process:
    #     process.wait()
