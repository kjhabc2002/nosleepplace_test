import json
from datetime             import datetime, timedelta

from django.http.response import JsonResponse
from django.views         import View
from django.db.models     import Q

from place.models        import Place

class PlaceListView(View):    
    def get(self, request):
        try: 
            menu     = request.GET.get('menu', None)
            category = request.GET.get('category', None)
            keyword  = request.GET.get('keyword', None)
            order    = request.GET.get('order', None)
        
            if category:
                places = Place.objects.filter(category__id = category)
                
            if keyword:
                places = Place.objects.filter(name__contains=keyword)
                
            if order:
                places = Place.objects.order_by(order)

            if menu:
                places = Place.objects.filter(category__menu__id=menu)

            if (menu or category or keyword or order) == None:
                places = Place.objects.all()

            result = [{
                'id'        : place.id,
                'place_name': place.name,
                'price'     : place.price,
                'capacity'  : place.capacity,
                'city'      : place.city.name,
                'parking'   : place.parking,
                'url'       : [image.url for image in place.image_set.all()],
                } for place in places]
            
            return JsonResponse({'result' : result}, status=200)
        
        except Place.DoesNotExist:
            return JsonResponse({'message' : 'DOES_NOT_FOUND'}, status=400)
        
        except TypeError:
            return JsonResponse({'message' : 'TYPE_ERROR'}, status=400)
        
        except ValueError:
            return JsonResponse({'message' : 'VALUE_ERROR'}, status=400)