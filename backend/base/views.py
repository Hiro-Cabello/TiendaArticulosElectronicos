from django.shortcuts import render
from django.http import JsonResponse 
from .products import products


from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.


@api_view(['GET'])
def getRoutes(request):
    routes=[
        '/api/products/',
        '/api/products/create/',


        '/api/products/upload/',


        '/api/products/<id>/reviews/',

        '/api/products/top/',
        '/api/products/<id>/',

        '/api/products/delete/<id>/',
        '/api/products/<update>/<id>/',

    ]
    return Response(routes)

    #return JsonResponse('Hello',safe=False)
    #return JsonResponse(routes,safe=False)

@api_view(['GET'])
def getProducts(request):
    return Response(products)
    #return JsonResponse(products,safe=False)

@api_view(['GET'])
def getProduct(request,pk):
    product=None
    for i in products:
        if i['_id']==pk:
            product=i
            break
    return Response(product)



#
#marco REST también le permite trabajar con vistas basadas en funciones regulares. Proporciona un conjunto 
#de decoradores simples que envuelven sus vistas basadas en funciones para garantizar que reciban una instancia 
#de Request(en lugar del Django habitual HttpRequest) y les permite devolver un Response(en lugar de un Django
# HttpResponse), y le permiten configurar cómo se procesa la solicitud



#Cuando esta usando @api_view() me originaba un problema de session asi que lo que se tiene que hacer es ...
#   El problema es pues no hay una base de datos  y la pagina de administracion busca la base de datos por eso 
#   es que hay ese problema
#


#Apagado el servidor ejecutar 
#   python manage.py makemigrations
#   python manage.py migrate
#
#Luego crear un superusuario 
#   python manage.py createsuperuser
#
#Luego reiniciar el servidor y listo





#Axios es un cliente http ligero  basado en el servicio hhtp en Angular.so v1.x y es similar a la API Fetch nativa de JavaScript


















