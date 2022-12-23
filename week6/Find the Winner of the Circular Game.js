function findWinner(totalPlayers, steps) {
  const initialState = {
    numPlayers: totalPlayers,
    startingIndex: 0,
    hops: steps - 1,
  };

  const lastSurvivor = playRoundAndGetLoser(initialState);
  const winnerLabel = lastSurvivor + 1;
  return winnerLabel;
}

function playRoundAndGetLoser(state) {
  const { numPlayers, startingIndex, hops } = state;

  if (numPlayers > 1) {
    const loser = (startingIndex + hops) % numPlayers;

    const nextState = getNextState({ numPlayers, loser, hops });
    const nextLoser = playRoundAndGetLoser(nextState);
    const indexOfNextLoser = getIndexOfNextLoser(loser, nextLoser);

    return indexOfNextLoser;
  } else {
    const indexOfLastSurvivor = 0;
    return indexOfLastSurvivor;
  }
}

function getNextState({ numPlayers, loser, hops }) {
  const nextNumPlayers = numPlayers - 1;
  const nextStartingIndex = loser % nextNumPlayers;

  const nextState = {
    numPlayers: nextNumPlayers,
    startingIndex: nextStartingIndex,
    hops,
  };

  return nextState;
}

function getIndexOfNextLoser(loser, nextLoser) {
  const nextLoserIsBehindCurrentLoser = nextLoser < loser;

  let indexOfNextLoser;
  if (nextLoserIsBehindCurrentLoser) indexOfNextLoser = nextLoser;
  else indexOfNextLoser = nextLoser + 1;

  return indexOfNextLoser;
}

//180 minutes
//1submission
