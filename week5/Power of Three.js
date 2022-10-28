function isPowerOfThree(number) {
  const power = Math.log10(number) / Math.log10(3);
  const powerIsInteger = power % 1 === 0;

  if (powerIsInteger) return true;
  else return false;
}

//5min
//1 submission
