# -*- encoding: utf-8 -*-
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
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
