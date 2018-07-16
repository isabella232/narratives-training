import json

with open('annual_aqi_2017_2.geojson') as f:
    data = json.load(f)
    for item in data['features']:
        item['properties']['Max AQI'] = int(item['properties']['Max AQI'].replace('.00', ''))


    # output dict to file
    with open('annual_aqi_2017_updated_2.geojson', 'w') as f:
        json.dump(data, f)
