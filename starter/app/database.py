from typing import List, Dict, Any

products_db: List[Dict[str, Any]] = []
id_counter = 0

def get_all_products() -> List[Dict[str, Any]]:
    return products_db

def create_product(name: str, price: float, description: str = "") -> Dict[str, Any]:
    global id_counter
    id_counter += 1
    product = {
        "id": id_counter,
        "name": name,
        "price": price,
        "description": description
    }
    products_db.append(product)
    return product