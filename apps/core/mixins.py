from django.contrib import messages

class MessageMixin(object):
    success_message = "Information saved successfully!"
    error_message = "The form has errors, please review the information!"
    already_exists_message = "A record with this data already exists!"

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super(MessageMixin, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, self.error_message)
        return super(MessageMixin, self).form_invalid(form)

    def form_invalid_exists(self, form):
        messages.error(self.request, self.already_exists_message)
        return super(MessageMixin, self).form_invalid(form)
