var carFleet = function (target, position, speed) {
	return countCarFleetsCrossingFinishLine(target, position, speed);
};

function countCarFleetsCrossingFinishLine(finishPosition, positions, speeds) {
	const numberOfCars = positions.length;

	if (numberOfCars === 1) return 1;
	else if (numberOfCars === 0) return 0;

	const cars = getCars(finishPosition, positions, speeds);

	let fleetCount = 1;
	let fleetHead = numberOfCars - 1;
	let tail = numberOfCars - 2;

	while (tail >= 0) {
		const headCar = cars[fleetHead];
		const tailCar = cars[tail];
		const tailIsMemberOfFleet = collideBeforeFinishLine(tailCar, headCar);

		if (tailIsMemberOfFleet) {
			tail--;
		} else {
			fleetCount++;
			fleetHead = tail;
			tail--;
		}
	}
	return fleetCount;
}
function getCars(finishPosition, positions, speeds) {
	const cars = [];
	for (let i = 0; i < positions.length; i++) {
		const position = positions[i];
		const speed = speeds[i];
		const timeToFinishLine = (finishPosition - position) / speed;

		cars.push({ position, speed, timeToFinishLine });
	}

	cars.sort((carA, carB) => {
		if (carA.position > carB.position) return 1;
		else return -1;
	});
	return cars;
}

function collideBeforeFinishLine(carBack, carFront) {
	const frontTimeToFinishLine = carFront.timeToFinishLine;
	const backTimeToFinishLine = carBack.timeToFinishLine;
	return backTimeToFinishLine <= frontTimeToFinishLine;
}

//3hrs
//4submission
