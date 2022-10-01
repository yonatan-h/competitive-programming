var evalRPN = function (tokens) {
	return evaluate(tokens);
};

function evaluate(tokens) {
	const stack = [];
	for (let token of tokens) {
		if (isOperator(token)) {
			const operator = token;
			const secondOperand = stack.pop();
			const firstOperand = stack.pop();

			const result = operate(operator, firstOperand, secondOperand);
			stack.push(result);
		} else {
			stack.push(token);
		}
	}

	return stack[0];
}

function isOperator(token) {
	return token === "+" || token === "-" || token === "*" || token === "/";
}

function operate(operand, num1, num2) {
	//convert to integers
	num1 = +num1;
	num2 = +num2;

	//operate
	if (operand === "+") return num1 + num2;
	else if (operand === "-") return num1 - num2;
	else if (operand === "*") return num1 * num2;
	else if (operand === "/") return Math.trunc(num1 / num2);
}
