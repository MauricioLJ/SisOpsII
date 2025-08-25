# 🚀 Hola Mundo con Python + Docker + HAProxy

Este proyecto es una **demo de arquitectura web en contenedores**.  
Consiste en una aplicación sencilla en **Python (Flask)** desplegada en múltiples instancias detrás de **HAProxy**, con soporte de **HTTPS (certificado autofirmado)**, **balanceo de carga**, **health-checks** y pruebas de carga con **JMeter**.

---

## 📂 Estructura del proyecto

- **app/** → Código fuente de la aplicación
  - `src/server.py` → Servidor Flask con dos endpoints:
    - `/` → Responde un HTML de “Hola mundo desde Python 🐍”.
    - `/health` → Responde `OK` para los health-checks.
  - `requirements.txt` → Dependencias de Python.
- **Dockerfile** → Construye la imagen de la aplicación (basada en Python 3.12 slim).
- **docker-compose.yml** → Levanta 2 instancias de la app (`app1`, `app2`) + HAProxy (modo local).
- **swarm-stack.yml** → Versión para despliegue en **Docker Swarm** (cluster).
- **haproxy/** → Configuración del balanceador.
  - `haproxy.cfg` → Configuración para entorno local (compose).
  - `haproxy.swarm.cfg` → Configuración para entorno en Swarm.
  - `certs/` → Certificado autofirmado generado aquí.
- **scripts/genSerlfSigned.sh** → Script para crear un certificado autofirmado.
- **test/jmeter/holamundo.jmx** → Plan de prueba de carga en JMeter.

---

## 🔧 Requisitos

- Docker y Docker Compose v2 instalados.
- (Opcional) Docker Swarm habilitado si quieres desplegar en cluster.
- (Opcional) Apache JMeter para ejecutar el test de carga.

---

## ▶️ Uso con Docker Compose (local)

1. Genera un certificado autofirmado:
   ```bash
   bash scripts/genSerlfSigned.sh
   ```
