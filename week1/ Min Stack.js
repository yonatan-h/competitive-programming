var MinStack = function () {
	this.minimum;
	this.list = [];
};

MinStack.prototype.isEmpty = function () {
	const lengthOfList = this.list.length;
	return lengthOfList === 0;
};

MinStack.prototype.getTopNode = function () {
	const lengthOfList = this.list.length;
	const topNode = this.list[lengthOfList - 1];
	return topNode;
};

MinStack.prototype.push = function (value) {
	let minValue;

	if (this.isEmpty()) {
		minValue = value;
	} else {
		const previousMinValue = this.getTopNode().minValue;
		if (value < previousMinValue) minValue = value;
		else minValue = previousMinValue;
	}

	const node = { minValue, value };
	this.list.push(node);
};

MinStack.prototype.pop = function () {
	const node = this.list.pop();
	return node.value;
};

MinStack.prototype.top = function () {
	const topNode = this.getTopNode();
	return topNode.value;
};

MinStack.prototype.getMin = function () {
	const topNode = this.getTopNode();
	return topNode.minValue;
};

//1hr
//one submission
const object = new MinStack();
object.push(100);
object.push(101);
object.push(0);
object.push(1);
object.getMin();
console.log(object.list);
