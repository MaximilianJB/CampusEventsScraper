from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')  # Run in background

# Setup the driver (this will download the driver if not present)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Navigate to the page
driver.get('https://gonzaga.campuslabs.com/engage/events')

# Wait for JavaScript to load
time.sleep(3)

# Find the event-discovery-list div
event_list_div = driver.find_element(By.ID, 'event-discovery-list')

# Find all event card div elements within the event-discovery-list div
event_cards = event_list_div.find_elements(By.CSS_SELECTOR, 'div[class="MuiPaper-root MuiCard-root MuiPaper-elevation3 MuiPaper-rounded"]')  # replace 'event-card-class' with the actual class

# Loop through each event card to extract information
for card in event_cards:
    
    # Assuming the event title is in an 'h3' tag within the event card div
    event_title = card.find_element(By.TAG_NAME, 'h3').text

    
    # Print or save the information as needed
    print(f'Title: {event_title}')

# Close the browser
driver.quit()
