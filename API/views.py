from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from API.serializers import appserializer
from Billit.models import inventory

@api_view(['GET','PUT'])
def getdetail(request,id):
    try:
        qset=inventory.objects.get(product_id=id)
    except Exception as e:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='GET':
        serialized_obj=appserializer(qset)
        return Response(serialized_obj.data)
    
    if request.method=='PUT':
        if request.user.is_authenticated():
            serialized_obj=appserializer(data = request.data ,instance=qset)
            if serialized_obj.is_valid():
                qset.sold_by=request.user
                serialized_obj.save()
                return Response(serialized_obj.data)
            return Response(serialized_obj.errors,status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_401_UNAUTHORIZED)
    
    
