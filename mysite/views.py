from django.views.generic import  TemplateView


class HomeView(TemplateView):
    template_name = 'home.html'

#HomeView -> home.html 열어주기로!!