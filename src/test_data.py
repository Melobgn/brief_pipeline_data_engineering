import requests

BASE_URL = "https://d37ci6vzurychx.cloudfront.net/trip-data"
YEAR = 2025

for month in range(1, 4):  # teste janvier à mars
    url = f"{BASE_URL}/yellow_tripdata_{YEAR}-{month:02d}.parquet"
    r = requests.head(url)
    print(url, "->", r.status_code)