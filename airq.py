import requests

url = 'https://api.openaq.org/v1/measurements'

headers = { 'X-API-Key': '5978ddd26696c3a1aa32b49c02ef63d28b67c2856dff1d19e471cf1903011b6c'}

# Set params for the request
params = {
    'city': 'Los Angeles',
    'datetime': '2023-09-01T00:00:00',
    'limit': 10,
    'order_by': 'date',
    'sort': 'desc'
}

try:
    response = requests.get(url, headers=headers, params=params, timeout=10)

    if response.status_code == 200:
        data = response.json()
        print("Air quality for LA: ")
        for measurement in data['results']:
            print(f"Parameter: {measurement['parameter']}, Value: {measurement['value']}, Unit:           {measurement['unit']}, Date: {measurement['date']['utc']}")
    else:
        print(f"Error: {response.status_code} - {response.text}")

except (ConnectionError, Timeout) as e:
    print(f"Connection error occurred: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
