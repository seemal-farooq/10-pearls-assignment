#!/usr/bin/env python

import time
import random
import string



class Enums(object):

    user_1 = 'admin_user1{}_test@gmail.com'
    user_1_first = 'Admin'
    user_1_last = 'Tester'



    user_2 = 'admin_user2{}_test@gmail.com'
    user_2_first = 'Tesoro'
    user_2_last = 'Tester'

    user_3 = 'admin_user3{}_test@gmail.com'
    user_3_first = 'John'
    user_3_last = 'Tester'
    pwd = 'tester123'

    May = 'May'
    June = 'June'
    Aug = 'August'

    year1 = '1990'
    year2 = '1991'
    year3 = '1992'

    state1 = 'California'
    state2 = 'Delaware'
    state3 = 'Alaska'

    city = 'lahore'
    company = 'abc'

    code = '12345'

    address1 = 'House no 1 , Stree no 1 , lahore'
    f_address = 'Karachi'

    home = '012345678'
    home1 = '5454851585'

    success_msg = 'Welcome to your account. Here you can manage all of your personal information and orders.'
    alert = 'There is 1 error'

    demo_email = 'demo@auto.com'
    card_success = 'Product successfully added to your shopping cart'
    empty_warning_msg = 'Your shopping cart is empty.'


class Xpaths(object):
    sign_in_button = "//div//a[contains(@class,'login')]"
    enter_email = '//input[@type="text" and @name="email_create"]'
    submit_email = '//button[@id="SubmitCreate"]//span'

    first_name = '//input[@name="customer_firstname"]'
    last_name = '//input[@name="customer_lastname"]'
    password = '//input[@name="passwd"]'


    day_dropdown = '//div[@id="uniform-days"]'
    select_day = '//select[@id="days"]//option[@value="{}"]'
    month_dropdown = '//div[@id="uniform-months"]'
    select_month = '//select[@id="months"]//option[contains(. , "{}")]'
    year_dropdown = '//div[@id="uniform-years"]'
    select_year = '//select[@id="years"]//option[contains(. , "{}")]'


    #address
    a_first_name = '//input[@name="firstname"]'
    a_last_name = '//input[@name="lastname"]'
    a_company = '//input[@name="company"]'
    a_address1 = '//input[@name="address1"]'
    a_address2 = '//input[@name="address2"]'
    a_city = '//input[@name="city"]'
    state_dropdown = '//div[@id="uniform-id_state"]'
    select_state = '//select[@id="id_state"]//option[contains(. , "{}")]'
    a_zip_code = '//input[@name="postcode"]'
    home_no = '//input[@name="phone"]'
    mob_no = '//input[@name="phone_mobile"]'
    register = '//button[@id="submitAccount"]'
    f_address = '//input[@name="alias"]'

    account_info = '//p[contains(@class,"info-account")]'
    sign_out = '//div//a[@title="Log me out"]'

    #login
    login_email = '//input[@id="email"]'
    login_pwd = '//input[@id="passwd"]'
    login_btn = '//button[@id="SubmitLogin"]//span'
    account_title = '//div//a[@title="View my customer account"]'
    alert = '//div[contains(@class,"alert-danger")]//p'


#method

