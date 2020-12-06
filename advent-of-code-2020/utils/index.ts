const fs = require('fs');

// Sometimes there are whitespaces
const trimAndParse = (string: string) => parseInt(string.trim(), 10)

module.exports = {
	readNumberArrayInput: (fileName: string) : number[] => fs.readFileSync(fileName).toString().split("\n").map(trimAndParse),
	readLinesInput: (fileName: string) : string[] => fs.readFileSync(fileName).toString().split("\n"),
	readLinesBetweenBlankSpacesInput: (fileName: string) : string[][] => 
		fs.readFileSync(fileName).toString().replace(/\r\n/g, "\n").split("\n\n").map(line => line.split(/[\s,]+/))
}
