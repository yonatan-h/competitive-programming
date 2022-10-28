function isPowerOfFour(number) {
  const power = Math.log10(number) / Math.log10(4);
  const powerIsInteger = power % 1 === 0;

  if (powerIsInteger) return true;
  else return false;
}

//1 minute
//1 submission
