var totalFruit = function (fruits) {
	return takeMaximumFruits(fruits);
};

function takeMaximumFruits(fruits) {
	const longestFruitsSlice = { start: 0, end: 0 };

	let firstFruit = null;
	let secondFruit = null;

	let left = 0;
	let middle = 0;
	let right = 0;

	while (right < fruits.length) {
		const currentFruit = fruits[right];
		const isFirstFruit = currentFruit === firstFruit;
		const isSecondFruit = currentFruit === secondFruit;
		const isNewFruit = !isFirstFruit && !isSecondFruit;

		if (isNewFruit) {
			left = middle;
			firstFruit = fruits[left];
			secondFruit = fruits[right];
		}

		const longestSliceRange = longestFruitsSlice.end - longestFruitsSlice.start;
		const currentSliceRange = right - left;
		if (currentSliceRange >= longestSliceRange) {
			longestFruitsSlice.start = left;
			longestFruitsSlice.end = right;
		}

		if (fruits[middle] !== currentFruit) middle = right;
		right++;
	}

	return longestFruitsSlice.end - longestFruitsSlice.start + 1;
}
//3hrs
//1submission
