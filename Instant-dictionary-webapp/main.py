# import inspect

import justpy as jp


from webapp.home import Home
from webapp.about import About
from webapp.dictionary import Dict


# imports = list(globals().values())
#
# for obj in imports:
#     if inspect.isclass(obj):
#         if issubclass(obj, page.Page) and obj is not page.Page:
#             jp.Route(obj.path,obj.serve)

jp.Route(Home.path,Home.serve)
jp.Route(About.path,About.serve)
jp.Route(Dict.path,Dict.serve)

jp.justpy(port=8001)