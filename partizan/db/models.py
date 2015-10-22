from oslo_db.sqlalchemy import models
import sqlalchemy as sa
from sqlalchemy.orm import relationship

from partizan.db import get_session
from partizan.db import base
from partizan.db import types


class Category(base.BASE, models.TimestampMixin):
    __tablename__ = "categories"
    name = sa.Column(sa.Unicode(100), nullable=False)

    parts = relationship("Part", backref="category")

    @classmethod
    def create(cls, values):
        session = get_session()
        inst = cls(**values)
        cls.save(inst, session)
        return inst


class Package(base.BASE, models.TimestampMixin):
    __tablename__ = "packages"
    name = sa.Column(sa.Unicode(100), nullable=False)

    parts = relationship("Part", backref="package")

    @classmethod
    def create(cls, values):
        session = get_session()
        inst = cls(**values)
        cls.save(inst, session)
        return inst


class Part(base.BASE, models.TimestampMixin):
    __tablename__ = "parts"
    name = sa.Column(sa.Unicode(100), nullable=False)
    package_id = sa.Column(types.UUID(), sa.ForeignKey("packages.id"))
    category_id = sa.Column(types.UUID(), sa.ForeignKey("categories.id"))

    @classmethod
    def create(cls, values):
        session = get_session()
        inst = cls(**values)
        cls.save(inst, session)
        return inst
