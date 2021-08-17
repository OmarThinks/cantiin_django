from pprint import pprint as pp


def serializer_renderer(the_serialzer):
	s = the_serialzer()
	pp(s)
	pp(s.fields)
	fields = s.fields
	for f in xrange(1,10):
		fields









