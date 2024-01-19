from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#extract URLs from file
urls = []
with open('links.txt', 'r') as file:
    content = file.read()
    urls = [url.strip().strip("'\"") for url in content.split(',')]

open('results.csv', 'w').close()

for url in urls:
    # Open the webpage
    scrape_url = 'https://www.similarweb.com/website/' + url + '/#overview'
    driver.get(scrape_url)

    # Wait for the dynamic content to load
    wait = WebDriverWait(driver, 10)
    
    #CSS selector to target the elements
    total_visits_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".engagement-list__item-value")))
    bounce_rate_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".engagement-list__item:nth-of-type(2) .engagement-list__item-value")))
    pages_per_visit_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".engagement-list__item:nth-of-type(3) .engagement-list__item-value")))
    average_visit_duration_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".engagement-list__item:nth-of-type(4) .engagement-list__item-value")))

    # extracting values from the elements
    total_visits = total_visits_element.text
    bounce_rate = bounce_rate_element.text
    pages_per_visit = pages_per_visit_element.text
    average_visit_duration = average_visit_duration_element.text


    # Printing the results for debugging
    print(f"URL: {url}")
    print(f"Total Visits for {url}: {total_visits}")
    print(f"Bounce Rate for {url}: {bounce_rate}")
    print(f"Pages per Visit for {url}: {pages_per_visit}")
    print(f"Average Visit Duration for {url}: {average_visit_duration}")
   
    
    with open('results.csv', 'a') as f:
        f.write(f"{url},")
        f.write(f"{total_visits},")
        f.write(f"{bounce_rate},")
        f.write(f"{pages_per_visit},")
        f.write(f"{average_visit_duration}\n")

    
    time.sleep(1)

driver.quit()
