import falcon
from oslo_serialization import jsonutils

from tests.functional import base

from partizan.db import models


class CategoryTest(base.BaseTest):
    def test_create(self):
        data = {
            "name": "IC"
        }
        response = self.simulate_post('/categories', body=data)
        body = jsonutils.loads(response[0])

        self.assertEqual(self.srmock.status, falcon.HTTP_201)
        self.assertEqual(data["name"], body["name"])
        self.assertIn("id", body)
        self.assertIn("updated_at", body)
        self.assertIn("created_at", body)
        self.assertIn("created_at", body)

    def test_get(self):
        data = {
            "name": "IC"
        }

        obj = models.Category.create(data)

        response = self.simulate_get('/categories/%s' % obj.id)
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
                "name": "Resistors"
            },
            {
                "name": "IC"
            }
        ]

        for i in items:
            obj = models.Category.create(i)

        response = self.simulate_get('/categories')
        body = jsonutils.loads(response[0])

        self.assertEqual(self.srmock.status , falcon.HTTP_200)

        for i in xrange(0, len(items)):
            item = body["categories"][i]
            self.assertEqual(items[i]["name"], item["name"])
            self.assertIn("id", item)
            self.assertIn("updated_at", item)
            self.assertIn("created_at", item)
            self.assertIn("created_at", item)

    def test_delete(self):
        data = {
            "name": "IC"
        }

        obj = models.Category.create(data)

        response = self.simulate_delete('/categories/%s' % obj.id)

        self.assertEqual(self.srmock.status, falcon.HTTP_204)
