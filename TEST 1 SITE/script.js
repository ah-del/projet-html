const btn = document.getElementById("btn")

    
function handleclick(e) {
	e.target.innerHTML = "bonjour"
    //window.location = "google.com"
}


//btn.addeventlistener


btn.addEventListener("click", handleClick)