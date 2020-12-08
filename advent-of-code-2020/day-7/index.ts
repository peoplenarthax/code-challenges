const { readLinesInput } = require("../utils")
const path = require("path");

// Matches the phrase "1 bloody red bag" by extracting in groups the amount and the name
const bagRegex = new RegExp(/^(\d)?[\s]?(.*) bags?/)

// Creates a graph where each node contains the nested bags and the amount of them
const getRelationshipMap = (phrases: string[][]) => {
	const relationshipMap = phrases.reduce((map, [container, contained]) => {
		const containerColor = container.match(bagRegex)[2]
		// Non nested bags are added as empty object
		if (contained.includes("no other bags")) return {...map, [containerColor]: {}}

		// Create the object from color to its direct relation
		const containedColors = contained.split(",").reduce((all, currentBag) => {
			const [_, amount, color] = currentBag.trim().match(bagRegex)

			return {...all, [color]: parseInt(amount, 10)}
		}, {})

		return {...map, [containerColor]: containedColors}
	}, {})

	return relationshipMap
}

// We call it reverse because instead of being a Parent:Children relation, is a Child:Parents[]
const getReverseRelationShipMap = (phrases: string[][]) => {
	let relationshipMap = phrases.reduce((map, [container, contained]) => {
		const containerColor = container.match(bagRegex)[2]

		if (contained.includes("no other bags")) return map

		const containedColors = contained.split(",").reduce((all, currentBag) => {
			const [_, amount, color] = currentBag.trim().match(bagRegex)

			// We need to deep merge the existing node with the already specified ones
			// This works because is only 1 level deep
			return {...all, [color]: {
				...map[color] ?? {},
				[containerColor]: true
			}}
		}, {})

		// Merge existing map with the new generated keys
		return {...map, ...containedColors}
	}, {})

	return relationshipMap
}

// Apply Breadth-First Search to find all the nodes from the given inital one
const findAllParentsBFS = (bagGraph: {[k: string]: {[k:string]: boolean}}, initialNode: string) => {
	// Keep track of visited nodes
	let visited = {}
	// We add the initial set of parents
	let queue = [...Object.keys(bagGraph[initialNode] ?? {})]

	while (queue.length > 0) {
		const nextNode = queue.shift()
		if (visited[nextNode]) continue;

		// We mark our node as visited and we add to the queue all the nodes except the ones we have visited
		visited[nextNode] = true
		queue = queue.concat(...Object.keys(bagGraph[nextNode] ?? {}).filter(bag => !visited[bag]))
	}

	// The amount of nodes we visited is the amount of parenting nodes
	return Object.keys(visited).length
}

// Recursively find the number of bags
const countBagsFor = (graph: {[k: string]: {[k:string]: number}}, name: string) => {
	const graphEntries = Object.entries(graph[name])

	// Base case, returns 0 because we already account for the bags in the map
	if (graphEntries.length === 0) return 0

	// We calculate the bags within a given bag by "amount of bags + aniybt of bags * all possible inner bags"
	// We can change it as long as we change the base case to adjust calculations
	const bagAmounts = graphEntries.map(([key, amount]) => amount + amount * countBagsFor(graph, key))

	// Sum all the bag amounts
	return bagAmounts.reduce((acc, val) => acc + val, 0)
}

/*** SOLUTION CALCULATION ***/
const input: string[] = readLinesInput(path.resolve(__dirname, "input.txt"))

// Split between container and contained
const splittedPhrases = input.map((phrase) => phrase.split("contain"))

const childToParentMap = getReverseRelationShipMap(splittedPhrases)

console.log("Solution 1: ", findAllParentsBFS(childToParentMap, "shiny gold"))

const parentToChildMap = getRelationshipMap(splittedPhrases)

console.log("Solution 2: ", countBagsFor(parentToChildMap, "shiny gold"))

// TODO: Fix the recursive implementation
/** Case where recursive and BFS dont count equally
* light red bags contain 1 bright white bag, 2 muted yellow bags.
* dark orange bags contain 3 bright white bags, 4 muted yellow bags.
* bright white bags contain 1 shiny gold bag.
* muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
* shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
* dark olive bags contain 3 faded blue bags, 4 dotted black bags.
* vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
* faded blue bags contain no other bags.
* dotted black bags contain no other bags.
* ugly red bags contain shiny gold bag.
* rare blue bags contain ugly red bag.
*/
// const findAllParents = (parents: {[k:string]: boolean}) => {
// 	if (!parents) return 1
	
// 	Problem must be related with nested parents and the fact that we just count at the end of the node but no nodes with nested parents
// 	const allParentsCount = Object.keys(parents).map(parent => findAllParents(childToParentMap[parent]))

// 	return allParentsCount.reduce((acc, val) => acc + val, deepParents)
// }