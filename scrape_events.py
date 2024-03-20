import feedparser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
import json

class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super(DateTimeEncoder, self).default(obj)

def convert_date_string(date_string):
    # Remove the trailing ' to' on the start date
    date_string = date_string.rstrip(' to')

    date_format = "%A, %B %d %Y at %I:%M %p %Z"

    # Convert the string to a datetime object
    datetime_object = datetime.strptime(date_string, date_format)

    return datetime_object

def create_event_JSON(title, location, hostID, hostName, startDate, endDate):
    event = {
        "title": title,
        "location": location,
        "hostID": hostID,
        "hostName": hostName,
        "startDate": startDate,
        "endDate": endDate
    }
    return event

# Set up the WebDriver
webdriver_options = Options()
webdriver_options.add_argument('--headless')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=webdriver_options)

# Parse RSS feed
feed_url = "https://gonzaga.campuslabs.com/engage/events.rss"
feed = feedparser.parse(feed_url)

# create list of event id's
event_urls = []
for entry in feed.entries:
    event_urls.append(entry.id)

# Scrape the event pages
events = []
for i in range(5):
    print('Scraping Event: ', event_urls[i])
    # Open the event page
    driver.get(event_urls[i])

    # Extract the data
    title = driver.find_element(By.TAG_NAME, 'h1').text
    location = driver.find_element(By.XPATH, "//strong[text()='Location']/following::div/p").text
    hostID = driver.find_element(By.XPATH, "//h2[text()='Host Organization']/following::a").get_attribute('href') # this is already a string
    hostName = driver.find_element(By.XPATH, "//h2[text()='Host Organization']/following::h3").text
    dateTimes = driver.find_elements(By.XPATH, "//strong[text()='Date and Time']/following::p")
    startDate = convert_date_string(dateTimes[0].text)
    endDate = convert_date_string(dateTimes[1].text)
    
    # create JSON object
    event = create_event_JSON(title, location, hostID, hostName, startDate, endDate)
    events.append(event)

# Close the WebDriver
driver.quit()

print(json.dumps(events, cls=DateTimeEncoder, indent=4))
