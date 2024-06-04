from django.conf import settings

from msgs.abstract.models import AbstractMessage
from sendgrid import SendGridAPIClient, Mail, Email, Attachment, FileContent, FileName, FileType, Disposition, ContentId

from msgs.providers.base import BaseEmailProvider
from msgs.mixins import TemplatingMixin


class TwilioProvider(Provider):
    settings = settings.MSGS['providers']['twilio']['options']

    def __init__(self):
        self.client = TwilioClient(
            self.settings['account_sid'],
            self.settings['auth_token'],
        )

    def perform(
            self, message: AbstractMessage, sender: str, lang: str, **kwargs
    ) -> (dict, bool):
        message = self.client.messages.create(
            body=f"{message.text}",
            from_=sender,
            to=message.recipient.phone_number,
        )
        return message.to_dict(), True  # Dummy True
