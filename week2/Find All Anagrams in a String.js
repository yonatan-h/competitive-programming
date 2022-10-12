function AnagramDetector(anagramWord) {
	const anagramLetterAmountPair = {};
	const windowLetterAmountPair = {};

	for (let letter of anagramWord) {
		if (anagramLetterAmountPair[letter]) {
			anagramLetterAmountPair[letter]++;
		} else {
			anagramLetterAmountPair[letter] = 1;
			windowLetterAmountPair[letter] = 0;
		}
	}

	this.anagramLetterAmountPair = anagramLetterAmountPair;
	this.windowLetterAmountPair = windowLetterAmountPair;

	this.parallelLettersInWindow = 0;
	this.anagramWordLength = anagramWord.length;
}

AnagramDetector.prototype.isInAnagramWord = function (letter) {
	const amountInAnagram = this.anagramLetterAmountPair[letter];
	const exists = amountInAnagram !== undefined;
	return exists;
};

AnagramDetector.prototype.add = function (letter) {
	if (this.isInAnagramWord(letter)) {
		this.windowLetterAmountPair[letter]++;

		const amountInAnagram = this.anagramLetterAmountPair[letter];
		const amountInWindow = this.windowLetterAmountPair[letter];
		const parallelLetterAdded = amountInWindow <= amountInAnagram;

		if (parallelLetterAdded) this.parallelLettersInWindow++;
	}
};

AnagramDetector.prototype.remove = function (letter) {
	if (this.isInAnagramWord(letter)) {
		this.windowLetterAmountPair[letter]--;

		const amountInAnagram = this.anagramLetterAmountPair[letter];
		const amountInWindow = this.windowLetterAmountPair[letter];
		const parallelLetterRemoved = amountInWindow < amountInAnagram;

		if (parallelLetterRemoved) this.parallelLettersInWindow--;
	}
};

AnagramDetector.prototype.anagramDetected = function () {
	const windowIsAnagram =
		this.parallelLettersInWindow === this.anagramWordLength;
	return windowIsAnagram;
};

function findAnagramIndexes(string, anagramWord) {
	const anagramDetector = new AnagramDetector(anagramWord);
	let anagramIndexes = [];

	const anagramLength = anagramWord.length;
	const stringLength = string.length;

	for (let i = 0; i < stringLength; i++) {
		const gainedLetter = string[i];
		const indexOfLostLetter = i - anagramLength;
		const lostLetter = indexOfLostLetter < 0 ? "" : string[indexOfLostLetter];

		anagramDetector.remove(lostLetter);
		anagramDetector.add(gainedLetter);
		if (anagramDetector.anagramDetected()) {
			const indexOfAnagram = indexOfLostLetter + 1;
			anagramIndexes.push(indexOfAnagram);
		}
	}

	return anagramIndexes;
}

var findAnagrams = function (s, p) {
	return findAnagramIndexes(s, p);
};
