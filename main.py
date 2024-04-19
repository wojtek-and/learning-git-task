lista_zakupów = {
    "piekarnia": ["chleb", "bułki", "pączek"],
    "warzywniak": ["marchew", "seler", "rukola"]
}

for shop, products in lista_zakupów.items():
    product_capital = [product.capitalize() for product in products]
    print(f"Idę do {shop.capitalize()} i kupuję tu następujące rzeczy: {product_capital}.")