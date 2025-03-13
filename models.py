from flask_sqlalchemy import SQLAlchemy
import datetime as dt
import uuid

db = SQLAlchemy()


class File(db.Model):
    id = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))
    filename = db.Column(db.String(255), nullable=False)
    path = db.Column(db.String(255), nullable=False)
    upload_date = db.Column(db.DateTime, default=dt.datetime.utcnow)


class DownloadLink(db.Model):
    id = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))
    file_id = db.Column(db.String, db.ForeignKey('file.id'), nullable=False)
    expiration_date = db.Column(db.DateTime)
    max_downloads = db.Column(db.Integer, nullable=True)
    current_downloads = db.Column(db.Integer, default=0)
    file = db.relationship('File', backref=db.backref('links', lazy=True))