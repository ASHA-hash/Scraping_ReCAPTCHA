from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time

from solveRecaptcha import solveRecaptcha

url = "https://kboc.kansas.gov/verify/"
sitekey = "6LdhH5opAAAAAEpg8kLw5GKoOq6MBKbcxMZXzLrj"

# Step 1: Initialize the WebDriver and open the URL
print("Initializing the WebDriver and opening the URL...")
driver = webdriver.Chrome()
driver.get(url)

# Step 2: Solve the reCaptcha
print("Solving reCaptcha...")
result = solveRecaptcha(
    sitekey=sitekey,
    url=url
)

# Step 3: Extract the reCaptcha response token
print("Extracting reCaptcha response token...")
code = result['code']
print(f"Solved reCaptcha token: {code}")

time.sleep(5)

# Step 5: Inject the reCaptcha token into the hidden field
print("Injecting the reCaptcha token into the hidden field...")
recaptcha_response = code
driver.execute_script("document.getElementById('g-recaptcha-response').value = arguments[0];", recaptcha_response)

# Step 6: Set the action value for form submission
print("Setting the action value for form submission...")
driver.execute_script("document.getElementById('action').value = 'verifySearch';")

# Trigger the callback function (replace 'showSearch' with the actual callback function name)
driver.execute_script("showSearch(arguments[0]);", recaptcha_response)


# Step 7: Wait for the search options to appear
print("Waiting for the search options to appear...")
time.sleep(15)

# Step 8: Fill the input fields on the form
print("Filling the input fields on the form...")
license_type = 'Cosmetologist'
# license_number = '000-25135'
license_number = '000-86184'
time.sleep(5)
# Step 9: Select the License Type from the dropdown
print("Selecting the License Type from the dropdown...")
select_xpath = "/html/body/div[1]/div/div/div/main/div[2]/form/div[2]/div/div[1]/div/div[1]/div/select"
select_click = driver.find_element(By.XPATH, select_xpath)
select_click.click()
select = Select(driver.find_element(By.XPATH, select_xpath))
time.sleep(5)
select.select_by_visible_text(license_type)

# Step 10: Fill the License Number
print("Filling the License Number...")
license_number_xpath = "/html/body/div[1]/div/div/div/main/div[2]/form/div[2]/div/div[1]/div/div[2]/div/input"
driver.find_element(By.XPATH, license_number_xpath).send_keys(license_number)

# Step 11: Submit the form (find the search button and click it)
print("Submitting the form by clicking the search button...")
search_button_xpath = "/html/body/div[1]/div/div/div/main/div[2]/form/div[2]/div/div[1]/div/div[7]/button"
search_button = driver.find_element(By.XPATH, search_button_xpath)
search_button.click()

# Step 12: Wait for the results page to load
print("Waiting for the results page to load...")
time.sleep(5)

# Step 13: Save the results page as HTML
print("Saving the results page as HTML...")
with open('000-25135_5.html', 'w', encoding='utf-8') as file:
    file.write(driver.page_source)

# Step 14: Close the browser
print("Closing the browser...")
driver.quit()

print("Script execution completed.")
