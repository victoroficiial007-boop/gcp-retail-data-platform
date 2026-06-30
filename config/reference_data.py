from decimal import Decimal

CATEGORIES = {
    "Eletrônicos": [
        "Smart TV 55",
        "Soundbar",
        "Caixa de Som Bluetooth",
        "Fone Bluetooth",
        "Monitor Gamer"
    ],
    "Informática": [
        "Notebook",
        "Mouse",
        "Teclado Mecânico",
        "SSD 1TB",
        "Memória RAM 16GB"
    ],
    "Celulares": [
        "Smartphone",
        "Smartwatch",
        "Carregador Turbo",
        "Capa",
        "Película"
    ],
    "Casa": [
        "Liquidificador",
        "Air Fryer",
        "Cafeteira",
        "Micro-ondas",
        "Aspirador"
    ],
    "Esportes": [
        "Bicicleta",
        "Tênis Corrida",
        "Mochila",
        "Garrafa Térmica",
        "Bola Futebol"
    ]
}

BRANDS = [
    "Samsung",
    "Apple",
    "Dell",
    "Lenovo",
    "LG",
    "Philips",
    "Nike",
    "Adidas",
    "Xiaomi",
    "Motorola"
]

ORDER_STATUS = [
    "CREATED",
    "APPROVED",
    "SHIPPED",
    "DELIVERED",
    "CANCELLED"
]

PAYMENT_METHODS = [
    "PIX",
    "CREDIT_CARD",
    "DEBIT_CARD",
    "BOLETO"
]