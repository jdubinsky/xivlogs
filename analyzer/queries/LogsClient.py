from django.conf import settings
from gql import Client
from gql.transport.aiohttp import AIOHTTPTransport
import requests
from requests.auth import HTTPBasicAuth


class LogsClient:
    def __init__(self, token=None):
        if token is not None:
            self.token = token
        else:
            self.token = self.fetch_token()

        self.client = self.setup_client()

    def fetch_token(self):
        basic_auth = HTTPBasicAuth(
            settings.FFLOGS_CLIENT_ID,
            settings.FFLOGS_CLIENT_SECRET,
        )

        response = requests.post(
            settings.FFLOGS_TOKEN_URL,
            auth=basic_auth,
            data={'grant_type': 'client_credentials'},
        )
        token = response.json()['access_token']
        return token

    def setup_client(self):
        if self.token is None:
            raise Exception('Missing token')

        transport = AIOHTTPTransport(
            url=settings.FFLOGS_GQL_URL,
            headers={'Authorization': f'Bearer {self.token}'},
        )
        client = Client(
            transport=transport,
            fetch_schema_from_transport=True,
        )
        return client

    def execute(self, query, variables=None):
        if self.client is None:
            raise Exception('Client is not setup. Call setup_client() first.')

        return self.client.execute(query, variable_values=variables)
