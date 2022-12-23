var removeKdigits = function (num, k) {
  return removeDigitsForLess(num, k);
};

function removeDigitsForLess(number, k) {
  const canPopEveryDigit = k >= number.length;
  if (canPopEveryDigit) return "0";

  const stack = [];
  let popsLeft = k;
  let digitIndex = 0;

  while (digitIndex < number.length) {
    const digit = number[digitIndex];
    const topDigit = stack[stack.length - 1];
    const stackIsEmpty = stack.length === 0;

    const shouldPop = popsLeft && !stackIsEmpty && digit < topDigit;

    if (shouldPop) {
      stack.pop();
      popsLeft--;
    } else {
      //stack is empty, or digit is greater/equal to top, or we have popped enough
      stack.push(digit);
      digitIndex++;
    }
  }

  const properLength = number.length - k;
  const smallestInteger = stack.join("").slice(0, properLength);
  return removeLeadingZeros(smallestInteger);
}

function removeLeadingZeros(string) {
  for (let i = 0; i < string.length; i++) {
    if (string[i] !== "0") return string.slice(i);
  }
  return "0";
}

removeDigitsForLess("123321", 3);

//145
//3 submissions
