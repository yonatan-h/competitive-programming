function validateParenthesis(string) {
	const bracketStack = [];
	const openClosePair = {
		"{": "}",
		"(": ")",
		"[": "]",
	};

	for (character of string) {
		console.log(bracketStack);
		const isOpeningBracket = openClosePair[character] !== undefined;
		if (isOpeningBracket) {
			bracketStack.push(character);
		} else {
			const topOpeningBracket = bracketStack.pop();
			const closingBracketForTop = openClosePair[topOpeningBracket];
			if (character !== closingBracketForTop) return false;
		}
	}
	//if stack is empty return true
	return bracketStack.length === 0;
}
