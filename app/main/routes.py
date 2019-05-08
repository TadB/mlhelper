from app import db
from app.models import Content, Image
from flask import request, jsonify
from app.main.parser import get_website_content, save_image, get_images
from app.main import bp


@bp.route('/add/text', methods=['POST'])
def add_content():
    website = request.get_json()
    web_url = website['url']
    web_text = get_website_content(web_url)
    content = Content.query.filter_by(url=web_url).first()
    if content is not None:
        # update existing object
        if content.text is not None:
            content.text = web_text
        else:
            # content text exists
            ret_data = {'msg': 'Text for this website already exists in db'}
            return jsonify(ret_data)
    else:
        # create new entry
        content = Content(text=web_text, url=web_url)
        db.session.add(content)
    db.session.commit()
    # ret_data = {'msg': 'Task successfully added to queue'}
    ret_data = {'msg': 'Text added to database'}
    result = jsonify(ret_data)
    return result


@bp.route('/add/img', methods=['POST'])
def add_images():
    website = request.get_json()
    web_url = website['url']
    content = Content.query.filter_by(url=web_url).first()
    if content is None:
        # content not created yet
        content = Content(url=web_url)
        db.session.add(content)
    # add image paths to database and save to storage
    # TODO: check if images for url already exists
    for img_url in get_images(web_url):
        img_path = save_image(img_url)
        img = Image(content_id=content.id, path=img_path)
        db.session.add(img)
    db.session.commit()
    return jsonify({'msg': 'Images added to database'})


@bp.route('/download', methods=['GET'])
def download():
    website = request.get_json()
    web_url = website['url']
    content = Content.query.filter_by(url=web_url).first()
    if content is None:
        return jsonify({'msg': 'Data for this url does not exits '})
    images = Image.query.filter_by(content_id=content.id)



