from rest_framework import serializers

class StageOneSerializer(serializers.Serializer):
    inn = serializers.CharField(max_length=12)
    full_name = serializers.CharField(max_length=255)
    phone = serializers.CharField(max_length=20)
    email = serializers.EmailField()
    consent = serializers.BooleanField()

class StageTwoSerializer(serializers.Serializer):
    # повторы полей из первой формы + доп. поля
    inn = serializers.CharField(max_length=12)
    full_name = serializers.CharField(max_length=255)
    phone = serializers.CharField(max_length=20)
    email = serializers.EmailField()
    consent = serializers.BooleanField()
    total_amount = serializers.DecimalField(max_digits=12, decimal_places=2)
    collateral = serializers.BooleanField()
    period_start = serializers.DateField()
    period_end = serializers.DateField()
    # …добавьте все поля, которые нужны для расчёта стоимости
