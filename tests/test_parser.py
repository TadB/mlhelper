from app.main.parser import get_website_content, get_images


url = "https://niebezpiecznik.pl/post/nic-nie-jest-bezpieczne-jesli-nie-zabezpieczysz-drukarki-urzadzenia-wielofunkcyjne-to-otwarte-drzwi-do-wrazliwych-danych-w-firmie/"


def test_get_website_content():
    with open("tests/test_page/niebezpiecznik_post_text.txt", "r") as f:
        target = f.read()
    web_content = get_website_content(url)
    assert target == web_content


def test_get_images_path():
    f = open("tests/test_page/niebezpiecznik_images_list.txt", "r")
    for img_path in get_images(url):
        # read line and cut unwanted new line character
        line = f.readline().rstrip("\n")
        assert img_path == line
    f.close()
