var argonauts = {};
argonauts.goal = "Golden Fleece";
argonauts.sailors = [];
argonauts.sailors[0] = { name: "Acastus", father: "Pelias" };
argonauts.sailors[1] = { name: "Actor", father: "Hippasus" };
argonauts.sailors[2] = { name: "Admentus", father: "Pheres" };
argonauts.sailors[3] = { name: "Amphiarus", father: "Oicles" };
argonauts.sailors[4] = { name: "Ancaeus", father: "Poseidon" };

var the_quest = JSON.stringify(argonauts);
// test
console.log(the_quest)