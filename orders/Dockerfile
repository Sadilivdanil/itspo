FROM python:3.11-slim
RUN pip install --no-cache-dir fastapi uvicorn httpx
WORKDIR /app
COPY main.py .
EXPOSE 8224
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8224"]