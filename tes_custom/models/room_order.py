from odoo import _, api, fields, models
from odoo.exceptions import ValidationError

class RoomOrder(models.Model):
    _name = 'room.order'
    _description = 'room order'

    name = fields.Char('Nomor Pemesanan', default='New', required=True)
    room_id = fields.Many2one('room', string='Ruangan', index=True)
    order_name = fields.Char('Nama Pemesanan', required=True)
    order_date = fields.Date('Tanggal Pemesanan', required=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('ongoing', 'On Going'),
        ('done', 'Done'),
    ], string='State', default='draft')
    notes = fields.Text('Catatan')

    @api.model
    def create(self, vals):
        res = super(RoomOrder, self).create(vals)
        name = self.env['ir.sequence'].next_by_code('room.order')\
            .replace('.', res.room_id.type.upper())
        res.write({'name': name})
        return res

    def action_ongoing(self):
        """Set state to be ongoing"""
        self.state = 'ongoing'

    def action_done(self):
        """Set state to be done"""
        self.state = 'done'

    @api.constrains('order_date')
    def check_order_date(self):
        """Restrict to set room order in same order date"""
        if len(self.search([('order_date', '=', self.order_date), 
                            ('room_id', '=', self.room_id.id)])) > 1:
            raise ValidationError(_('Tanggal pemesanan tidak boleh sama'))
        
    @api.constrains('order_name')
    def check_order_name(self):
        """Restrict to set room order in same order date"""
        if len(self.search([('order_date', '=', self.order_date), 
                            ('order_name', '=', self.order_name)])) > 1:
            raise ValidationError(_('Nama pemesanan tidak boleh sama'))

    