from pathlib import Path

from ..models.settings_model import SettingsModel
from ..models.path_models import TemplateModel
from ..base.abstract import AbstractStrategy
import shutil
from typer import Abort
from ..repositories.json_repositories import SavedTemplatesRepository
from rich import print
from rich.console import Console




class FromAliasInterface(AbstractStrategy):
	def __init__(self):
		super().__init__(repository=SavedTemplatesRepository())

	def build_from(self, value: SettingsModel, console: Console) -> None:
		print('[green]started build template from alias...[/green]')
		template = self.repository.get()
		try:
			settings = value
			tmp_path = template.get(settings.alias)['path']
			print(f'[green]building from path: {tmp_path}[/green]')
			if self.verify(path=Path(tmp_path), settings=settings):
				with console.status(f'[bold green]Building...[/bold green]'):
					return shutil.copytree(tmp_path, fr'{settings.final_path}\{settings.folder_name}',
					                       dirs_exist_ok=True)
			else:
				print('[red]something went wrong[/red]')
				raise Abort()
		except Exception as e:
			print('[red]failed[/red]')
			raise e
