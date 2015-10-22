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
