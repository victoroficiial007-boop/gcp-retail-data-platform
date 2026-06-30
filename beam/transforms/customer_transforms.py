def normalize_customer(customer: dict) -> dict:
    """
    Padroniza os dados do cliente.
    """

    customer["name"] = customer["name"].upper()
    customer["email"] = customer["email"].lower()

    return customer