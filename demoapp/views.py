
from django.forms import ValidationError
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.authtoken.models import Token 
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, permission_classes, renderer_classes, authentication_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Artist, Work
from .serializers import ArtistSerializer, WorkSerializer
from rest_framework.exceptions import NotFound




def home(request):
    return render(request, "base.html")

@api_view(['POST'])
def signup(request):
    if request.method == "POST":
        username = request.data.get('username')
        fname = request.data.get('firstname')
        lname = request.data.get('lastname')
        email = request.data.get('email')
        pass1 = request.data.get('password')
        pass2 = request.data.get('confirmpassword')

        try:
            User.objects.get(username=username)
            return Response({"error": "Username already exists."}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            pass

        try:
            User.objects.get(email=email)
            return Response({"error": "Email already registered."}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            pass

        if len(username) > 40:
            return Response({"error": "Username must be under 10 characters."}, status=status.HTTP_400_BAD_REQUEST)

        if pass1 != pass2:
            return Response({"error": "Passwords didn't match."}, status=status.HTTP_400_BAD_REQUEST)

        if not username.isalnum():
            return Response({"error": "Username must be Alpha-Numeric."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            myuser = User.objects.create_user(username, email, pass1)
            myuser.first_name = fname
            myuser.last_name = lname
            myuser.save()

            return Response({"success": "Your Account has been successfully created."}, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            return Response({"error": e.messages[0]}, status=status.HTTP_400_BAD_REQUEST)

    return Response({"error": "Invalid Request Method."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)



@api_view(['GET', 'POST'])
@renderer_classes([JSONRenderer, TemplateHTMLRenderer])
def signin(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            
            if request.accepted_renderer.format == 'html':
                fname = user.first_name
                return render(request, "base.html", {'fname':fname, 'Token':token.key})
            else:
                return Response({'token': token.key, 'message':'successfully logged in '}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    if request.method == 'GET':
        return render(request, "signin.html")
@api_view(['GET'])
def signout(request):
    if request.method == 'GET':
        logout(request)
        return Response({'message':'successfully logged out '}, status=status.HTTP_200_OK)
    

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def Work_list_view(request):
    if request.method == 'GET':
        work_type = request.query_params.get('work_type')
        artist_name = request.query_params.get('artist')
        queryset = Work.objects.all()
        if work_type:
            queryset = queryset.filter(work_type=work_type)
        if artist_name:
            try:
                artist= Artist.objects.get(name=artist_name)
                queryset = artist.works.all()
               
            except Artist.DoesNotExist:
                raise NotFound(detail="Artist not found.")
        
        serializer = WorkSerializer(queryset, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = WorkSerializer(data=request.data)
        if serializer.is_valid():
            user=request.user
            try:
                artist = Artist.objects.get(user=user)
            except Artist.DoesNotExist:
                return Response({"detail":"Artist not found"}, status=status.HTTP_404_NOT_FOUND)
            serializer.save()
            artist.works.add(serializer.instance)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
class ArtistListView(generics.ListAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    def get(self, request, *args, **kwargs):
        if self.request.accepted_renderer.format == 'html':
            artists = self.get_queryset()
            return render(request, 'artists_list.html', {'artists': artists})
        return super().get(request, *args, **kwargs)


# Create your views here.
