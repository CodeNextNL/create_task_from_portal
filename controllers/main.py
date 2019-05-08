# -*- coding: utf-8 -*-

import base64

from parts.odoo.addons.website_form.controllers.main import WebsiteForm
from odoo.http import request
from odoo.tools.translate import _
from odoo.exceptions import ValidationError


class WebsiteForm(WebsiteForm):
    _custom_label = "%s\n___________\n\n" % _("Custom infos extension!")  # Title for custom fields

    def extract_data(self, model, values):
        data = {
            'record': {},  # Values to create record
            'attachments': [],  # Attached files
            'custom': '',  # Custom fields values
            'meta': '',  # Add metadata if enabled
        }

        authorized_fields = model.sudo()._get_form_writable_fields()
        error_fields = []

        for field_name, field_value in values.items():
            # If the value of the field if a file
            if hasattr(field_value, 'filename'):
                # Undo file upload field name indexing
                field_name = field_name.rsplit('[', 1)[0]

                # If it's an actual binary field, convert the input file
                # If it's not, we'll use attachments instead
                if field_name in authorized_fields and authorized_fields[field_name]['type'] == 'binary':
                    data['record'][field_name] = base64.b64encode(field_value.read())
                else:
                    field_value.field_name = field_name
                    data['attachments'].append(field_value)

            # If it's a known field
            elif field_name in authorized_fields:
                try:
                    input_filter = self._input_filters[authorized_fields[field_name]['type']]
                    data['record'][field_name] = input_filter(self, field_name, field_value)
                except ValueError:
                    error_fields.append(field_name)

            # If it's a custom field
            elif field_name != 'context':
                data['custom'] += u"%s\n%s\n\n" % (field_name, field_value)

        # Add metadata if enabled
        environ = request.httprequest.headers.environ
        if (request.website.website_form_enable_metadata):
            data['meta'] += "%s : %s\n%s : %s\n%s : %s\n%s : %s\n" % (
                "IP", environ.get("REMOTE_ADDR"),
                "USER_AGENT", environ.get("HTTP_USER_AGENT"),
                "ACCEPT_LANGUAGE", environ.get("HTTP_ACCEPT_LANGUAGE"),
                "REFERER", environ.get("HTTP_REFERER")
            )

        # This function can be defined on any model to provide
        # a model-specific filtering of the record values
        # Example:
        # def website_form_input_filter(self, values):
        #     values['name'] = '%s\'s Application' % values['partner_name']
        #     return values
        dest_model = request.env[model.sudo().model]
        if hasattr(dest_model, "website_form_input_filter"):
            data['record'] = dest_model.website_form_input_filter(request, data['record'])

        missing_required_fields = [label for label, field in authorized_fields.items() if
                                   field['required'] and not label in data['record']]
        if any(error_fields):
            raise ValidationError(error_fields + missing_required_fields)

        return data
