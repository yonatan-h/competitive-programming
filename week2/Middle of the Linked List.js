var middleNode = function (head) {
	return getMiddleNode(head);
};

function getMiddleNode(headOfLinkedList) {
	const nodeArray = [];
	let currentNode = headOfLinkedList;

	while (currentNode) {
		nodeArray.push(currentNode);
		currentNode = currentNode.next;
	}

	const length = nodeArray.length;
	const middle = Math.floor(length / 2);
	return nodeArray[middle];
}
