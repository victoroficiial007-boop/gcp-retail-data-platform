import random
from datetime import datetime

import pandas as pd

from config.reference_data import BRANDS, CATEGORIES


def generate_products(quantity: int = 100) -> pd.DataFrame:
    """
    Gera um catálogo de produtos fictício.
    """

    products = []

    for product_id in range(1, quantity + 1):

        category = random.choice(list(CATEGORIES.keys()))

        product_name = random.choice(CATEGORIES[category])

        cost_price = round(random.uniform(50, 3000), 2)

        unit_price = round(cost_price * random.uniform(1.2, 2.2), 2)

        stock_quantity = random.randint(10, 500)

        products.append(
            {
                "product_id": product_id,
                "product_name": product_name,
                "category": category,
                "brand": random.choice(BRANDS),
                "cost_price": cost_price,
                "unit_price": unit_price,
                "stock_quantity": stock_quantity,
                "created_at": datetime.now(),
            }
        )

    return pd.DataFrame(products)