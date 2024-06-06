from ._renderer import Renderer
from .rich import RichRenderer
from .csv import CSVRenderer
from .html import HTMLRenderer


from enum import Enum

class OutputType(Enum):
    rich = "rich"
    csv = "csv"
    html = "html"


def render(output_type, *objects):
    renderer: Renderer | None = None
    match OutputType(output_type):
        case OutputType.rich:
            renderer = RichRenderer()
        case OutputType.csv:
            renderer = CSVRenderer()
        case OutputType.html:
            renderer = HTMLRenderer()
        case _:
            raise ValueError(f"unknown renderer: {output_type}")

    for obj in objects:
        renderer.render(obj)
