# Imagen ligera con Python 3.12
FROM python:3.12-slim

# Buenas prácticas
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=8080

WORKDIR /app

# Instalar dependencias
COPY app/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código fuente
COPY app/src/ ./src/

EXPOSE 8080
CMD ["python", "-m", "src.server"]
