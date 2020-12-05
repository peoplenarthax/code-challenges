const { readLinesInput } = require("../utils")
const path = require("path");

const DIRECTION_MAP = {
	B: "1",
	F: "0",
	R: "1",
	L: "0"
} as const

// Basically the BF and the RL are the binary encoding of the problem
const toBinaryString = (instructions: string) : string => instructions.trim().replace(
	RegExp( '[BFRL]', 'g' ), 
	(letter: string) => DIRECTION_MAP[letter]
)

const toInteger = (binaryString: string) => parseInt(binaryString, 2)

const toRowAndColumn = (line: string) => 
	[line.slice(0, 7), line.slice(7)].map(toInteger) as [number, number]

// We can iterate throw the array by knowing which was the first element and moving
// to the right until we see it is not sequential
const findGap = (sorted: number[]) => {
	const initialIndex = sorted[0]

	let index = 0
	while (index + initialIndex === sorted[index]) {
		index++;
	}

	return index + initialIndex
}
/*** SOLUTION CALCULATION ***/
const input: string[] = readLinesInput(path.resolve(__dirname, "input.txt"))

const rowsAndColumns = input
	.map(toBinaryString)
	.map(toRowAndColumn)

const ticketIds = rowsAndColumns.map(([row, column] : [number, number]) => row * 8 + column).sort((a, b) => a-b)

console.log("Solution 1: ", ticketIds[ticketIds.length - 1])

console.log("Solution 2: ", findGap(ticketIds))