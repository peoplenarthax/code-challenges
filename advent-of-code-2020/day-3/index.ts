const { readLinesInput } = require("../utils")
const path = require("path");

const RIGHT_STEP_SIZE = 3
const DOWN_STEP_SIZE = 1

// Transforms into a boolean grid where true means there is a tree.
// We don't really need this, actually it adds a bit of overhead
// But I prefer to treat the grid as a boolean one instead
const lineToTreeGrid = (line: string) : boolean[] => {
	const trimmedLine = line.trim()

	// We slice because trim adds one \r character at the end
	return line.split("").slice(0, -1).map(letter => letter === "#" ? true : false)
}

// Brute force go through all rows
const goDownSlope = (grid: boolean[][],{downStep, rightStep}: { downStep: number, rightStep: number}) => {
	let treeCount = 0
	const rowSize = grid[0].length

	for (let y = downStep, x = rightStep; y < grid.length; y = y + downStep, x = (x + rightStep) % rowSize) {
		if (grid[y][x]) {
			treeCount++
		} 
	}
	
	return treeCount
}
/*** SOLUTION CALCULATION ***/
const input: string[] = readLinesInput(path.resolve(__dirname, "input.txt"))

const grid = input.map(lineToTreeGrid)

console.log("Solution 1: ", goDownSlope(grid, { downStep: 1, rightStep: 3}) )

const steps = [
	{ downStep: 1, rightStep: 1},
	{ downStep: 1, rightStep: 3},
	{ downStep: 1, rightStep: 5},
	{ downStep: 1, rightStep: 7},
	{ downStep: 2, rightStep: 1}
]
const multipliedTrees = steps
							.map(stepVector => goDownSlope(grid, stepVector))
							.reduce((acc, val) => acc * val)
							
console.log("Solution 2: ", multipliedTrees)

