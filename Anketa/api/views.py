from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import StageOneSerializer, StageTwoSerializer
from .utils import send_application_email

class StageOneView(APIView):
    def post(self, request):
        serializer = StageOneSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        # Отправляем почту
        send_application_email(
            subject="Новая заявка — этап 1",
            template_name="stage_one.html",
            context=data,
            recipient_list=["target@example.com"]
        )
        return Response({"detail": "Заявка успешно отправлена"}, status=status.HTTP_200_OK)

class StageTwoView(APIView):
    def post(self, request):
        serializer = StageTwoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        # Отправляем почту
        send_application_email(
            subject="Новая заявка — этап 2 (расчёт)",
            template_name="stage_two.html",
            context=data,
            recipient_list=["target@example.com"]
        )
        # При необходимости можно вернуть какие-то данные расчёта,
        # например итоговую стоимость, но тут просто OK.
        return Response({"detail": "Расчёт отправлен"}, status=status.HTTP_200_OK)
