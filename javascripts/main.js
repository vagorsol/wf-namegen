var hexisPrefix = ["Strategist", "Probate", "Scholar", "Vigilant", "Centurion", "Venator", "Adept", "Arbiter", "Armsman", "Seneschal"];
var sudaPrefix = ["Arch-Mem", "Disp-Arch", "Surv-Tel", "Expi-Dyna", "Log-Rec", "Seek-Loc", "Res-Arc", "Cura-Phano", "Pion-Rec", "Inves-Resp", "Ult-Pho"];

/*-------------------------------------*/

function generate() {
    var faction = document.getElementById("faction").value;
    var output = document.getElementById("result");
    var names; // empty array for output

    // alert if try to generate without selecting a faction, otherwise pass name of function to name generator function
    if (!faction) {
        alert("Please select a faction!");
        return;
    } else {
        // pass function by name. i guess
        names = genNames(faction);
    }

    // convert to string to append
    var nameslst = "";
    for (let i = 0; i < names.length; i ++) {
        // avoid prepending newline for first one for nice formating
        if (i == 0) {
            nameslst += names[i];
        } else {
            nameslst += ("\r\n" + names[i]);
        }
    }

    // output names
    output.textContent = nameslst; 
}

// given a faction, use the associated name generation rules and return randomly generated names
function genNames(faction) {
    var names = [];
    for (let i = 0; i < 10; i ++) {
        var name = window[faction].apply(); 
        names.push(name);
    }
    return names;
}

/*-------------------------------------*/
// name generation rules

function grineer() {
    return "testing";
}

function corpus() {

}

function hexis() {

}

function suda() {

}

function veil() {

}

function loka() {

}