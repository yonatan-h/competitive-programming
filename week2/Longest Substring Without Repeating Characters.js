//244
var lengthOfLongestSubstring = function (s) {
	return findLongestNonRepeatingSubString(s);
};
function findLongestNonRepeatingSubString(string) {
	if (string.length === 0) return 0;

	let maxRange = 0;
	let left = 0;
	let right = 0;
	const windowLetters = new Set();

	while (right < string.length) {
		const rightLetter = string[right];
		const leftLetter = string[left];
		const rightIsInWindow = windowLetters.has(rightLetter);

		if (rightIsInWindow) {
			windowLetters.delete(leftLetter);
			left++;
		} else {
			windowLetters.add(rightLetter);
			const rangeOfWindow = right + 1 - left;
			maxRange = Math.max(maxRange, rangeOfWindow);
			right++;
		}
	}

	return maxRange;
}

console.log(findLongestNonRepeatingSubString("abcabcbb"));
