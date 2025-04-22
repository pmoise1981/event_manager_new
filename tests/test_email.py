import pytest
from unittest.mock import AsyncMock

from app.services.email_service import EmailService
from app.utils.template_manager import TemplateManager

@pytest.mark.asyncio
async def test_send_markdown_email(monkeypatch):
    # Mocking the email sending method
    monkeypatch.setattr(EmailService, "send_user_email", AsyncMock(return_value=True))

    template_manager = TemplateManager()
    email_service = EmailService(template_manager=template_manager)

    user_data = {
        "email": "test@example.com",
        "name": "Test User",
        "verification_url": "http://example.com/verify?token=abc123"
    }

    await email_service.send_user_email(user_data, 'email_verification')

