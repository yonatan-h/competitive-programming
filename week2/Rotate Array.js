var rotate = function (nums, k) {
	rotateArray(nums, k);
};

function rotateArray(numbers, jumps) {
	const length = numbers.length;
	const minimumJumps = jumps % length; //incase jumps > length

	const spillOvers = numbers.splice(length - minimumJumps);
	numbers.unshift(...spillOvers);
}
