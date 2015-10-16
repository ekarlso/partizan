from oslo_config import cfg
from oslo_db.sqlalchemy import session
from oslo_db import options as db_options

_FACADE = None


def _create_facade_lazily():
    global _FACADE

    if _FACADE is None:
        _FACADE = session.EngineFacade.from_config(cfg.CONF, sqlite_fk=True)

    return _FACADE


def get_engine():
    """Helper method to grab engine."""
    facade = _create_facade_lazily()
    return facade.get_engine()


def get_session(autocommit=True, expire_on_commit=False):
    """Helper method to grab session."""
    facade = _create_facade_lazily()
    return facade.get_session(autocommit=autocommit,
                              expire_on_commit=expire_on_commit)
