import json
from django.http import JsonResponse

def api_home(request,*args,**kwargs):
    body = request.body
    data = {}
    try:
        data = json.loads(body)
    except:
        pass
    # print(data)
    print(request.GET)
    print(request.POST)
    # print(request.headers)
    # data['headers'] = dict(request.headers)
    data['params'] = request.GET
    data['content_type'] = request.content_type

    print(data)
    return JsonResponse(data)