from ..base.abstract import AbstractRepository
from ..models.path_models import TemplateModel, ListTemplateModel
import json
from pathlib import Path
import os
from typer import BadParameter


class LastTemplateRepository(AbstractRepository):
	def __init__(self):
		self.path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'json_dir/last_template.json')

	def get(self):
		with open(self.path, 'r') as f:
			return json.load(f)

	def update(self, template: TemplateModel):
		with open(self.path, 'w') as f:
			json.dump(template.model_dump(), f)

	def delete(self):
		raise NotImplementedError

	def clear(self):
		with open(self.path, 'w') as f:
			json.dump(None, f)

	def save(self, template: TemplateModel):
		raise NotImplementedError


class SavedTemplatesRepository(AbstractRepository):
	def __init__(self):
		self.path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'json_dir/saved_templates.json')

	def get(self):
		try:
			with open(self.path, 'r') as f:
				return json.load(f)
		except json.JSONDecodeError as e:
			if e.msg == "Expecting value":
				return {}
			else:
				raise

	def update(self, template: TemplateModel):
		data = self.get()
		with open(self.path, 'w') as f:
			data[template.alias] = template.model_dump()
			json.dump(data, f)

	def delete(self, alias: str):
		try:
			data = self.get()
			del data[alias]
			with open(self.path, 'w') as f:
				json.dump(data, f)
		except KeyError:
			raise BadParameter(f'Template with alias {alias} not found')

	def clear(self):
		with open(self.path, 'w') as f:
			json.dump({}, f)

	def save(self, template: TemplateModel):
		raise NotImplementedError
