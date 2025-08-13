import random
from pages.existing_user_signup import get_random_user_to_signup
from faker import Faker

fake = Faker()

actions = ["Need help with", "Issue regarding", "Question about", "Request for", "Feedback on"]
topics = ["my order", "account login", "a recent invoice", "product details", "delivery status", "technical support"]
order_ID = fake.random_number(digits=6)

#generate contact us form subject
def contact_us_subject():
    random_actions = random.choice(actions)
    random_topics = random.choice(topics)

    return f"{random_actions} {random_topics} Order ID: {order_ID}"

def contact_us_message():
    user_data = get_random_user_to_signup()
    subject = contact_us_subject()

    return (f"Hello Team, \n\n"
            f"My name is {user_data['Name']} \n\n"
            f"I am having issue with {subject}"
            f"Please assist with your support as soon as possible, \n\n Thanks \n\n"
            )


