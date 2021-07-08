from rest_framework import permissions



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
	Object-level permission to only allow owners of an object to edit it.
	Assumes the model instance has an `owner` attribute.
	"""
	def has_object_permission(self, request, view, obj):
		# Read permissions are allowed to any request,
		# so we'll always allow GET, HEAD or OPTIONS requests.
		if request.method in permissions.SAFE_METHODS:
			return True 
			# Every one can see the details of the website
		try:
			if obj.author == request.user:
				return True 
				# The author can edit his items
				#some models have no author
		except Exception as e:
			pass
		if request.user.is_superuser:
			return True
			# The superuser can any model (Except the user model)
		return False