from djoser.views import UserViewSet as DjoserViewSet
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView


class AuthViewSet(DjoserViewSet):
	renderer_classes = [TemplateHTMLRenderer]
	template_name = 'base_layout.html'	
		

