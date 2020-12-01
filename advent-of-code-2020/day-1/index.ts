const { readInput } = require("../utils")
const path = require("path");

const SUM = 2020

// We assume numbers is sorted increasingly
const findPairWithSum = (sum: number, numbers: number[]) : [number, number] | null => {
	let leftIndex = 0
	let rightIndex = numbers.length - 1
	
	// If this condition is meet we did not found any pair
	while (leftIndex < rightIndex) {
		// We found the solution! Return this indexes
		if (numbers[leftIndex] + numbers[rightIndex] == sum) break
	
		// Since the array is order increasingly we can move indexes depending on the sum
		if (numbers[leftIndex] + numbers[rightIndex] < sum) {
			leftIndex++
		} else {
			rightIndex--
		}
	}

	// If the indexes are right we have a solution, otherwise return null
	return leftIndex < rightIndex ? [numbers[leftIndex], numbers[rightIndex]] : null
}

// We assume numbers are sorted increasingly
const findTripleWithSum = (sum: number, numbers: number[]) : [number, number, number] => {
	// We reduce triplets problem to the same nature as the pair problem
	
	for(let index = 0; index < numbers.length - 2; index++ ) {
		// Find a pair that sums to `SUM minus the current element` from the numbers that are left
		const pair = findPairWithSum(SUM - numbers[index], numbers.slice(index + 1))

		// Return triplet if we found the pair - We assume there is always an answer
		if (pair) {
			return [numbers[index], ...pair]
		}
	}
}

const multiplyAll = (acc: number, val: number) => acc * val

/*** SOLUTION CALCULATION ***/
const input: number[] = readInput(path.resolve(__dirname, "input.txt"))

// Sort increasingly
const sortedInput = input.sort((a, b) => a-b)

const pair = findPairWithSum(SUM, sortedInput)
// Solution 1 - We do not check solution since we know it exists
console.log("Solution 1: ", pair.reduce(multiplyAll))


const triple = findTripleWithSum(SUM, sortedInput)
// Solution 2 - We do not check solution since we know it exists
console.log("Solution 2: ", triple.reduce(multiplyAll))