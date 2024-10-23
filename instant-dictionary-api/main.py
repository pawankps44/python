import justpy as jp
from api import Api
from documentation import Doc

jp.Route('/api',Api.serve)
jp.Route('/',Doc.serve)
jp.justpy()