

from pydantic import BaseModel
from rich.tree import Tree


def visualize_pydantic_model(model):
	tree = Tree(f"[bold blue]{model.__class__.__name__}[/bold blue]")

	for field_name in model.__fields__.keys():
		field_value = getattr(model, field_name)
		if isinstance(field_value, BaseModel):
			field_node = tree.add(f"[bold]{field_name}[/bold]: [green]{field_value.__class__.__name__}[/green]")
			tree.add(visualize_pydantic_model(field_value))
		elif field_value is not None:
			tree.add(f"[bold]{field_name}[/bold]: [yellow]{field_value}[/yellow]")

	return tree
