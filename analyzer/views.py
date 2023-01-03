from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
import dataclasses

from analyzer.queries.fights import find_fights_by_code

class DataClassJSONSerializer(DjangoJSONEncoder):
    def default(self, o):
        if dataclasses.is_dataclass(o):
            return dataclasses.asdict(o)
        return super().default(o)

def fights(request, report_code):
    fights = find_fights_by_code(report_code)
    return JsonResponse(fights, encoder=DataClassJSONSerializer, safe=False)
