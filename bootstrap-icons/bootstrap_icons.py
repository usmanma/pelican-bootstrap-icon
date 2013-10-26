from __future__ import unicode_literals

from docutils import nodes, utils
from docutils.parsers.rst import roles

from pelican.readers import PelicanHTMLTranslator


class icon(nodes.Inline, nodes.Node):
    def __init__(self, rawsource, text):
        self.rawsource = rawsource
        self.text = text
        self.children = []
        self.attributes = {}

    def astext(self):
        return self.text


def icon_role(typ, rawtext, text, lineno, inliner, options={}, content=[]):
    text = utils.unescape(text)
    icon_code = '<span class="glyphicon glyphicon-{}"></span>'.format(text)
    return [icon(text, icon_code)], []


def register():
    roles.register_local_role('icon', icon_role)

PelicanHTMLTranslator.visit_icon = lambda self, node: self.body.append(node.astext())
PelicanHTMLTranslator.depart_icon = lambda self, node: None
