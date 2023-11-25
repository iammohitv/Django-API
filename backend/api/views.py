import json
# from django.http import JsonResponse
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.models import Product
from products.serializers import ProductSerializer

@api_view(["POST"])
def api_home(request,*args,**kwargs):
    """
    DRF API VIEW
    """
    data = request.data
    # model_data = Product.objects.all().order_by("?").first()
    # data = {}
    # if model_data:
    #     data['id'] = model_data.id
    #     data['title'] = model_data.title
    #     data['content'] = model_data.content
    #     data['price'] = model_data.price
    # if model_data:
        # data = model_to_dict(model_data,fields = ['id','price', 'title', 'sale_price'])
    serializer = ProductSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        # instance = serializer.save()
        
        # print(instance)
        data = serializer.data
        return Response(data)