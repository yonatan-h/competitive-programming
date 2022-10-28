function deleteNode(node) {
  let currentNode = node;

  while (true) {
    const nextNode = currentNode.next;
    const currentNodeShouldBeLast = nextNode.next === null;

    if (currentNodeShouldBeLast) {
      currentNode.val = nextNode.val;
      currentNode.next = null;
      break;
    } else {
      currentNode.val = nextNode.val;
      currentNode = nextNode;
    }
  }
}

//20 minutes
//1submission
