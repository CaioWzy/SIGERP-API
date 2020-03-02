from sigerpapi.api.models import (
    Cliente,
    Funcionario,
    ClienteFuncionario,
    FuncionarioEscala,
)
from rest_framework import serializers


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ["id", "company_name", "fantasy_name", "cnpj"]


class ClienteFuncionarioSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    fantasy_name = serializers.SerializerMethodField()
    company_name = serializers.SerializerMethodField()

    class Meta:
        model = ClienteFuncionario
        fields = ["id", "fantasy_name", "company_name", "start_date"]

    def get_id(self, obj):
        return obj.cliente.id

    def get_fantasy_name(self, obj):
        return obj.cliente.fantasy_name

    def get_company_name(self, obj):
        return obj.cliente.company_name


class FuncionarioSerializer(serializers.ModelSerializer):
    client = serializers.SerializerMethodField()
    people_times = serializers.SerializerMethodField()

    class Meta:
        model = Funcionario
        fields = [
            "id",
            "name",
            "enrolment",
            "cpf",
            "date_of_birth",
            "email",
            "admission_date",
            "client",
            "people_times",
        ]

    def get_client(self, obj):
        queryset = (
            ClienteFuncionario.objects.filter(funcionario=obj).order_by("-id").first()
        )
        if queryset:
            serialized_data = ClienteFuncionarioSerializer(queryset)
            return serialized_data.data
        return {}

    def get_people_times(self, obj):
        queryset = (
            FuncionarioEscala.objects.filter(funcionario=obj).order_by("weekday").all()
        )
        if queryset:
            serialized_data = FuncionarioEscalaSerializer(queryset, many=True)
            return serialized_data.data
        return {}


class FuncionarioEscalaSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuncionarioEscala
        fields = ["weekday", "marking_in", "marking_out"]

