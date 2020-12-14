import { maxHeaderSize } from "http";

const { readLinesInput } = require("../utils")
const path = require("path");

const getMaskedNumber = (mask: string[], value: string) => {
	const binaryString = Number(value).toString(2)
	let paddedString = binaryString.padStart(36, "0").split("")

	for(let i = 0; i < mask.length; i++) {
		if (mask[i] === "1") {
			paddedString[i] = "1"
			continue;
		}
		if (mask[i] === "0") {
			paddedString[i] = "0"
			continue;
		}
	}

	return parseInt(paddedString.join(""), 2)
}

const floatingValue = (mask: string[], paddedString: string[], indexMem: number) => {
	// console.log("Mask is now size: ", mask.length)
	// console.log("Mask: ", mask.join(""))
	// console.log("Index at: ", indexMem)
	if (mask.length === 0) return [paddedString]
	let index = indexMem
	while (mask[index] !== 'X' && index < mask.length) {
		index++
		
	}
	// console.log("Index is ", index)
	// console.log("Exiting", index >= mask.length)
	if (index >= mask.length) return [paddedString]

	let copy1 = Array.from(paddedString)
	copy1[index] = "1"
	let copy0 = Array.from(paddedString)
	copy0[index] = "0"
	// console.log("Mask ")
	return [...floatingValue(mask, copy1, index + 1) , ...floatingValue(mask, copy0, index + 1)]
}

// TODO: Unnefficient way of getting all the addreses. Fix other day
const getMemoryAddresses = (mask: string[], index: string) => {
	const binaryString = Number(index).toString(2)
	let paddedString = binaryString.padStart(36, "0").split("")

	for(let i = 0; i < mask.length; i++) {
		if (mask[i] === "X") continue;
		// @ts-ignore
		paddedString[i] = mask[i] | paddedString[i]
	}

	console.log("FLOATING VALUE FOR ", mask.join(""))
	return floatingValue(mask, paddedString, 0)
}

const decode = (input: string[], version: string = "version1") => {
	let mask = []
	let memory : { [k: number]: number }= {}
	
	for (let index = 0; index < input.length; index++) {
		if (input[index].includes("mask")) {
			mask = input[index].slice(7).trim().split("")
			continue;
		}
		
		const [_, memoryIndex, value] = input[index].match(/mem\[(\d+)\] = (\d+)/)
		if (version === "version1") {
			memory[memoryIndex] = getMaskedNumber(mask, value)
		} else {
			const memoryAdresses = getMemoryAddresses(mask, memoryIndex)

			console.log(memoryAdresses)
		}
	}

	return memory
}
/*** SOLUTION CALCULATION ***/
const input: string[]= readLinesInput(path.resolve(__dirname, "input.txt"))

const memoryVersion1 = decode(input)
console.log("Solution 1: ", Object.values(memoryVersion1).reduce((acc, val) => acc+val, 0))

const memoryVersion2 = decode(input, "version2")
