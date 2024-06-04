from ..base.abstract import AbstractFacade
from .visualizers import TextualVisualizer, JsonVisualizer, SyntaxVisualizer, MarkdownVisualizer
from .readers import TextualReader, JsonReader
from typer import BadParameter
from pathlib import Path


class Visualizer(AbstractFacade):
	__dict_suffix__ = {
		'.txt': (TextualVisualizer, TextualReader,),
		'.json': (JsonVisualizer, JsonReader,),
		'.py': (SyntaxVisualizer, TextualReader,),
		'.md': (MarkdownVisualizer, TextualReader,),
		'.pyc': (TextualVisualizer, TextualReader,),

	}

	def execute(self, path: Path):
		suffix = path.suffix
		if suffix in self.__dict_suffix__:
			visualizer, reader = self.__dict_suffix__[suffix]
			renderable = visualizer(reader=reader()).visualize(path)
			self.console.print(renderable)
		else:
			visualizer = TextualVisualizer(reader=TextualReader())
			renderable = visualizer.visualize(path)
			self.console.print(renderable)
