function getLastMonotonicPortion(numbers) {
  const stack = [];
  let i = 0;

  while (i < numbers.length) {
    const currentNumber = numbers[i];
    const topNumber = stack[stack.length - 1];

    const shouldPush = stack.length === 0 || currentNumber > topNumber;
    if (shouldPush) {
      stack.push(currentNumber);
      i++;
    } else {
      stack.pop();
    }
  }

  console.log(stack);
}

getLastMonotonicPortion([5, 4, 3, 2, 1]);
