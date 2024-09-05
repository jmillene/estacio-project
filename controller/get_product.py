from service.get_product import get_all_products

def fetch_products():
    try:
        products = get_all_products()
        return products, 200
    except Exception as e:
        return {"message": str(e)}, 500
