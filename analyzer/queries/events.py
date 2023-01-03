from gql import gql
from pprint import pprint

from .LogsClient import LogsClient

def find_events_for_encounter(report_code: str, encounter_id: int, fight_id: int, kill: bool = True):
    client = LogsClient()
    
    query = gql(
        """
        query ReportData($code: String!, $startTime: Float, $encounterId: Int, $fightIds: [Int], $killType: KillType) {
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
        #  pprint(events)
        for event in event_data:
            print(event.keys())
            events.append(event_data)

        start_time = result['reportData']['report']['events']['nextPageTimestamp']
        print("start time",start_time)

    return events
