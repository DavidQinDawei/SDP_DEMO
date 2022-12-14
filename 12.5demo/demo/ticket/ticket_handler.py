from django.http import JsonResponse
import json
from users.models import Users
from ticket.models import Ticket

def get_ticket(request):
    qs = Ticket.objects.values()

    retlist = list(qs)

    return JsonResponse({'ret': 0, 'retlist': retlist})