from fastapi import APIRouter, HTTPException, Depends
from typing import Literal, Dict, Any
from ..services.state_service import read_state, write_state, STATE_VALUES, SERVICE_NAME
from ..core.auth import hybrid_auth, hybrid_role_check
from ..core.config import REQUIRED_ROLE

router = APIRouter()

@router.get("/status")
def get_status(current_user: Dict[str, Any] = Depends(hybrid_auth)):
    """Get current service status (requires authentication)"""
    data = read_state()
    return {
        "service_name": SERVICE_NAME, 
        "state": data["state"], 
        "hostname": data["hostname"],
        "user": current_user.get("preferred_username", current_user.get("username", "unknown")),
        "auth_type": current_user.get("auth_type", "keycloak")
    }

@router.put("/state")
def set_state(
    new_state: Literal["primary", "secondary", "notset", "noset"],
    current_user: Dict[str, Any] = Depends(hybrid_role_check(REQUIRED_ROLE)),
):
    """Change service status (requires dominus-admin role for Keycloak or authentication for local)"""
    if new_state not in STATE_VALUES:
        raise HTTPException(status_code=400, detail="Invalid state value")
    data = read_state()
    write_state(new_state, data["hostname"])
    return {
        "service_name": SERVICE_NAME, 
        "state": new_state, 
        "hostname": data["hostname"],
        "user": current_user.get("preferred_username", current_user.get("username", "unknown")),
        "auth_type": current_user.get("auth_type", "keycloak")
    }

@router.put("/status")
def set_status_via_status_endpoint(
    new_state: Literal["primary", "secondary", "notset", "noset"],
    current_user: Dict[str, Any] = Depends(hybrid_role_check(REQUIRED_ROLE)),
):
    """Alternative endpoint for changing status via /status (for compatibility)"""
    return set_state(new_state, current_user) 