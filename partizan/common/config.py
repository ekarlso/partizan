from oslo_config import cfg
from oslo_db import options as db_options
from oslo_log import log


LOG = log.getLogger(__name__)


def set_db_defaults():
    # Update the default QueuePool parameters. These can be tweaked by the
    # conf variables - max_pool_size, max_overflow and pool_timeout
    db_options.set_defaults(
        cfg.CONF,
        connection='sqlite://',
        sqlite_db='', max_pool_size=10,
        max_overflow=20, pool_timeout=10)

set_db_defaults()
