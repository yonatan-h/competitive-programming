var compress = function (chars) {
	return compressString(chars);
};
function compressString(charactersArray) {
	const characterNumberPairs = [{ character: "", number: 0 }];

	for (let character of charactersArray) {
		const lastCharacterNumberPair = getLastElement(characterNumberPairs);
		const lastCharacter = lastCharacterNumberPair.character;

		if (lastCharacter === character) {
			lastCharacterNumberPair.number++;
		} else {
			const newCharacterNumberPair = { character, number: 1 };
			characterNumberPairs.push(newCharacterNumberPair);
		}
	}

	const compressedCharactersArray = [];
	for (let i = 1; i < characterNumberPairs.length; i++) {
		const characterNumberPair = characterNumberPairs[i];
		const character = characterNumberPair.character;
		const number = characterNumberPair.number;

		compressedCharactersArray.push(character);

		if (number !== 1) {
			const digits = number.toString().split("");
			compressedCharactersArray.push(...digits);
		}
	}

	//copy compressedCharactesArray to charactersArray
	charactersArray.length = 0;
	charactersArray.push(...compressedCharactersArray);
	return compressedCharactersArray.length;
}

function getLastElement(array) {
	const lastIndex = array.length - 1;
	const lastElement = array[lastIndex];
	return lastElement;
}
