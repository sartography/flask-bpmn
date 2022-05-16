"""Group."""
from flask_bpmn.models.db import db


class GroupModel(db.Model):
    """GroupModel."""

    __tablename__ = "groups"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
