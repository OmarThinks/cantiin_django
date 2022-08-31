from rest_framework.reverse import reverse as rest_reverse


def reverse(self, url_name:str,query_params:dict=None):
	request = self.context.get("request")
	url_string = str(rest_reverse(url_name, request = request))
	if query_params != None:
		url_string +="?"
		for key in query_params:
			url_string += key + "=" + str(query_params[key])+"&"
		url_string = url_string[:-1]
	return url_string
