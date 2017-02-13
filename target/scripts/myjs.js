function value_check() {
	var returnval = true;

	var pass = document.getElementById('search');

	if (pass.value) {
		if (pass.value.length != 9) {
			alert("String must be 9 letters!")
			pass.style.borderColor = "Red";
			return false;
		}
		
	} else {
		return false;
	}

}

function clickfunction(id) {
	var el = document.getElementById(id);
	
	var hide = el.style.display == "block";
	if (hide) {
		el.style.display = "none";
	} else {
		el.style.display = "block";
	}
}