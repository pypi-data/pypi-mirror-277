import os
import pathlib
import sys
from typing import Tuple

from rich import print
from rich.filesize import decimal
from rich.markup import escape
from rich.text import Text
from rich.tree import Tree
from rich.panel import Panel
from rich.table import Table


def walk_directory(directory: pathlib.Path, tree: Tree) -> None:
	paths = sorted(
		pathlib.Path(directory).iterdir(),
		key=lambda path: (path.is_file(), path.name.lower()),
	)
	for path in paths:
		# Remove hidden files
		if path.name.startswith("."):
			continue
		if path.is_dir():
			style = "dim" if path.name.startswith("__") else ""
			branch = tree.add(
				f"[bold magenta]:open_file_folder: [link file://{path}]{escape(path.name)}",
				style=style,
				guide_style=style,
			)
			walk_directory(path, branch)
		else:
			text_filename = Text(path.name, "green")
			text_filename.highlight_regex(r"\..*$", "bold red")
			text_filename.stylize(f"link file://{path}")
			file_size = path.stat().st_size
			text_filename.append(f" ({decimal(file_size)})", "blue")
			icon = "🐍 " if path.suffix in [".py", ".pyc"] else "📄 "
			tree.add(Text(icon) + text_filename)


def get_all_files(directory: pathlib.Path) -> list[pathlib.Path]:
	files = []
	for path in directory.iterdir():
		if path.is_dir():
			files.extend(get_all_files(path))
		else:
			files.append(path)
	return [path for path in files if path.suffix in [".py"]]


def check_directory(directory: pathlib.Path) -> bool:
	if '__init__.py' in os.listdir(directory):
		return True
	else:
		return False


def search_in_directory(directory: pathlib.Path, filename: str) -> tuple[str, ...]:
	return tuple(os.path.join(root, file)
	             for root, dirs, files in os.walk(directory)
	             for file in files
	             if file == filename)


def visualize_matched_files(files: tuple[str, ...]) -> Panel:
	table = Table(show_header=False, show_lines=False, box=None)
	for num, file in enumerate(files):
		table.add_row(f"[bold red]{num + 1}.[/bold red]",
		              f"[bold magenta][link file://{file}]{escape(file)}[/bold magenta]",
		              f'[bold blue]{str(os.path.getsize(file))} bytes[/bold blue]')

	panel = Panel.fit(title="[bold magenta]Matched files[/bold magenta]", border_style='yellow', renderable=table)

	return panel


def authorize_template(path: pathlib.Path) -> bool:
	if len(get_all_files(path)) == 0 and not check_directory(path):
		return confirm("This directory does not look like a template. Do you want to continue?", default=False)
	return True
