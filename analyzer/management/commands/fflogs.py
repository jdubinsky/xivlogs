from django.core.management.base import BaseCommand

from analyzer.queries.fights import find_fights_by_url
from analyzer.queries.events import find_events_for_encounter
from analyzer.queries.players import find_players_in_fight

class Command(BaseCommand):
    help = 'Prints out data from an FFLogs report.'

    def add_arguments(self, parser):
        parser.add_argument('-r', '--report', type=str, help='URL to fflogs report.')

    def handle(self, *args, **kwargs):
        report = kwargs['report']
        if not report:
            raise Exception("Missing FFLogs report URL")

        fights = find_fights_by_url(report)
        print(fights)

        for fight in fights:
            if fight.kill is True:
                print(fight)
                #  events = find_events_for_encounter(fight.report_code, fight.encounter_id, fight.id)
                find_players_in_fight(fight.report_code, fight.id)
                break
