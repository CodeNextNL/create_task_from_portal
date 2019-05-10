# Copyright (C) codeNext
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, SUPERUSER_ID
import logging

_logger = logging.getLogger(__name__)


def post_init_hook(cr, registry):
    """Whitelist form fields in ir.model.fields."""
    whitelist_fields = {
        "name": "project.task",
        "date_deadline": "project.task",
        "project_id": "project.task",
        "stage_id": "project.task",
        "user_id": "project.task"
    }
    with api.Environment.manage():
        env = api.Environment(cr, SUPERUSER_ID, {})
        for name, model in list(whitelist_fields.items()):
            env.cr.execute(
                "UPDATE ir_model_fields"
                " SET website_form_blacklisted=false"
                " WHERE model=%s AND name =%s", (model, name))
            _logger.info('%s whitelisted!', name)
