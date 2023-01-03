from gql import gql
from pprint import pprint
import re

from analyzer.queries.LogsClient import LogsClient
from analyzer.entities.Event import Event


EVENTS_TO_SKIP = set(['combatantinfo', 'gaugeupdate'])

def find_events_for_encounter(report_code: str, encounter_id: int, fight_id: int, kill: bool = True):
    client = LogsClient()
    
    query = gql(
        """
        query Events($code: String!, $startTime: Float, $encounterId: Int, $fightIds: [Int], $killType: KillType) {
                reportData {
                    report(code: $code) {
                        events(startTime: $startTime, encounterID: $encounterId, fightIDs: $fightIds, killType: $killType) {
                            data
                            nextPageTimestamp
                        }
                    }
                }
            }
        """
    )

    if kill is True:
        kill_type = 'Kills'
    else:
        kill_type = 'All'

    start_time = 0
    events = []
    event_types = set()
    while start_time is not None:
        variables = {
            'code': report_code,
            'encounterId': encounter_id,
            'fightIds': [fight_id],
            'killType': kill_type,
            'startTime': start_time,
        }
        print(variables)

        result = client.execute(query, variables=variables)
        event_data = result['reportData']['report']['events']['data']
        for event in event_data:
            print(event.keys())
            print(event['type'])
            event_types.add(event['type'])
            if event['type'] in EVENTS_TO_SKIP:
                continue
            try:
                events.append(Event(**{ to_snake_case(k): v for k, v in event.items() }))
            except TypeError as e:
                pprint(event)
                raise e

        start_time = result['reportData']['report']['events']['nextPageTimestamp']
        print("start time",start_time)

    pprint(event_types)
    return events


def to_snake_case(s: str) -> str:
    return re.sub('([A-Z]+)', r'_\1', s).lower()
