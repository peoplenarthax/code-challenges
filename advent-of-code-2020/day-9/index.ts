const { readNumberArrayInput } = require("../utils")
const path = require("path");

const NUMBER_WINDOW = 25


// Copied from day-1 to bring clarity to those who check this file
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

const findInvalidNumber = (numbers: number[]) => {
	for(let i = NUMBER_WINDOW; i < input.length; i++) {
		const pair = findPairWithSum(input[i], input.slice(i - NUMBER_WINDOW, i).sort((a, b) => a-b))
	
		if (!pair) { return input[i] }
	}
}

const findConsecutiveSum = (sum: number, numbers: number[]) => {
	for (let i = 0; i < numbers.length; i++) {
		for(let j = 1; j< numbers.length-i; j++) {
			const sumList = numbers.slice(i, i+j)
			const checkSum = sumList.reduce((acc, val) => acc+val, 0)

			if (checkSum > sum) break;

			if (checkSum === sum) return Math.min(...sumList) + Math.max(...sumList)
		}
	}
}

/*** SOLUTION CALCULATION ***/
const input: number[] = readNumberArrayInput(path.resolve(__dirname, "input.txt"))

const invalidNumber = findInvalidNumber(input)

console.log("Solution 1: ", invalidNumber)

console.log("Solution 2: ", findConsecutiveSum(invalidNumber, input))
