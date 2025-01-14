from odoo import _, api, fields, models
from odoo.exceptions import ValidationError

class Room(models.Model):
    _name = 'room'
    _description = 'Room'

    name = fields.Char('Nama', required=True)
    type = fields.Selection([
        ('kecil', 'Ruang Meeting Kecil'),
        ('besar', 'Ruang Meeting Besar'),
        ('aula', 'Aula')
    ], string='Tipe', required=True)
    location = fields.Selection([
        ('1a', '1A'),
        ('1b', '1B'),
        ('1c', '1C'),
        ('2a', '2A'),
        ('2b', '2B'),
        ('2c', '2C'),
    ], string='Lokasi', required=True)
    photo = fields.Binary('Foto', required=True)
    capacity = fields.Integer('Kapasitas', required=True)
    notes = fields.Text('Keterangan')

    @api.constrains('name')
    def check_name(self):
        """Restrict to set room with same name"""
        if len(self.search([('name', '=', self.name)])) > 1:
            raise ValidationError(_('Nama ruangan tidak boleh sama'))



    