import json

import requests

from src.database import db

locations_endpoint = 'https://ic.emich.edu/api/external/mapitems'
response = requests.get(locations_endpoint)

location_types = {'building', 'parking'}


def transform_location(location):
    return {
        'emu_id': location['id'],
        'name': location['name'],
        'type': location['itemType'],
        'address': location.get('address'),
        'latitude': location['latitudeSatellite'],
        'longitude': location['longitudeSatellite'],
    }


def filter_location(location):
    if location['itemType'] not in location_types:
        return False
    if location['itemType'] == 'parking' and 'Parking Meter' in location['name']:
        return False
    return True


locations = response.json()
transformed_locations = [transform_location(location) for location in locations if filter_location(location)]

print(f'Filtered {len(transformed_locations)}/{len(locations)} locations')

if input('Write to file? y/n: ') == 'y':
    fname = 'locations.json'
    print(f'Writing json to {fname}')
    fp = open(fname, 'w')
    json.dump(transformed_locations, indent=2, fp=fp)
    fp.close()
else:
    print(json.dumps(transformed_locations, indent=2))

if input('Write to locations table? y/n: ') == 'y':
    print('Writing to postgres locations table')
    cursor = db.cursor()
    cursor.executemany(
        """
        insert into locations (emu_id, name, type, address, latitude, longitude)
        values (%(emu_id)s, %(name)s, %(type)s, %(address)s, %(latitude)s, %(longitude)s)
        """,
        transformed_locations)
    db.commit()
