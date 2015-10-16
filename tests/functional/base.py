from falcon import testing
from oslo_config import cfg
from oslo_serialization import jsonutils
from oslotest import base

from partizan.api import app
from partizan.common import config
from partizan import db
from partizan.manage import database

from tests.functional.fixtures import database as database_fixture

cfg.CONF.import_group("database", "oslo_db.options")


CONF  = cfg.CONF
_DB_CACHE = None


test_opts = [
    cfg.StrOpt('sqlite_clean_db',
               default='clean.sqlite',
               help='File name of clean sqlite database.')
]

CONF.register_opts(test_opts)


class BaseTest(base.BaseTestCase):
    def setUp(self):
        super(BaseTest, self).setUp()

        self.headers = {
            "content-type": "application/json"
        }

        # Simulate WSGI
        self.app = app.api
        self.srmock = testing.StartResponseMock()

        self._include_default_fixtures()

    def _include_default_fixtures(self):
        global _DB_CACHE
        if not _DB_CACHE:
            DB_CACHE = database_fixture.Database(
                db,
                database.get_manager(),
                sql_connection=CONF.database.connection,
                sqlite_db=CONF.database.sqlite_db,
                sqlite_clean_db=CONF.sqlite_clean_db,
            )
        self.useFixture(DB_CACHE)

    def setup_database(self):
        """Setup test data."""
        # Create tables from SQLAlchemy config
        Base.metadata.create_all(self.engine)

    def teardown_database(self):
        Base.metadata.drop_all(self.engine)
        # Remove it, so that the next test gets a new Session()
        self.session.remove()

    def simulate_request(self, path, **kwargs):
        headers = kwargs.setdefault("headers", self.headers).copy()
        kwargs["headers"] = headers

        if "body" in kwargs and isinstance(kwargs["body"], dict):
            kwargs["body"] = jsonutils.dumps(kwargs["body"])

        env = testing.create_environ(path=path, **kwargs)
        return self.app(env, self.srmock)

    def simulate_get(self, *args, **kwargs):
        kwargs['method'] = 'GET'
        return self.simulate_request(*args, **kwargs)

    def simulate_post(self, *args, **kwargs):
        kwargs['method'] = 'POST'
        return self.simulate_request(*args, **kwargs)

    def simulate_put(self, *args, **kwargs):
        kwargs['method'] = 'PUT'
        return self.simulate_request(*args, **kwargs)

    def simulate_patch(self, *args, **kwargs):
        kwargs['method'] = 'PATCH'
        return self.simulate_request(*args, **kwargs)

    def simulate_delete(self, *args, **kwargs):
        kwargs['method'] = 'DELETE'
        return self.simulate_request(*args, **kwargs)

    def simulate_options(self, *args, **kwargs):
        kwargs['method'] = 'OPTIONS'
        return self.simulate_request(*args, **kwargs)
