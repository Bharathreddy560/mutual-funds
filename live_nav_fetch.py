"""
Mutual Fund Analytics - Live NAV fetch

Fetches the latest NAV values for selected mutual fund schemes
using the mfapi.in API and stores the results for analysis.

Functions:
- Fetch live NAV
- Handle API responses
- Save latest NAV data

Author: Bandi Bharath
Project: Bluestock Mutual Fund Analytics Capstone
"""
import os
import requests
import pandas as pd

schemes = {
    "HDFC_Top100": 125497,
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_LargeCap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

os.makedirs("data/raw/live_nav", exist_ok=True)

for name, code in schemes.items():
    print(f"Fetching {name}...")

    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()["data"]
        df = pd.DataFrame(data)

        df.to_csv(f"data/raw/live_nav/{name}.csv", index=False)

        print(f"✅ {name} saved successfully.")
    else:
        print(f"❌ Failed to fetch {name}")