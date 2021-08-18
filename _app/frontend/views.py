from django.shortcuts import render

from cantiin.serializers import ProductSerializer

from cantiin.views import (
	UserViewSet as _UserViewSet, ProductViewSet as _ProductViewSet,
	OrderViewSet as _OrderViewSet, CommentViewSet as _CommentViewSet)

from rest_framework.renderers import (
	TemplateHTMLRenderer,JSONRenderer, BrowsableAPIRenderer)


from my_functions.forms import (form_renderer,
	form_fields_names_list, form_errors_ids_list)


#import pprint
from pprint import pprint as pp


from markupsafe import Markup





def homepage(request):
	#return HttpResponse("Home Page")
	return render(request, "pages/home.html",
		{
			"active_main_navbar": "home",
			"title": "Home"
		}			
	)






class UserViewSet(_UserViewSet):
	renderer_classes = [TemplateHTMLRenderer]
	template_name = 'base_layout.html'


def generate_custom_renderer(
	items_plural, active_main_navbar, title,
	additional_css_files=[], item_url_name="", create_text="",
	create_link=""):
	class customRenderer(TemplateHTMLRenderer):
		def get_template_context(self, data, renderer_context, 
			items_plural= items_plural, active_main_navbar=active_main_navbar,
			title=title, additional_css_files= additional_css_files,
			item_url_name= item_url_name, create_text=create_text,
			create_link=create_link):
			#print(type(info))
			#print(self.__dir__(),flush=True)
			#print(self.get_template_context.__dir__(),flush=True)
			#print(renderer_context,flush=True)
			#  The only userful thing in renderer_context is ["view"]
			#print(renderer_context["view"].__dict__,flush=True)

			
			#print(renderer_context["request"].__dict__,flush=True)
			#print(renderer_context["view"].get(renderer_context["request"]).__dict__, flush=True)

			#if just_renderer_context:
			#	return TemplateHTMLRenderer.get_template_context(self,data,renderer_context)
			response = dict(renderer_context["view"].get(renderer_context["request"]).data)
			#print(response, flush=True)
			#print(type(response), flush=True)
			#print(type(dict(response)), flush=True)
			#print(self, flush=True)
			#print(response, flush=True)
			#print(type(response), flush=True)
			#print(renderer_context["response"].__dict__, flush=True)
			#print(renderer_context["view"].__dir__(), flush=True)
			items_plural = items_plural 
			additional_css_files = additional_css_files
			active_main_navbar = active_main_navbar
			title = title
			item_url_name = item_url_name

			paginator = renderer_context["view"].paginator
			#print(paginator.__dir__(), flush=True)

			context = {
			"response":response,
			"item_url_name":item_url_name,
			"items_plural" : items_plural, 
			"additional_css_files": additional_css_files,
			"active_main_navbar": active_main_navbar, "title": title,
			"paginator":paginator,
			"create_text":create_text,
			"create_link":create_link
			}
			try:
				paginator = renderer_context["view"].paginator
				context["paginator"] = paginator
			except Exception as e:
				pass
			#print(context,flush=True)
			return context
	return customRenderer


class ProductViewSet(_ProductViewSet):
	#renderer_classes = [JSONRenderer, customRenderer]
	template_name = 'base_layout.html'


	def get_template_names(self):
		#print(self.action,flush=True)
		if self.action == "list":
			return ["resources/products/list.html"]
		if self.action == "retrieve":
			return ["resources/products/retrieve.html"]
		return ["base_layout.html"]
	def get_renderers(self):
		customRenderer = generate_custom_renderer(
			items_plural="products",active_main_navbar= "products",
			title="Product Details", additional_css_files=[], 
			item_url_name="frontend:product-detail")
		renderers = [customRenderer]
		return [renderer() for renderer in renderers]




def create_product(request):
	#return HttpResponse("Login")
	#pprint(ProductSerializer().__dict__)
	#pprint(ProductSerializer().__dir__())
	#pprint(ProductSerializer().fields)
	#pprint(ProductSerializer.Meta.__dict__)
	#uctSerializer.__dir__())
	form_list = [
		{	"name":"name",
			"name_capitalized":"Name",
			"type":"text"
		},
		{	"name":"price",
			"name_capitalized":"Price",
			"type":"number"
		},
		{	"name":"in_stock",
			"name_capitalized":"In Stock",
			"type":"checkbox"
		},
	]
	rendered_form = form_renderer(form_list)
	
	fields_names = form_fields_names_list(form_list)
	errors_ids=form_errors_ids_list(form_list)
	
	#pp(rendered_form)
	#pp(fields_names)
	#pp(errors_ids)

	return render(request, "form_master.html",
		{
			"title": "Create Product",
			"serializer":ProductSerializer,
			"request_destination":"/api/products/",
			"request_method":"POST", 
			"rendered_form":rendered_form,
			"after_scuess_url":"/my_products/",
			"fields_names":fields_names,
			"errors_ids":errors_ids
		})		
	

