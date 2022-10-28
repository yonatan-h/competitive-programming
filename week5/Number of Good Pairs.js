var numIdenticalPairs = function (nums) {
  return getNumberOfGoodPairs(nums);
};

function getNumberOfGoodPairs(numbers) {
  let numberOfGoodPairs = 0;
  for (let i = 0; i < numbers.length; i++) {
    for (let j = i + 1; j < numbers.length; j++) {
      const leftNumber = numbers[i];
      const rightNumber = numbers[j];

      if (leftNumber === rightNumber) numberOfGoodPairs++;
    }
  }
  return numberOfGoodPairs;
}

//10minutes
//1 submission
