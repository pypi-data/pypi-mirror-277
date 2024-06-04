from ..utils import path_utils
from pydantic import BaseModel, validator
from pathlib import Path
from typing import Optional


class TemplateModel(BaseModel):
	path: str
	alias: str = None


class ListTemplateModel(BaseModel):
	templates: list[TemplateModel]


class OperationModel(BaseModel):
	template: TemplateModel
	final_path: Path
