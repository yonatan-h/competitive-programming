function decodeString(originalString) {
  let i = 0;
  return expand();

  function expand() {
    let currentRepeats = "";
    let expanded = "";

    while (true) {
      if (i === originalString.length) return expanded;
      const char = originalString[i];
      i++;

      if (isNumber(char)) {
        currentRepeats += char;
      } else if (char === "[") {
        const expandedSubString = expand();
        const repeatedSubString = repeat(currentRepeats, expandedSubString);
        currentRepeats = "";
        expanded += repeatedSubString;
      } else if (char === "]") {
        return expanded;
      } else {
        expanded += char;
      }
    }
  }
}

function repeat(repeatsInString, string) {
  const repeats = +repeatsInString;
  let repeadedString = "";
  for (let i = 0; i < repeats; i++) repeadedString += string;
  return repeadedString;
}

function isNumber(string) {
  const isNumber = Number.isNaN(+string) === false;
  return isNumber;
}

//10 submissions
//3 hrs
