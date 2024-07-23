#-*- coding: utf-8 -*-

from odoo import http, fields
from werkzeug.utils import redirect

class EventManagement(http.Controller):
    @http.route(['/events/page/<int:page>','/events/page/1'], type='http', auth='public', website=True)
    def events_page(self, page=1, date=None):
        condition = [('state', 'not in', ['started', 'finished', 'cancelled'])]
        if date:
            condition.append(('start_date', '>', date))
        page = int(page)
        # gava
        events_per_page = 3
        Event = http.request.env['event.event']
        all_events = Event.search_count(condition)
        total_pages = (all_events + events_per_page - 1) // events_per_page
        events = Event.search(condition, limit=events_per_page, offset=(page - 1) * events_per_page)

        pager = http.request.website.pager(
            url='/events',
            total=all_events,
            page=page,
            step=events_per_page,
            scope=total_pages,
        )
        event = events.search(condition, limit=events_per_page, offset=events_per_page*(page-1))
        return http.request.render('event_management.events',{
            'events': events,
            'pager': pager,
            'page': page
            # 'date' : date
        })

    @http.route('/events', type='http', auth="public", website=True)
    def events(self):
        return redirect('/events/page/1')

    @http.route('/events/<int:page>/details/<int:id>', type='http', auth='public', website=True)
    def event_details(self, id, page=1):
        page = int(page)
        event_d = http.request.env['event.event'].browse(id)
        return http.request.render('event_management.event_details',{
            'event_d': event_d,
            'page': page
        })
