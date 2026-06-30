from pathlib import Path

from ingestion.generators.customer_generator import generate_customers
from ingestion.generators.product_generator import generate_products
from ingestion.utils.csv_writer import save_dataframe

BASE_DIR = Path(__file__).resolve().parent.parent

CUSTOMERS_OUTPUT = (
    BASE_DIR / "data" / "raw" / "customers" / "customers.csv"
)

PRODUCTS_OUTPUT = (
    BASE_DIR / "data" / "raw" / "products" / "products.csv"
)


def main():
    customers = generate_customers(100)
    save_dataframe(customers, CUSTOMERS_OUTPUT)

    products = generate_products(100)
    save_dataframe(products, PRODUCTS_OUTPUT)


if __name__ == "__main__":
    main()