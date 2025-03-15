from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from .serializers import ItemSerializer
from django.db import transaction

class ItemUpdate(APIView):
   
    def put(self, request):
        # Handling bulk update
        data = request.data
        with transaction.atomic():
             
                user, created = User.objects.update_or_create(
                    id=data.get('id'),
                    defaults={
                        'name': data.get('name'),
                        'description': data.get('description')
                    }
                )
        return Response({'status': 'Updated products successfully'}, status=status.HTTP_200_OK)