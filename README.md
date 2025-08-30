# MetaOps

MetaOps es un servicio de automatización para administrar catálogos, contenidos, mensajería, campañas y reportes utilizando las APIs oficiales de Meta (Facebook, Instagram y WhatsApp) y Google Sheets.

## Características

* **Catálogo**: Sincroniza productos desde Google Sheets con el Catálogo de Facebook/Instagram.
* **Calendario de contenidos**: Programa publicaciones con texto e imagen/video y publícalas en el momento indicado.
* **Mensajería**: Configura reglas simples de auto-respuesta para comentarios y DMs en Facebook/Instagram y mensajes en WhatsApp Business.
* **Reportes diarios**: Envía KPIs diarios a Google Sheets y a correos configurables.
* **Cumplimiento**: Usa únicamente las APIs oficiales y respeta límites de uso y políticas de privacidad.

## Requisitos

* Python 3.11
* Acceso a las APIs de Meta (Graph, Marketing, WhatsApp), con los tokens correspondientes.
* Cuenta de Google Cloud y credenciales de servicio para acceder a Google Sheets.
* Base de datos PostgreSQL (o SQLite para pruebas).

## Configuración

1. Clona este repositorio.
2. Copia `.env.example` a `.env` y completa las variables según tu entorno (tokens, IDs de páginas, etc.).
3. Coloca el archivo de credenciales de servicio de Google en `creds/service_account.json`.
4. Opcionalmente, ajusta `docker-compose.yml` para apuntar a tu servidor de base de datos.

## Uso rápido con Docker

```bash
# Construye y levanta los servicios
make up

# Corre migraciones (pendiente configuración de Alembic)
# make migrate

# Ejecuta las pruebas
make test
```

## Licencia

Este proyecto está licenciado bajo los términos de la licencia MIT. Consulta el archivo `LICENSE` para más detalles.