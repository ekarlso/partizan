import falcon
from oslo_serialization import jsonutils

from tests.functional import base

from partizan.db import models


class PackageTest(base.BaseTest):
    def test_create(self):
        data = {
            "name": "TO-220"
        }
        response = self.simulate_post('/packages', body=data)
        body = jsonutils.loads(response[0])

        self.assertEqual(self.srmock.status, falcon.HTTP_201)
        self.assertEqual(data["name"], body["name"])
        self.assertIn("id", body)
        self.assertIn("updated_at", body)
        self.assertIn("created_at", body)
        self.assertIn("created_at", body)

    def test_get(self):
        data = {
            "name": "TO-220"
        }

        obj = models.Package.create(data)

        response = self.simulate_get('/packages/%s' % obj.id)
        body = jsonutils.loads(response[0])

        self.assertEqual(self.srmock.status , falcon.HTTP_200)
        self.assertEqual(data["name"], body["name"])
        self.assertIn("id", body)
        self.assertIn("updated_at", body)
        self.assertIn("created_at", body)
        self.assertIn("created_at", body)

    def test_list(self):
        items = [
            {
                "name": "TO-220"
            },
            {
                "name": "MSOP-8"
            }
        ]

        for i in items:
            obj = models.Package.create(i)

        response = self.simulate_get('/packages')
        body = jsonutils.loads(response[0])

        self.assertEqual(self.srmock.status , falcon.HTTP_200)

        for i in xrange(0, len(items)):
            item = body["packages"][i]
            self.assertEqual(items[i]["name"], item["name"])
            self.assertIn("id", item)
            self.assertIn("updated_at", item)
            self.assertIn("created_at", item)
            self.assertIn("created_at", item)

    def test_delete(self):
        data = {
            "name": "TO-220"
        }

        obj = models.Package.create(data)

        response = self.simulate_delete('/packages/%s' % obj.id)

        self.assertEqual(self.srmock.status, falcon.HTTP_204)
