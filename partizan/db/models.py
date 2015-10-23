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
