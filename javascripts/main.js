var hexisPrefix = ["Strategist", "Probate", "Scholar", "Vigilant", "Centurion", "Venator", "Adept", "Arbiter", "Armsman", "Seneschal"];
var sudaPrefix = ["Arch-Mem", "Disp-Arch", "Surv-Tel", "Expi-Dyna", "Log-Rec", "Seek-Loc", "Res-Arc", "Cura-Phano", "Pion-Rec", "Inves-Resp", "Ult-Pho"];

/*-------------------------------------*/

function generate() {
    var faction = document.getElementById("faction").value;
    var output = document.getElementById("result");

    // temp text to prove that button works
    // haven't figured out how to make global variables work but i'm getting the impression it just Doesn't™
    output.textContent = faction; 

    switch(faction) {
        case "corpus":
            break;
        case "grineer":
            break;
        case "hexis":
            break;
        case "suda":
            break;
        case "veil":
            break;
        case "loka": 
            break;
    }
}

var grineer = new function() {

}