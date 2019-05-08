from app import db


class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    path = db.Column(db.String(128), index=True, unique=True)
    content_id = db.Column(db.Integer, db.ForeignKey("content.id"))

    def __repr__(self):
        return f"<Image: {self.path}>"


class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(128), index=True, unique=True)
    text = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f"<Content from site: {self.url}>"
