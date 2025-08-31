"""
Webhook handler for WhatsApp events.
"""

from fastapi import APIRouter, Request

router = APIRouter()


@router.post("/webhooks/wa")
async def handle_wa_event(request: Request):
    """Handle incoming WhatsApp webhook events."""
    payload = await request.json()
    # TODO: Process WhatsApp messages and trigger automations
    return {"status": "received"}
