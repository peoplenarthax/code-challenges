import { isConstructorDeclaration } from "../node_modules/typescript/lib/typescript";

const { readLinesInput } = require("../utils")
const path = require("path");

const ADDRESS_VECTOR = {
	N: [0, 1],
	S: [0, -1],
	E: [1, 0],
	W: [-1, 0]
}

// Map for turns
const TURN = {
	N: ['N', 'E', 'S', 'W'],
	E: ['E', 'S', 'W', 'N'],
	S: ['S', 'W', 'N', 'E'],
	W: ['W', 'N', 'E', 'S']
} 

type Coord = [number, number]
const move = ([order, number]: [string, number]) : Coord => ADDRESS_VECTOR[order].map(coord => coord*number)

// Given a compass directions, find the new one 
const getNewDirection = ([side, angle]: [string, number], currentDirection: string) => {
	const turns = angle / 90
	if (side === "R") {
		// Easy way of dealing with circular array (even tho example does not have more than 270)
		return TURN[currentDirection][turns % 4]
	}

	return TURN[currentDirection][4 - (turns % 4)]
}

// Applying a rotation matrix to the 2D vector. Math in JS takes radiants 
const rotateVector = ([x, y]: Coord, degrees: number) : Coord => {
	const newX = Math.round(x*Math.cos(degrees* Math.PI / 180) - y*Math.sin(degrees* Math.PI / 180))
	const newY = Math.round(x*Math.sin(degrees* Math.PI / 180) + y*Math.cos(degrees* Math.PI / 180))

	return [newX, newY]
}

// Utils for operating with vectors
const addVector = ([x1, y1]: Coord, [x2, y2]:Coord ) : Coord => [x1+x2, y1+y2]
const multiplyVector = ([x1, y2]: Coord, factor: number ) : Coord=> [x1*factor, y2*factor]

const processOrders = (input: Array<[string, number]>) => {
	let lastDirection = 'E'
	let position = [0, 0] as [number, number]
	for (let i = 0; i < input.length; i++) {
		const line = input[i]

		if (Object.keys(ADDRESS_VECTOR).includes(line[0])) {
			position = addVector(position, move(line as any)) as [number, number]
			continue;
		}
		if (line[0] === 'F') {
			position = addVector(position, move([lastDirection, line[1] as any])) as [number, number]
			continue;
		}
		lastDirection = getNewDirection(line as any, lastDirection)
	}
	return position
}

const processOrdersWaypoint = (input: Array<[string, number]>) => {
	let directionVector: Coord = [10, 1]
	let position = [0, 0] as Coord
	for (let i = 0; i < input.length; i++) {
		const line = input[i]

		if (Object.keys(ADDRESS_VECTOR).includes(line[0])) {
			directionVector= addVector(directionVector, move(line)) as Coord
			continue;
		}
		if (line[0] === 'F') {
			position = addVector(position, multiplyVector(directionVector, line[1]))
			continue;
		}

		directionVector = rotateVector(directionVector, line[0] === 'L' ? line[1] : line[1] * -1)
	}

	return position
}

/*** SOLUTION CALCULATION ***/
const input: Array<[string, number]> = readLinesInput(path.resolve(__dirname, "input.txt")).map(([order, ...number]) => ([order, parseInt(number.join(''), 10)]))

const pos = processOrders(input)

console.log("Solution 1: ", pos.reduce((acc, val) => acc + Math.abs(val), 0))

const posWaypoint = processOrdersWaypoint(input)

console.log("Solution 2: ", posWaypoint.reduce((acc, val) => acc + Math.abs(val), 0))