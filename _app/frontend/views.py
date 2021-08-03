from django.shortcuts import render

from cantiin.views import (
	UserViewSet as _UserViewSet, ProductViewSet as _ProductViewSet,
	OrderViewSet as _OrderViewSet, CommentViewSet as _CommentViewSet)

from rest_framework.renderers import (
	TemplateHTMLRenderer,JSONRenderer)








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
	additional_css_files=[], item_url_name=""):
	class customRenderer(TemplateHTMLRenderer):
		def get_template_context(self, data, renderer_context, 
			items_plural= items_plural, active_main_navbar=active_main_navbar,
			title=title, additional_css_files= additional_css_files,
			item_url_name= item_url_name):
			response = dict(data)
			#print(self, flush=True)
			#print(response, flush=True)
			#print(type(response), flush=True)
			#print(renderer_context["response"].__dir__(), flush=True)
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
			"paginator":paginator
			}
			try:
				paginator = renderer_context["view"].paginator
				context["paginator"] = paginator
			except Exception as e:
				pass
			#print(context["paginator"],flush=True)
			return context
	return customRenderer


class ProductViewSet(_ProductViewSet):
	#renderer_classes = [JSONRenderer, customRenderer]
	template_name = 'base_layout.html'


	def get_template_names(self):
		print(self.action,flush=True)
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
		renderers = [JSONRenderer, customRenderer]
		return [renderer() for renderer in renderers]


class OrderViewSet(_OrderViewSet):
	renderer_classes = [TemplateHTMLRenderer]
	template_name = 'base_layout.html'

class CommentViewSet(_CommentViewSet):
	renderer_classes = [TemplateHTMLRenderer]
	template_name = 'base_layout.html'







### Authentication


from djoser.serializers import UserCreateSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class SignupView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'resources/auth/createuser.html'

    def get(self, request):
        serializer = UserCreateSerializer()
        return Response({'serializer': serializer, "title":"Sign Up"})



