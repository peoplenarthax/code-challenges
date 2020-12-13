const { readLinesInput } = require("../utils")
const path = require("path");

const getNextCellState = (row: number, column: number, input: string[], notAdjacent?: boolean) => {
	// Base all the logic if the place is occupied or not
	const isOccupied = input[row][column] === '#'
	let adjacentOccupied = 0
	for (let rowIndex = -1; rowIndex < 2; rowIndex++) {
		for (let columnIndex = -1; columnIndex < 2; columnIndex++){
			let newRow = row+rowIndex
			let newColumn = column+columnIndex
			// Check limits 
			if (newRow === row && newColumn === column) continue;
			if (newRow < 0 || (newRow >= input.length)) continue;
			if (newColumn < 0 || (newColumn >= input[0].length)) continue;
			
			if (notAdjacent) {
				let factor = 2
				// Check limits and keep searching for points as long as it is not a seat
				while((newRow >= 0 && newColumn >= 0) && (newRow < input.length && newColumn < input[0].length) && input[newRow][newColumn] === '.') {
					// We multiply by the direction vector
					newRow = row + (rowIndex * factor)
					newColumn = column + (columnIndex * factor)
					factor++
				}
				// One more check for the notAdjacent way
				if (newRow >= input.length || newColumn >= input[0].length || newRow < 0 || newColumn < 0) continue;
			}
			
			if (input[newRow][newColumn] === '#') { adjacentOccupied++ }
			if (isOccupied  && adjacentOccupied >= (notAdjacent ? 5 : 4)) return "L"
			if (!isOccupied  && adjacentOccupied > 0) return "L"
		}
	}
	return '#'
}

const getNextState = (grid: string[], checkNotAdjacent?: boolean) => {
	let newGrid = []

	// For each character, unless is a ., we check the next state for the given point
	for (let i = 0; i < input.length; i++) {
		let row = ''
		for (let j = 0; j < input[0].length; j++) {
			if (grid[i][j] === '.') {
				row = row.concat('.')
			} else {
				row = row.concat(getNextCellState(i, j, grid, checkNotAdjacent))
			}
		}
		newGrid.push(row)
	}

	return newGrid
}

const iterate = (input: string[], adjacent?: boolean) => {
	let grid = input
	let newGrid = getNextState(input)

	let count = 0
	// Keep iterating until we do not change from the previous grid
	while (grid.join("\n") !== newGrid.join("\n")) {
		grid = newGrid
		newGrid = getNextState(grid, adjacent)
		count++
	}
	return (newGrid.join().match(/#/g) || []).length
}
/*** SOLUTION CALCULATION ***/
const input: string[] = readLinesInput(path.resolve(__dirname, "input.txt"))

console.log("Solution 1: ", iterate(input))

console.log("Solution 2: ", iterate(input, true))