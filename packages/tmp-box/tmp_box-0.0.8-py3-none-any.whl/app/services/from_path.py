from pathlib import Path

from ..models.settings_model import SettingsModel
from ..base.abstract import AbstractStrategy
import shutil
from typer import Abort
from rich import print
from rich.console import Console

class FromPathInterface(AbstractStrategy):

	def build_from(self, value: SettingsModel, console: Console) -> None:
		try:
			print('[green]started build from path...[/green]')
			tmp_path = value.template
			final = value.final_path
			print(f'[green]building from path: {tmp_path}[/green]')
			if self.verify(path=Path(tmp_path), settings=value):
				with console.status(f'[bold green]Building...[/bold green]'):
					return shutil.copytree(tmp_path, fr'{final}\{value.folder_name}', dirs_exist_ok=True)
			else:
				print('[red]something went wrong[/red]')
				raise Abort()
		except Exception as e:
			print('[red]failed[/red]')
			raise e

