function maxSumTwoNoOverlap(numbers, firstLength, secondLength) {
	const firstWindowSums = getWindowSums(numbers, firstLength);
	const secondWindowSums = getWindowSums(numbers, secondLength);

	let maxNonOverlappingSum = -Infinity;

	for (let i = 0; i < firstWindowSums.length; i++) {
		for (let j = 0; j < secondWindowSums.length; j++) {
			const firstWindowSum = firstWindowSums[i];
			const secondWindowSum = secondWindowSums[j];

			if (!windowsOverlap(i, firstLength, j, secondLength)) {
				const sumOfWindows = firstWindowSum + secondWindowSum;
				maxNonOverlappingSum = Math.max(sumOfWindows, maxNonOverlappingSum);
			}
		}
	}

	return maxNonOverlappingSum;
}

function windowsOverlap(leftIndex1, length1, leftIndex2, length2) {
	const rightIndex1 = leftIndex1 + length1 - 1;
	const rightIndex2 = leftIndex2 + length2 - 1;

	const oneIsLeftOfTwo = rightIndex1 < leftIndex2;
	const oneIsRightOfTwo = leftIndex1 > rightIndex2;

	const noOverlap = oneIsLeftOfTwo || oneIsRightOfTwo;
	return !noOverlap;
}

function getWindowSums(numbers, windowLength) {
	const windowSums = [];

	let currentWindowSum = 0;
	for (let i = 0; i < numbers.length; i++) {
		const gainedNumber = numbers[i];
		const lostIndex = i - windowLength;
		const lostNumber = lostIndex < 0 ? 0 : numbers[lostIndex];

		currentWindowSum += gainedNumber;
		currentWindowSum -= lostNumber;

		const leftIndex = lostIndex + 1;
		if (leftIndex >= 0) windowSums.push(currentWindowSum);
	}

	return windowSums;
}
