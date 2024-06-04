from typer import Typer, Option, Argument, BadParameter, prompt, Abort
from app.context import ManagerContext
from app.utils.path_utils import walk_directory, search_in_directory, visualize_matched_files
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.tree import Tree
from rich.box import DOUBLE
from rich.markup import escape
from pathlib import Path
from ..visualize.facade import Visualizer
app = Typer()
console = Console()
context = ManagerContext
visualizer = Visualizer()


def view(template: Path):
	tree = Tree(f'[bold magenta]:open_file_folder: [link file://{template}]{escape(template.name)}')
	walk_directory(directory=template, tree=tree)
	table = Panel.fit(renderable=tree, title=f"[bold magenta]{str(template)}[/bold magenta]",
	                  border_style='yellow')
	console.print(table)


@app.command('alias')
def get_template_by_alias(alias: str = Argument(..., help='Alias of template')) -> None:
	service = context.get('alias')
	template = Path(service.repository.get().get(alias).get('path'))
	view(template)


@app.command('last')
def get_latest_template() -> None:
	service = context.get('last')
	template = Path(service.repository.get()['path'])
	view(template)


@app.command('path')
def get_path(path: Path = Argument(..., help='Path to template')) -> None:
	if path.is_dir():
		view(path)
	else:
		raise BadParameter('Path must be directory')


@app.command('file')
def get_file(file: str = Argument(..., help='Path to file'),
             alias: str = Option(None, '-a', help='Alias of template'),
             path: Path = Option(None, '-p', help='Path to template')) -> None:
	file_name = file
	if alias:
		path = context.get('alias').repository.get().get(alias)['path']
	if not path and not alias:
		raise BadParameter('Argument path or alias must be set')

	matched_files = search_in_directory(path, file_name)
	if len(matched_files) > 1:
		panel = visualize_matched_files(matched_files)
		console.print(panel)
		key = prompt('Choose file and enter number', type=int, default=1, show_choices=True)
		if key-1 in range(len(matched_files)):
			visualizer.execute(Path(matched_files[key-1 if key > 0 else 0]))
		else:
			raise Abort('Wrong number')
	elif len(matched_files) == 1:
		visualizer.execute(Path(matched_files[0]))

	else:
		raise BadParameter('File not found')




