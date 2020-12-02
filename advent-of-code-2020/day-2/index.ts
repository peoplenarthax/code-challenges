const { readLinesInput } = require("../utils")
const path = require("path");

type PasswordInfo = { range: [number, number], letter: string, password: string}

// Parse line to `range`-`range` `letter`: `password`
const lineToPasswordInfo = (line: string) : PasswordInfo => {
	const trimmedLine = line.trim()
	// Love doing regex for this :D basically I created capturing groups for each part that i want
	const regexCapturedGroups = trimmedLine.match(/([0-9]+\-[0-9]+)\ (.)\: (.*)/)

	return {
		range: regexCapturedGroups[1].split("-").map((n) => parseInt(n, 10)) as [number, number],
		letter: regexCapturedGroups[2],
		password: regexCapturedGroups[3]
	}
}

// Do not forget the -1, split always returns 1 at least
const countLetter = (letter: string, phrase: string) : number => phrase.split(letter).length-1

// Counter of given letter within min-max range
const isPasswordValidForOldPolicy = ({ range: [min, max], letter, password}: PasswordInfo) => {
	const letterOcurrences = countLetter(letter, password)

	return letterOcurrences >= min && letterOcurrences <= max 
}

// New policy with equality XOR
const isPasswordValidForNewPolicy = ({ letter, range: [firstIndex, secondIndex], password}: PasswordInfo) => {
	const firstLetterIsEqual = password[firstIndex - 1] === letter
	const secondLetterIsEqual = password[secondIndex - 1] === letter

	// XOR operation
	return  (firstLetterIsEqual || secondLetterIsEqual) && !(firstLetterIsEqual && secondLetterIsEqual) 
}

/*** SOLUTION CALCULATION ***/
const input: string[] = readLinesInput(path.resolve(__dirname, "input.txt"))

const passwordInfo = input.map(lineToPasswordInfo)

console.log("Solution 1: ", passwordInfo.filter(isPasswordValidForOldPolicy).length)

console.log("Solution 2: ", passwordInfo.filter(isPasswordValidForNewPolicy).length)
