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


class CategoriesResource(object):
    def on_get(self, req, resp):
        session = db.get_session()
        q = session.query(models.Category)
        rows = q.all()
        resp.json = {"categories": map(dict, rows)}

    @falcon.before(utils.deserialize)
    def on_post(self, req, resp):
        obj = models.Category.create(req.json)
        resp.json = dict(obj)
        resp.status = falcon.HTTP_201


class CategoryResource(object):
    def on_delete(self, req, resp, category_id):
        models.Category.delete(category_id)
        resp.status = falcon.HTTP_204

    def on_get(self, req, resp, category_id):
        session = db.get_session()
        q = session.query(models.Category)
        q = q.filter_by(id=category_id)
        obj = q.one()
        resp.json = dict(obj)
