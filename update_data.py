from dotenv import dotenv_values
import pandas as pd
import requests
import gspread
from google.oauth2.service_account import Credentials

def retrieve_fuel_station_data(api_key: str, 
                               request_url: str = 'https://developer.nlr.gov/api/alt-fuel-stations/v1.json'
                               ) -> dict[str, int]:

    request_parameters = {
        'api_key': api_key,
        'status': 'E,T',
        'access': 'public',
        'fuel_type': 'ELEC'
    }

    response = requests.get(request_url, request_parameters).json()

    stations = response['fuel_stations']

    station_counts_per_state = {}

    for station in stations:
        state = station['state']
        if state not in station_counts_per_state:
            station_counts_per_state[state] = 0
        station_counts_per_state[state] += 1

    return station_counts_per_state


def update_google_sheet(station_counts_per_state: dict[str, int], 
                        sheet_id: str = '1FmMJVAk6W1L2veZvVDxvsMcP87MpYYxukhWnmuGm3no') -> None:
    
    scopes = ['https://www.googleapis.com/auth/spreadsheets']
    creds = Credentials.from_service_account_file('credentials.json', scopes=scopes)
    client = gspread.authorize(creds)

    sheet = client.open_by_key(sheet_id)

    states = sheet.sheet1.col_values(1)

    for row, state in enumerate(states):
        count =  station_counts_per_state[str(state)] if str(state) in station_counts_per_state else 0
        sheet.sheet1.update_cell(row + 1, 2, count)

    for s, c in zip(sheet.sheet1.col_values(1), sheet.sheet1.col_values(2)):
        print(f'{s}: {c}')


if __name__ == '__main__':

    config = dotenv_values('.env')

    api_key = config['API_KEY']

    if api_key is None:
        raise Exception('.env file is missing NLR API key')

    station_counts_per_state = retrieve_fuel_station_data(api_key, 'http://127.0.0.1:8000')

    update_google_sheet(station_counts_per_state)