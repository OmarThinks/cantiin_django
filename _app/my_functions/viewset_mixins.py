from rest_framework import viewsets

class HasAuthorViewsetMixin(viewsets.ModelViewSet):
	def perform_create(self, serializer):
		# The request user is set as author automatically.
		serializer.save(author=self.request.user)
