var isPalindrome = function (string) {
  return isValidPalindrome(string);
};

function isValidPalindrome(nonAlphanumbericString) {
  const string = nonAlphanumbericString
    .split("")
    .map((char) => (isAlphanumeric(char) ? char : ""))
    .join("")
    .toLowerCase();

  for (let i = 0; i < 1 + string.length / 2; i++) {
    const leftParallel = string[i];
    const rightParallel = string[string.length - 1 - i];

    if (leftParallel !== rightParallel) return false;
  }

  return true;
}

function isAlphanumeric(char) {
  const alphaNumeric = /[A-Z]|[a-z]|[0-9]/;
  const match = char.match(alphaNumeric);
  return match !== null;
}

//20min
