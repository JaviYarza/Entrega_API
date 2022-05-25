from rest_framework.views import APIView
from rest_framework.response import Response
from entries.models import Entry
from entries.api.serializers import EntrySerializer

from rest_framework import status
from django.shortcuts import get_object_or_404

class EntryListAPI(APIView):
    def get(self,request):
        
        entries = Entry.objects.all()
        
        serializer = EntrySerializer(entries, many=True)
        
        return Response(serializer.data)
    
    def post(self,request):
        
        serializer = EntrySerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        
        return Response(status=400, data = serializer.errors)

class EntryDetailAPI(APIView):
#    permission_classes = (UserPermission,)

    def get_user(self, request, pk):
        entry = get_object_or_404(Entry, pk=pk)
#        self.check_object_permissions(request, entry)
        return entry

    def get(self, request, pk):

        entry = self.get_user(request, pk)

        serializer = EntrySerializer(instance=entry)
        return Response(serializer.data)


    def put(self, request, pk):

        #user = User.object.get(pk=pk)
        entry = get_object_or_404(Entry, pk=pk)

#        self.check_object_permissions(request, user)

        serializer = EntrySerializer(instance=entry, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

    def delete(self, request, pk):
#        self.check_permissions(request)

        user = get_object_or_404(Entry, pk=pk)

#        self.check_object_permissions(request, user)

        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)