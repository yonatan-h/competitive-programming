/**
 * @param {string} s
 * @return {string}
 */
var reverseParentheses = function (s) {
	return reverseStringsBetweenBrackets(s);
};

function reverseStringsBetweenBrackets(string) {
	const stack = [];
	for (let character of string) {
		const shouldReverse = character === ")";
		if (shouldReverse) reverseUptoOpeningBracket(stack);
		else stack.push(character);
	}

	const finalString = stack.join("");
	return finalString;
}

function reverseUptoOpeningBracket(stack) {
	const reversedStringStack = [];
	while (true) {
		const character = stack.pop();
		if (character === "(") break;
		else reversedStringStack.push(character);
	}

	stack.push(...reversedStringStack);
}

//30 minutes
//two accepted solutions
const s = "(ed(et(oc))el)";
console.log(reverseStringsBetweenBrackets(s));
