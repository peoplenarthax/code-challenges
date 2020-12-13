const { readLinesInput } = require("../utils")
const path = require("path");

const findEarliestDeparture = (departureTime: number, buses: number[]) : { minsToNext: number, bus: number}=> {
	let selectedBus = {minsToNext: Infinity, bus: undefined}

	for (let i = 0; i < buses.length; i++) {
		const minsToNext = buses[i] - (departureTime % buses[i])

		if (minsToNext < selectedBus.minsToNext ) { selectedBus = { minsToNext, bus: buses[i]}}
	}

	return selectedBus
}
// Find x such as a*x = 1 mod(modulus)
const modularMultiplicativeInverse = (a: bigint, modulus: bigint) => {
	const b = BigInt(a % modulus);
	
	// Brute force search
    for (let hipothesis = 1n; hipothesis <= modulus; hipothesis++) {
        if ((b * hipothesis) % modulus == 1n) return hipothesis;
	}
	
    return 1n;
}

// First https://brilliant.org/wiki/chinese-remainder-theorem/
const solveCRT = (remainders: bigint[], modules: bigint[]) => {
	// Multiply all the modulus
	const prod : bigint = modules.reduce((acc: bigint, val) => acc * val, 1n);
	
    return modules.reduce((sum, mod, index) => {
		// Find the modular multiplicative inverse and calculate the sum
		const p = prod / mod;
        return sum + (remainders[index] * modularMultiplicativeInverse(p, mod) * p);
    }, 0n) % prod;
}

const getRemaindersAndModules = (buses: string[]) => {
	return buses.reduce(({remainders, modules}, val: string, index: number) => {
		if (val === 'x') return {remainders, modules}
		const mod = parseInt(val, 10)
		return { 
			remainders: [...remainders, BigInt(mod - index)],
			modules: [...modules, BigInt(mod)]
		}
	}, { remainders: [], modules: []})
}

/*** SOLUTION CALCULATION ***/
const input: [string, string]= readLinesInput(path.resolve(__dirname, "input.txt"))

const departureTime = parseInt(input[0], 10)
const buses = input[1].split(',').filter(x => x !== 'x').map(x => parseInt(x, 10))

const { minsToNext, bus } = findEarliestDeparture(departureTime, buses)
console.log("Solution 1: ", minsToNext * bus)


const {remainders, modules, } = getRemaindersAndModules(input[1].split(','))

console.log("Solution 2: ", solveCRT(remainders, modules))