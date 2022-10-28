function isPalindrome(head) {
  const numbers = [];
  let currentNode = head;
  while (currentNode) {
    numbers.push(currentNode.val);
    currentNode = currentNode.next;
  }

  for (let i = 0; i < numbers.length / 2; i++) {
    const leftNumber = numbers[i];

    const parallelToI = numbers.length - 1 - i;
    const rightNumber = numbers[parallelToI];

    if (leftNumber !== rightNumber) return false;
  }
  return true;
}

//6min
//1sub
