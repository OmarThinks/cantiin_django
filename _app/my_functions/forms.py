from pprint import pprint as pp


def render_text(field_name, field_name_capitalized):
	return ""
def render_number(field_name, field_name_capitalized):
	return ""
def render_checkbox(field_name, field_name_capitalized):
	return ""


def render_field(field_name:str, field_name_capitalized:str, field_type:str):
	if field_type == "text":
		return render_text(field_name, field_name_capitalized)
	if field_type == "number":
		return render_number(field_name, field_name_capitalized)
	if field_type == "checkbox":
		return render_checkbox(field_name, field_name_capitalized)
	raise Exception("This field is unknown: "+str(field_name))



def form_renderer(form_list):
	final_form = ""
	for element in form_list:
		field_name = element["name"]
		field_name_capitalized = element["name_capitalized"]
		field_type = element["type"]
		final_form += render_field(field_name, 
			field_name_capitalized, field_type)
	return final_form








