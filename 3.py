import random
from pyscript import document

# ASSIGNS TEAMS
def get_team(name, grade, section):
	# GRADE 11 will have manual assignments... felt wrong to not include some </3
	if "Miguel Cerrado" in name:
		return ('Blue Bears', 'blue', '🐻')
	elif "Angelo Clar" in name:
		return ('Red Bulldogs', 'red', '🐂')
	elif "Rey Allerite" in name:
		return ('Yellow Tigers', 'yellow', '🐯')

	# STANDARD TEAM ASSIGNMENTS
	if section.lower() == 'emerald' and grade in [7, 10]:
		return ('Green Hornets', 'green', '🐝')
	elif section.lower() == 'emerald' and grade in [8, 9]:
		return ('Red Bulldogs', 'red', '🐂')
	elif section.lower() == 'ruby' and grade in [7, 10]:
		return ('Yellow Tigers', 'yellow', '🐯')
	elif section.lower() == 'ruby' and grade in [8, 9]:
		return ('Blue Bears', 'blue', '🐻')

def render_players():
	# PLAYER LIST BY GRADE AND SECTION
	players = [
		# GRADE 7
		{'name': 'Abby Levine', 'grade': 7, 'section': 'emerald'},
		{'name': 'Sabbine Orlajo', 'grade': 7, 'section': 'emerald'},
		{'name': 'Daphne Castro', 'grade': 7, 'section': 'ruby'},
		{'name': 'Thirdy Yangco', 'grade': 7, 'section': 'ruby'},
		# GRADE 8
		{'name': 'Bjorn Bengco', 'grade': 8, 'section': 'emerald'}, # mkns :[
		{'name': 'Zoe Jarlego', 'grade': 8, 'section': 'emerald'},
		{'name': 'Ethan Park', 'grade': 8, 'section': 'emerald'},
		{'name': 'Maki Cuevas', 'grade': 8, 'section': 'ruby'},
		{'name': 'Joaquin Cerrado', 'grade': 8, 'section': 'ruby'},
		{'name': 'Brian Nayve', 'grade': 8, 'section': 'ruby'},
		# GRADE 9
		{'name': 'Bhavik Aku', 'grade': 9, 'section': 'emerald'},
		{'name': 'David Barretto', 'grade': 9, 'section': 'emerald'},
		{'name': 'Oslyn Donato', 'grade': 9, 'section': 'emerald'},
		{'name': 'Simon Malimban', 'grade': 9, 'section': 'emerald'},
		{'name': 'Adam Villarica', 'grade': 9, 'section': 'emerald'},
		{'name': 'Aivind Belen', 'grade': 9, 'section': 'ruby'},
		{'name': 'Vincent Venus', 'grade': 9, 'section': 'ruby'},
		# GRADE 10
		{'name': 'David Alwit', 'grade': 10, 'section': 'emerald'},
		{'name': 'Opdesh Brar', 'grade': 10, 'section': 'emerald'},
		{'name': 'CJ Estabillo', 'grade': 10, 'section': 'emerald'},
		{'name': 'Simrat Kaur', 'grade': 10, 'section': 'emerald'},
		{'name': 'Sophia Macala', 'grade': 10, 'section': 'emerald'},
		{'name': 'Travis Platon', 'grade': 10, 'section': 'emerald'},
		{'name': 'Samuel de los Santos', 'grade': 10, 'section': 'emerald'},
		{'name': 'Tristan Aclaro', 'grade': 10, 'section': 'ruby'},
		{'name': 'Arianne Aguilar', 'grade': 10, 'section': 'ruby'},
		{'name': 'Dylan Banzali', 'grade': 10, 'section': 'ruby'},
		{'name': 'Eaden Bulo', 'grade': 10, 'section': 'ruby'},
		{'name': 'Sahilpreet Dhaliwal', 'grade': 10, 'section': 'ruby'},
		{'name': 'Sasha Ignacio', 'grade': 10, 'section': 'ruby'},
		{'name': 'Jianna Misa', 'grade': 10, 'section': 'ruby'},
		{'name': 'Jisella Ombao', 'grade': 10, 'section': 'ruby'},
		{'name': 'Curtney Sumndad', 'grade': 10, 'section': 'ruby'},
		# GRADE 11
		{'name': 'Rey Allerite', 'grade': 11, 'section': 'amorsolo'},
		{'name': 'Miguel Cerrado', 'grade': 11, 'section': 'amorsolo'},
		{'name': 'Angelo Clar', 'grade': 11, 'section': 'amorsolo'}
	]

	# SHUFFLE BC WHY NOT
	random.shuffle(players)

	# ROW PER PLAYER
	rows_html = ''
	for i, player in enumerate(players):
		name = player['name']
		grade = player['grade']
		section = player['section'].capitalize()

		# WHAT TEAM ARE THEY
		team_name, color, icon = get_team(name, grade, player['section'])

		# STORYTIME: we were supposed to be like the NBA website, but since we don't have pics, initials nalang wahhaha
		parts = name.split()
		initials = parts[0][0] + (parts[-1][0] if len(parts) > 1 else '')
		
		# ANIMATION TINGZ
		delay = i * 0.02 

		rows_html += f'''
			<tr data-team="{color}" data-name="{name.lower()}" style="animation-delay: {delay}s;">
				<td>
					<div class="td-player">
						<div class="p-avatar av-{color}">{initials}</div>
						<div>
							<div class="p-full-name">{name}</div>
							<div class="p-grade-sub">Grade {grade}</div>
						</div>
					</div>
				</td>
				<td><span class="team-pill tp-{color}">{icon} {team_name}</span></td>
				<td><span class="section-pill">{section}</span></td>
			</tr>
		'''

	# IF NO PLAYER MATCHES SEARCH
	rows_html += '<tr class="table-empty" id="empty-row" style="display:none;"><td colspan="3">No matches.</td></tr>'

	document.getElementById('roster-body').innerHTML = rows_html
	document.getElementById('row-count').textContent = f'{len(players)} Players'

