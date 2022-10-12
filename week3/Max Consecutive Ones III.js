var longestOnes = function (nums, k) {
	return findLongestOnes(nums, k);
};

function findLongestOnes(binaryArray, onesInBucket) {
	function shiftLeft() {
		//shift left so that a zero is lost from the window
		const leftIsOnOne = binaryArray[left] === 1;
		if (leftIsOnOne) {
			while (binaryArray[left] !== 0) left++;
		}
		left++;
	}

	let maxChainLength = 0;
	let left = 0;

	for (let right = 0; right < binaryArray.length; right++) {
		const gainedAZero = binaryArray[right] === 0;
		if (gainedAZero) {
			if (onesInBucket > 0) {
				onesInBucket--;
			} else {
				shiftLeft();
			}
		}

		const chainLength = right + 1 - left;
		maxChainLength = Math.max(maxChainLength, chainLength);
	}
	return maxChainLength;
}

//3hrs
//2submissions
