def shop_from_grocery_list(budget, grocery_list, *products):
    bought_products = set()
    grocery_set = set(grocery_list)

    for product_name, product_price in products:
        if product_name in grocery_set and product_name not in bought_products and budget >= product_price:
            bought_products.add(product_name)
            budget -= product_price
        elif budget < product_price:
            break

    missing_products = grocery_set - bought_products
    if not missing_products:
        return f"Shopping is successful. Remaining budget: {budget:.2f}."
    else:
        missing_products_str = ', '.join(missing_products)
        return f"You did not buy all the products. Missing products: {missing_products_str}."
