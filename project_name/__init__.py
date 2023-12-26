from typing import Any

from django.db.backends.base.base import BaseDatabaseWrapper
from django.db.backends.signals import connection_created


def activate_foreign_keys(sender: Any, connection: BaseDatabaseWrapper, **kwargs: Any):  # noqa: ARG001
    if connection.vendor == "sqlite":
        cursor = connection.cursor()
        cursor.execute("PRAGMA journal_mode = wal;")


connection_created.connect(activate_foreign_keys)
