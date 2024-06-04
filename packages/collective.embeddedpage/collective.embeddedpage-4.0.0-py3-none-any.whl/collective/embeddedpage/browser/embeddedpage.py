from lxml import etree
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from urllib.parse import urljoin
from urllib.parse import urlparse

from collective.embeddedpage import _
from plone.registry.interfaces import IRegistry
from zope.component import getUtility

import chardet
import lxml
import re
import requests


class EmbeddedPageView(BrowserView):

    template = ViewPageTemplateFile("embeddedpage.pt")

    def get_zope_request_http_headers(self):
        """Return a dict with all x-*http headers in their original format"""
        headers = {}
        for name, value in self.request.environ.items():
            if not name.startswith("HTTP_"):
                continue
            name = name[5:].lower().replace("_", "-")
            headers[name] = f"{value}"
        return self.filter_x_http_headers(headers)

    def filter_x_http_headers(self, headers):
        filtered = {}
        for name, value in headers.items():
            if name.lower().startswith("x-"):
                filtered[name] = value
        return filtered

    def process_page(self):
        registry = getUtility(IRegistry)
        data = {
            "content-type": "text/html",
            "content": "",
        }

        # external js resources
        resource = self.request.form.get("embeddedpage_get_resource", "")
        if resource:
            return {
                "content-type": "application/javascript",
                "content": requests.get(resource).content,
            }

        request_type = self.request["REQUEST_METHOD"]
        method = getattr(requests, request_type.lower(), requests.get)
        params = {
            "url": self.context.url,
            # Forward request x-* headers
            "headers": self.get_zope_request_http_headers(),
            "timeout": registry.get("collective.embeddedpage.timeout"),
        }
        if request_type == "GET":
            params["params"] = self.request.form
        else:
            params["data"] = self.request.form
            # Plone mix GET and POST parameters, and customer 'complex search' use same parameter for two things...  # noqa
            # https://docs.plone.org/develop/plone/serving/http_request_and_response.html#post-variables  # noqa
            if "komplexesuche" in params["data"].get("ifab_modus", ""):
                params["data"]["ifab_modus"] = "suchergebnis"
        try:
            response = method(**params)
        except requests.exceptions.MissingSchema:
            return data
        except requests.exceptions.ReadTimeout:
            data["content"] = _("Could not load page")
            return data

        # Forward response x-* headers
        for k, v in self.filter_x_http_headers(response.headers).items():
            self.request.response.setHeader(k, v)

        # Normalize charset to unicode
        content = response.content
        if content.strip() == "":
            data["content"] = ""
            return data

        encoding = None
        content_type_header = response.headers.get("Content-Type", "")
        if content_type_header is not None:
            match = re.match(r"text/html; charset=(.*)", content_type_header)
            if match is not None:
                # text/html with an encoding
                encoding = match.group(1)
        if encoding is None:
            # Magic ONLY if not text/html with an encoding
            encoding = chardet.detect(content)["encoding"]

        try:
            content = content.decode(encoding)
        except Exception:
            # use default decoding on errors
            content = content.decode("utf-8")
        # https://stackoverflow.com/a/28545721/2116850
        content = re.sub(r"\<\?xml.*encoding.*\?\>\ *?\n", "", content)
        el = lxml.html.fromstring(content)
        url = self.context.absolute_url()
        for script in el.findall(".//script"):
            src = script.attrib.get("src", "")
            if src == "":
                continue
            script.attrib["src"] = f"{url}?embeddedpage_get_resource={src}"
        for iframe in el.findall(".//iframe"):
            src = iframe.attrib.get("src", "")
            if urlparse(src).scheme != "":
                continue
            iframe.attrib["src"] = urljoin(self.context.url, src)
        body = el.find("body")
        if body is not None:
            for link in el.findall(".//head//link"):
                body.insert(0, link)
            el = body
        data["content"] = etree.tostring(el, method="html")
        return data

    def __call__(self):
        data = self.process_page()
        if data.get("content-type", "text/html") != "text/html":
            self.request.response.setHeader("content-type", data["content-type"])
            self.request.response.setBody(data["content"])
            return

        self.embeddedpage = data["content"]
        return self.template()
