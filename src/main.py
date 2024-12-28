import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Define the URL
url = "https://info.classroomav.vt.edu/RoomSchedule.aspx"  # Replace with the actual URL

# Step 2: Send a GET request
response = requests.get(url)
if response.status_code == 200:
    print("Page fetched successfully!")
else:
    print(f"Failed to fetch page, status code: {response.status_code}")
    exit()

# Step 3: Parse the page content
soup = BeautifulSoup(response.text, 'html.parser')

# Step 4: Locate the data (example with tables or specific div elements)
# Replace with specific tags/IDs/classes used by the page
data = []
table = soup.find('table', {'id': 'building-occupancy'})  # Example: Find a table by ID
if table:
    rows = table.find_all('tr')
    for row in rows[1:]:  # Skip the header row
        cols = row.find_all('td')
        data.append([col.text.strip() for col in cols])



print(soup) 
