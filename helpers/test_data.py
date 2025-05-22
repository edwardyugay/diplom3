from faker import Faker

fake = Faker()

def generate_user():
    return {
        "email": fake.email(),
        "password": "123456",
        "name": fake.first_name()
    }
