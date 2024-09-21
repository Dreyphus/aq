from openaq import OpenAQ
import pandas as pd

client = OpenAQ(api_key='5978ddd26696c3a1aa32b49c02ef63d28b67c2856dff1d19e471cf1903011b6c')
response = client.locations.get(locations_id=2178)
data_dict = response.dict()
df = pd.json_normalize(data_dict['results'])
client.close()
print(df.head())