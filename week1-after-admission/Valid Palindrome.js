var isPalindrome = function (string) {
  return isValidPalindrome(string);
};

function isValidPalindrome(nonAlphanumbericString) {
  const string = nonAlphanumbericString
    .split()
    .map((char) => (isAlphanumeric(char) ? char : ""))
    .join("")
    .toLowerCase();

  console.log(string);

  for (let i = 0; i < string.length / 2; i++) {
    const leftParallel = string[i];
    const rightParallel = string[string.length - 1 - i];
    if (leftParallel !== rightParallel) return false;
  }

  return true;
}

function isAlphanumeric(char) {
  const alphaNumeric = /[A-z]|[1-9]/;
  const match = char.match(alphaNumeric);
  return match !== null;
}

console.log(isValidPalindrome("A man, a plan, a canal: Panama"));
