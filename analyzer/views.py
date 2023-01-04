from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
import dataclasses

from analyzer.queries.events import find_events_for_fight
from analyzer.queries.fights import find_fights_by_code
from analyzer.queries.players import find_players_in_fight

class DataClassJSONSerializer(DjangoJSONEncoder):
    def default(self, o):
        if dataclasses.is_dataclass(o):
            return dataclasses.asdict(o)
        return super().default(o)

def fights(request, report_code):
    fights = find_fights_by_code(report_code)
    return JsonResponse(fights, encoder=DataClassJSONSerializer, safe=False)


def players(request, report_code, fight_id):
    players = find_players_in_fight(report_code, fight_id)
    return JsonResponse(players, encoder=DataClassJSONSerializer, safe=False)


def events(request, report_code, fight_id):
    events = find_events_for_fight(report_code, fight_id)
    return JsonResponse(events, encoder=DataClassJSONSerializer, safe=False)
