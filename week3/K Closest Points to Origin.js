var kClosest = function (points, k) {
	return getKClosestPointsToTheOrigin(points, k);
};

function getKClosestPointsToTheOrigin(points, k) {
	const raduisAndPoints = [];

	for (let i = 0; i < points.length; i++) {
		const point = points[i];
		const [x, y] = point;
		const radius = Math.hypot(x, y);
		raduisAndPoints[i] = { radius, point };
	}
	raduisAndPoints.sort(pointComparer);

	const firstKPoints = [];
	for (let i = 0; i < k; i++) {
		const radiusAndPoint = raduisAndPoints[i];
		firstKPoints.push(radiusAndPoint.point);
	}
	return firstKPoints;
}

function pointComparer(point1, point2) {
	const rad1 = point1.radius;
	const rad2 = point2.radius;
	return rad1 > rad2 ? 1 : -1;
}

//30 min
//1 submission
