from app import db
from flask import current_app


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
    tasks = db.relationship('Task', backref='content', lazy='dynamic')

    def __repr__(self):
        return f"<Content from site: {self.url}>"

    def launch_task(self, name, *args, **kwargs):
        rq_job = current_app.task_queue.enqueue('app.tasks.' + name, self.id,
                                                *args, **kwargs)
        task = Task(id=rq_job.get_id(), name=name, content=self)
        db.session.add(task)
        return task

    def get_task_in_progress(self, name):
        return Task.query.filter_by(name=name, content=self,
                                    complete=False).all().first()


class Task(db.Model):
    id = db.Column(db.String(36), primary_key=True)
    name = db.Column(db.String(128), index=True)
    complete = db.Column(db.Boolean, default=False)
    content_id = db.Column(db.Integer, db.ForeignKey("content.id"))
