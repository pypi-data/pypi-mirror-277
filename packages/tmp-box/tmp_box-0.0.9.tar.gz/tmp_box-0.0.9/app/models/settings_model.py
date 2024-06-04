from pydantic import BaseModel


class SettingsModel(BaseModel):
	template: str
	folder_name: str
	in_directory: bool
	final_path: str
	alias: str = None
	from_last: bool = False
