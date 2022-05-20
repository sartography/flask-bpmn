"""Group."""
from flask_bpmn.models.db import db


class FlaskBpmnGroupModel(db.Model):  # type: ignore
    """FlaskBpmnGroupModel."""

    __tablename__ = "group"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
