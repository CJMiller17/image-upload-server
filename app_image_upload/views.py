from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status

from .models import *
from .serializers import *

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_profile(request):
  user = request.user
  profile = user.profile
  serializer = ProfileSerializer(profile, many=False)
  return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser]) # Helps read form data
def create_image(request):
  print('PooP')
  image_serialized = ImageSerializer(data=request.data) #What is being sent by the user and serialize it
  if image_serialized.is_valid(): #Built in Djnago thing
    image_serialized.save()
    return Response(image_serialized.data, status=status.HTTP_201_CREATED) #Sending back the image and a status 
  return Response(image_serialized.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_images(request):
  images =Image.objects.all()
  images_serialized = ImageSerializer(images, many=True) # Allows more than one object. Returns as a list
  return Response(images_serialized.data)

