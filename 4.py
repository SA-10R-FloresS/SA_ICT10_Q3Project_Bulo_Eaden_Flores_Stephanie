from pyscript import document

# errors is a list that stores what's wrong about your registration

def username_verification(username):
	errors = []
	username_length = len(username)

	if username_length < 7:
		errors.append(f'Username is too short. Add at least {7 - username_length} more character/s.')

	return errors

def password_verification(password):
	errors = []
	password_length     = len(password)
	password_has_number = any(char.isdigit() for char in password)
	password_has_letter = any(char.isalpha() for char in password)

	if password_length < 10:
		errors.append(f'Password is too short. Add at least {10 - password_length} more character/s.')

	if not password_has_letter:
		errors.append('Password must contain at least one letter.')

	if not password_has_number:
		errors.append('Password must contain at least one number.')

	return errors

# combining functions and displaying the results
def create_acct(*args):
	output_div = document.getElementById('output')

	username = document.getElementById('username').value
	password = document.getElementById('password').value

	all_errors = username_verification(username) + password_verification(password)

	if all_errors:
		# thank you to claude again for helping me figure that out... wowie
		items = ''.join([f'<li>{e}</li>' for e in all_errors])
		output_div.innerHTML = f'''
			<div class="result-box ineligible">
				<div class="result-status">✗ NOT VALID</div>
				<div class="result-msg">Please fix the following before signing up:</div>
				<ul class="reasons">
					{items}
				</ul>
			</div>
		'''
	else:
		output_div.innerHTML = '''
			<div class="result-box eligible">
				<div class="result-status">✓ SUCCESS</div>
				<div class="result-msg">
					Account created! You may now log in using your credentials.
				</div>
			</div>
		'''