# controllers/main.py
import os
import json

from odoo import http, tools
from odoo.http import request


class RoomOrder(http.Controller):

    # get all room order
    @http.route('/api/room_order', type='http', auth='public', methods=['GET'], csrf=False)
    def get_room_order(self, **kw):
        orders = request.env['room.order'].search([])
        data = []
        for o in orders:
            data.append({
                'id': o.id,
                'no_order': o.name,
                'order_date': o.order_date.strftime('%Y-%m-%d') if o.order_date else None,
                'room': o.room_id.name,
                'state': o.state,
            })
        return request.make_response(json.dumps({'orders': data}),
                                 headers=[('Content-Type', 'application/json')])
    
    # get room order based on room id
    @http.route('/api/room_order/room/<int:room_id>', type='http', auth='public', methods=['GET'], csrf=False)
    def get_room_order_by_room_id(self, room_id, **kw):
        orders = request.env['room.order'].search([('room_id', '=', room_id)])
        if orders.exists():
            data = []
            for o in orders:
                data.append({
                    'id': o.id,
                    'no_order': o.name,
                    'order_date': o.order_date.strftime('%Y-%m-%d') if o.order_date else None,
                    'room': o.room_id.name,
                    'state': o.state,
                })
            return request.make_response(json.dumps({'orders': data}),
                                 headers=[('Content-Type', 'application/json')])
        else:
            return request.make_response(json.dumps({'error': 'Order not found'}),
                                 headers=[('Content-Type', 'application/json')])
        
    # get room order based on order name  
    @http.route('/api/room_order/order_name/<string:order_name>', type='http', auth='public', methods=['GET'], csrf=False)
    def get_room_order_by_order_name(self, order_name, **kw):
        orders = request.env['room.order'].search([('order_name', '=', order_name)])
        if orders.exists():
            data = []
            for o in orders:
                data.append({
                    'id': o.id,
                    'no_order': o.name,
                    'order_date': o.order_date.strftime('%Y-%m-%d') if o.order_date else None,
                    'room': o.room_id.name,
                    'state': o.state,
                })
            return request.make_response(json.dumps({'orders': data}),
                                 headers=[('Content-Type', 'application/json')])
        else:
            return request.make_response(json.dumps({'error': 'Order not found'}),
                                 headers=[('Content-Type', 'application/json')])
        
    @http.route('/api-docs/swagger.yml', type='http', auth='public', methods=['GET'], csrf=False)
    def swagger_spec(self):
        try:
            module_path = tools.config['custom_path']
            path = os.path.join(module_path, 'tes_custom', 'static', 'swagger.yml')

            with open(path, 'r') as file:
                swagger_content = file.read()

            return http.Response(swagger_content, content_type='application/x-yaml')

        except Exception as e:
            return http.Response(f"Error: {str(e)}", status=500, content_type='text/plain')
    
    
