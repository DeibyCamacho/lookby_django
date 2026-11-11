# LookBy Django

Proyecto Django puro para la plataforma LookBy, con autenticación, paneles por rol y base de datos PostgreSQL.

## Requisitos

- Python 3.11+
- PostgreSQL 14+
- pip

## Instalación

1. Entrar al proyecto:
   ```bash
   cd django_lookby
   ```
2. Crear entorno virtual:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
3. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```
4. Crear base de datos PostgreSQL:
   ```sql
   CREATE DATABASE lookby;
   CREATE USER postgres WITH PASSWORD 'postgres';
   ALTER ROLE postgres WITH SUPERUSER;
   ```
5. Ejecutar migraciones:
   ```bash
   python manage.py migrate
   ```
6. Levantar servidor:
   ```bash
   python manage.py runserver 0.0.0.0:8000
   ```

## Configuración de base de datos

La conexión a PostgreSQL está definida en [django_lookby/lookby_django/settings.py](django_lookby/lookby_django/settings.py) con variables de entorno:

- POSTGRES_DB
- POSTGRES_USER
- POSTGRES_PASSWORD
- POSTGRES_HOST
- POSTGRES_PORT

Ejemplo:

```bash
export POSTGRES_DB=lookby
export POSTGRES_USER=postgres
export POSTGRES_PASSWORD=postgres
export POSTGRES_HOST=127.0.0.1
export POSTGRES_PORT=5432
```

## Estructura

- [django_lookby/lookby_django](django_lookby/lookby_django): configuración del proyecto
- [django_lookby/lookby_app](django_lookby/lookby_app): vistas, rutas, templates y lógica Django

## Acceso

- Landing: http://localhost:8000/
- Login: http://localhost:8000/login/
