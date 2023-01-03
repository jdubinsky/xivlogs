from gql import gql

from .fflogs_url_parser import get_report_code_from_url
from .LogsClient import LogsClient
from analyzer.entities.Fight import Fight

def find_fights(report_url: str, difficulty_filter=100):
    report_code = get_report_code_from_url(report_url)
    variables = {'code': report_code}
    client = LogsClient()
    
    query = gql(
        """
        query ReportData($code: String!) {
                reportData {
                    report(code: $code) {
                        fights {
                            id
                            name
                            difficulty
                            bossPercentage
                            encounterID
                            kill
                            startTime
                            endTime
                            friendlyPlayers
                        }
                    }
                }
            }
        """
    )

    result = client.execute(query, variables=variables)
    fight_data = result['reportData']['report']['fights']
    fights = []

    for fight in fight_data:
        if fight['difficulty'] is None:
            continue

        if difficulty_filter and fight['difficulty'] < difficulty_filter:
            continue

        f = Fight(
            id=fight['id'],
            name=fight['name'],
            report_code=report_code,
            difficulty=fight['difficulty'],
            encounter_id=fight['encounterID'],
            kill=fight['kill'],
            boss_percentage=fight['bossPercentage'],
            players=fight['friendlyPlayers'],
            start_time=fight['startTime'],
            end_time=fight['endTime'],
        )
        fights.append(f)


    return fights
