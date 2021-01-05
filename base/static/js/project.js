/* Project specific Javascript goes here. */
const url = document.location.toString().toLowerCase();
const path = url.split('//')[1];
const domain = path.split('/')[0];

// const org_name = document.title;
const org_name = domain;
$(document).ready(function() { // print org_name
	let org_slots = document.querySelectorAll(".org_name");
	for (var i = 0, slot; slot = org_slots[i]; i++) {
		slot.textContent = org_name;
	}
});
var lights_on = function() { // turn on the lights
	document.body.style.color = '#343a40';
	document.body.style.backgroundColor = '#f8f9fa';
	console.log('lights on');
	document.cookie = `off=false; domain=${domain}.`;
	setCookie("off", "false", 1000);

	};
var lights_off = function() { // turn off the lights
	document.body.style.color = '#f8f9fa';
	document.body.style.backgroundColor = '#343a40';
	console.log('lights off');
	document.cookie = `off=true; domain=${domain}.`;
	setCookie("off", "true", 1000);

	};
function setCookie(c_name,value,exdays) {
    var exdate=new Date();
    exdate.setDate(exdate.getDate() + exdays);
    var c_value=escape(value) + ((exdays==null)
                                 ? "" : "; expires="+exdate.toUTCString())
                                + "; path=/";
    document.cookie=c_name + "=" + c_value;
}	
function getCookie(cname) { // create a generic cookie
    var name = cname + "=";
    var ca = document.cookie.split(';');
    for(var i=0; i<ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0)==' ') c = c.substring(1);
        if (c.indexOf(name) == 0) return c.substring(name.length,c.length);
    }
    return "";
}
const light_switch = document.getElementById("light_switch");
$(document).ready(function() { // light switch
	$(light_switch).click(function() {
		var off = getCookie("off"); 
		if(off == "") {
			lights_off();
			};	
		if(off == "true") {
			lights_on();
		} else {
			lights_off();
		}
	});
});
$(document).ready(function() { // light checker
		if(off == "true") {
			lights_off();
		} else {
			lights_on();
		}
});
const off = getCookie("off"); // init off cookie
