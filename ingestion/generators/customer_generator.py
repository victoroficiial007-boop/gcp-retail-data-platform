from faker import Faker
import pandas as pd

fake = Faker("pt_BR")


def generate_customers(quantity: int = 100) -> pd.DataFrame:
    """
    Gera clientes fictícios para o projeto.
    """

    customers = []

    for customer_id in range(1, quantity + 1):
        customers.append(
            {
                "customer_id": customer_id,
                "name": fake.name(),
                "email": fake.email(),
                "city": fake.city(),
                "state": fake.estado_sigla(),
            }
        )

    return pd.DataFrame(customers)