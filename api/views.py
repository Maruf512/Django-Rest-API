from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializer import UserSerializer


@api_view(['GET'])
def get_users(request):
    # get data from db
    users = User.objects.all()
    # serialize it from object to redable data
    serializer = UserSerializer(users, many=True)
    # return the data
    return Response(serializer.data)


@api_view(['POST'])
def create_user(request):
    # pass the request data through the serializer to get the correct formated data
    serializer = UserSerializer(data=request.data)
    # check if the data is valid or not
    if serializer.is_valid():
        # if its valid then save the data to db
        serializer.save()
        # and return a respond to the user
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    else:
        # if the data is not valid then show some kind of error
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
