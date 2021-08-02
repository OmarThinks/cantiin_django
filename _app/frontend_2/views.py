from django.shortcuts import render

# Create your views here.

import json

from cantiin.views import UserViewSet as _UserViewSet
from cantiin.views import ProductViewSet as _ProductViewSet
from cantiin.views import OrderViewSet as _OrderViewSet
from cantiin.views import CommentViewSet as _CommentViewSet
from rest_framework.renderers import (
	TemplateHTMLRenderer,BrowsableAPIRenderer,JSONRenderer,
	 StaticHTMLRenderer)
from rest_framework.views import APIView

from frontend.abstract_renderers import abstract_list_renderer
from django.http.response import HttpResponseBase
from rest_framework.response import Response
from django.utils.cache import cc_delim_re, patch_vary_headers


from rest_framework.views import APIView


def base_page(request):
	#return HttpResponse("Home Page")
	#print(request.__dir__(), flush=True)
	#['environ', 'path_info', 'path', 'META', 'method', 'content_type', 'content_params', '_stream', '_read_started', 'resolver_match', 'COOKIES', 'session', 'user', '_messages', 'csrf_processing_done', '__module__', '__init__', '_get_scheme', 'GET', '_get_post', '_set_post', 'FILES', 'POST', '__doc__', '_encoding', '_upload_handlers', '__repr__', 'headers', 'accepted_types', 'accepts', '_set_content_type_params', '_get_raw_host', 'get_host', 'get_port', 'get_full_path', 'get_full_path_info', '_get_full_path', 'get_signed_cookie', 'get_raw_uri', 'build_absolute_uri', '_current_scheme_host', 'scheme', 'is_secure', 'is_ajax', 'encoding', '_initialize_handlers', 'upload_handlers', 'parse_file_upload', 'body', '_mark_post_parse_error', '_load_post_and_files', 'close', 'read', 'readline', '__iter__', 'readlines', '__dict__', '__weakref__', '__hash__', '__str__', '__getattribute__', '__setattr__', '__delattr__', '__lt__', '__le__', '__eq__', '__ne__', '__gt__', '__ge__', '__new__', '__reduce_ex__', '__reduce__', '__subclasshook__', '__init_subclass__', '__format__', '__sizeof__', '__dir__', '__class__']
	#print(request.path_info, flush=True)
	return render(request, "base.html")




class UserViewSet(_UserViewSet):
	renderer_classes = [TemplateHTMLRenderer]
	template_name = 'base.html'


