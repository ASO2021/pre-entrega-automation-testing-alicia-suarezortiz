from decimal import Decimal

from faker import Faker

fake = Faker()


def random_checkout_data():
    return {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "postal_code": fake.postcode(),
    }


def parse_price(text):
    """Convierte '$29.99' o 'Item total: $29.99' en Decimal('29.99')."""
    return Decimal(text.split("$")[-1].strip())
