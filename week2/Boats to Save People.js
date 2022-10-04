var numRescueBoats = function (people, limit) {
	return findMinimumBoats(people, limit);
};

function findMinimumBoats(weightsOfPeople, weightLimit) {
	const sortedWeights = weightsOfPeople.sort((a, b) => a - b);

	let leftPointer = 0;
	let rightPointer = sortedWeights.length - 1;
	let minimumBoatsNeeded = 0;

	while (leftPointer <= rightPointer) {
		const bigWeight = sortedWeights[rightPointer];
		const smallWeight = sortedWeights[leftPointer];

		if (bigWeight + smallWeight <= weightLimit) {
			minimumBoatsNeeded++;
			leftPointer++;
			rightPointer--;
		} else {
			//assuming the person is always possible to carry
			minimumBoatsNeeded++;
			rightPointer--;
		}
	}
	return minimumBoatsNeeded;
}
