import falcon

from partizan.api import utils
from partizan.db import models
from partizan import db


class PackagesResource(object):
    def on_get(self, req, resp):
        session = db.get_session()
        q = session.query(models.Package)
        rows = q.all()
        resp.json = {"packages": map(dict, rows)}

    @falcon.before(utils.deserialize)
    def on_post(self, req, resp):
        obj = models.Package.create(req.json)
        resp.json = dict(obj)
        resp.status = falcon.HTTP_201


class PackageResource(object):
    def on_delete(self, req, resp, package_id):
        models.Package.delete(package_id)
        resp.status = falcon.HTTP_204

    def on_get(self, req, resp, package_id):
        session = db.get_session()
        q = session.query(models.Package)
        q = q.filter_by(id=package_id)
        obj = q.one()
        resp.json = dict(obj)
