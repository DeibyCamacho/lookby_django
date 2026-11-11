# LookBy

Aplicacion web construida con Django para la plataforma LookBy. Incluye
registro e inicio de sesion, recuperacion de contrasena y paneles por tipo de
usuario.

## Requisitos

- Python 3.12 o superior
- PostgreSQL 14 o superior
- pip

## Configuracion local en Windows

Abre PowerShell en la raiz del proyecto y crea el entorno virtual:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
Copy-Item .env.example .env
```

Genera una clave secreta nueva:

```powershell
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Copia el resultado en `DJANGO_SECRET_KEY` dentro de `.env`. Completa tambien
los valores `POSTGRES_DB`, `POSTGRES_USER`, `POSTGRES_PASSWORD`,
`POSTGRES_HOST` y `POSTGRES_PORT` con las credenciales de una base de datos
PostgreSQL existente. No compartas ni subas `.env`.

| Variable | Uso | Valor local predeterminado |
| --- | --- | --- |
| `DJANGO_SECRET_KEY` | Clave criptografica de Django; es obligatoria | Sin valor; genera una clave |
| `DJANGO_DEBUG` | Activa el modo de depuracion | `1` |
| `DJANGO_ALLOWED_HOSTS` | Hosts permitidos separados por comas | `127.0.0.1,localhost` |
| `POSTGRES_DB` | Nombre de la base de datos | `lookby` |
| `POSTGRES_USER` | Usuario de PostgreSQL | `postgres` |
| `POSTGRES_PASSWORD` | Contrasena de PostgreSQL | Sin valor; configurar localmente |
| `POSTGRES_HOST` | Host de PostgreSQL | `127.0.0.1` |
| `POSTGRES_PORT` | Puerto de PostgreSQL | `5432` |

Por defecto, la configuracion local espera una base `lookby` y el servidor
PostgreSQL en `127.0.0.1:5432`. El usuario configurado debe tener permisos
sobre esa base. Crea la base si aun no existe:

```sql
CREATE DATABASE lookby OWNER postgres;
```

Ejecuta las migraciones y levanta el servidor:

```powershell
python manage.py migrate
python manage.py runserver
```

Abre http://127.0.0.1:8000/. Para comprobar la configuracion y ejecutar las
pruebas:

```powershell
python manage.py check
python manage.py test lookby_app
```

## Rutas principales

| Ruta | Uso |
| --- | --- |
| `/` | Pagina de inicio |
| `/login/` | Inicio de sesion |
| `/register/` | Registro |
| `/recuperar/` | Recuperacion de contrasena |
| `/cliente/` | Panel de cliente |
| `/negocio/` | Panel de negocio |
| `/proveedor/` | Panel de proveedor |
| `/superadmin/` | Panel de administracion |

## Alcance actual

Las pantallas de registro, inicio de sesion y recuperacion son demostrativas:
usan cuentas de ejemplo y datos en memoria/sesion. El registro no crea
usuarios persistentes, la recuperacion no envia correos y los paneles no
representan datos guardados en PostgreSQL. No uses las cuentas de demostracion
ni esta autenticacion como sistema de produccion.

## Estructura

```text
.
├── config/                 # Configuracion, URLs, ASGI y WSGI
├── lookby_app/             # Aplicacion Django
│   ├── migrations/
│   ├── static/lookby_app/  # CSS y otros recursos estaticos
│   └── templates/lookby_app/
├── .env.example            # Plantilla sin credenciales
├── .gitignore
├── manage.py
└── requirements.txt
```

Las credenciales, el entorno virtual, las bases de datos locales y los
archivos generados se excluyen de Git mediante `.gitignore`.

## Despliegue

`runserver` y `DJANGO_DEBUG=1` son solo para desarrollo. En produccion configura
una clave secreta propia, `DJANGO_DEBUG=0`, `DJANGO_ALLOWED_HOSTS` restrictivo,
HTTPS, un servidor WSGI/ASGI de produccion y `collectstatic`. No reutilices
credenciales de desarrollo.
