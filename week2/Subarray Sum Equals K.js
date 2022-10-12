var subarraySum = function (nums, k) {
	return findNumberOfSubArraysThatSum(nums, k);
};

function findNumberOfSubArraysThatSum(numbers, targetSum) {
	let subarraysThatSatisfySum = 0;

	const cumulativeSums = getCumulativeSums(numbers);
	const length = cumulativeSums.length;
	for (let left = 0; left < length - 1; left++) {
		for (let right = left + 1; right < length; right++) {
			const sumInBetween = cumulativeSums[right] - cumulativeSums[left];
			if (sumInBetween === targetSum) subarraysThatSatisfySum++;
		}
		console.log(left);
	}

	return subarraysThatSatisfySum;
}

function getCumulativeSums(numbers) {
	const cumulativeSums = [0];
	for (let i = 0; i < numbers.length; i++) {
		const cumulativeSumBefore = cumulativeSums[i];
		const value = numbers[i];
		const cumulativeSum = cumulativeSumBefore + value;
		cumulativeSums.push(cumulativeSum);
	}
	return cumulativeSums;
}
