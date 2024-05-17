from odoo import models, fields


class ProjectTask(models.Model):
    _inherit = ["project.task"]
    # no se hereda mail.threads ni mixing porque project.task ya los hereda al crearse

    # tracking=True deberia funcionar
    description = fields.Html(tracking=True)
