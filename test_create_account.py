#!/usr/bin/env python


import time
import unittest

import seemal.sign_up_page
import sign_up_page as s
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

browser = webdriver.Chrome(executable_path='/usr/bin/chromedriver')

action = ActionChains(browser)

browser.get("http://automationpractice.com/index.php")

time.sleep(3)


class TestLogin(unittest.TestCase):

    def setUp(self):
        pass


    def test_create_account_with_all_fields(self):
        out = s.create_account_with_all_fields(browser,s.Enums.user_1,s.Enums.user_1_first,s.Enums.user_1_last)
        s.click_by_xpath(browser , s.Xpaths.sign_out)
        self.assertIn(s.Enums.success_msg , out, msg = "Account not creared successfully")

    def test_verify_login_for_registered_account(self):
        verify = {}
        user_1 = s.create_account_with_all_fields(browser,s.Enums.user_1,s.Enums.user_1_first,s.Enums.user_1_last,login=True)

        ##logout after creation
        s._sign_out_account(browser)

        _name1 = s._verify_login_of_account(browser ,user_1,s.Enums.pwd)
        expected = s.Enums.user_1_first + " " + s.Enums.user_1_last

        verify['Account # 1 ->> Successful Login'] = expected in _name1

        ##logout after creation
        s._sign_out_account(browser)



        user_2 = s.create_account_with_all_fields(browser,s.Enums.user_2,s.Enums.user_2_first,s.Enums.user_2_last,login=True)

        ##logout after creation
        s._sign_out_account(browser)

        _name2 = s._verify_login_of_account(browser, user_2, s.Enums.pwd)
        expected = s.Enums.user_2_first + " " + s.Enums.user_2_last

        verify['Account # 2 ->> Successful Login'] = expected in _name2

        ##logout after creation
        s._sign_out_account(browser)

        user_3 = s.create_account_with_all_fields(browser,s.Enums.user_3,s.Enums.user_3_first,s.Enums.user_3_last,login=True)
        ##logout after creation
        s._sign_out_account(browser)

        _name3 = s._verify_login_of_account(browser, user_3, s.Enums.pwd)
        print(_name3)
        expected = s.Enums.user_3_first + " " + s.Enums.user_3_last

        verify['Account # 3 ->> Successful Login'] = expected in _name3

        ##logout after creation
        s._sign_out_account(browser)


        print(verify)
        self.assertTrue(all(verify.values()), msg='Account Login Failed')

    def test_if_any_non_mandatory_filed_is_missing(self):
        s.create_account_with_all_fields(browser, s.Enums.user_1, s.Enums.user_1_first, s.Enums.user_1_last,
                                                  login=True ,non_mandatory=True )


        out = s._get_text_by_xpath(browser, s.Xpaths.account_title)

        ##logout after creation
        s._sign_out_account(browser)

        expected = s.Enums.user_1_first + " " + s.Enums.user_1_last

        res = expected in out
        self.assertTrue(res , msg="Account creation is successful")

    def test_if_any_mandatory_filed_is_missing(self):
        out = s.create_account_with_all_fields(browser, s.Enums.user_1, s.Enums.user_1_first, s.Enums.user_1_last, mandatory=True)
        res = s.Enums.alert in out
        self.assertTrue(res, msg="Error message is not appearing")

    def test_failed_attempt_to_login(self):
        out = s._verify_login_of_account(browser, s.Enums.demo_email, s.Enums.pwd , login=False)
        res = s.Enums.alert in out
        self.assertTrue(res, msg="Error message is not appearing")

    def test_addition_and_delete_of_product_in_card(self):
        verify = {}
        s.title_click(browser)
        out , msg = s._add_card(browser)
        print(out)
        print("here",msg)
        verify['Item added in card successfully'] = out

        verify['Card deleted Successfully'] = s.Enums.empty_warning_msg in msg
        print(verify)

        self.assertTrue(all(verify.values()), msg='Account Login Failed')


if __name__ == '__main__':
    unittest.main()