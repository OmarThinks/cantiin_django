from django.shortcuts import render

# Create your views here.

import json

from cantiin.views import UserViewSet as _UserViewSet
from cantiin.views import ProductViewSet as _ProductViewSet
from cantiin.views import OrderViewSet as _OrderViewSet
from cantiin.views import CommentViewSet as _CommentViewSet
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView

from frontend.abstract_renderers import abstract_list_renderer



def base_page(request):
	#return HttpResponse("Home Page")
	#print(request.__dir__(), flush=True)
	#['environ', 'path_info', 'path', 'META', 'method', 'content_type', 'content_params', '_stream', '_read_started', 'resolver_match', 'COOKIES', 'session', 'user', '_messages', 'csrf_processing_done', '__module__', '__init__', '_get_scheme', 'GET', '_get_post', '_set_post', 'FILES', 'POST', '__doc__', '_encoding', '_upload_handlers', '__repr__', 'headers', 'accepted_types', 'accepts', '_set_content_type_params', '_get_raw_host', 'get_host', 'get_port', 'get_full_path', 'get_full_path_info', '_get_full_path', 'get_signed_cookie', 'get_raw_uri', 'build_absolute_uri', '_current_scheme_host', 'scheme', 'is_secure', 'is_ajax', 'encoding', '_initialize_handlers', 'upload_handlers', 'parse_file_upload', 'body', '_mark_post_parse_error', '_load_post_and_files', 'close', 'read', 'readline', '__iter__', 'readlines', '__dict__', '__weakref__', '__hash__', '__str__', '__getattribute__', '__setattr__', '__delattr__', '__lt__', '__le__', '__eq__', '__ne__', '__gt__', '__ge__', '__new__', '__reduce_ex__', '__reduce__', '__subclasshook__', '__init_subclass__', '__format__', '__sizeof__', '__dir__', '__class__']
	#print(request.path_info, flush=True)
	return render(request, "base.html")




class UserViewSet(_UserViewSet):
	renderer_classes = [TemplateHTMLRenderer]
	template_name = 'base.html'



	

class ProductViewSet(_ProductViewSet):
	renderer_classes = [TemplateHTMLRenderer]
	template_name = 'list_test.html'

	def get_template_names(self):
		print(self.__dir__(),flush=True)
		if self.action == "list":
			return ["list_test.html"]

		return ["base.html"]



class OrderViewSet(_OrderViewSet):
	renderer_classes = [TemplateHTMLRenderer]
	template_name = 'base.html'

class CommentViewSet(_CommentViewSet):
	renderer_classes = [TemplateHTMLRenderer]
	template_name = 'base.html'







