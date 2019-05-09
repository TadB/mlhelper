from app import create_app, db
from app.models import Content, Image
from app.main.parser import get_website_content


app = create_app()
app.app_context().push()


def add_content(content_id):
    content = Content.query.filter_by(id=content_id).first()
    web_text = get_website_content(content.url)
    if content.text is None:
        content.text = web_text
        db.session.commit()
