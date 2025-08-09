from random import choice
from faker import Faker
import json
import random
import os
import pytest

class FakeUserData:
    def __init__(self):
        self.faker = Faker()

    def generate_sex(self):
        user_sex = random.choice(["Male", "Female"])
        return user_sex

    def generate_name(self, generate_sex = None):

        if not generate_sex:
            generate_sex = self.generate_sex()

        if generate_sex == "Male":
            firstname = self.faker.first_name_male()
        elif generate_sex == "Female":
            firstname = self.faker.first_name_female()
        else:
            firstname = self.faker.first_name()

        lastname = self.faker.last_name()

        fullname = f"{firstname} {lastname}"
        print(fullname)
        return firstname, lastname, fullname

    def generate_email(self):
        email_addr = self.faker.email()
        return email_addr

    def generate_password(self, length = 12):
        user_password = self.faker.password(length=length, upper_case=True, lower_case=True, special_chars=True, digits=True)
        return user_password

    def generate_dob(self, min_age = 18, max_age = 80):
        dob = self.faker.date_of_birth(minimum_age=min_age, maximum_age=max_age)
        dob_day = dob.day
        dob_month = dob.month
        dob_year = dob.year
        return dob_day, dob_month, dob_year

    def generate_company(self):
        user_company = self.faker.company()
        return user_company

    def generate_country(self):
        allowed_countries = ["India", "United States", "Canada", "Australia", "Israel", "New Zealand", "Singapore"]
        user_country = random.choice(allowed_countries)
        return user_country

    def generate_state(self):
        user_state = self.faker.state()
        return user_state

    def generate_city(self):
        user_city = self.faker.city()
        return user_city

    def generate_zipcode(self):
        user_zipcode = self.faker.zipcode()
        return user_zipcode

    def generate_address(self):
        user_address_line1 = self.faker.street_address()
        user_address_line2 = f"{self.generate_city()},{self.generate_state()},{self.generate_country()},{self.generate_zipcode()}"
        return user_address_line1,user_address_line2

    def generate_mobile_number(self):
        user_mob_num = self.faker.phone_number()
        return user_mob_num

@pytest.fixture()
def generate_complete_user_data():
    fake_user_data = FakeUserData()
    sex = fake_user_data.generate_sex()
    firstname, lastname, fullname = fake_user_data.generate_name(generate_sex=sex)
    email = fake_user_data.generate_email()
    password = fake_user_data.generate_password()
    day, month, year = fake_user_data.generate_dob()
    company = fake_user_data.generate_company()
    addr_line1, addr_line2 = fake_user_data.generate_address()
    country = fake_user_data.generate_country()
    state = fake_user_data.generate_state()
    city = fake_user_data.generate_city()
    zipcode = fake_user_data.generate_zipcode()
    mobile_number = fake_user_data.generate_mobile_number()

    formatted_user_data = {
    "Sex": sex,
    "Name": fullname,
    "Email": email,
    "Password": password,
    "Day": day,
    "Month": month,
    "Year": year,
    "First Name": firstname,
    "Last Name": lastname,
    "Company": company,
    "AddressLine1": addr_line1,
    "AddressLine2": addr_line2,
    "Country": country,
    "State": state,
    "City": city,
    "Zipcode": zipcode,
    "Mobile Number": mobile_number
    }
    return formatted_user_data

def append_user_data_to_json(user_data, file_path="test_data/signup_form_data.json"):
    if os.path.exists(file_path):
        try:
            with open(file_path, 'r') as json_file:
                users = json.load(json_file)
                if not isinstance(users, list):
                    users = []
        except json.JSONDecodeError:
            users = []
    else:
        users = []

    users.append(user_data)
    with open(file_path, 'w') as json_file:
        json.dump(users, json_file, indent=4)
        print("User data updated in to json file")









