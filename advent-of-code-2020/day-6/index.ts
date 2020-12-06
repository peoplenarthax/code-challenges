const { readLinesBetweenBlankSpacesInput } = require("../utils")
const path = require("path");

const getSetIntersections = (answerGroup: string[]) => {
	// Create a set from every string, then sort increasingly
	const [smallestSet, ...otherSets] = answerGroup.map((answers) => new Set(answers)).sort((a, b) => a.size - b.size)
	
	// We create a set that only contains the common elements between one set and another
	// We use the smallestSet as initialValue since it is the smallest one, so
	// it defines the biggest amount of common answers
	const commonAnswers = otherSets.reduce((hipothesisCommonAnswers : Set<String>, currentSet : Set<String>) => {
		return new Set([...hipothesisCommonAnswers].filter(answer => currentSet.has(answer)))
	}, smallestSet)

	return commonAnswers.size
}
/*** SOLUTION CALCULATION ***/
const input: string[][] = readLinesBetweenBlankSpacesInput(path.resolve(__dirname, "input.txt"))

// Simply join all the answers from a group and create a set from it. Then just count the answers
const sumYesAnswers = input
	.map(group => group.join(""))
	.reduce((acc, val) => acc + new Set(val).size, 0)
console.log("Solution 1: ", sumYesAnswers)

const countCommonAnswers = input.map(getSetIntersections).reduce((acc, val) => acc + val, 0)
console.log("Solution 2: ", countCommonAnswers)