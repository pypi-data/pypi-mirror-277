# -- coding: utf-8 --
# @Time : 2024/6/6 14:26
# @Author : PinBar
# @File : startapp.py
import shutil
from pathlib import Path

import click

from .remove_header import remove_header


@click.command(help="To create the app, you need to navigate to the you_project directory in the project, and then run it.")
@click.argument('app_name')
def main(app_name: str):
    target_dir = Path.cwd()
    package_dir = Path(__file__).parent
    project_path = list(target_dir.glob('src/api'))
    if not project_path:
        raise Exception("No project found")
    api_dir = project_path[0]
    shutil.copytree(package_dir / 'example_file/init_app', api_dir / app_name)
    with open(Path(api_dir / app_name / '__init__.py'), 'w') as fp:
        fp.write(f"APP_NAME = '{app_name}'")
    remove_header(target_dir)
    print(f"Successfully created app {app_name}, app dir: {api_dir}, enjoy it...")


if __name__ == '__main__':
    main()