# FILTER AND SEARCH STATE
_current_team = 'all'
_current_search = ''

# LOOPS THROUGH FILTERS AND SHOWS/HIDES
def _apply_filters():
	rows = document.querySelectorAll('#roster-body tr[data-team]')
	visible = 0

	for i in range(rows.length):
		# GO THROUGH EACH ROW
		row = rows.item(i)

		# IS THE PLAYER ON THE TEAM FILTER?
		team_match = (_current_team == 'all' or row.dataset.team == _current_team)

		# DOES THIS PLAYER'S NAME CONTAIN WHAT'S ON THE SEARCH?
		name_match = (_current_search == '' or _current_search in row.dataset.name)

		# NEEDS BOTH TO PASS TO BE VISIBLE
		if team_match and name_match:
			row.style.display = ''
			visible += 1
		else:
			row.style.display = 'none'

	# UPDATES THE COUNT LABEL
	count_el = document.getElementById('row-count')
	count_el.textContent = f'{visible} Players' if _current_team == 'all' else f'{visible} Results'
	
	empty = document.getElementById('empty-row')
	if empty: empty.style.display = '' if visible == 0 else 'none'

# WHICH FILTER BUTTON IS ACTIVE? WHICH ONES RESET TO DEFAULT STYLE?
def _set_active_btn(active_id):
	btns = {
		'btn-all': 'act-all', 
		'btn-green': 'act-green', 
		'btn-red': 'act-red', 
		'btn-yellow': 'act-yellow', 
		'btn-blue': 'act-blue'
		}
	for bid, active_class in btns.items():
		btn = document.getElementById(bid)
		if btn:
			btn.className = f'f-btn {active_class} active' if bid == active_id else 'f-btn'

def filter_all(*args):
	global _current_team
	_current_team = 'all'
	_set_active_btn('btn-all')
	_apply_filters()

def filter_green(*args):
	global _current_team
	_current_team = 'green'
	_set_active_btn('btn-green')
	_apply_filters()

def filter_red(*args):
	global _current_team
	_current_team = 'red'
	_set_active_btn('btn-red')
	_apply_filters()

def filter_yellow(*args):
	global _current_team
	_current_team = 'yellow'
	_set_active_btn('btn-yellow')
	_apply_filters()

def filter_blue(*args):
	global _current_team
	_current_team = 'blue'
	_set_active_btn('btn-blue')
	_apply_filters()

# TRIGGERED BY PY-INPUT
def search_players(*args):
	global _current_search
	# LOWERCASE + BYE WHITESPACE
	_current_search = document.getElementById('search-input').value.lower().strip()
	_apply_filters()

# RUN ON LOAD
render_players()