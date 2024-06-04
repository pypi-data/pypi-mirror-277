from abc import ABC, abstractmethod
from typing import Optional
from pathlib import Path
from app.models.settings_model import SettingsModel
from typer import confirm
from ..utils.path_utils import walk_directory
from ..utils.models_utils import visualize_pydantic_model
from rich.tree import Tree
from rich.console import Console
from rich.panel import Panel
from rich.console import ConsoleRenderable

class AbstractRepository(ABC):
	@abstractmethod
	def get(self, **kw):
		pass

	@abstractmethod
	def save(self, **kw):
		pass

	@abstractmethod
	def delete(self, **kw):
		pass

	@abstractmethod
	def clear(self, **kw):
		pass

	@abstractmethod
	def update(self, **kw):
		pass


class AbstractStrategy(ABC):
	def __init__(self, repository: Optional[AbstractRepository] = None):
		self.repository = repository

	@staticmethod
	def verify(settings: SettingsModel, path: Path) -> bool:
		settings.template = path
		console = Console()
		mdl_tree = visualize_pydantic_model(settings)
		panel = Panel.fit(renderable=mdl_tree, border_style='yellow',
		                  title=f'[bold magenta]Template: {path}[/bold magenta]')
		console.print(panel)
		flag = confirm("Are you sure to use this template?", default=False)
		return flag

	@abstractmethod
	def build_from(self, value: SettingsModel, console: Console):
		pass


class AbstractContext(ABC):
	@abstractmethod
	def execute(self, settings: SettingsModel):
		pass


class AbstractReader(ABC):
	@abstractmethod
	def read(self, path: Path) -> str:
		pass


class AbstractVisualizer(ABC):

	def __init__(self, reader: AbstractReader):
		self.reader = reader

	@abstractmethod
	def visualize(self, path: Path) -> ConsoleRenderable:
		pass


class AbstractFacade(ABC):

	def __init__(self):
		self.console = Console()

	@abstractmethod
	def execute(self, path: Path):
		pass
