from js import document

def show_winner():
	winners = document.getElementsByClassName("win")
	
	for win_div in winners:
		target = win_div.nextElementSibling
		
		if target and "tri" in target.classList:
			target.style.opacity = 1

show_winner()