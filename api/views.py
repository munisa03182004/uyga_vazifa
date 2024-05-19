from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model 

from app_main.models import Note
from .serializers import NoteSerializer 



User = get_user_model()

@api_view(['GET'])
def create_note(request):
    if request.method == 'POST':
        owner_id=request.data['owner']
        title = request.data['title']
        body = request.data['body']
        
        user = User.object.get(id=owner_id)
        note = Note.object.create(owner=user,title=title,body=body)
        note.save()
        return Response(data='Create', status=status.HTTP_201_CREATED)
    return Response()
@api_view(['GET'])
def create_user(request):
    if request.method == 'POST':
        first_name_id=request.data['first_name_id']
        last_name = request.data['last_name']
        email = request.data['email']
        
        user = User.object.get(id=first_name_id)
        user = Note.object.create(user_name=user,last_name=last_name,email=email)
        user.save()
        return Response(data='Create', status=status.HTTP_201_CREATED)
    return Response()