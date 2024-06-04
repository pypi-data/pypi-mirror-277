"""Module where all interfaces, events and exceptions live."""

from collective.embeddedpage import _
from plone.app.textfield import RichText
from plone.autoform import directives as form
from z3c.form.browser.checkbox import SingleCheckBoxFieldWidget
from zope import schema
from zope.interface import Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class ICollectiveEmbeddedpageLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class IEmbeddedPage(Interface):

    url = schema.URI(
        title=_("URI"),
        required=False,
    )

    before = RichText(
        title=_("Show Before"),
        required=False,
    )

    after = RichText(
        title=_("Show After"),
        required=False,
    )

    form.widget(disable_right_portlet=SingleCheckBoxFieldWidget)
    disable_right_portlet = schema.Bool(
        title=_("Disable Right Portlet"),
        required=False,
    )
