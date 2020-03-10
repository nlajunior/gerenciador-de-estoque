from ..orm import AbstractOrm
from ..models import User, Order
from django.shortcuts import render

class HomeView():

    def __init__(self):
        self.abstractOrm = AbstractOrm()
        self.user = User()
        self.order = Order()

    def index(self, request):
        return render(request, template_name='home.html')

