var deleteDuplicates = function removeDuplicates(head) {
  if (head === null) return head;
  if (head.next === null) return head;

  let leftNode = head;
  let rightNode = head.next;

  let wasInDuplicateRow = false;
  while (rightNode !== null) {
    const sameNumber = leftNode.val === rightNode.val;

    if (sameNumber && wasInDuplicateRow) {
      //searching for the next different number or null
      rightNode = rightNode.next;
    } else if (sameNumber && !wasInDuplicateRow) {
      //just entered a duplicate row
      wasInDuplicateRow = true;
      leftNode.next = null; //incase duplicates all the way down
      rightNode = rightNode.next;
    } else if (wasInDuplicateRow && !sameNumber) {
      //exited duplicate row
      wasInDuplicateRow = false;
      leftNode.next = rightNode;

      rightNode = rightNode.next;
      leftNode = leftNode.next;
    } else {
      //running fine in non duplicate row
      rightNode = rightNode.next;
      leftNode = leftNode.next;
    }
  }
  return head;
};

//30 minutes
//2submission
