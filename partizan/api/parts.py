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
import falcon

from partizan.api import utils
from partizan.db import models
from partizan import db


class PartsResource(object):
    def on_get(self, req, resp):
        session = db.get_session()
        q = session.query(models.Part)
        data = q.all()
        resp.json = {
            "parts": map(dict, data)
        }

    @falcon.before(utils.deserialize)
    def on_post(self, req, resp):
        obj = models.Part.create(req.json)
        resp.json = dict(obj)
