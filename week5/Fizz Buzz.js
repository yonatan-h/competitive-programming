function fizzBuzz(number) {
  const answer = [];
  for (let i = 1; i <= number; i++) {
    answer.push(sayFizzBuzz(i));
  }
  return answer;
}

function sayFizzBuzz(number) {
  const by3 = number % 3 === 0;
  const by5 = number % 5 === 0;
  //(by5 && by3) is faster (~11th percentile) to evaluate than (by3 && by5), (~80th percentile)
  if (by5 && by3) return "FizzBuzz";
  else if (by3) return "Fizz";
  else if (by5) return "Buzz";
  else return number.toString();
}
//5minutes
//2submissions
