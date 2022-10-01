var sortSentence = function (unsortedSentence) {
	const words = unsortedSentence.split(" ");

	const numberWordPair = {};

	//get numbers of words
	for (let word of words) {
		const wordNumber = word[word.length - 1];
		const realWord = word.slice(0, word.length - 1);

		numberWordPair[wordNumber] = realWord;
	}

	//sort the words
	let sortedWords = [];
	for (let i = 1; i <= words.length; i++) {
		const word = numberWordPair[i];
		sortedWords.push(word);
	}

	const sortedSentence = sortedWords.join(" ");
	return sortedSentence;
};
