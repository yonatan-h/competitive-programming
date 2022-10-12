var NumMatrix = function (matrix) {
	this.regionSumsFromOrigin = this.buildRegionSums(matrix);
};

NumMatrix.prototype.makeEmptyMatrix = function (width, height) {
	const emptyMatrix = [];
	for (let y = 0; y < height; y++) {
		const nullRow = [];
		nullRow.length = width;
		nullRow.fill(null);
		emptyMatrix.push(nullRow);
	}
	return emptyMatrix;
};

NumMatrix.prototype.buildRegionSums = function (matrix) {
	const height = matrix.length;
	const width = matrix[0].length;

	const cumulativeSumsInRows = this.makeEmptyMatrix(width, height);

	//first column in the matrix and in the rowSum are the same
	for (let y = 0; y < height; y++) {
		cumulativeSumsInRows[y][0] = matrix[y][0];
	}

	//fill all spots with cumulative sum of their respective rows
	for (let y = 0; y < height; y++) {
		for (let x = 1; x < width; x++) {
			const value = matrix[y][x];
			const cumulativeSumBefore = cumulativeSumsInRows[y][x - 1];

			const cumulativeSum = value + cumulativeSumBefore;
			cumulativeSumsInRows[y][x] = cumulativeSum;
		}
	}

	const regionSumsFromOrigin = this.makeEmptyMatrix(width, height);

	//same first row in regionSums and rowSums
	regionSumsFromOrigin[0] = cumulativeSumsInRows[0];

	//build the region sum from top to bottom, row by row
	for (let y = 1; y < height; y++) {
		for (let x = 0; x < width; x++) {
			const rowSum = cumulativeSumsInRows[y][x];
			const regionSumAbove = regionSumsFromOrigin[y - 1][x];

			const regionSum = rowSum + regionSumAbove;
			regionSumsFromOrigin[y][x] = regionSum;
		}
	}

	return regionSumsFromOrigin;
};

NumMatrix.prototype.sumRegion = function (y1, x1, y2, x2) {
	const regionSumsFromOrigin = this.regionSumsFromOrigin;

	let leftRectangleSum;
	let topRectangleSum;
	let topLeftRectanglesInstersectionSum;
	let bottomRightCornerSum;

	//get values for sums inside several rectangles
	bottomRightCornerSum = regionSumsFromOrigin[y2][x2];

	const rectangleStartsAtTop = y1 === 0;
	const rectangleStartsAtLeft = x1 === 0;

	if (rectangleStartsAtTop) topRectangleSum = 0;
	else topRectangleSum = regionSumsFromOrigin[y1 - 1][x2];

	if (rectangleStartsAtLeft) leftRectangleSum = 0;
	else leftRectangleSum = regionSumsFromOrigin[y2][x1 - 1];

	if (rectangleStartsAtLeft || rectangleStartsAtTop) {
		topLeftRectanglesInstersectionSum = 0;
	} else {
		topLeftRectanglesInstersectionSum = regionSumsFromOrigin[y1 - 1][x1 - 1];
	}

	//finally calculate the sum inside the rectangle in question
	const rectangleRegionSum =
		bottomRightCornerSum -
		topRectangleSum -
		leftRectangleSum +
		topLeftRectanglesInstersectionSum;

	return rectangleRegionSum;
};
