from rest_framework.renderers import BrowsableAPIRenderer


class LightBrowsableAPIRenderer(BrowsableAPIRenderer):

    def get_context(self, data, accepted_media_type, renderer_context):
        context = super(LightBrowsableAPIRenderer, self).get_context(data,
            accepted_media_type, renderer_context)
        context['display_edit_forms'] = False
        return context

    def get_rendered_html_form(self, data, view, method, request):
        """Overwritten to avoid generating useless db queries"""
        return ""
