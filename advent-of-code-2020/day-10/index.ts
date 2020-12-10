const { readNumberArrayInput } = require("../utils")
const path = require("path");

const getJumps = (jolts: number[]) => {
	const jumps = { 1: 0, 3: 0}
	
	// Just count the jumps of 3 and 1 jolts
	for (let i = 0; i + 1 < jolts.length; i++) {
		jumps[jolts[i+1]-jolts[i]] = jumps[jolts[i+1]-jolts[i]] + 1
	}
	return jumps
}

const getAlternatives = (jolts: number[]) => {
	// Save results so we only calculate each value once
	const dynamicTable = {}
	const getForksDynamic= (index: number) => {
		// From the last node there is only 1 fork
		if (index === input.length -1) return 1
		// Lookup in the dynamic table
		if (dynamicTable[index]) return dynamicTable[index]

		let pathAmount = 0
		// Count all the alternatives for the next nodes which are between 1 and 3
		for (let j = index + 1; (input[j] - input[index] < 4) && (j < input.length); j++) {
			pathAmount = pathAmount + getForksDynamic(j) 
		}
		// Save the result
		dynamicTable[index] = pathAmount
		return pathAmount
	}

	return getForksDynamic(0)
}


/*** SOLUTION CALCULATION ***/
let input: number[] = readNumberArrayInput(path.resolve(__dirname, "input.txt")).sort((a, b) => a - b)
// Add first and last element manually
input = [0, ...input, input[input.length-1]+3]

const jumps = getJumps(input)
console.log("Solution 1:", jumps[1]*jumps[3])

console.log("Solution 2: ", getAlternatives(input))