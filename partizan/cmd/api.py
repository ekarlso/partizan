import sys

from oslo_config import cfg
from oslo_log import log

from wsgiref import simple_server

from partizan.api import app

def main():
    log.register_options(cfg.CONF)
    cfg.CONF(sys.argv[1:], project='partizan')
    log.setup(cfg.CONF, 'partizan')
    srv = simple_server.make_server("", 8080, app.api)
    srv.serve_forever()
