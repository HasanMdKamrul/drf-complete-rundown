import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from products.models import Product

# import jsonparser

pre_data = {
    "success" : True,
    "message" : "Home Api Enabled"
}

@csrf_exempt
def api_home(request,*args,**kwargs):
    body = request.body 
    data = {}
    try:
        data = json.loads(body)
    except :
        pass
    # print(data)
    # print(request.headers)
    # data["headers"] = dict(request.headers)
    # data['my_custom_data'] = "My data send from the backend"
    # print(dict(request.GET))
    
    # print(data)
    
    if data.__len__() == 0:
        data = pre_data
        data['classRoll'] = 123
        return JsonResponse(data)
    else:
        data['message'] = "Data received"
        return JsonResponse(data)
        
    

def get_all_products(request,*args,**kwargs):
    data = {}
    count = Product.objects.all().count() + 1
    # ** New data created at every request
    Product.objects.create(id=count,title="Product",content="New Content",price=123.45)
    # ** Geting random object from the database (model data is not serialised)
    model_data = Product.objects.all().order_by('?').first()
    if model_data:
        data['id'] = model_data.id
        data['title'] = model_data.title
        data['content'] = model_data.content
        data['price'] = model_data.price
    return JsonResponse(data=data,safe=False)