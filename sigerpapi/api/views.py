from django.db import transaction
from rest_framework import filters, status, viewsets
from rest_framework.response import Response

from sigerpapi.api.models import (
    Cliente,
    ClienteFuncionario,
    Funcionario,
    FuncionarioEscala,
)
from sigerpapi.api.serializers import (
    ClienteSerializer,
    FuncionarioEscalaSerializer,
    FuncionarioSerializer,
)


class ClienteViewSet(viewsets.ModelViewSet):
    search_fields = ["company_name"]
    filter_backends = (filters.SearchFilter,)
    queryset = Cliente.objects.all().order_by("id")
    serializer_class = ClienteSerializer


class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all().order_by("id")
    serializer_class = FuncionarioSerializer

    @transaction.atomic
    def create(self, request, *args, **kwawrgs):
        _cliente = request.data.pop("client", None)
        if not (_cliente and _cliente.get("id")):
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer = FuncionarioSerializer(data=request.data)

        if serializer.is_valid():
            funcionario = serializer.save()
            cliente = Cliente.objects.filter(pk=_cliente["id"]).first()
            ClienteFuncionario.objects.create(
                funcionario=funcionario,
                cliente=cliente,
                start_date=funcionario.admission_date,
            )
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @transaction.atomic
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = FuncionarioSerializer(instance, data=request.data, partial=True)

        cliente = None
        _cliente = request.data.pop("client", None)
        if _cliente and _cliente.get("id"):
            cliente = Cliente.objects.filter(pk=_cliente["id"]).first()
            if not cliente:
                return Response(status=status.HTTP_404_NOT_FOUND)

        if serializer.is_valid():
            funcionario = serializer.save()

            if cliente:
                ClienteFuncionario.objects.create(
                    funcionario=funcionario,
                    cliente=cliente,
                    start_date=funcionario.admission_date,
                )
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class FuncionarioEscalaViewSet(viewsets.ModelViewSet):
    queryset = FuncionarioEscala.objects.all().order_by("id")
    serializer_class = FuncionarioEscalaSerializer
