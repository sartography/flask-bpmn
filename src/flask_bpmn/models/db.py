"""Db."""
from __future__ import annotations

import time

from flask_migrate import Migrate  # type: ignore
from flask_sqlalchemy import SQLAlchemy  # type: ignore
from sqlalchemy import event  # type: ignore
from sqlalchemy.engine.base import Connection  # type: ignore
from sqlalchemy.orm.mapper import Mapper  # type: ignore

db = SQLAlchemy()
migrate = Migrate()


class SpiffworkflowBaseDBModel(db.Model):  # type: ignore
    """SpiffworkflowBaseDBModel."""

    __abstract__ = True

    @classmethod
    def _all_subclasses(cls) -> list[type[SpiffworkflowBaseDBModel]]:
        """Get all subclasses of cls, descending.

        So, if A is a subclass of B is a subclass of cls, this
        will include A and B.
        (Does not include cls)
        """
        children = cls.__subclasses__()
        result = []
        while children:
            next = children.pop()
            subclasses = next.__subclasses__()
            result.append(next)
            # check subclasses of subclasses SpiffworkflowBaseDBModel. i guess we only go down to grandchildren, which seems cool.
            for subclass in subclasses:
                children.append(subclass)
        return result


def update_created_modified_on_create_listener(
    mapper: Mapper, _connection: Connection, target: SpiffworkflowBaseDBModel
) -> None:
    """Event listener that runs before a record is updated, and sets the create/modified field accordingly."""
    if "created_at_in_seconds" in mapper.columns.keys():
        target.created_at_in_seconds = round(time.time())
    if "updated_at_in_seconds" in mapper.columns.keys():
        target.updated_at_in_seconds = round(time.time())


def update_modified_on_update_listener(
    mapper: Mapper, _connection: Connection, target: SpiffworkflowBaseDBModel
) -> None:
    """Event listener that runs before a record is updated, and sets the modified field accordingly."""
    if "updated_at_in_seconds" in mapper.columns.keys():
        if db.session.is_modified(target, include_collections=False):
            target.updated_at_in_seconds = round(time.time())


def add_listeners() -> None:
    """Adds the listeners to all subclasses.

    This should be called after importing all subclasses
    """
    for cls in SpiffworkflowBaseDBModel._all_subclasses():
        event.listen(cls, "before_insert", update_created_modified_on_create_listener)
        event.listen(cls, "before_update", update_modified_on_update_listener)
