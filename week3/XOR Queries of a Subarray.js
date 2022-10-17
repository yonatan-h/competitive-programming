var xorQueries = function (arr, queries) {
	return computeAllXOROperations(arr, queries);
};

function computeAllXOROperations(numbers, queries) {
	const cumulativeXOR = [0, ...numbers];
	for (let i = 1; i < cumulativeXOR.length; i++) {
		cumulativeXOR[i] = cumulativeXOR[i] ^ cumulativeXOR[i - 1];
	}

	const queryResults = [];
	for (const query of queries) {
		const i1 = query[0] + 1;
		const i2 = query[1] + 1;

		const cumulativeUptoI2 = cumulativeXOR[i2];
		const cumulativeBeforeI1 = cumulativeXOR[i1 - 1];

		const cumulativeFrom1to2 = cumulativeUptoI2 ^ cumulativeBeforeI1;
		queryResults.push(cumulativeFrom1to2);
	}

	return queryResults;
}

//35 min
//4submissions
