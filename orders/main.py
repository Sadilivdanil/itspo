from fastapi import FastAPI, HTTPException, Query
import httpx
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("orders-svc")

app = FastAPI(title="orders-service")

PRODUCTS_SERVICE_URL = "http://products-svc-s14:8223/api/products"

@app.get("/health")
def health():
    return {"status": "healthy", "service": "orders-service"}

@app.post("/api/orders")
async def create_order(product_id: int = Query(..., description="ID продукта для заказа")):
    logger.info(f" Нано Банано Лог: Попытка создать заказ для продукта с ID {product_id}")
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(PRODUCTS_SERVICE_URL)
            response.raise_for_status()
            products = response.json()
        except Exception as e:
            logger.error(f"Ошибка при обращении к products-svc: {e}")
            raise HTTPException(
                status_code=503, 
                detail="Сервис каталога продуктов временно недоступен"
            )
    
    product_exists = any(p.get("id") == product_id for p in products)
    
    if not product_exists:
        logger.warning(f"Продукт с ID {product_id} не найден в каталоге")
        raise HTTPException(
            status_code=404, 
            detail=f"Продукт с ID {product_id} не существует в каталоге!"
        )
        
    logger.info(f"Заказ для продукта ID {product_id} успешно создан")
    return {
        "order_id": 42, 
        "product_id": product_id, 
        "status": "Успешно оформлено через products-svc-s14"
    }