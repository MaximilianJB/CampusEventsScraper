import feedparser
import json
from bs4 import BeautifulSoup
import re
from datetime import datetime, timedelta


# URL of the RSS feed
rss_url = 'https://gonzaga.campuslabs.com/engage/events.rss'

# Fetch and parse the RSS feed
feed = feedparser.parse(rss_url)

# Function to extract the description text
def extract_description(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    description_div = soup.find('div', class_='p-description description')
    if description_div:
        return description_div.get_text(strip=True)
    return None

# Extract information
extracted_data = []
for entry in feed.entries:
    description_html = entry.get("description", "")
    description_text = extract_description(description_html)

    extracted_data.append({
        'title': entry.title,
        'link': entry.link,
        'location': entry.get('location', 'Unknown'),
        'host': entry.get('host', 'Unknown'),
        'start_date': entry.start,
        'end_date': entry.end,
        'description': description_text
    })

# Convert data to JSON
json_data = json.dumps(extracted_data, indent=4)

print(json_data)
