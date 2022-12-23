//'use strict';

const fs = require("fs");

process.stdin.resume();
process.stdin.setEncoding("utf-8");

let inputString = "";
let currentLine = 0;

process.stdin.on("data", function (inputStdin) {
  inputString += inputStdin;
});

process.stdin.on("end", function () {
  inputString = inputString.split("\n");

  main();
});

function readLine() {
  return inputString[currentLine++];
}

function gradingStudents(grades) {
  for (let i = 0; i < grades.length; i++) {
    grades[i] = roundUpIfPossible(grades[i]);
  }
  return grades;
}

function roundUpIfPossible(number) {
  const remainder5 = number % 5;
  const stepsTill5 = 5 - remainder5;
  if (number >= 38 && stepsTill5 <= 2) {
    const nextMultipleOf5 = number - remainder5 + 5;
    return nextMultipleOf5;
  } else {
    return number;
  }
}

function main() {
  const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

  const gradesCount = parseInt(readLine().trim(), 10);

  let grades = [];

  for (let i = 0; i < gradesCount; i++) {
    const gradesItem = parseInt(readLine().trim(), 10);
    grades.push(gradesItem);
  }

  const result = gradingStudents(grades);

  ws.write(result.join("\n") + "\n");

  ws.end();
}

//15 minutes
//1 submission
