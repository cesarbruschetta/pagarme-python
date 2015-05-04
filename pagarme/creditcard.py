# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import requests

from pagarme import PagarMe


class Creditcard(PagarMe):

    def __init__(self, card_hash='',):
        self.card_hash = card_hash
        self.data = {}

    def charge(self):
        params = {
            'api_key': self.api_key,
            'card_hash': self.card_hash
        }

        data = requests.post(
            self.api_endpoint + '/cards', data=params
        )

        self.data = data.json()
