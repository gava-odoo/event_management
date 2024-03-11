#-*- coding: utf-8 -*-

# from odoo import api, fields, models, Command


# class AccountEstateProperty(models.Model):
#     _inherit = 'event.event'
    
#     def action_start(self):
#         self.ensure_one()
#         values = {
#             'partner_id': self.buyer_id.id,
#             'move_type': 'out_invoice',
#             'invoice_line_ids': [
#                 Command.create({'name': self.name, 'quantity': 1, 'price_unit': 0.06 * self.selling_price}),
#                 Command.create({'name': 'Administrative Fees', 'quantity': 1, 'price_unit': 100}),
#             ],
#         }
#         self.env['account.move'].create(values)
#         return super().action_start()