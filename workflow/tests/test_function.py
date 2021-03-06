from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait

class FunctionalTest(LiveServerTestCase):
    def setUp(self):
        self.selenium = webdriver.Firefox()
        self.selenium.maximize_window()
        super(FunctionalTest, self).setUp()

    def login(self):
        self.selenium.get(
            '%s%s' % (self.live_server_url, "/workflow/login/")
        )
        username = self.selenium.find_element_by_id("id_username")
        password = self.selenium.find_element_by_id("id_password")
        username.send_keys("zxiong")
        password.send_keys("tsl")
        login_submit = self.selenium.find_element_by_id("login")
        login_submit.click()

    def tearDown(self):
        self.selenium.quit()
        super(FunctionalTest, self).tearDown()

    def test_functions(self):
        self.login()
        self.create_assignment()
        self.edit_article()
        self.selenium.get(
            '%s%s' % (self.live_server_url, "/workflow/logout/")
        )

    def create_assignment(self):
        self.selenium.get(
            '%s%s' % (self.live_server_url, "/workflow/assignments/new/")
        )
        title = self.selenium.find_element_by_id("id_title")
        content = self.selenium.find_element_by_id("id_content")
        section = self.selenium.find_element_by_id("id_section")
        type = self.selenium.find_element_by_id("id_type")
        receiver = self.selenium.find_element_by_id("id_receiver")
        due_date = self.selenium.find_element_by_id("id_due_date")
        title.send_keys('Take photo of Oldenborg')
        content.send_keys('Go into Oldenborg during lunch, and take a picture of their apples')
        Select(section).select_by_visible_text("News")
        Select(type).select_by_visible_text("Photo Assignment")
        Select(receiver).select_by_visible_text("kshikama")
        due_date.clear()
        due_date.send_keys("03/11/2011")
        submit = self.selenium.find_element_by_id("submit_assignment")
        submit.click()
        title = self.selenium.find_element_by_css_selector('a[href="/workflow/assignments/3/"]')
        assert "Take photo of Oldenborg" in title.text

    def edit_article(self):
        self.selenium.get(
            '%s%s' % (self.live_server_url, "/workflow/articles/issue/85/2906/")
        )
        # Workflow Article Page
        edit = self.selenium.find_element_by_id("edit")
        edit.click()

        # Edit Article Page
        title = self.selenium.find_element_by_id("id_title")
        title.clear()
        title.send_keys("Pomona to Open Millikan to Math and Physics Faculty by June 1")

        ckeditor = self.selenium.find_element_by_class_name("cke_wysiwyg_frame")
        self.selenium.switch_to.frame(ckeditor)
        content = self.selenium.find_element_by_tag_name('body')
        content.clear()
        content.send_keys("""Walking through the Robert A. Millikan Laboratory, Pomona College's new physics and mathematics building, it is easy to visualize what the building will look like next fall. Light from the ceiling's skylight reaches all three floors, helping to illuminate the scattered study spaces and blackboards. A floating staircase connects the first floor to the second floor, where the atom sculpture from the original Millikan can be seen in the window. Although workers are still putting the finishing touches on the 75,000-square-foot building, testing lighting and touching up paint, Millikan is almost ready for faculty to move in to their new offices and for spaces to host students.

        The $63 million construction project began in fall 2014 after three years of planning and is scheduled for completion by June 1.

        Assistant Vice President of Facilities and Campus Services Bob Robinson said that the construction process for Millikan was faster than anticipated due to efficient construction methods, careful planning and favorable weather conditions, among other factors.

        """)

        self.selenium.switch_to.default_content()
        section_caret = self.selenium.find_element_by_xpath('/html/body/div/div[1]/form/div[2]/div/span')
        section_caret.click()
        section_caret.click()
        section = self.selenium.find_element_by_xpath('/html/body/div/div[1]/form/div[2]/div/ul/li[3]')
        section.click()

        author_delete = self.selenium.find_element_by_class_name("remove")
        author_delete.click()
        author = self.selenium.find_element_by_id("id_authors-autocomplete")
        author.send_keys("kshik")
        author_select = WebDriverWait(self.selenium, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="id_authors-wrapper"]/span[2]/span')))
        author_select.click()
        submit = self.selenium.find_element_by_id("edit")
        submit.click()