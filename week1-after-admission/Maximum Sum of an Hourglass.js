var maxSum = function (grid) {
  return findMaxSum(grid);
};

function sumOfHourGlass(matrix, y, x) {
  const topLeft = matrix[y][x];
  const top = matrix[y][x + 1];
  const topRight = matrix[y][x + 2];
  const middle = matrix[y + 1][x + 1];
  const bottomLeft = matrix[y + 2][x];
  const bottom = matrix[y + 2][x + 1];
  const bottomRight = matrix[y + 2][x + 2];

  return topLeft + top + topRight + middle + bottomLeft + bottom + bottomRight;
}

function findMaxSum(matrix) {
  const width = matrix[0].length;
  const height = matrix.length;

  const glassSize = 3;
  let maximumSum = -Infinity;

  for (y = 0; y <= height - glassSize; y++) {
    for (x = 0; x <= width - glassSize; x++) {
      const sum = sumOfHourGlass(matrix, y, x);
      if (sum > maximumSum) maximumSum = sum;
    }
  }
  return maximumSum;
}

//35min
