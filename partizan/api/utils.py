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
from oslo_serialization import jsonutils as json

import falcon


def serialize(req, resp):
    if resp.json is not None:
        resp.content_type = "application/json"
        resp.body = json.dumps(resp.json)


def check_mediatype(req, resp, params):
    if not req.client_accepts_json:
        raise falcon.HTTPNotAcceptable(
            'This API only supports responses encoded as JSON.')


def deserialize(req, resp, params):
    body = req.stream.read()

    if req.content_type is not None and (
            req.content_type.split(";")[0] == "application/json"):
        if not body:
            raise falcon.HTTPBadRequest("No body..", "No data present in body")

        req.json = json.loads(body)
    else:
        raise falcon.HTTPUnsupportedMediaType("Invalid Content-Type")


class Request(falcon.Request):
    def __init__(self, env, options=None):
        super(Request, self).__init__(env, options)
        self.json = None


# Response with a json attribute
class Response(falcon.Response):
    def __init__(self):
        super(Response, self).__init__()
        self.json = None
