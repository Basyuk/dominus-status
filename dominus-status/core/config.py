import os

SERVICE_NAME = os.getenv("SERVICE_NAME", "dominus-status")
STATE_PATH = os.getenv("STATE_PATH", "state.bin")
STATE_VALUES = ("primary", "secondary", "notset", "noset")
DEFAULT_STATE = "noset"

# Authentication type: "keycloak" or "local"
AUTH_TYPE = os.getenv("AUTH_TYPE", "local")

# Local authentication (for AUTH_TYPE=local)
MANAGE_USERNAME = os.getenv("MANAGE_USERNAME", "admin")
MANAGE_PASSWORD = os.getenv("MANAGE_PASSWORD", "password")

# Keycloak settings (for AUTH_TYPE=keycloak)
KEYCLOAK_URL = os.getenv("KEYCLOAK_URL", "http://localhost:8080")
KEYCLOAK_REALM = os.getenv("KEYCLOAK_REALM", "master")
KEYCLOAK_CLIENT_ID = os.getenv("KEYCLOAK_CLIENT_ID", "dominus-status")
KEYCLOAK_PUBLIC_KEY = os.getenv("KEYCLOAK_PUBLIC_KEY", "")

# Roles for API access (for Keycloak)
REQUIRED_ROLE = os.getenv("REQUIRED_ROLE", "dominus-admin")

# HTTPS settings
USE_HTTPS = os.getenv("USE_HTTPS", "false").lower() == "true"
SSL_CERTFILE = os.getenv("SSL_CERTFILE", "")
SSL_KEYFILE = os.getenv("SSL_KEYFILE", "") 