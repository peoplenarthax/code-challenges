const fs = require('fs');

// Sometimes there are whitespaces
const trimAndParse = (string: string) => {
	return parseInt(string.trim(), 10)
}

module.exports = {
	readInput: (fileName: string) => {
		return fs.readFileSync(fileName).toString().split("\n").map(trimAndParse);	
	}
}
