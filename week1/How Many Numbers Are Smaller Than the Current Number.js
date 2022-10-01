var smallerNumbersThanCurrent = function (nums) {
	return getHowManySmallerNumbers(nums);
};

function sortIntegers(numbers) {
	const comparer = (a, b) => (a - b > 0 ? 1 : -1);
	numbers.sort(comparer);
	return numbers;
}

function getHowManySmallerNumbers(numbers) {
	const sortedNumbers = sortIntegers([...numbers]);
	//regester number of lesser numbers
	const numberLesserAmountsPair = {};
	for (let i = 0; i < sortedNumbers.length; i++) {
		const number = sortedNumbers[i];
		const lesserAmounts = i;

		//if number has already been regestered, skip regestering
		if (numberLesserAmountsPair[number] !== undefined) continue;
		numberLesserAmountsPair[number] = lesserAmounts;
	}

	//replace each number by its number of lesser numbers
	const smallerNumbersThanCurrentArray = [...numbers];
	for (let i = 0; i < numbers.length; i++) {
		const number = numbers[i];
		const lesserAmounts = numberLesserAmountsPair[number];
		smallerNumbersThanCurrentArray[i] = lesserAmounts;
	}

	return smallerNumbersThanCurrentArray;
}
