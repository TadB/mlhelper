import json


def test_add_content(client):
    response = client.post('/add/content',
                           data=json.dumps(dict(url='some test url')),
                           content_type='application/json')

    assert response.status_code == 201


def test_download_resources():
    pass


def test_add_images():
    pass


def test_check_add_content_status_done():
    pass


def test_check_add_content_status_in_progress():
    pass


def test_check_add_images_status_done():
    pass


def test_check_add_images_status_in_progress():
    pass


def test_check_download_resources_status_done():
    pass


def test_check_download_resources_status_in_progress():
    pass
