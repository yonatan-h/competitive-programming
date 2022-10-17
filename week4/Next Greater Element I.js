var nextGreaterElement = function (nums1, nums2) {
	return findTheNextGreatElements(nums1, nums2);
};
function findTheNextGreatElements(subset, numbers) {
	const numberNextGreaterNumberPair =
		getNextGreaterElementForEveryNumber(numbers);
	const nextGreaterNumberArray = [];
	for (const number of subset) {
		const nextGreaterNumber = numberNextGreaterNumberPair[number];
		if (nextGreaterNumber === undefined) {
			nextGreaterNumberArray.push(-1);
		} else {
			nextGreaterNumberArray.push(nextGreaterNumber);
		}
	}
	return nextGreaterNumberArray;
}

function getNextGreaterElementForEveryNumber(numbers) {
	const decreasingStack = [Infinity];
	const peek = () => decreasingStack[decreasingStack.length - 1];

	const numberGreaterNumberPair = {};
	for (const currentNumber of numbers) {
		const topNumber = peek();
		const isGreaterElement = currentNumber > topNumber;

		if (isGreaterElement) {
			//pop all whose next greater element is "currentNumber"
			//save their next greater element = currentNumber
			while (currentNumber > peek()) {
				const poppedNumber = decreasingStack.pop();
				numberGreaterNumberPair[poppedNumber] = currentNumber;
			}
			//once current number is less than peek() (can't be equal in this question), put it back in stack
			decreasingStack.push(currentNumber);
		} else {
			decreasingStack.push(currentNumber);
		}
	}
	return numberGreaterNumberPair;
}

//30min
//1 submission
