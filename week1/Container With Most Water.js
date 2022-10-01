function findMaximumArea(wallHeights) {
	let maximumArea = 0;
	let leftIndex = 0;
	let rightIndex = wallHeights.length - 1;

	for (let i = 0; i < wallHeights.length; i++) {
		const leftHeight = wallHeights[leftIndex];
		const rightHeight = wallHeights[rightIndex];

		const area = calculateArea(leftIndex, leftHeight, rightIndex, rightHeight);
		if (area > maximumArea) maximumArea = area;

		const leftIsTaller = leftHeight > rightHeight;
		if (leftIsTaller) rightIndex--;
		else leftIndex++;
	}

	return maximumArea;
}

function calculateArea(x1, height1, x2, height2) {
	const lowerHeight = height1 < height2 ? height1 : height2;
	const width = x2 - x1;
	const area = lowerHeight * width;
	return area;
}
