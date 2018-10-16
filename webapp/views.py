# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.http import Http404
from django.core import serializers
from django.conf import settings 
from webapp.models import airQuality
from datetime import datetime, date, time, timedelta
import calendar
import json

@api_view(['POST'])
def airQualityPost(sensordata):
    try:
        data = json.loads(sensordata.body)
        if data['Value'] == 0:
            respuestaJson = "Airqulity: no ha sido enviado el valor del sensor"
        elif data['Variable'] == 0:
            respuestaJson = "Airqulity: no ha sido enviado el nombre de la variable"   
        else:
             objectAirQ = airQuality()
             objectAirQ.valor = data['Value']
             objectAirQ.variable = data['Variable']
             objectAirQ.fecha = data['Date']
             objectAirQ.save()
             respuestaJson = "AirQuality: Json Subido correctamente."
        return JsonResponse(respuestaJson,safe = False)
    except ValueError as ex:
        return Response(ex.args[0],status.HTTP_400_BAD_REQUEST)

#class airQualityList(APIView):

 #   def get(self,request):
        #airQuality1 = airQuality.objects.all()
        #serialize = airQualitySerializer(airQuality1,many = True)
        #return response(serialize.data)	

    #def post(self):
        #pass





# Create your views here.
