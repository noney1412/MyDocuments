const math = require("mathjs");

let tensile_Result = [1037, 1047, 1066, 1048, 1059, 1073, 1070, 1040];

let R = math.mean(tensile_Result);

console.log(R);
