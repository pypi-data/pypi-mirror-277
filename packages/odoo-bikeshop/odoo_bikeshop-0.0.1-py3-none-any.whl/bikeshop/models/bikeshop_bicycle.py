from odoo import api, fields, models, _


class Bicycle(models.Model):
    _name = "bikeshop.bicycle"
    _description = "A customer owned bicycle"
    _rec_name = 'serial'

    serial = fields.Char(string='Serial Number',
                         required=True, index='btree', copy=False)
    color = fields.Char(string='Color', required=True, translate=True)
    make = fields.Char(string='Make', required=True)
    model = fields.Char(string='Model', required=True)
    owner_id = fields.Many2one(
        string='Owner', comodel_name='res.partner', ondelete='set null')
    battery_key = fields.Char(string='Battery Key', required=False)
    notes = fields.Text(string='Notes', required=False)
    display_name = fields.Char(compute='_compute_display_name', store=False)
    workorder_id = fields.One2many(string='Work Orders',
                                   comodel_name='sale.order',
                                   inverse_name='bike_id')

    _sql_constraints = [
        ('unique_sn', 'UNIQUE (serial)',
         'Bicycle serial numbers should be unique.'),
    ]

    @api.depends('color', 'make', 'model')
    def _compute_display_name(self):
        for record in self:
            record.update({
                'display_name': _(f"{record.color} {record.make} {record.model}"),
            })
