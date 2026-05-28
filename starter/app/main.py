from fastapi import FastAPI
from .models import Product
from .database import get_all_products, create_product
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("products-svc")

app = FastAPI(title="products-svc-s14")

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "products-svc-s14"}

@app.get("/api/products")
def list_products():
    return get_all_products()

@app.post("/api/products")
def add_product(product: Product):
    return create_product(
        name=product.name,
        price=product.price,
        description=product.description
    )

@app.on_event("startup")
def startup_event():
    logger.info("Starting gRPC server 'ProductsService' on port 50051 [package: products.v1]")