def update_product(request, pk):
	print(pk, flush=True)
	#return HttpResponse("Login")
	#pprint(ProductSerializer().__dict__)
	#pprint(ProductSerializer().__dir__())
	#pprint(ProductSerializer().fields)
	#pprint(ProductSerializer.Meta.__dict__)
	#uctSerializer.__dir__())
	form_list = [
		{	"name":"name",
			"name_capitalized":"Name",
			"type":"text"
		},
		{	"name":"price",
			"name_capitalized":"Price",
			"type":"number"
		},
		{	"name":"in_stock",
			"name_capitalized":"In Stock",
			"type":"checkbox"
		},
	]
	rendered_form = form_renderer(form_list)
	
	fields_names = form_fields_names_list(form_list)
	errors_ids=form_errors_ids_list(form_list)
	
	#pp(rendered_form)
	#pp(fields_names)
	#pp(errors_ids)

	return render(request, "form_master.html",
		{
			"title": "Create Product",
			"serializer":ProductSerializer,
			"request_destination":"/api/products/",
			"request_method":"POST", 
			"rendered_form":rendered_form,
			"after_scuess_url":"/my_products/",
			"fields_names":fields_names,
			"errors_ids":errors_ids
		})		
	
	










class OrderViewSet(_OrderViewSet):
	renderer_classes = [TemplateHTMLRenderer]
	template_name = 'base_layout.html'

class CommentViewSet(_CommentViewSet):
	renderer_classes = [TemplateHTMLRenderer]
	template_name = 'base_layout.html'




































"""

Deprecated


"""










def genrateMyCustomRenderer(template_name):
	class MyRenderer(BrowsableAPIRenderer):
		template = template_name
	return MyRenderer
			



class ProductViewSetMod(_ProductViewSet):
	def get_renderers(self):
		print(self.__dict__, flush=True)
		if self.action == "list":
			template_name = "resources/products/list.html"
		if self.action == "retrieve":
			template_name = "resources/products/retrieve.html"
		
		renderers = [genrateMyCustomRenderer(template_name)]
		return [renderer() for renderer in renderers]
	
	def get_renderer_context(self):
		context = APIView.get_renderer_context(self)
		print(context, flush=True)
		#{'view': <frontend.views.ProductViewSetMod object at 0x0000020B1ECC59A0>, 'args': (), 'kwargs': {}, 'request': <rest_framework.request.Request: GET '/products/'>}
		print(context["request"].__dict__, flush=True)
		print(context["view"].__dict__, flush=True)
		print(context["view"]._paginator.__dict__, flush=True)
		print(context["view"].get(context["request"]).__dict__, flush=True)
		return context


	"""def get_template_names(self):
		print(self.action,flush=True)
		if self.action == "list":
			return ["resources/products/list.html"]
		if self.action == "retrieve":
			return ["resources/products/retrieve.html"]
		return ["base_layout.html"]"""
	"""def get_renderers(self):
		customRenderer = generate_custom_renderer(
			items_plural="products",active_main_navbar= "products",
			title="Product Details", additional_css_files=[], 
			item_url_name="frontend:product-detail")
		renderers = [JSONRenderer, customRenderer]
		return [renderer() for renderer in renderers]"""















### Authentication

"""
from djoser.serializers import UserCreateSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class SignupView(APIView):
	renderer_classes = [TemplateHTMLRenderer]
	template_name = 'resources/auth/createuser.html'

	def get(self, request):
		serializer = UserCreateSerializer()
		return Response({'serializer': serializer, "title":"Sign Up"})

"""




from djoser.views import UserViewSet as _DjoserUserViewSet
from rest_framework.views import APIView
from rest_framework.response import Response


class UserRenderer(BrowsableAPIRenderer):
	template = "base_layout.html"
		





def genrateDjoserRenderer(title):
	items_plural ="users"
	active_main_navbar="login"
	renderer = generate_custom_renderer(
		items_plural=items_plural, active_main_navbar=active_main_navbar, 
		title=title)
	class MyRenderer(renderer):
		def get_template_context(self, data, renderer_context, 
			items_plural= items_plural, active_main_navbar=active_main_navbar,
			title=title):
			
			context = renderer.get_template_context(self, data, 
				renderer_context, 
			items_plural= items_plural, active_main_navbar=active_main_navbar,
			title=title)
			
			return context
	return MyRenderer
			





class DjoserUserViewSet(_DjoserUserViewSet):
	renderer_classes = [JSONRenderer,genrateDjoserRenderer("Sign Up")]
	def create(self, request, *args, **kwargs):
		response = _DjoserUserViewSet.create(
			self, request, *args, **kwargs)
		return response
	template_name = 'resources/auth/createuser.html'
	#template_name = 'base_layout.html'
	"""renderer_classes = [JSONRenderer, 
		generate_custom_renderer(
		items_plural="users", active_main_navbar="", title="User",
		additional_css_files=[], item_url_name="", just_renderer_context=True)]"""
	#renderer_classes = [UserRenderer]

