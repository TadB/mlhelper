from app import create_app, db
from app.models import Content, Image, Task
from app.main.parser import get_website_content, get_images, save_image
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


def add_images(content_id):
    content = Content.query.filter_by(id=content_id).first()
    web_url = content.url
    job = get_current_job()
    task = Task.query.get(job.get_id())

    for img_url in get_images(web_url):
        img_path = save_image(img_url)
        img = Image(content_id=content.id, path=img_path)
        db.session.add(img)
    task.complete = True
    db.session.commit()
