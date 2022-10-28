function findFibonacci(nth) {
  let firstNumber = 0;
  let secondNumber = 1;

  for (let n = 2; n < nth; n++) {
    const sumOfPreviousTwo = firstNumber + secondNumber;
    firstNumber = secondNumber;
    secondNumber = sumOfPreviousTwo;
  }

  return firstNumber + secondNumber;
}

//7min
//2 submissions
