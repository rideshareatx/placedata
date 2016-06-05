import simplejson as json
from os.path import join
from shapely.geometry import shape
import geocoder
import os
from sys import stdout
import requests

root_dir = os.path.dirname(os.path.realpath(__file__))
#
# server_url = 'http://localhost:8080'
#
# auth = {'grant_type': 'password', 'username': 'test', 'password': 'password'}
#
# token = requests.post(server_url+'/management/token', data=auth).json()
#
# org = 'test-organization'
# app = "newapp"
# url = server_url+'/{}/{}/place?access_token={}'.format(org, app, token['access_token'])
#

def buildings():
    with open(join(root_dir, 'geojson', 'austin_texas_buildings.geojson')) as f:
        austin = json.load(f)['features']
        for bldg in austin:
            pnt = list(shape(bldg['geometry']).centroid.coords[0])
            pnt.reverse()
            loc = geocoder.osm(pnt, method="reverse").json
            loc['name'] = loc['osm_id']
            fields_to_remove = ['encoding', 'status_code', 'confidence', 'provider', 'accuracy', 'status', 'importance',
                                'icon', 'osm_type', 'place_rank', 'lat', 'lng']
            yield {k: loc[k] for k in loc if k not in fields_to_remove}

with open(join(root_dir, 'buildings.txt'), 'w+') as f:
    for i, bldg in enumerate(buildings()):
        f.write("{}\n".format(json.dumps(bldg)))
        stdout.write("\r{} buildings.".format(i))
        stdout.flush()
    stdout.write('\n')
    stdout.flush()

# for i, bldg in enumerate(buildings()):
#     r = requests.put(url, data=json.dumps(bldg))
#     print "{}: {}".format(i, r)