import xml.etree.ElementTree as ET

from jinja2 import Environment, PackageLoader, select_autoescape

from budget.table import Table

from ._renderer import Renderer


class HTMLRenderer(Renderer):
    def __init__(self):
        self.env = Environment(
            loader=PackageLoader("budget.rendering", "templates"),
            autoescape=select_autoescape(),
        )

    def render_table(self, table: Table):
        template = self.env.get_template("table.html")
        print(template.render(table=table))
