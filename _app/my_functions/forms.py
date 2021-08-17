from pprint import pprint as pp


def render_text(field_name, field_name_capitalized, field_type):
	return f'''

		<label>{field_name_capitalized}</label>
		<input name="{field_name}" class="form-control" 
		type="{field_type}"  value="" >

	'''

def render_number(field_name, field_name_capitalized,field_type):
	return render_text(field_name, field_name_capitalized, field_type)

def render_checkbox(field_name, field_name_capitalized, field_type):
	return f'''
		
		<div class="{field_type}">
		<label>
		  <input type="{field_type}" name="{field_name}" value="true" >
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

		final_form += '''
		
		</div>

		'''



	return final_form








