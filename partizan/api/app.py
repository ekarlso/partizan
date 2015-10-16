import json

import falcon

from partizan.api import utils
from partizan.api import parts
from partizan.api import packages


api = falcon.API(before=[utils.check_mediatype], after=[utils.serialize],
                 request_type=utils.Request,
                 response_type=utils.Response)

api.add_route("/packages", packages.PackagesResource())
api.add_route("/packages/{package_id}", packages.PackageResource())
api.add_route("/parts", parts.PartsResource())
