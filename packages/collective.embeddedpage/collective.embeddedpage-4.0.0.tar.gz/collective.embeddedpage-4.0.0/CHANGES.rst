Changelog
=========


4.0.0 (2024-06-03)
------------------

- Add support for Python 3.10 and 3.11
  [tisto]

- Add timeout to request
  [wolbernd]


3.0.3 (2022-04-05)
------------------

- Support pip-based installations of Plone
  [ericof]

- Support Plone 6
  [ericof]


3.0.2 (2022-03-21)
------------------

- Use encoding specified in a text/html response
  [reebalazs]


3.0.1 (2021-12-03)
------------------

- Remove title/description field from the IEmbeddedPage behavior. Fixes #42
  [timo]



3.0.0 (2021-10-08)
------------------

- Migrate to non interface name behaviors.
  [sneridagh]

- Add DublinCore behavior to EmbeddedPage content type.
  [sneridagh]

- Drop Python 2 support.
  [timo]

- Drop Plone 5.1 and 4.3 support.
  [timo]


2.2.1 (2021-04-26)
------------------

- Fix charmap error with 'Windows-1254' encoding. Use utf-8 as fallback
  [robdayz]


2.2.0 (2021-04-14)
------------------

- Add Python 3.8 support (worked before, just added it to classifiers)
  [timo]


2.1.4 (2020-09-26)
------------------

- Do not fail on invalid URLs
  [timo]

- Run black on codebase
  [timo]


2.1.3 (2020-06-27)
------------------

- Don't purge behaviors
  [csenger]


2.1.2 (2020-06-18)
------------------

- Fix getting js resources (#28).
  [csenger]


2.1.1 (2020-05-06)
------------------

- Do not fail on missing params in process_page.
  [timo]


2.1.0 (2020-05-04)
------------------

- Added i18n translation files for EN, ES, CA.
  [robdayz]

- Add serializer for Volto support.
  [rodfersou]


2.0.0 (2020-04-09)
------------------

- Plone 5.2/Python 3 compatibility.
  [timo,rodfersou]


1.3.2 (2020-02-04)
------------------

- Don't raise an exception when target page is empty.
  [rodfersou]


1.3.1 (2019-06-12)
------------------

- Change development status to Production/Stabel in setup.py.
  [timo]


1.3.0 (2019-06-12)
------------------

- Change header forwarding: Only forward http x-* headers and convert
  zopes header names (e.g. HTTP_X_FORWARD_FOR to x-forward-for)
  [csenger]


1.2.2 (2019-05-28)
------------------

- Dont double decode XML HTML pages.
  [rofersou]

- Pass headers forward from original request.
  [rodfersou]

- Make URL field not required.
  [rodfersou]


1.2.1 (2019-05-10)
------------------

- Fix German translation "Show After" and "Show Before".
  [timo]


1.2.0 (2019-05-10)
------------------

- Use chardet package to detect the encoding of the embedded page.
  [rodfersou]


1.1.0 (2019-04-18)
------------------

- Move stylesheets from head to body.
  [rodfersou]

- Add tests.
  [rodfersou]

- Add data-embedded attribute to inspect what page
  is being embedded with no need to login.
  [rodfersou]


1.0.2 (2019-03-30)
------------------

- Fix the content type when request script.
  [rodfersou]

- Fix iframe relative path to full path.
  [rodfersou]


1.0.1 (2019-03-28)
------------------

- Forward script requests from plone server.
  [rodfersou]

- Forward requests and params to original page.
  [rodfersou]

- Convert html parsed data to string with html method.
  [rodfersou]


1.0.0 (2019-02-23)
------------------

- Re-release 1.0.0a6 as final release.
  [timo]


1.0.0a6 (2019-02-13)
--------------------

- Add extra standard behaviors.
  [rodfersou]


1.0.0a5 (2019-02-12)
--------------------

- Fix when html is encoded as UTF-8.
  [rodfersou]


1.0.0a4 (2019-02-11)
--------------------

- Fix when there is no body tag inside html.
  [rodfersou]


1.0.0a3 (2019-01-22)
--------------------

- Add Rich Text to add content before the page embedded.
  [rodfersou]

- Add Rich Text to add content after the page embedded.
  [rodfersou]

- Add One parameter to disable right portlet column.
  [rodfersou]


1.0.0a2 (2019-01-14)
--------------------

- Do not show title and description of the content page itself.
  [timo]

- Add pypi classifier for development status.
  [timo]


1.0.0a1 (2018-11-01)
--------------------

- Initial release.
  [kitconcept]
