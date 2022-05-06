from beerlog.core import add_beer_to_database, get_beers_from_database


def test_add_beer_to_database():
    assert add_beer_to_database('Blue Moon', 'Witbier', 10, 3, 6)


def test_get_beers_from_database():
    results = get_beers_from_database()
    assert len(results) > 0
