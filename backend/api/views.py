from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/backend/',
            'method': 'GET',
            'body': None,
            'description': 'n/a'
        },
        {
            'Endpoint': '/backend/id',
            'method': 'GET',
            'body': None,
            'description': 'n/a'
        },
        {
            'Endpoint': '/backend/id',
            'method': 'POST',
            'body': None,
            'description': 'create new user'
        },

        {
            'Endpoint': '/backend/id/update',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing user with data sent in'
        },
        {
            'Endpoint': '/backend/id/delete',
            'method': 'GET',
            'body': None,
            'description': 'deletes user'
        }


    ]
    return Response(routes)
