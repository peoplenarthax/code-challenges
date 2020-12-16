const { readLinesBetweenBlankSpacesInput } = require("../utils")

const path = require("path");

const merge = (ranges: [number, number][]) => {
	let result = []
	let last : [number, number];

    ranges.forEach(function (r) {
        if (!last || r[0] > last[1])
            result.push(last = r);
        else if (r[1] > last[1])
            last[1] = r[1];
    });

    return result;
}

/*** SOLUTION CALCULATION ***/
const [features, myTicket, nearbyTickets]: string[][] = readLinesBetweenBlankSpacesInput(path.resolve(__dirname, "input.txt"))

const isRange = (features: string) => features.includes("-")

const ranges = features.filter(isRange).map((string) => string.split('-').map(n => parseInt(n, 10))).sort((a, b) => a[0]-b[0] || a[1]-b[1]) as [number, number][];

// We merge ranges so that we create unions out of overlapping ranges
const constraints = merge(ranges)

// Slice to remove "nearby tickets:"
// We reduce by checking if any number is not within the range constraints
const invalid = nearbyTickets.slice(2).reduce((invalidNumbers, val) =>{
	if (constraints.some(([min, max]) => val >= min && val <= max)) {
		return invalidNumbers
	} 
	return [...invalidNumbers, parseInt(val, 10) ]
} , [])

console.log("Solution 1: ", invalid.reduce((acc, val) => acc + val, 0))

// TODO Solution 2: Basically need to check the possibilities for each column
// Then need to check exclusive fields