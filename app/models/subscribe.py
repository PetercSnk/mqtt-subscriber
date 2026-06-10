from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.extensions import db


class Topic(db.Model):
    """Model for SQLAlchemy. The topic table keeps a record of the MQTT topic
    currently subscribed to."""
    __tablename__ = "topic"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(16), unique=True)
    runStatus: Mapped[bool] = mapped_column(default=False)

    def setRunStatus(self, runStatus: bool):
        """Method for updating the topics running status. This is used for
        tracking jobs.
        """
        self.runStatus = runStatus
        db.session.commit()

    def __repr__(self):
        return "<Topic {0}>".format(self.name)
