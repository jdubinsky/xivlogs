from django.core.management.base import BaseCommand
from django.conf import settings

import requests
from requests.auth import HTTPBasicAuth
from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport

class Command(BaseCommand):
    help = 'Prints out data from an FFLogs report.'

    def handle(self, *args, **kwargs):
        basic_auth = HTTPBasicAuth(
            settings.FFLOGS_CLIENT_ID,
            settings.FFLOGS_CLIENT_SECRET,
        )

        response = requests.post(
            settings.FFLOGS_TOKEN_URL,
            auth=basic_auth,
            data={'grant_type': 'client_credentials'},
        )

        print(response)
        print(response.status_code)
        print(response.content)
        print(response.json().keys())
        token = response.json()['access_token']
        print(token)

        transport = AIOHTTPTransport(
            url=settings.FFLOGS_GQL_URL,
            headers={'Authorization': f'Bearer {token}'},
        )
        client = Client(
            transport=transport,
            fetch_schema_from_transport=True,
        )

        query = gql(
            """
            query ReportData($code: String!) {
                reportData {
                    report(code: $code) {
                        owner {
                            id
                            name
                        }
                    }
                }
            }
            """
        )

        result = client.execute(query, variable_values={'code': 'zbR2CcnYDPv8qwZx'})
        print(result)
