const { readLinesInput } = require("../utils")
const path = require("path");

const toInstructions = (line: string, index: number) => {
	const [instruction, value] = line.trim().split(' ')

	return { instruction, index, value: parseInt(value, 10)}
}

// Yes... when we have a nested array (with object or array) we can't just spread
const deepCopy = <T>(obj: T) : T => JSON.parse(JSON.stringify(obj))
const getLoopAccumulator = (instructions: Array<{instruction: string, value: number}>) => {
	let acc = 0
	let lasIndex = 0
	let visited = {}
	for(let i = 0; i < instructions.length; i++) {
		const { instruction, value} = instructions[i]

		if (visited[i]) {break;}

		if (instruction === "jmp") { 
			// We add  -1 to correct the loop iteration i++
			i=i+value -1
		}
		if (instruction === "acc") {
			acc = acc + value
		}

		visited[i] = true
		lasIndex = lasIndex < i ? i : lasIndex
	}

	return [acc, lasIndex]
}

const getAccumulatorWithoutLoop = (instructions: Array<{instruction: string, value: number}>) => {
	// Look and substitute each nop and jmp, starting from top, until lastInstruction === EOInput
	for(let i = 0; i < instructions.length; i++) {
		const { instruction } = instructions[i]
		// Avoid iterating through these
		if (instruction === "acc") continue;
	
		let copyInstructions = deepCopy(instructions)
		copyInstructions[i] = {...copyInstructions[i], instruction: instruction === "nop" ? "jmp" : "nop"}
	
		const [acc, lastIndex] = getLoopAccumulator(copyInstructions)
	
		if (lastIndex === instructions.length - 1) { return acc}
	}
}
/*** SOLUTION CALCULATION ***/
const input: string[] = readLinesInput(path.resolve(__dirname, "input.txt"))

const instructions = input.map(toInstructions)

const accumulator = getLoopAccumulator(instructions)[0]
console.log("Solution 1: ", accumulator)

console.log("Solution 2: ", getAccumulatorWithoutLoop(instructions))

