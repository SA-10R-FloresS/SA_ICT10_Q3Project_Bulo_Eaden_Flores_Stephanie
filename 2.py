from pyscript import document

def intrams_checker(*args):

	# CHECK IF USER IS REGISTERED AND CLEARED
	reg_el = document.querySelector('input[name="register"]:checked')
	clr_el = document.querySelector('input[name="clear"]:checked')

	# RETURNS BOOLEAN VALUE
	registered = reg_el is not None
	cleared    = clr_el is not None

	# CHECK IF USER SELECTED GRADE AND SECTION
	grade   = document.getElementById('level').value
	section = document.getElementById('section').value

	result_div = document.getElementById('result')

	if not registered:
		result_div.innerHTML = '''
			<div class="result-box ineligible">
				<div class="result-status">✗ NOT ELIGIBLE</div>
				<div class="result-msg">
					Student is not registered for Intramurals '26.
					Ask your PE teacher regarding the online registration.
				</div>
			</div>
		'''

	elif not cleared:
		result_div.innerHTML = '''
			<div class="result-box ineligible">
				<div class="result-status">✗ NOT ELIGIBLE</div>
				<div class="result-msg">
					Medical clearance required.
					Go to the clinic and secure your clearance.
				</div>
			</div>
		'''

	elif not grade:
		result_div.innerHTML = '''
			<div class="result-box ineligible">
				<div class="result-status">✗ NOT ELIGIBLE</div>
				<div class="result-msg">
					Please select a grade level.
				</div>
			</div>
		'''

	elif not section:
		result_div.innerHTML = '''
			<div class="result-box ineligible">
				<div class="result-status">✗ NOT ELIGIBLE</div>
				<div class="result-msg">
					Please select a section.
				</div>
			</div>
		'''

	else:
		# converts grade to an integer
		g = int(grade)

		# is g a member of the list [,]?
		if section == 'emerald' and g in [7, 10]:
			team       = 'Green Hornets'
			color      = 'green'
			desc       = 'Grades 7 & 10; Emerald'
			image_src  = 'gh.png'
			image_alt  = 'Green Hornets'

		elif section == 'emerald' and g in [8, 9]:
			team       = 'Red Bulldogs'
			color      = 'red'
			desc       = 'Grades 8 & 9; Emerald'
			image_src  = 'rbd.png'
			image_alt  = 'Red Bulldogs'

		elif section == 'ruby' and g in [7, 10]:
			team       = 'Yellow Tigers'
			color      = 'yellow'
			desc       = 'Grades 7 & 10; Ruby'
			image_src  = 'yt.png'
			image_alt  = 'Yellow Tigers'

		elif section == 'ruby' and g in [8, 9]:
			team       = 'Blue Bears'
			color      = 'blue'
			desc       = 'Grades 8 & 9; Ruby'
			image_src  = 'bb.png'
			image_alt  = 'Blue Bears'

		result_div.innerHTML = f'''
			<div class="result-box eligible">
				<div class="team-badge {color}" style="height: 500px;">
					<div id="image" class="mt-3">
						<img src="{image_src}" alt="{image_alt}" style="max-width: 300px; border-radius: 8px;">
					</div>
					<div>
						<div class="team-name fw-bold">{team}</div>
						<div class="team-desc">{desc}</div>
					</div>
				</div>
				
			</div>
		'''