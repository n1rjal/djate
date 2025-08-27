from rest_framework import generics

from rester.tasks import add_record_for_calculation
from rester import serializers


# Create your views here.
class Adder(generics.CreateAPIView):
    serializer_class = serializers.AdderSerializer

    # def perfrom_create(self, serializer):
    #     return data

    def perform_create(self, serializer):
        super().perform_create(serializer)
        n1 = serializer.data.get("n1")
        n2 = serializer.data.get("n2")
        res = serializer.data.get("res")
        add_record_for_calculation.delay(n1, n2, res)
