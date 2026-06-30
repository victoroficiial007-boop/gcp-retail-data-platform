"""
Configurações gerais do projeto.
"""

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_PATH = PROJECT_ROOT / "data"

RAW_PATH = DATA_PATH / "raw"

TRUSTED_PATH = DATA_PATH / "trusted"

CURATED_PATH = DATA_PATH / "curated"

CUSTOMERS_PATH = RAW_PATH / "customers" / "customers.csv"

PRODUCTS_PATH = RAW_PATH / "products" / "products.csv"