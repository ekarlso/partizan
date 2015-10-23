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
import json

import falcon

from partizan.api import utils
from partizan.api import category
from partizan.api import parts
from partizan.api import packages


api = falcon.API(before=[utils.check_mediatype], after=[utils.serialize],
                 request_type=utils.Request,
                 response_type=utils.Response)

api.add_route("/categories", category.CategoriesResource())
api.add_route("/categories/{category_id}", category.CategoryResource())
api.add_route("/packages", packages.PackagesResource())
api.add_route("/packages/{package_id}", packages.PackageResource())
api.add_route("/parts", parts.PartsResource())
