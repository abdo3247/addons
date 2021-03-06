# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2015 BADEP (<http://badep.ma>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name' : 'Fleet Accounting',
    'version' : '0.1',
    'author' : 'BADEP',
    'category': 'Fleet with Accounting',
    'website' : 'http://www.badep.ma',
    'summary' : 'Vehicle, accounting',
    'description' : """
Directly link the fleet management to accounting.
""",
    'depends' : [
        'fleet',
        'account',
    ],
    'data' : [
              'fleet_view.xml'
    ],
    'installable' : True,
    'application' : False,
}
