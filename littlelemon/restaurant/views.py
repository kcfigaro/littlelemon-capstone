from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication

from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer
from rest_framework import status
from rest_framework.decorators import (
    api_view,
    permission_classes,
    authentication_classes,
)
from rest_framework.permissions import IsAuthenticated


@api_view()
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def msg(request):
    return Response({"message": "This view is protected"})


class SingleMenuItemView(APIView):
    def get(self, request, pk):
        item = Menu.objects.get(pk=pk)
        serializer = MenuSerializer(item)
        return Response(serializer.data)


class MenuItemsView(APIView):
    def get(self, request):
        items = Menu.objects.all()
        serializer = MenuSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MenuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@permission_classes([IsAuthenticated])
class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]


def index(request):
    return render(request, "index.html", {})


# def sayHello(request):
#     return HttpResponse("Hello World")
