from selenium import webdriver

# Workflow Login Page
from website import settings

selenium = webdriver.Chrome()
selenium.maximize_window()
selenium.get("http://localhost:8000/workflow/album/86/4263/")
username = selenium.find_element_by_id("id_username")
password = selenium.find_element_by_id("id_password")
username.send_keys("zxiong")
password.send_keys("tsl")
login_submit = selenium.find_element_by_id("login")
login_submit.click()

# Workflow Album View Page
edit = selenium.find_element_by_id("edit")
edit.click()

# Workflow Album Edit Page
upload1 = selenium.find_element_by_id("id_photo_set-0-image")
upload1.send_keys(str(settings.BASE_DIR) + "/website/fixtures/goldengatebridge.jpg")
selenium.find_element_by_xpath('//*[@id="id_photo_set-0-credit"]/option[3]').click()

upload2 = selenium.find_element_by_id("id_photo_set-1-image")
upload2.send_keys(str(settings.BASE_DIR) + "/website/fixtures/pearlharbor.jpg")
selenium.find_element_by_xpath('//*[@id="id_photo_set-1-credit"]/option[3]').click()

submit = selenium.find_element_by_id("edit")
submit.click()

# Article - When Nerdy Becomes Trendy
selenium.get("http://localhost:8000/workflow/album/86/4264/")
# Workflow Album View Page
edit = selenium.find_element_by_id("edit")
edit.click()

# Workflow Album Edit Page
upload3 = selenium.find_element_by_id("id_photo_set-0-image")
upload3.send_keys(str(settings.BASE_DIR) + "/website/fixtures/ramune.jpg")
selenium.find_element_by_xpath('//*[@id="id_photo_set-0-credit"]/option[4]').click()

submit = selenium.find_element_by_id("edit")
submit.click()

selenium.get("http://localhost:8000/workflow/logout/")