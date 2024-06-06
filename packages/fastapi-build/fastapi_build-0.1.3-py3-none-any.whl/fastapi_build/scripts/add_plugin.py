# -- coding: utf-8 --
# @Time : 2024/6/6 15:04
# @Author : PinBar
# @File : add_plugin.py
import shutil
from pathlib import Path

import click

from .remove_header import remove_header


@click.command(help="Add a plugin, 目前支持数据库插件db, dao crud插件, celery插件")
@click.argument('plugin_name', type=click.Choice(['db', 'celery', 'dao'], ))
def main(plugin_name: str):
    if plugin_name == 'celery':
        plugin_name = 'celery_task'
    target_dir = Path.cwd()
    project_path = list(target_dir.glob('src'))
    if not project_path:
        raise Exception("No project found")
    package_dir = Path(__file__).parent.parent

    shutil.copytree(package_dir / 'db', target_dir / 'src' / plugin_name)
    (target_dir / 'src' / plugin_name / 'models' / 'user.py').unlink()
    remove_header(target_dir)
    print(f"Successfully install plugin {plugin_name}")


if __name__ == '__main__':
    main()
