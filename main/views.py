
import json
from urllib.request import Request
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
class Contactos(View):
    #Habilitar los cors para sitios cruzados
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    #Funcion que se ejecuta en metodo get
    def get(self, response):
        return JsonResponse({"data":"Metodo Get"})
    
    
    #Funcion que se ejecuta en metodo post 
    def post(self, request):
            data2 = json.loads(self.request.body)
            # print(data2)
            # data = "Hola me llamo "+data2+" y pase por Django"
            # print(request.POST)
            name = data2['nombre']
            # print(name)
            response = "Hola me asignaste "+name+" y esto se hizo en Django"
            return JsonResponse({"data" : response})    
        
    #Funcion que se ejecuta en metodo put
    def put(self, response):
        return
    #Funcion que se ejecuta en metodo delete
    def delete(self, response):
        return
