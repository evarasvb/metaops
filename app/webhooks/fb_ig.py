"""
Webhook handler for Facebook and Instagram events.
"""

from fastapi import APIRouter, Request, HTTPException

from ..config import settings

router = APIRouter()

@router.get("/webhooks/fb-ig")
async def verify_fb_ig(mode: str, hub_challenge: str, hub_verify_token: str):
    """
    Verify webhook subscription with Meta. Responds with the hub.challenge if tokens match.
    """
    if hub_verify_token != settings.meta_verify_token:
        raise HTTPException(status_code=403, detail="Invalid verify token")
    return hub_challenge


@router.post("/webhooks/fb-ig")
async def handle_fb_ig_event(request: Request):
    """
    Handle incoming webhook events from Facebook and Instagram.
    Placeholder implementation.
    """
    payload = await request.json()
    # TODO: Process events based on object type and event type
    return {"status": "received"}
