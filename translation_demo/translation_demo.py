import logging
import inspect
import os

from odoo import api, models

_logger = logging.getLogger(__name__)


class TranslationHelper(models.Model):
    _name = "translation.demo"
    _inherit = "installer.helper"

    @api.model
    def execute(self):
        self.update_translations()
        return super(TranslationHelper, self).execute()

    @api.model
    def update_translations(self):
        translation_installer = self.env['translation.installer']
        modules = [
            'account', 'base', 'crm', 'hr', 'hr_timesheet', 'project', 'resource', 'sale', 'utm', 'web'
        ]
        module_module_env = self.env['ir.module.module']
        for module in modules:
            m = module_module_env.search([('name', '=', module)], limit=1)
            if m and m.state == 'installed':
                path = '%s/translation_demo/translation/%s/vi_VN.po' % \
                       (os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))[:-17], module)
                translation_installer.update_translations(path, 'vi_VN', True)
        return True
