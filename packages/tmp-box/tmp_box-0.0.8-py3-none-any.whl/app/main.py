import os
from pathlib import Path
from typer import Typer, Exit, BadParameter, Argument, Option, Abort
from app.models.path_models import OperationModel, TemplateModel
from app.models.settings_model import SettingsModel
from app.context import ManagerContext
from app.utils.path_utils import get_all_files, check_directory, authorize_template
from rich.console import Console
from rich.tree import Tree
from typer import prompt, confirm
from app.routers import view

app = Typer()
app.add_typer(view.app, name='view')
console = Console()
context = ManagerContext


@app.command('build')
def build(path: str = Option('', '-p', '--path', help='Path to template'),
          from_last: bool = Option(False, '--from-last', '-l', help='Build from last template'),
          from_alias: str = Option('', '--from-alias', '-a', help='Build from alias'),
          name: str = Option('', '--name', '-n', help='Name of directory'),
          in_directory: bool = Option(False, '--in-directory', help='Create in current directory')) -> None:
	if path and authorize_template(Path(path)):
		if Path(path).is_file():
			raise BadParameter('Path must be directory')
		if not name:
			name = Path(path).name
	if in_directory:
		name = ''
	try:
		settings = SettingsModel(
			template=path,
			final_path=os.getcwd(),
			folder_name=name,
			in_directory=in_directory,
			alias=from_alias,
			from_last=from_last
		)
		service = context.execute(settings)
		service.build_from(settings, console)
		console.print('[bold green]Success![/bold green]')
	except Exception as e:
		raise e
	finally:
		last = context.get('last')
		if path:
			last.update_on_end(TemplateModel(path=path, name=name))


@app.command('add')
def add_new_template(path: Path = Argument(..., help='Path to template'),
                     name: str = Option(None, '-n', help='Alias of template')) -> None:
	service = context.get('alias')
	if path.is_dir() and authorize_template(Path(path)):
		try:
			if not name:
				name = path.name
			service.repository.update(TemplateModel(path=str(path), alias=name))
			console.print(f'[bold green]Success![/bold green]')
		except Exception as e:
			raise e
	else:
		raise BadParameter('Path must be directory')


@app.command('del')
def delete_template(name: str = Argument(..., help='Alias of template')) -> None:
	service = context.get('alias')
	try:
		service.repository.delete(name)
		console.print(f'[bold green]Success![/bold green]')
	except Exception as e:
		raise e


if __name__ == '__main__':
	app()
