from twilio.rest import Client as TwilioClient

from django.conf import settings

from msgs.abstract.models import AbstractMessage

from msgs.providers.base import BaseEmailProvider
from msgs.providers.base import BaseSMSProvider
from msgs.mixins import TemplatingMixin


class TwilioBaseProvider(TemplatingMixin):
    settings = settings.MSGS['providers']['twilio']['options']

    def __init__(self):
        self.client = TwilioClient(
            self.settings['account_sid'],
            self.settings['auth_token'],
        )

    def perform(
            self, message: AbstractMessage, sender: str, lang: str, **kwargs
    ) -> (dict, bool):
        context = self.get_context_data(message)
        _, body = self.render(message, lang, context)

        result = self.client.messages.create(
            body=body,
            from_=sender,
            to=message.recipient,
        )
        result = {'sid': result.sid}
        message.provider_response = result
        return result, True  # Dummy True


class TwilioEmailProvider(TwilioBaseProvider, BaseEmailProvider):
    pass


class TwilioSMSProvider(TwilioBaseProvider, BaseSMSProvider):
    pass
