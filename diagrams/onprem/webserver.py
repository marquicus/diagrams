# This module is automatically generated by autogen.sh. DO NOT EDIT.

from . import _OnPrem


class _Webserver(_OnPrem):
    _type = "webserver"
    _icon_dir = "resources/onprem/webserver"


class Apache(_Webserver):
    _icon = "apache.png"


class Caddy(_Webserver):
    _icon = "caddy.png"


class Haproxy(_Webserver):
    _icon = "haproxy.png"


class Nginx(_Webserver):
    _icon = "nginx.png"


class Traefik(_Webserver):
    _icon = "traefik.png"


# Aliases
