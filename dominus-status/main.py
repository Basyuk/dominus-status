import logging
import socket
from fastapi import FastAPI
from .core.config import DEFAULT_STATE, STATE_PATH, USE_HTTPS, SSL_CERTFILE, SSL_KEYFILE
from .services.state_service import read_state, write_state, get_hostname
from .api.status import router as status_router
import os

app = FastAPI()

app.include_router(status_router)

# Setup basic logger
logging.basicConfig(level=logging.INFO)

@app.on_event("startup")
def startup_event():
    hostname = socket.gethostname()
    if not os.path.exists(STATE_PATH):
        write_state(DEFAULT_STATE, hostname)
        logging.info(f"State file '{STATE_PATH}' created with default state '{DEFAULT_STATE}' and hostname '{hostname}'")
    else:
        try:
            data = read_state()
            if data["hostname"] != hostname:
                write_state(data["state"], hostname)
                logging.info(f"State file '{STATE_PATH}' hostname updated to '{hostname}'")
            else:
                logging.info(f"State file '{STATE_PATH}' hostname matches, no changes required")
        except Exception as e:
            logging.error(f"State file '{STATE_PATH}' corrupted: {e}")
            raise RuntimeError(f"State file '{STATE_PATH}' corrupted: {e}")

if __name__ == "__main__":
    import uvicorn
    uvicorn_kwargs = {
        "app": "dominus_status.main:app",
        "host": "0.0.0.0",
        "port": 8000,
        "reload": True,
    }
    if USE_HTTPS and SSL_CERTFILE and SSL_KEYFILE:
        uvicorn_kwargs["ssl_certfile"] = SSL_CERTFILE
        uvicorn_kwargs["ssl_keyfile"] = SSL_KEYFILE
    uvicorn.run(**uvicorn_kwargs) 