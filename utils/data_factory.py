from faker import Faker


fake = Faker('en_US')

class DataFactory:
    @staticmethod
    def generate_user_data():
        """Gera um dicionário com dados de usuário aleatórios e válidos"""
        return {
            "name": fake.name(),
            "email": fake.email(),
            "password": fake.password(length=12),
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "address": fake.street_address(),
            "country": "United States",
            "state": fake.state(),
            "city": fake.city(),
            "zipcode": fake.zipcode(),
            "mobile_number": fake.phone_number()
        }