function reverseLinkedList(head) {
  if (node === null) return node;
  let tail;

  function reversArrowsAfterNode(node) {
    const nextNode = node.next;
    if (nextNode === null) {
      tail = node;
      return node;
    } else {
      const reversedNextNode = reversArrowsAfterNode(nextNode);
      reversedNextNode.next = node;
      node.next = null;
      return node;
    }
  }

  reversArrowsAfterNode(head);
  return tail;
}

//10 minutes
//1submission
