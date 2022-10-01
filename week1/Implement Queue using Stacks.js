function Stack() {
	this.array = [];
}
Stack.prototype.push = function (element) {
	this.array.push(element);
};
Stack.prototype.peek = function () {
	return this.array[this.size() - 1];
};
Stack.prototype.pop = function () {
	return this.array.pop();
};
Stack.prototype.size = function () {
	return this.array.length;
};
Stack.prototype.isEmpty = function () {
	return this.size() === 0;
};

var MyQueue = function () {
	this.mainStack = new Stack();
	this.helperStack = new Stack();
};

MyQueue.prototype.push = function (element) {
	this.mainStack.push(element);
};

MyQueue.prototype.loadElementsToHelperStack = function () {
	while (this.mainStack.size()) {
		const element = this.mainStack.pop();
		this.helperStack.push(element);
	}
};

MyQueue.prototype.returnElementsToMainStack = function () {
	while (this.helperStack.size()) {
		const element = this.helperStack.pop();
		this.mainStack.push(element);
	}
};

MyQueue.prototype.pop = function () {
	this.loadElementsToHelperStack();
	const topElementInHelperStack = this.helperStack.pop();
	this.returnElementsToMainStack();
	return topElementInHelperStack;
};

MyQueue.prototype.peek = function () {
	this.loadElementsToHelperStack();
	const topElementInHelperStack = this.helperStack.peek();
	this.returnElementsToMainStack();
	return topElementInHelperStack;
};

MyQueue.prototype.empty = function () {
	return this.mainStack.isEmpty();
};
