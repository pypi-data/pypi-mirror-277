from .base.abstract import AbstractContext
from .services.from_alias import FromAliasInterface
from .services.from_last import FromLastInterface
from .services.from_path import FromPathInterface
from .models.settings_model import SettingsModel

from typing import Literal


class ManagerContext(AbstractContext):
	for_path = FromPathInterface()
	for_alias = FromAliasInterface()
	for_last = FromLastInterface()

	@classmethod
	def execute(cls, settings: SettingsModel):
		if settings.template:
			return cls.for_path
		elif settings.alias:
			return cls.for_alias
		elif settings.from_last:
			return cls.for_last

	@classmethod
	def get(cls, kind: str):
		if kind == 'path':
			return cls.for_path
		elif kind == 'alias':
			return cls.for_alias
		elif kind == 'last':
			return cls.for_last
