from app.parser import get_website_content


def test_get_website_content():
    with open('test_page/niebezpiecznik_post_text.txt', 'r') as f:
        target = f.read()
    web_content = get_website_content('https://niebezpiecznik.pl/post/nic-nie-jest-bezpieczne-jesli-nie-zabezpieczysz-drukarki-urzadzenia-wielofunkcyjne-to-otwarte-drzwi-do-wrazliwych-danych-w-firmie/')
    assert target == web_content
