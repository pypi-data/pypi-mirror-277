
from django.conf import settings
from django.template import loader
from django.shortcuts import render
from django.template.exceptions import TemplateDoesNotExist


def robots(request):

    context = {}

    template_name = f"robots/{settings.SERVER_ENV}.txt"
    try:
        loader.get_template(template_name)
    except TemplateDoesNotExist:
        template_name = "robots/default.txt"

    return render(request, template_name, context=context, content_type="text/plain")
