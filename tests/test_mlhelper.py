import json

web_url = "https://niebezpiecznik.pl/post/nic-nie-jest-bezpieczne-jesli-nie-zabezpieczysz-drukarki-urzadzenia-wielofunkcyjne-to-otwarte-drzwi-do-wrazliwych-danych-w-firmie/"


def test_add_content(client):
    response = client.post('/add/text',
                           data=json.dumps(dict(url=web_url)),
                           content_type='application/json')

    # assert b'Task successfully added to queue' in response.data
    # testing before adding tasks to queue option
    assert b'Text added to database' in response.data


def test_download_resources():
    pass


def test_add_images(client):
    response = client.post('/add/img',
                           data=json.dumps(dict(url=web_url)),
                           content_type='application/json')
    assert b'Images added to database' in response.data


def test_check_add_content_status_done():
    pass


def test_check_add_content_status_in_progress():
    pass


def test_check_add_images_status_done():
    pass


def test_check_add_images_status_in_progress():
    pass
