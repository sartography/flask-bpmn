"""Db."""
from flask_migrate import Migrate  # type: ignore
from flask_sqlalchemy import SQLAlchemy  # type: ignore

db = SQLAlchemy()
migrate = Migrate()
