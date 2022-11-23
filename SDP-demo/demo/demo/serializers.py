from rest_framework import serializers
from public.models import User
from ticket.models import Ticket

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name','email', 'netid', 'password', 'isactive')

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields=('title','created_date','description','department','student', 'issolved')