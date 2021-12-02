const { readLinesInput } = require("../utils")
const path = require("path");

const move = (instructions: [string, string][])  => {
    let horizontal = 0
    let vertical = 0

    for (let instruction of instructions) {
        if (instruction[0] === 'forward') {
            horizontal += parseInt(instruction[1])
        } else if (instruction[0] === 'down') {
            vertical += parseInt(instruction[1])
        } else {
            vertical -= parseInt(instruction[1])
        }
    }

    return horizontal * vertical
}

const moveWithAim = (instructions: [string, string][])  => {
    let horizontal = 0
    let aim = 0
    let vertical = 0

    for (let instruction of instructions) {
        if (instruction[0] === 'forward') {
            horizontal += parseInt(instruction[1])
            vertical += aim*parseInt(instruction[1])
        } else if (instruction[0] === 'down') {
            aim += parseInt(instruction[1])
        } else {
            aim -= parseInt(instruction[1])
        }
    }

    return horizontal * vertical
}

/*** SOLUTION CALCULATION ***/
const input = readLinesInput(path.resolve(__dirname, "input.txt"))

const actionInput = input.map(line => line.split(' '))

const position = move(actionInput)
// Solution 1 - We do not check solution since we know it exists
console.log("Solution 1: ", position)

const aimPosition = moveWithAim(actionInput)
// Solution 1 - We do not check solution since we know it exists
console.log("Solution 2: ", aimPosition)
