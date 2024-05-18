from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def get_notes(request):
    users = [
        {
            "id": "1",
            "username": "admin",
            "email": "admin@gmail.com",
            "password": "123"
        },
        {
            "id": "1",
            "username": "admin",
            "email": "admin@gmail.com",
            "password": "123"
        }
    ]
    return Response(data=users)
