# Copyright (C) codeNext
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, SUPERUSER_ID
import logging

_logger = logging.getLogger(__name__)


def post_init_hook(cr, registry):
    """Whitelist form fields in ir.model.fields."""
    with api.Environment.manage():
        env = api.Environment(cr, SUPERUSER_ID, {})
        base_nl = env.ref('base.nl')
        _logger.info('Setting Netherlands NUTS configuration')
        base_nl.write({'state_level': 3})