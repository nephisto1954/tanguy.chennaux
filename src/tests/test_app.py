from src import routes


def test_homepage():
    assert routes.homepage() == "Hello, TG!"
