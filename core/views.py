from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


from .models import (
    operation
)

from .serializers import (
    OperationSerializer
)
# Create your views here.
class OperationView(APIView):
    
    def get(self, request):
        print("operation route hit")
        print("operation route get view")
        queryset = operation.objects.all()
        serializer = OperationSerializer(queryset, many=True)
        Response.status_code = 200
        return Response({"status": "success", "data": serializer.data})
    
    def post(self, request):
        print("operation object create route hit")
        serializer = OperationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print("operation object saved")
            Response.status_code = 201
            return Response({"status": "Successfully Created", "data": serializer.data})
        else:
            Response.status_code = 400
            return Response(serializer.errors)
