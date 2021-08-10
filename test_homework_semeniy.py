"""TEST RELATED TO START PAGE"""
from time import sleep

import pytest
import random
import string
from selenium import webdriver

from conftest import BaseTest


class TestLoginPage(BaseTest):

    @pytest.fixture(scope="class")
    def driver(self):
        driver = webdriver.Chrome(executable_path="/Users/slava/PycharmProjects/QaComplexApp/drivers/chromedriver")
        yield driver
        driver.close()

    def test_empty_fields(self, driver):
        """
        - Open start page
        - Clear password and login fields
        - Click on Sign In button
        - Verify error message
        """
        # Open start page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com")
        self.log.info("Open page")

        # Clear fields
        username = driver.find_element_by_xpath(".//input[@placeholder='Username']")
        username.clear()
        password = driver.find_element_by_xpath(".//input[@placeholder='Password']")
        password.clear()
        self.log.info("Fields were cleared")

        # Click on Sign in

        signin = driver.find_element_by_xpath(".//button[contains(text(), 'Sign In')]")
        signin.click()
        self.log.info("Clicked on sign in")

        error_message = driver.find_element_by_xpath(".//div[contains(text(), 'Invalid username / password')]")

        assert error_message.is_displayed()
        self.log.info("Message tested")

    def test_wrong_fields_login(self, driver):
        """
        - Open start page
        - Clear password and login fields
        - Enter any value
        - Click on Sign In button
        - Verify error message
        """

        # Open start page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com")
        self.log.info("Open page")

        # Clear fields
        username = driver.find_element_by_xpath(".//input[@placeholder='Username']")
        username.clear()
        username.send_keys("test")
        password = driver.find_element_by_xpath(".//input[@placeholder='Password']")
        password.clear()
        password.send_keys("test")
        self.log.info("Fields were cleared")

        # Click on Sign in

        signin = driver.find_element_by_xpath(".//button[contains(text(), 'Sign In')]")
        signin.click()
        self.log.info("Clicked on sign in")

        error_message = driver.find_element_by_xpath(".//div[contains(text(), 'Invalid username / password')]")

        assert error_message.is_displayed()
        self.log.info("Message tested")

    def test_success_login(self, driver):
        """
        - Open start page
        - Clear username password and login fields
        - Set any valid values into the username password and login fields
        - Click on Sign up button
        - Verify Sign Out btn is visible
        """

        # Open start page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com")
        self.log.info("Open page")

        # make a random text
        def random_char(y):
            return ''.join(random.choice(string.ascii_letters) for x in range(y))

        # Clear fields
        pick_a_username = driver.find_element_by_xpath(".//input[@placeholder='Pick a username']")
        pick_a_username.clear()
        pick_a_username.send_keys(random_char(8))
        email_filed = driver.find_element_by_xpath(".//input[@placeholder='you@example.com']")
        email_filed.clear()
        email_filed.send_keys(random_char(8) + "@gmail.com")
        password_field = driver.find_element_by_xpath(".//input[@placeholder='Create a password']")
        password_field.clear()
        password_field.send_keys(random_char(12))
        self.log.info("Fields were cleared and filled")

        # Click on Sign up
        signup = driver.find_element_by_xpath(".//button[contains(text(), 'Sign up for OurApp')]")
        sleep(5)
        signup.click()
        self.log.info("Clicked on sign up")

        # Check that sign out btn displayed

        sign_out_btn = driver.find_element_by_xpath(".//button[contains(text(), 'Sign Out')]")
        sleep(5)
        assert sign_out_btn.is_displayed()
        self.log.info("Login tested")

    def test_signout(self, driver):
        """
        - Open start page
        - Clear username password and login fields
        - Set any valid values into the username password and login fields
        - Click on Sign up button
        - Click Sign Out btn
        - Check that Sign up btn is visible
        """

        # Open start page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com")
        self.log.info("Open page")

        # make a random text
        def random_char(y):
            return ''.join(random.choice(string.ascii_letters) for x in range(y))

        # Clear fields
        pick_a_username = driver.find_element_by_xpath(".//input[@placeholder='Pick a username']")
        pick_a_username.clear()
        pick_a_username.send_keys(random_char(8))
        email_filed = driver.find_element_by_xpath(".//input[@placeholder='you@example.com']")
        email_filed.clear()
        email_filed.send_keys(random_char(8) + "@gmail.com")
        password_field = driver.find_element_by_xpath(".//input[@placeholder='Create a password']")
        password_field.clear()
        password_field.send_keys(random_char(12))
        self.log.info("Fields were cleared and filled")

        # Click on Sign up
        signup = driver.find_element_by_xpath(".//button[contains(text(), 'Sign up for OurApp')]")
        sleep(5)
        signup.click()
        self.log.info("Clicked on sign up")

        # Check that my profile btn displayed

        sign_out_btn = driver.find_element_by_xpath(".//button[contains(text(), 'Sign Out')]")
        sleep(5)
        sign_out_btn.click()
        self.log.info("Signout clicked")

        # Check that Sign up btn is vissible

        sleep(5)
        signup = driver.find_element_by_xpath(".//button[contains(text(), 'Sign up for OurApp')]")
        assert signup.is_displayed()
        self.log.info("Sign Up is visible")

    def test_post_creation_without_title_and_text(self, driver):
        """
        - Open start page
        - Clear username password and login fields
        - Set any valid values into the username password and login fields
        - Click on Sign up button
        - Leave all fields empty
        - Click on create new post button
        - Check that user at the same page
        """

        # Open start page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com")
        self.log.info("Open page")

        # make a random text
        def random_char(y):
            return ''.join(random.choice(string.ascii_letters) for x in range(y))

        # Clear fields
        pick_a_username = driver.find_element_by_xpath(".//input[@placeholder='Pick a username']")
        pick_a_username.clear()
        pick_a_username.send_keys(random_char(8))
        email_filed = driver.find_element_by_xpath(".//input[@placeholder='you@example.com']")
        email_filed.clear()
        email_filed.send_keys(random_char(8) + "@gmail.com")
        password_field = driver.find_element_by_xpath(".//input[@placeholder='Create a password']")
        password_field.clear()
        password_field.send_keys(random_char(12))
        self.log.info("Fields were cleared and filled")

        # Click on Sign up
        signup = driver.find_element_by_xpath(".//button[contains(text(), 'Sign up for OurApp')]")
        sleep(5)
        signup.click()
        self.log.info("Clicked on sign up")

        # Click on create new post

        create_post_btn = driver.find_element_by_xpath("./html/body/header/div/div/a[3]")
        sleep(5)
        create_post_btn.click()
        self.log.info("create new post clicked")

        # Click on save new post btn

        sleep(5)
        save_new_post = driver.find_element_by_xpath(".//button[contains(text(), 'Save New Post')]")
        save_new_post.click()
        self.log.info("Save new post clicked")

        # Check that user still at the same page
        save_new_post = driver.find_element_by_xpath(".//button[contains(text(), 'Save New Post')]")
        assert save_new_post.is_displayed()
        self.log.info("Save new post still displayed")

    def test_post_creation(self, driver):
        """
        - Open start page
        - Clear username password and login fields
        - Set any valid values into the username password and login fields
        - Click on Sign up button
        - Click on create new post button
        - Enter any value into new post
        - Check that new post created
        """

        # Open start page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com")
        self.log.info("Open page")

        # make a random text
        def random_char(y):
            return ''.join(random.choice(string.ascii_letters) for x in range(y))

        # Clear fields
        pick_a_username = driver.find_element_by_xpath(".//input[@placeholder='Pick a username']")
        pick_a_username.clear()
        pick_a_username.send_keys(random_char(8))
        email_filed = driver.find_element_by_xpath(".//input[@placeholder='you@example.com']")
        email_filed.clear()
        email_filed.send_keys(random_char(8) + "@gmail.com")
        password_field = driver.find_element_by_xpath(".//input[@placeholder='Create a password']")
        password_field.clear()
        password_field.send_keys(random_char(12))
        self.log.info("Fields were cleared and filled")

        # Click on Sign up
        signup = driver.find_element_by_xpath(".//button[contains(text(), 'Sign up for OurApp')]")
        sleep(5)
        signup.click()
        self.log.info("Clicked on sign up")

        # Click on create new post
        sleep(5)
        create_post_btn = driver.find_element_by_xpath("./html/body/header/div/div/a[3]")
        create_post_btn.click()
        self.log.info("create new post clicked")

        # Enter any value into post fields
        title = driver.find_element_by_id("post-title")
        title.send_keys("test")
        body_cnt = driver.find_element_by_id("post-body")
        body_cnt.send_keys("test2")
        self.log.info("Post fields filled")

        # Click on save new post btn

        sleep(5)
        save_new_post = driver.find_element_by_xpath(".//button[contains(text(), 'Save New Post')]")
        save_new_post.click()
        self.log.info("Save new post clicked")

        # Check that new post created
        new_post_message = driver.find_element_by_xpath(".//div[contains(text(), 'New post successfully created.')]")
        assert new_post_message.is_displayed()
        self.log.info("Save new post still displayed")

    def test_signup_without_username(self, driver):
        """
        - Open start page
        - Clear username password and login fields
        - Set any valid values into the password and login fields (username should be empty)
        - Click on Sign up button
        - Check error message for username field
        """

        # Open start page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com")
        self.log.info("Open page")

        # make a random text
        def random_char(y):
            return ''.join(random.choice(string.ascii_letters) for x in range(y))

        # Clear fields
        pick_a_username = driver.find_element_by_xpath(".//input[@placeholder='Pick a username']")
        pick_a_username.clear()
        email_filed = driver.find_element_by_xpath(".//input[@placeholder='you@example.com']")
        email_filed.clear()
        email_filed.send_keys(random_char(8) + "@gmail.com")
        password_field = driver.find_element_by_xpath(".//input[@placeholder='Create a password']")
        password_field.clear()
        password_field.send_keys(random_char(12))
        self.log.info("Fields were cleared and filled")

        # Click on Sign up
        signup = driver.find_element_by_xpath(".//button[contains(text(), 'Sign up for OurApp')]")
        sleep(5)
        signup.click()
        self.log.info("Clicked on sign up")

        # Check error message for username field
        username_error_message = driver.find_element_by_xpath(
            ".//div[contains(text(), 'Username must be at least 3 characters.')]")
        assert username_error_message.is_displayed()
        self.log.info("Save new post still displayed")
