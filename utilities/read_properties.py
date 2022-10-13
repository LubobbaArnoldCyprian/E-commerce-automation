import configparser

config = configparser.RawConfigParser()
# Incase you're using Mac-Os use command below
# config.read("../Configurations/config.ini")
config.read(".\\Configurations\\config.ini")


class ReadConfig:
    @staticmethod
    def get_application_url():
        url = config.get('Common required information', 'baseURL')
        return url

    @staticmethod
    def get_page_title():
        page_title = config.get('Common required information', 'page_title')
        return page_title

    @staticmethod
    def get_email():
        email = config.get('Common required information', 'email')
        return email

    @staticmethod
    def get_first_name():
        first_name = config.get('Common required information', 'first_name')
        return first_name

    @staticmethod
    def get_last_name():
        last_name = config.get('Common required information', 'first_name')
        return last_name

    @staticmethod
    def get_password():
        password = config.get('Common required information', 'password')
        return password

    @staticmethod
    def get_address_first_name():
        address_first_name = config.get('Common required information', 'address_first_name')
        return address_first_name

    @staticmethod
    def get_address_last_name():
        address_last_name = config.get('Common required information', 'address_last_name')
        return address_last_name

    @staticmethod
    def get_company():
        company = config.get('Common required information', 'company')
        return company

    @staticmethod
    def get_address():
        address = config.get('Common required information', 'address')
        return address

    @staticmethod
    def get_city():
        city = config.get('Common required information', 'city')
        return city

    @staticmethod
    def get_postal_code():
        postal_code = config.get('Common required information', 'postal_code')
        return postal_code

    @staticmethod
    def get_mobile():
        mobile_phone = config.get('Common required information', 'mobile_phone')
        return mobile_phone

    @staticmethod
    def get_address_reference():
        address_reference = config.get('Common required information', 'address_reference')
        return address_reference

    @staticmethod
    def get_day_DOB():
        day_DOB = config.get('Common required information', 'day_DOB')
        return day_DOB

    @staticmethod
    def get_month_DOB():
        month_DOB = config.get('Common required information', 'month_DOB')
        return month_DOB

    @staticmethod
    def get_year_DOB():
        year_DOB = config.get('Common required information', 'year_DOB')
        return year_DOB

    @staticmethod
    def get_state():
        state = config.get('Common required information', 'state')
        return state

    @staticmethod
    def get_product_search():
        product_search = config.get('Common required information', 'product_search')
        return product_search

    @staticmethod
    def get_unit_price():
        unit_price = config.get('Common required information', 'product_search')
        return unit_price

    @staticmethod
    def get_product_search_criteria():
        product_search_criteria = config.get('Common required information', 'product_search_criteria')
        return product_search_criteria








