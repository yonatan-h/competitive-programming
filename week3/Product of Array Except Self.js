var productExceptSelf = function (nums) {
	return getProductOfArrayExceptSelf(nums);
};
function getProductOfArrayExceptSelf(numbers) {
	const length = numbers.length;

	//are cumulative and reverse cumulative product arrays
	const forwardProducts = [...numbers];
	const backwardProducts = [...numbers];

	for (let i = 1; i < length; i++) {
		forwardProducts[i] = forwardProducts[i] * forwardProducts[i - 1];
	}
	for (let i = length - 2; i >= 0; i--) {
		backwardProducts[i] = backwardProducts[i] * backwardProducts[i + 1];
	}

	const productsExceptSelf = [];

	for (let i = 0; i < length; i++) {
		const isFirst = i === 0;
		const isLast = i === length - 1;

		const cumulativeFromLeft = isFirst ? 1 : forwardProducts[i - 1];
		const cumulativeFromRight = isLast ? 1 : backwardProducts[i + 1];

		const productExceptSelf = cumulativeFromLeft * cumulativeFromRight;
		productsExceptSelf[i] = productExceptSelf;
	}

	return productsExceptSelf;
}
//35min
//3sub
