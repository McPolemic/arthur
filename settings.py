from datetime import date
from arthur.settings_defaults import *

global_conf = {
	'number': '15135',
}

#Set revision date to today
for i in (program_specs, unit_test, implementation):
	i['revision_history'][0]['last_update'] = date.today().strftime('%m/%d/%Y')
