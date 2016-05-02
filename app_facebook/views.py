from django.shortcuts import render
from django.views.generic import View
from app_facebook.models import Settings


class Home(View):
    def get(self,request):
        settings = Settings.objects.first()
        print settings
        return render(request, 'index.html',
            {"app_id":settings.app_id})
            
            
    def post(self, request):
        print request

