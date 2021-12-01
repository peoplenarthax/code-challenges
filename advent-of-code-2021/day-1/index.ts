const { readNumberArrayInput } = require("../utils")
const path = require("path");

const findIncrements = (numbers: number[]) : number => {
    let increments = 0
    for (let i = 1; i < numbers.length; i++) {
        if (numbers[i] > numbers [i-1]){
            increments += 1
        }
    }

    return increments
}

const calcWindow = (array: number[], index: number) : number => {
    return array[index] + (array[index + 1] ?? 0) + (array[index + 2] ?? 0)
}

const findIncrementsWithWindow = (numbers: number[]) : number => {
    let increments = 0
    let windows = [calcWindow(numbers, 0)]

    for (let i = 1; i < numbers.length; i++) {
        const windowSum = calcWindow(numbers, i)

        if (windowSum > windows[i - 1]) {
            increments += 1
        }

        windows.push(windowSum)
    }

    return increments
}

/*** SOLUTION CALCULATION ***/
const input = readNumberArrayInput(path.resolve(__dirname, "input.txt"))

const increments = findIncrements(input)
// Solution 1 - We do not check solution since we know it exists
console.log("Solution 1: ", increments)

const windowIncrements = findIncrementsWithWindow(input)
// Solution 2
console.log("Solution 2: ", windowIncrements)
