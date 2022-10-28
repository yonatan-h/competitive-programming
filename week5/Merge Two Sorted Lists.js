function LinkedList() {
  this.pointerToHead = { next: null };
  this.pointerToTail = { next: null };
}

LinkedList.prototype.append = function (newTail) {
  const oldTail = this.pointerToTail.next;

  if (newTail === null) {
    return;
  } else if (oldTail === null) {
    this.pointerToHead.next = newTail;
    this.pointerToTail.next = newTail;
  } else {
    oldTail.next = newTail;
    this.pointerToTail.next = newTail;
  }
};

LinkedList.prototype.getHead = function () {
  return this.pointerToHead.next;
};

var mergeTwoLists = function (list1, list2) {
  return mergeTwoSortedLinkedLists(list1, list2);
};

function mergeTwoSortedLinkedLists(head1, head2) {
  let currentHead1 = head1;
  let currentHead2 = head2;
  const mergedLinkedList = new LinkedList();

  while (currentHead1 && currentHead2) {
    const value1 = currentHead1.val;
    const value2 = currentHead2.val;

    if (value1 < value2) {
      const nextNode1 = currentHead1.next;
      currentHead1.next = null;
      mergedLinkedList.append(currentHead1);
      currentHead1 = nextNode1;
    } else {
      const nextNode2 = currentHead2.next;
      currentHead2.next = null;
      mergedLinkedList.append(currentHead2);
      currentHead2 = nextNode2;
    }
  }
  mergedLinkedList.append(currentHead1);
  mergedLinkedList.append(currentHead2);

  return mergedLinkedList.getHead();
}

//30 min
//2 submission
