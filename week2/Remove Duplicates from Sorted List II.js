function deleteDuplicates(firstNode) {
	const head = { next: firstNode };
	let currentNode = head;

	while (twoNodesFollow(currentNode)) {
		if (twoDuplicatesFollow(currentNode)) {
			const secondOfTheDuplicates = currentNode.next.next;
			currentNode.next = getNextDistinctNode(secondOfTheDuplicates) || null;
		} else {
			currentNode = currentNode.next;
		}
	}

	return head.next;
}

function twoNodesFollow(node) {
	const bothNodesExist = node && node.next && node.next.next;
	return bothNodesExist;
}

function twoDuplicatesFollow(node) {
	const nextValue = node.next.val;
	const nextNextValue = node.next.next.val;
	return nextValue === nextNextValue;
}

function getNextDistinctNode(node) {
	let currentNode = node;
	const duplicateValue = node.val;

	while (true) {
		const isNull = currentNode === null;
		const distinctNodeFound = currentNode && currentNode.val !== duplicateValue;

		if (isNull) return undefined;
		else if (distinctNodeFound) return currentNode;
		else currentNode = currentNode.next;
	}
}
