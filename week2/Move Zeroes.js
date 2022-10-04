var moveZeroes = function (nums) {
	return moveZerosToRight(nums);
};

function moveZerosToRight(numbers) {
	let leftPointer = 0;
	let rightPointer = 0;

	while (rightPointer < numbers.length) {
		const leftOnZero = numbers[leftPointer] === 0;
		const rightOnNonZero = numbers[rightPointer] !== 0;

		if (leftOnZero && rightOnNonZero) {
			const nonZeroNumber = numbers[rightPointer];
			//pull non zero number through zeros in between
			numbers[leftPointer] = nonZeroNumber;
			numbers[rightPointer] = 0;

			//move both by one step
			leftPointer++;
			rightPointer++;
		} else if (leftOnZero && !rightOnNonZero) {
			//keep searching for a non zero
			rightPointer++;
		} else {
			//search for a zero
			leftPointer++;
			rightPointer = leftPointer;
		}
	}
	return numbers;
}
