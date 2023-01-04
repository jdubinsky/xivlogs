from gql import gql
from pprint import pprint

from analyzer.queries.LogsClient import LogsClient
from analyzer.entities.Ability import Ability
from analyzer.services.abilities import bulk_create_abilities

def find_abilities():
    client = LogsClient()

    query = gql(
        """
        query Abilities($page: Int) {
            gameData {
                abilities(page: $page) {
                    data {
                        id
                        name
                        description
                    }
                    from
                    to
                    current_page
                    last_page
                    has_more_pages
                }
            }
        }
        """
    )

    page = 1

    while True:
        variables = {'page': page}
        result = client.execute(query, variables=variables)
        ability_data = result['gameData']['abilities']['data']

        abilities = [
            Ability(
                id=ability['id'],
                name=ability['name'],
                description=ability['description'],
            ) for ability in ability_data
        ]

        yield abilities

        if result['gameData']['abilities']['has_more_pages'] is False:
            break

        page += 1
