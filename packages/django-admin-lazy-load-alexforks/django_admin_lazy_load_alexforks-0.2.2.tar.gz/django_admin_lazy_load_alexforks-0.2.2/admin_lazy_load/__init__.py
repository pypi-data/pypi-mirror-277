from functools import partial

import easy
from django.contrib import admin
from django.http import HttpResponse
from django.urls import reverse
from django.utils.html import format_html
from django.template.loader import render_to_string

def underscore_to_capitalize(string):
    return string.replace('_', ' ').capitalize()

class LazyLoadAdminMixin(easy.MixinEasyViews):


    lazy_loaded_fields = ()

    class Media:
        css = {
            "all": (
                "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css",
            )
        }
        js = (
            'js/lazyload.js',  # located in the app static folder
        )

    def _add_readonly_fields(self, field_name):

        if not self.readonly_fields:
            self.readonly_fields = []

        if field_name not in self.readonly_fields:
            self.readonly_fields = list(self.readonly_fields) + [field_name]


    def __init__(self, *args, **kwargs):

        def x_lazy(obj, field_name, is_click=False):

            app_label = obj._meta.app_label
            model_name = obj._meta.model.__name__.lower()
            url = reverse(
                'admin:{}_{}_easy'.format(app_label, model_name),
                args=(obj.pk, '%s_lazy' % field_name)
            )
            
            return render_to_string(
                'lazy_load_field.html', 
                context=dict(
                    id='{field}_lazy_click_{obj_id}'.format(field=field_name, obj_id=obj.pk),
                    url_to_load=url,
                    loading_type="on_click" if is_click else "immediately"
                )
            )
  
        def easy_view_x(field_name, request, pk=None, ):
            # do something here
            obj = self.get_object(request, pk)

            if obj is None:
                return HttpResponse('-')

            if hasattr(self, field_name):
                result = getattr(self, field_name)(obj)
            elif field_name in dir(obj):  # Because hasattr executes property getter code!
                result = getattr(obj, field_name)
            else:
                raise ValueError('Field {0} was not found neither in admin class nor in obj {1}'.format(field_name, obj))

            if isinstance(result, bool):
                result = '<img src="/static/admin/img/icon-yes.svg" alt="Yes" />' \
                    if result else \
                    '<img src="/static/admin/img/icon-no.svg" alt="No" />'
                result = format_html(result)
            elif result is None:
                result = '<img src="/static/admin/img/icon-unknown.svg" alt="Unknown" />'
                result = format_html(result)

            return HttpResponse(
                result
            )


        for f in self.lazy_loaded_fields:


            setattr(self, 'easy_view_%s_lazy' % f, partial(easy_view_x, f))


            func = partial(x_lazy, field_name=f, is_click=False)
            func.short_description = getattr(getattr(self, f), 'short_description', underscore_to_capitalize(f))

            setattr(self, '%s_lazy' % f, func)


            func = partial(x_lazy, field_name=f, is_click=True)
            func.short_description = getattr(getattr(self, f), 'short_description', underscore_to_capitalize(f))

            setattr(self, '%s_lazy_click' % f, func)

        super(LazyLoadAdminMixin, self).__init__(*args, **kwargs)
