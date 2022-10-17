function getSeatsForFlights(bookings, numberOfFlights) {
	const changeInBookingsPerFlight = [];
	changeInBookingsPerFlight.length = numberOfFlights;
	changeInBookingsPerFlight.fill(0);

	for (let booking of bookings) {
		//-1 to for 1st to be on 0
		const startingFlight = booking[0] - 1;
		const endingFlight = booking[1] - 1;
		const seatsReserved = booking[2];

		changeInBookingsPerFlight[startingFlight] += seatsReserved;
		changeInBookingsPerFlight[endingFlight + 1] -= seatsReserved;
	}

	let currentNumberOfBookings = 0;
	const bookingsPerFlight = [];
	for (let flight = 0; flight < numberOfFlights; flight++) {
		const changeInBookings = changeInBookingsPerFlight[flight];
		currentNumberOfBookings += changeInBookings;
		bookingsPerFlight.push(currentNumberOfBookings);
	}

	return bookingsPerFlight;
}

//1hr
//1submission
