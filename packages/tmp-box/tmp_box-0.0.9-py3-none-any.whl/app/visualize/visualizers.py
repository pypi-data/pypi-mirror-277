from ..base.abstract import AbstractVisualizer, AbstractReader
from rich.syntax import Syntax
from rich.markdown import Markdown
from rich.console import Console
from rich.json import JSON
from pathlib import Path
from rich.text import Text


class JsonVisualizer(AbstractVisualizer):
	def visualize(self, path: Path):
		data = self.reader.read(path)
		return JSON(data, highlight=True)


class MarkdownVisualizer(AbstractVisualizer):
	def visualize(self, path: Path):
		data = self.reader.read(path)
		return Markdown(data)


class TextualVisualizer(AbstractVisualizer):
	def visualize(self, path: Path):
		data = self.reader.read(path)
		return Text(data)


class SyntaxVisualizer(AbstractVisualizer):
	def visualize(self, path: Path):
		data = self.reader.read(path)
		return Syntax(data, 'python', theme='monokai', line_numbers=True)
