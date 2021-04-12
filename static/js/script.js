function ce() {
	elem = document.getElementById("eq")
	prevval = elem.value
	prevval = prevval.substring(0, prevval.length - 2);
	elem.value = prevval
}

function ac() {
	elem = document.getElementById("eq")
	elem.value = ""
}

function editeq(val) {
	elem = document.getElementById("eq")
	prevval = elem.value
	console.log(prevval.includes("Error"))
	if (prevval.includes("Error")) {
		ac()
	}
	elem = document.getElementById("eq")
	prevval = elem.value
	const e = prevval.split(' ')
	if (e[e.length - 1].includes(".")) {
		elem.value = prevval + val
	}
	if (val == "."){
		elem.value = prevval + val	
	}
	else {
	elem.value = prevval + " " + val
	}
	
}
