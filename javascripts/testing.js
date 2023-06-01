// testing code for convenience

function generate() {
    var faction = "grineer"

    var names = genNames(faction);
    console.log("names: " + names);
}

// given name generation rules (for a given faction) return randomly generated names
function genNames(faction) {
    console.log(faction);
    let namingScheme = globalThis.windowVar[faction];
    var names = [];
    for (let i = 0; i < 10; i ++) {
        names.push(namingScheme());
    }
    return names;
}

/*-------------------------------------*/
// name generation rules

var grineer = new function() {
    console.log("called");
    return "testing";
}

generate();