/**
 * @param {number[]} pushed
 * @param {number[]} popped
 * @return {boolean}
 */
var validateStackSequences = function (pushed, popped) {
	return validateStackSequence(pushed, popped);
};
function validateStackSequence(pushed, popped) {
	const stack = [];
	let poppedIndex = 0;
	let pushedIndex = 0;

	for (let i = 0; i < 2 * pushed.length; i++) {
		const topElement = getTopElement(stack);
		const elementToPop = popped[poppedIndex];
		const elementToPush = pushed[pushedIndex];

		if (topElement === elementToPop) {
			stack.pop();
			poppedIndex++;
		} else {
			stack.push(elementToPush);
			pushedIndex++;
		}
	}
	//stack should be empty
	return stack.length === 0;
}

function addBufferElements(array) {
	for (let i = 0; i < array.length; i++) {
		array.push(null);
	}
}

function getTopElement(stack) {
	const lastElement = stack.length ? stack[stack.length - 1] : undefined;
	return lastElement;
}
