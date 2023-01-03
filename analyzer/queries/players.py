from gql import gql
from pprint import pprint

from analyzer.queries.LogsClient import LogsClient
from analyzer.entities.Player import Player

def find_players_in_fight(report_code: str, fight_id: int, kill: bool = True):
    client = LogsClient()

    query = gql(
        """
        query Players($code: String!, $fightIds: [Int], $killType: KillType) {
            reportData {
                report(code: $code) {
                    playerDetails(fightIDs: $fightIds, killType: $killType)
                }
            }
        }
        """
    )

    if kill is True:
        kill_type = 'Kills'
    else:
        kill_type = 'All'

    players = []
    variables = {'code': report_code, 'fightIds': [fight_id], 'killType': kill_type}
    result = client.execute(query, variables=variables)
    player_details = result['reportData']['report']['playerDetails']['data']['playerDetails']

    dps = player_details['dps']
    for player in dps:
        p = Player(
            id=player['id'],
            name=player['name'],
            server=player['server'],
            type=player['type'],
            role='dps',
        )
        players.append(p)

    healers = player_details['healers']
    for player in healers:
        p = Player(
            id=player['id'],
            name=player['name'],
            server=player['server'],
            type=player['type'],
            role='healer',
        )
        players.append(p)

    tanks = player_details['tanks']
    for player in tanks:
        p = Player(
            id=player['id'],
            name=player['name'],
            server=player['server'],
            type=player['type'],
            role='tank',
        )

    print(players)
    return players
