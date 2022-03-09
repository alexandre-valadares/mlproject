from curses import halfdelay
from mlproject.distance import haversine

def test_coord():
    # Le Wagon location
    lat1, lon1 = 48.865070, 2.380009
    #Insert your coordinates from google maps here
    lat2, lon2 = 23.543171, 46.64252
    distance = haversine(lon1, lat1, lon2, lat2)
    assert  distance > 0
