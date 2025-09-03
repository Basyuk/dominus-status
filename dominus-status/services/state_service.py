import os
import pickle
import logging
import socket
from fastapi import HTTPException
from ..core.config import STATE_PATH, STATE_VALUES, DEFAULT_STATE

SERVICE_NAME = os.getenv("SERVICE_NAME", "dominus-status")


def read_state() -> dict:
    logging.info(f"Reading state from {STATE_PATH}")
    if not os.path.exists(STATE_PATH):
        logging.error(f"State file '{STATE_PATH}' not found when reading state.")
        raise HTTPException(status_code=500, detail="State file not found")
    with open(STATE_PATH, "rb") as f:
        try:
            data = pickle.load(f)
            logging.info(f"State content: {data}")
        except Exception as e:
            logging.error(f"Invalid pickle in state file '{STATE_PATH}': {e}")
            raise HTTPException(status_code=500, detail="Invalid state file format")
    if "state" not in data or data["state"] not in STATE_VALUES:
        logging.error(f"Invalid state value in file '{STATE_PATH}': '{data}'")
        raise HTTPException(status_code=500, detail="Invalid state value in state file")
    if "hostname" not in data:
        logging.error(f"Hostname missing in state file '{STATE_PATH}'")
        raise HTTPException(status_code=500, detail="Hostname missing in state file")
    return data


def write_state(state: str, hostname: str):
    with open(STATE_PATH, "wb") as f:
        pickle.dump({"state": state, "hostname": hostname}, f)


def get_hostname() -> str | None:
    try:
        data = read_state()
        return data["hostname"]
    except Exception as e:
        logging.error(f"Failed to get hostname from state: {e}")
        return None 