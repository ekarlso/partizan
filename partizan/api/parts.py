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
