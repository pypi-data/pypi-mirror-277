# -*- coding: utf-8 -*-
import json
from pathlib import Path

import typer
import os
from rich import print
from autowork_cli.common.config.LoginConfig import DefaultLoginConfig
from autowork_cli.common.config.template.hello_world_template import HELLO_WORD
from autowork_cli.common.config.template.pyproject_template import PYPROJECT_TEMPLATE
from autowork_cli.common.config.template.sandbox_readme_template import SANDBOX_README_TEMPLATE
from autowork_cli.common.config.template.sandbox_start_template import SANDBOX_START
from autowork_cli.flow.flow_cmd import service
from autowork_cli.util.fileutil import FileUtil
from poetry.core.factory import Factory


cf_app = typer.Typer(name='cf', help='Autowork Cloud Function Tool')

@cf_app.command(help='初始沙盒函数工程')
def init(project_id: str = typer.Option(None, '-p', '--project-id', prompt='工程ID', help='工程ID')):
    # 初始化函数
    src_dir = project_id.strip().lower()
    if not os.path.exists(src_dir):
        os.mkdir(src_dir)
    if not os.path.exists('tests'):
        os.mkdir('tests')

    # init pyproject.toml
    content = PYPROJECT_TEMPLATE.replace('{project_id}', src_dir, 2)
    FileUtil.generate_file('./pyproject.toml', content)

    # init SANDBOX_README.md
    FileUtil.generate_file('./SANDBOX_README.md', SANDBOX_README_TEMPLATE)

    # init hello world
    FileUtil.generate_file(f"./{src_dir}/hello_world.py", HELLO_WORD)
    FileUtil.generate_file(f"./{src_dir}/__init__.py", '')

    # add tests init
    FileUtil.generate_file(f"./tests/__init__.py", '')

    # init sandbox_start
    FileUtil.generate_file(f"./sandbox_start.py", SANDBOX_START)

    typer.echo("project inited")


@cf_app.command()
def run():
    # 初始化函数
    typer.echo("run project...")


@cf_app.command(help='下载依赖关系')
def dldeps():
    # 下载依赖关系
    current_path = Path(os.getcwd())
    pyproject = current_path.joinpath('pyproject.toml')
    if Path(pyproject).exists():
        print('开始查询写入依赖关系...')
        file = Factory().create_poetry(Path(pyproject))
        project_info = file.package
        print("项目名称:", project_info.pretty_name)
        input_data = {"input": {"code": f'{project_info.pretty_name}', "app_id": DefaultLoginConfig.get_dev_apps()}}
        result = service(app_code="metabase", flow_code="get_package_dependencies", data=json.dumps(input_data))
        if result.get('message'):
            print(f"[red]{result.get('message')}，请先在沙盒函数中配置")
            return
        write_pyproject_toml(pyproject, result)
        print(f'写入依赖关系完成')

    else:
        print("[red]未找到pyproject.toml文件，请切换到项目根目录后重试")


def write_pyproject_toml(pyproject_toml_path, content):
    """将依赖写入pyproject.toml文件"""
    lib_code = content["py_lib_info"]["code"]
    lib_code_version = content["py_lib_info"]["version"]
    with open(pyproject_toml_path, 'a', encoding='utf8') as file:
        file.write('\n\n')
        file.write('[tool.autowork]\n')
        file.write(f'pylib = "{lib_code}"\n')
        file.write(f'pylib_version = "{lib_code_version}"\n')
        file.write('\n')
        file.write(f'[tool.poetry.group.{lib_code}.dependencies]\n')
        for dep in content['lib_pkg_info']:
            if dep['pkg_opt'] in ['eq']:
                dep['pkg_opt'] = ''
            file.write(f'{dep["code"]} = "{dep["pkg_opt"]}{dep["pkg_version"]}"\n')
