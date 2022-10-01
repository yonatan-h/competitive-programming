var targetIndices = function (nums, target) {
	return getTargetIndicesAfterSorting(nums, target);
};

function getTargetIndicesAfterSorting(numbers, target) {
	const sortedNumbers = [...numbers];
	sortedNumbers.sort((a, b) => a - b);

	const matcher = (element) => element === target;
	const firstTargetIndexInSorted = sortedNumbers.findIndex(matcher);

	const targetIndices = [];
	for (let i = firstTargetIndexInSorted; i < sortedNumbers.length; i++) {
		const elementAtIndex = sortedNumbers[i];
		if (elementAtIndex === target) targetIndices.push(i);
		else break;
	}

	return targetIndices;
}
