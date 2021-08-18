from pprint import pprint as pp
from markupsafe import Markup

def render_text(field_name, field_name_capitalized, field_type):
	return f'''

		<label>{field_name_capitalized}</label>
		<input id="input_field_{field_name}"
		name="{field_name}" class="form-control" 
		type="{field_type}"  value="" >
	'''

def render_number(field_name, field_name_capitalized,field_type):
	return render_text(field_name, field_name_capitalized, field_type)

def render_checkbox(field_name, field_name_capitalized, field_type):
	return f'''
		
		<div class="{field_type}">
		<label>
		  <input id="input_field_{field_name}"
		  type="{field_type}" name="{field_name}" value=true >
		    {field_name_capitalized}
		</label>
		</div>

	'''


def render_field(field_name:str, field_name_capitalized:str, field_type:str):
	if field_type == "text":
		return render_text(field_name, field_name_capitalized, field_type)
	if field_type == "number":
		return render_number(field_name, field_name_capitalized, field_type)
	if field_type == "checkbox":
		return render_checkbox(field_name, field_name_capitalized, field_type)
	raise Exception("This field is unknown: "+str(field_name))


def form_renderer(form_list):
	final_form = ""
	for element in form_list:
		field_name = element["name"]
		field_name_capitalized = element["name_capitalized"]
		field_type = element["type"]
		final_form += '''
		
		<div class="form-group ">

		'''
		final_form += render_field(field_name, 
			field_name_capitalized, field_type)

		final_form += f'''

			<ul class="form_field_error" 
				id="form_field_error_{field_name}"">
				<li>Something is wrong</li>
			</ul>
		
		</div>

		'''
	return Markup(final_form)





def form_fields_names_list(form_list):
	fields_names = []
	for form_element in form_list:
		#pp(form_element["name"])
		fields_names.append(form_element["name"])
	#pp(fields_names)
	return fields_names


def form_errors_ids_list(form_list):
	fields_names = form_fields_names_list(form_list)
	errors_ids = []
	for field_name in fields_names:
		errors_ids.append( "form_field_error_" + field_name)
	return errors_ids