class customRenderer(TemplateHTMLRenderer):
	"""def resolve_context(self, args2, request, 
		response, *args, **kwargs):
		#print(self.__dir__(),flush=True)
		#print(type(self),flush=True)
		#print(args2.__dict__,flush=True) a function
		#print(type(request),flush=True)
		#print(response.__dir__(),flush=True)
		print(self.__dict__,flush=True)
		print(args2.__dict__,flush=True)
		print(request.__dict__,flush=True)
		print(response.__dict__,flush=True)
		#print(request.user.__dir__(),flush=True)
		#results = response.data["results"]
		print(results ,flush=True)
		for product in results:
			print(product, flush=True)
			print(product["id"], flush=True)
		#results_new = 
		return{	
			"response":response,
			"items_plural":"products",
			"additional_css_files":[],
			"active_main_navbar": "products",
			"title": "Products List",
			"item_url_name" : "product-detail"
		}"""
	def get_default_renderer(*args,**kwargs):
		return BrowsableAPIRenderer.get_default_renderer(*args, **kwargs)

	def get_template_context(self, data,  
		renderer_context , accepted_media_type= "txt/html"):
		"""
		Returns the context used to render.
		"""
		view = renderer_context['view']
		request = renderer_context['request']
		response = renderer_context['response']

		renderer = self.get_default_renderer(view)

		raw_data_post_form = self.get_raw_data_form(data, view, 'POST', request)
		raw_data_put_form = self.get_raw_data_form(data, view, 'PUT', request)
		raw_data_patch_form = self.get_raw_data_form(data, view, 'PATCH', request)
		raw_data_put_or_patch_form = raw_data_put_form or raw_data_patch_form

		response_headers = OrderedDict(sorted(response.items()))
		renderer_content_type = ''
		if renderer:
			renderer_content_type = '%s' % renderer.media_type
			if renderer.charset:
				renderer_content_type += ' ;%s' % renderer.charset
		response_headers['Content-Type'] = renderer_content_type

		if getattr(view, 'paginator', None) and view.paginator.display_page_controls:
			paginator = view.paginator
		else:
			paginator = None

		csrf_cookie_name = settings.CSRF_COOKIE_NAME
		csrf_header_name = settings.CSRF_HEADER_NAME
		if csrf_header_name.startswith('HTTP_'):
			csrf_header_name = csrf_header_name[5:]
		csrf_header_name = csrf_header_name.replace('_', '-')

		final_context =  {
			'content': self.get_content(renderer, data, accepted_media_type, renderer_context),
			'code_style': pygments_css(self.code_style),
			'view': view,
			'request': request,
			'response': response,
			'user': request.user,
			'description': self.get_description(view, response.status_code),
			'name': self.get_name(view),
			'version': VERSION,
			'paginator': paginator,
			'breadcrumblist': self.get_breadcrumbs(request),
			'allowed_methods': view.allowed_methods,
			'available_formats': [renderer_cls.format for renderer_cls in view.renderer_classes],
			'response_headers': response_headers,

			'put_form': self.get_rendered_html_form(data, view, 'PUT', request),
			'post_form': self.get_rendered_html_form(data, view, 'POST', request),
			'delete_form': self.get_rendered_html_form(data, view, 'DELETE', request),
			'options_form': self.get_rendered_html_form(data, view, 'OPTIONS', request),

			'extra_actions': self.get_extra_actions(view, response.status_code),

			'filter_form': self.get_filter_form(data, view, request),

			'raw_data_put_form': raw_data_put_form,
			'raw_data_post_form': raw_data_post_form,
			'raw_data_patch_form': raw_data_patch_form,
			'raw_data_put_or_patch_form': raw_data_put_or_patch_form,

			'display_edit_forms': bool(response.status_code != 403),

			'api_settings': api_settings,
			'csrf_cookie_name': csrf_cookie_name,
			'csrf_header_name': csrf_header_name
		}	
		print(final_context, flush=True)
		return final_context
		
	


class ProductViewSet(_ProductViewSet):
	renderer_classes = [JSONRenderer, TemplateHTMLRenderer]
	template_name = 'base_layout.html'

	"""def resolve_context(self):
		return {"response":self.response}"""
	
	def get_renderer_context(self, response):
		# https://github.com/encode/django-rest-framework/blob/98e56e0327596db352b35fa3b3dc8355dc9bd030/rest_framework/views.py#L205
		context = APIView.get_renderer_context(self)
		print(context, flush=True)
		"""{
			'view': <frontend_2.views.ProductViewSet object at 
				0x00000107495DAC40>, 
			'args': (), 'kwargs': {}, 
			'request': <rest_framework.request.Request: 
				GET '/base/products/'>
		}"""
		print(self.__dir__(), flush=True)
		print(self.request.__dir__(), flush=True)
		print(self.request._full_data, flush=True)
		print(self.request._data, flush=True)
		#context["response"] = self.response
		return context
	def finalize_response(self, request, response, *args, **kwargs):
		"""
		Returns the final response object.
		"""
		# Make the error obvious if a proper response is not returned
		assert isinstance(response, HttpResponseBase), (
			'Expected a `Response`, `HttpResponse` or `HttpStreamingResponse` '
			'to be returned from the view, but received a `%s`'
			% type(response)
		)

		if isinstance(response, Response):
			if not getattr(request, 'accepted_renderer', None):
				neg = self.perform_content_negotiation(request, force=True)
				request.accepted_renderer, request.accepted_media_type = neg

			response.accepted_renderer = request.accepted_renderer
			response.accepted_media_type = request.accepted_media_type
			response.renderer_context = self.get_renderer_context(response)

		# Add new vary headers to the response instead of overwriting.
		vary_headers = self.headers.pop('Vary', None)
		if vary_headers is not None:
			patch_vary_headers(response, cc_delim_re.split(vary_headers))

		for key, value in self.headers.items():
			response[key] = value

		return response

	def get_template_names(self):
		#print(self.response.data,flush=True)
		if self.action == "list":
			#return ["list_test.html"]
			return ["resources/products/list.html"]

		return ["base_layout.html"]



class OrderViewSet(_OrderViewSet):
	renderer_classes = [TemplateHTMLRenderer]
	template_name = 'base.html'

class CommentViewSet(_CommentViewSet):
	renderer_classes = [TemplateHTMLRenderer]
	template_name = 'base.html'