def get_random_string(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def click_by_xpath(browser , xpath):
    _find = browser.find_element_by_xpath(xpath)
    _find.click()

def _sign_out_account(browser):
    click_by_xpath(browser, Xpaths.sign_out)
    time.sleep(5)

def _enter_text_by_xpath(browser , xpath , text):
    _find = browser.find_element_by_xpath(xpath)
    _find.send_keys(text)

def _get_text_by_xpath(browser,xpath):
    elem = browser.find_element_by_xpath(xpath)
    txt = elem.text
    return txt

def create_account_with_all_fields(browser,email , f_name , l_name , login=False , non_mandatory=False , mandatory=False):

    sign_in_button = Xpaths.sign_in_button
    click_by_xpath(browser , sign_in_button)

    enter_email = Xpaths.enter_email
    user_email = email.format(get_random_string(3))
    _enter_text_by_xpath(browser , enter_email,user_email)

    submit_email = Xpaths.submit_email
    click_by_xpath(browser , submit_email)

    time.sleep(10)

    ############ account info ##########3

    first_name = Xpaths.first_name
    _enter_text_by_xpath(browser , first_name,f_name)

    last_name = Xpaths.last_name
    _enter_text_by_xpath(browser , last_name , l_name)

    password = Xpaths.password
    _enter_text_by_xpath(browser , password , Enums.pwd)



    #### date of birth

    click_by_xpath(browser , Xpaths.day_dropdown)
    time.sleep(3)

    click_by_xpath(browser , Xpaths.select_day.format(5))
    time.sleep(3)


    click_by_xpath(browser , Xpaths.month_dropdown)
    time.sleep(3)

    click_by_xpath(browser , Xpaths.select_month.format(Enums.May))
    time.sleep(3)


    click_by_xpath(browser , Xpaths.year_dropdown)
    time.sleep(3)

    click_by_xpath(browser ,Xpaths.select_year.format(Enums.year1))
    time.sleep(3)



    #address

    # first_name = Xpaths.a_first_name
    # _enter_text_by_xpath(browser ,first_name,Enums.user_1_first)
    #
    #
    # last_name = Xpaths.a_last_name
    # _enter_text_by_xpath(browser , last_name,Enums.user_1_last)


    if not non_mandatory:
        company = Xpaths.a_company
        _enter_text_by_xpath(browser , company,Enums.company)

    if not mandatory :
        address = Xpaths.a_address1
        _enter_text_by_xpath(browser , address,Enums.address1)

    if not non_mandatory:
        address2 = Xpaths.a_address2
        _enter_text_by_xpath(browser , address2,Enums.address1)


    city = Xpaths.a_city
    _enter_text_by_xpath(browser , city, Enums.city)

    click_by_xpath(browser , Xpaths.state_dropdown)
    time.sleep(3)

    click_by_xpath(browser , Xpaths.select_state.format(Enums.state1))
    time.sleep(3)

    code = Xpaths.a_zip_code
    _enter_text_by_xpath(browser , code,Enums.code)

    home = Xpaths.home_no
    _enter_text_by_xpath(browser , home,Enums.home)


    phone = Xpaths.mob_no
    _enter_text_by_xpath(browser , phone,Enums.home1)

    f_address = Xpaths.f_address
    _enter_text_by_xpath(browser , f_address,Enums.f_address)



    register = Xpaths.register
    click_by_xpath(browser,register)

    time.sleep(10)


    if not mandatory:
        out = _get_text_by_xpath(browser, Xpaths.account_info)

        time.sleep(5)
        if login:
            return user_email
        else:
            return out
    else:
        return  _get_text_by_xpath(browser,Xpaths.alert)

def _verify_login_of_account(browser , email , pwd , login=True):
    sign_in_button = Xpaths.sign_in_button
    click_by_xpath(browser, sign_in_button)
    time.sleep(3)

    _enter_text_by_xpath(browser,Xpaths.login_email,email)

    _enter_text_by_xpath(browser,Xpaths.login_pwd,pwd)

    click_by_xpath(browser,Xpaths.login_btn)

    time.sleep(8)
    if login:
        return  _get_text_by_xpath(browser,Xpaths.account_title)
    else:
        return  _get_text_by_xpath(browser,Xpaths.alert)

def is_element_present(browser, xpath):
    e = browser.find_element_by_xpath(xpath)
    st = True
    return st

def title_click(browser):
    title = '//a[@title="My Store"]//img'
    click_by_xpath(browser,title)
    time.sleep(10)

def _add_card(browser):
    item = '//h5//a[@title="Blouse"]'
    click_by_xpath(browser,item)
    time.sleep(15)

    add_to_cart = '//div//p[@id="add_to_cart"]//button'
    click_by_xpath(browser,add_to_cart)

    card_success = '//div[contains(@class,"layer_cart_product")]//h2'
    out = is_element_present(browser,card_success)

    time.sleep(10)
    close_popup = '//div//span[@title="Close window"]'
    click_by_xpath(browser,close_popup)

    view_my_cart = '//a[@title="View my shopping cart"]'
    click_by_xpath(browser,view_my_cart)
    time.sleep(7)
    delete_cart = '//div//a[@title="Delete"]//i'
    click_by_xpath(browser,delete_cart)
    time.sleep(5)
    empty_warning = '//p[contains(@class,"alert-warning")]'
    text = _get_text_by_xpath(browser , empty_warning)
    return out , text

