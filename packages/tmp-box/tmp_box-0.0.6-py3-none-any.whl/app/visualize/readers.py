from ..base.abstract import AbstractReader
import json
from pathlib import Path


class TextualReader(AbstractReader):
	def read(self, path: Path) -> str:
		with open(path, 'r') as file:
			return file.read()


class JsonReader(AbstractReader):
	def read(self, path: Path) -> str:
		with open(path, 'r') as file:
			return json.dumps(json.load(file), indent=4)
