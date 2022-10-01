var sortColors = function (nums) {
	return bubbleSort(nums);
};

function bubbleSort(numbers) {
	for (let rightMostI = numbers.length - 1; rightMostI > 0; rightMostI--) {
		let hasSwappedThisRound = false;

		for (let i = 1; i <= rightMostI; i++) {
			const previousNumber = numbers[i - 1];
			const currentNumber = numbers[i];

			if (previousNumber > currentNumber) {
				swap(i - 1, i, numbers);
				hasSwappedThisRound = true;
			}
		}

		if (!hasSwappedThisRound) break;
	}
	return numbers;
}

function swap(index1, index2, array) {
	const element1 = array[index1];
	const element2 = array[index2];

	array[index2] = element1;
	array[index1] = element2;
}
