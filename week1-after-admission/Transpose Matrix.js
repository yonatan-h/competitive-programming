function transpose(matrix) {
  const flipped = [];
  const height = matrix.length;
  const width = matrix[0].length;

  for (let i = 0; i < width; i++) {
    const emptyRow = [];
    emptyRow.length = height;
    flipped.push(emptyRow);
  }

  for (let y = 0; y < height; y++) {
    for (let x = 0; x < width; x++) {
      const value = matrix[y][x];
      flipped[x][y] = value;
    }
  }
  return flipped;
}

//20min
