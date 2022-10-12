var pivotIndex = function (nums) {
	return findPivotIndex(nums);
};
function findPivotIndex(numbers) {
	const sumsFromLeft = [0, ...numbers, 0];
	const sumsFromRight = [0, ...numbers, 0];
	const length = numbers.length + 2;

	for (let i = 1; i < length; i++) {
		sumsFromLeft[i] = sumsFromLeft[i] + sumsFromLeft[i - 1];
	}
	for (let i = length - 2; i >= 0; i--) {
		sumsFromRight[i] = sumsFromRight[i] + sumsFromRight[i + 1];
	}

	for (let i = 1; i < length - 1; i++) {
		if (sumsFromLeft[i] === sumsFromRight[i]) {
			const pivotIndex = i - 1;
			return pivotIndex;
		}
	}
	return -1;
}
