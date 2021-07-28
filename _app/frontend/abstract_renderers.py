from django.shortcuts import render

def abstract_list_renderer(request, list_template_link, items, items_plural, 
	additional_css_files, active_main_navbar, title, item_url_name):
	return render(request, list_template_link,
		{
			items_plural:items,
			"additional_css_files":additional_css_files,
			"active_main_navbar": active_main_navbar,
			"title": title,
			"item_url_name" : item_url_name
		})


