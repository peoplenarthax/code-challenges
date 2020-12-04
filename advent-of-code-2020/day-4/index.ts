import { access } from "fs/promises";

const { readLinesBetweenBlankSpacesInput } = require("../utils")
const path = require("path");

type CheckFunction = (value: string) => boolean
type Passport = { byr: string, iyr: string,	eyr: string, hgt: string, hcl: string, ecl: string,	pid: string, cid: string }

// Given min and max check if number is in range
const checkRange = (min: number, max: number) : CheckFunction => 
	(candidate: string) => parseInt(candidate, 10) >= min && parseInt(candidate, 10) <= max

// Maps unit to their range	
const heightUnitMap = {
	cm: checkRange(150, 193),
	in: checkRange(59, 76)
}
const checkHeight : CheckFunction = (height: string) => {

	if (height.includes("cm")) {
		const amount = height.match(/\d+/)[0]
		return heightUnitMap.cm(amount)
	}
	if (height.includes("in")) {
		const amount = height.match(/\d+/)[0]
		return heightUnitMap.in(amount)
	}
	
	return false
}

// Match a 6 digit hexadecimal. Check that is only 6 digits
const checkHairColor : CheckFunction = (haircolor: string) => 
	RegExp(/^#[0-9|a-f]{6}$/).test(haircolor)

// Check that color must be one of the list
const checkEyeColor : CheckFunction= (eyecolor: string) => 
	["amb", "blu", "brn", "gry", "grn", "hzl", "oth"].some((colorCode) => colorCode === eyecolor)

// PassportId must be exactly 9 numbers, check for beginning and end operator 
const checkPassportId : CheckFunction = (passportId: string) => 
	RegExp(/^\d{9}$/).test(passportId)

// We map the passport attribute to its own validation function
const validationMap : { [k: string] : CheckFunction }= {
	byr: checkRange(1920, 2002),
	iyr: checkRange(2010, 2020),
	eyr: checkRange(2020, 2030),
	hgt: checkHeight,
	hcl: checkHairColor,
	ecl: checkEyeColor,
	pid: checkPassportId
}

// All except CID
const MANDATORY_FIELDS = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

/*** SOLUTION CALCULATION ***/
const input: string[][] = readLinesBetweenBlankSpacesInput(path.resolve(__dirname, "input.txt"))

// Transform key:value into object from entries
const toPassportFields = (array: string[]) : Passport => { 
	const entries = array.map((keyValue)=> keyValue.split(":"))

	return Object.fromEntries(entries) as Passport
}

// Check by passport key size (we can do that because no weird key is added in the input)
const hasRequiredFields = (passport: Passport) => {
	const passportKeys = Object.keys(passport)
	
	if (passportKeys.length === 8) return true

	if (passportKeys.length === 7 && !passport.cid) return true

	return false
}

// A Passport is valid if all the fields are validated
const isValidPassport = (passport: Passport) => 
	MANDATORY_FIELDS.every(key => validationMap[key](passport[key]))


const allValidFields = input.map(toPassportFields).filter(hasRequiredFields)

console.log("Solution 1: ", allValidFields.length)

console.log("Solution 2: ", allValidFields.filter(isValidPassport).length)
