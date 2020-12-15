const { readLinesInput } = require("../utils")

const path = require("path");
/*** SOLUTION CALCULATION ***/
const input: string[]= readLinesInput(path.resolve(__dirname, "input.txt"))

const initial = input[0].trim().split(',').map(x => parseInt(x, 10))

// Change this number
const TURNS = 30000000

let indexDic = initial.slice(0, initial.length - 1).reduce((acc, val, index) => ({...acc, [val]: index + 1}), {})
let turns = [...initial]

for (let i = initial.length - 1; i < TURNS; i++ ) {
	if (!indexDic[turns[i]]) {
		indexDic[turns[i]] = i + 1
		turns.push(0)
	} else {
		turns.push(i+ 1 - indexDic[turns[i]] )
		indexDic[turns[i]] = i + 1
	}	
}
console.log("Solution: ", TURNS -1)