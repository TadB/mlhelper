from app import create_app, db
from app.models import Content, Image, Task
from app.main.parser import get_website_content
from rq import get_current_job


app = create_app()
app.app_context().push()


def add_content(content_id):
    content = Content.query.filter_by(id=content_id).first()
    web_text = get_website_content(content.url)
    job = get_current_job()
    task = Task.query.get(job.get_id())

    if content.text is None:
        content.text = web_text
        task.complete = True
        db.session.commit()
