from fastapi import FastAPI
import json
import random

source_data: str = "{'CA': 20218, 'VT': 559, 'OR': 1706, 'WA': 3228, 'IL': 1849, 'ID': 251, 'WI': 909, 'IA': 500, 'NJ': 1887, " \
"'TX': 3853, 'NY': 5685, 'SC': 691, 'CT': 1602, 'OH': 1963, 'WV': 197, 'MO': 1365, 'GA': 2430, 'UT': 1042, 'KS': 593, " \
"'FL': 4501, 'MA': 4427, 'CO': 2880, 'MI': 2102, 'NC': 1951, 'VA': 1831, 'TN': 1151, 'AL': 573, 'AZ': 1560, 'HI': 411, " \
"'MD': 1721, 'MN': 1181, 'AR': 373, 'RI': 343, 'PA': 2105, 'LA': 282, 'DC': 328, 'ME': 676, 'KY': 420, 'MS': 227, 'SD': 123, " \
"'DE': 240, 'IN': 742, 'NM': 484, 'OK': 408, 'ND': 109, 'NH': 318, 'NE': 329, 'NV': 661, 'WY': 121, 'AK': 77, 'MT': 161, " \
"'PR': 31}"

state_counts = json.loads(source_data.replace('\'', '\"'))
fuel_stations = []

for state in state_counts:
    for _ in range(int(state_counts[state])):
        fuel_stations.append({'state': state})
random.shuffle(fuel_stations)

response = {'fuel_stations': fuel_stations}

app = FastAPI()

@app.get('/')
def get_dummy_data() -> dict:
    return response