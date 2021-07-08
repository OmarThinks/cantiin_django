from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
"""
Every one can view all detail of the website
(

User (username, id, url)
Product (id, url, name, in_stock, ..)
Order (id, url, amount, product, author,..)
Comment (id, url, Content, product, Author)

)
"""



class CanttinPermission(permissions.BasePermission):


	"""
	Model Level
	(List and Post)
	"""
	def has_permission(self, request, view):
		if request.method in permissions.SAFE_METHODS:
			return True
			# Anyone can list
		if request.user.is_authenticated:
			print(request.auth,flush=True)
			return True
			# No one can Post if he is not authenticated
		return False
		# If the user is authenticated, he can Post

	"""
	Object-level permission to only allow owners of an object to edit it.
	Assumes the model instance has an `owner` attribute.

	(Details, Edit and Delete)
	"""
	def has_object_permission(self, request, view, obj):
		# Read permissions are allowed to any request,
		# so we'll always allow GET, HEAD or OPTIONS requests.
		if request.method in permissions.SAFE_METHODS:
			return True 
			# Every one can see the details of the website
		if request.user.is_authenticated == False:
			return False
			# unauthenticated users can not change any thing
		try:
			if obj.author == request.user:
				return True 
				# The author can edit his items
				# some models have no author
		except Exception as e:
			return False
		if request.user.is_superuser:
			return True
			# The superuser can modify any model (Except the user model)
		return False
