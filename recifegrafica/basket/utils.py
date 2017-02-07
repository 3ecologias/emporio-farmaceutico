from oscar.apps.basket.utils import BasketMessageGenerator as CoreBasketMessageGenerator
from django.contrib import messages
from django.template.loader import render_to_string




class BasketMessageGenerator(CoreBasketMessageGenerator):
    configured_art_template_name = 'basket/messages/art_configurated.html'


    def get_conf_sucess(self, request, basket, include_buttons=True):
        conf_message = []
        print render_to_string(self.configured_art_template_name,
                               {'basket': basket,
                                'include_buttons': include_buttons})

        msg = render_to_string(self.configured_art_template_name,
                               {'basket': basket,
                                'include_buttons': include_buttons})
        conf_message.append((messages.SUCCESS, msg))
        print conf_message
        for level, msg in conf_message:
            messages.add_message(request, level, msg, extra_tags='safe noicon')

        return messages
