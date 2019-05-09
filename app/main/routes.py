import io
import zipfile
import os
from os.path import basename
from app import db
from app.models import Content, Image
from flask import request, jsonify, current_app as app, send_file
from app.main.parser import save_image, get_images
from app.main import bp


@bp.route("/add/text", methods=["POST"])
def add_content():
    website = request.get_json()
    web_url = website["url"]
    content = Content.query.filter_by(url=web_url).first()
    if content is None:
        content = Content(url=web_url)
        db.session.add(content)
        db.session.commit()
    content.launch_task('add_content')
    db.session.commit()
    ret_data = {"msg": "Task successfully added to queue"}
    result = jsonify(ret_data)
    return result


@bp.route("/add/img", methods=["POST"])
def add_images():
    website = request.get_json()
    web_url = website["url"]
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
    return jsonify({"msg": "Images added to database"})


@bp.route("/download", methods=["GET"])
def download():
    website = request.get_json()
    web_url = website["url"]
    content = Content.query.filter_by(url=web_url).first()
    if content is None:
        return jsonify({"msg": "Data for this url does not exits "})
    images = Image.query.filter_by(content_id=content.id).all()
    data = io.BytesIO()
    with zipfile.ZipFile(data, mode="w") as zf:
        zf.writestr("web_text.txt", content.text)
        for img_path in images:
            file = os.path.join(app.config["IMAGES_FOLDER"], img_path.path)
            zf.write(file, basename(file))
    data.seek(0)
    return send_file(
        data,
        mimetype="application/zip",
        attachment_filename="resources.zip",
        as_attachment=True,
    )
