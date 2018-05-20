var ceiling = prompt("Enter ceiling number", "1000");

function* range(start, end) {
	for (let i = start; i <= end; i++) {
		yield i;
	}
}

var values = [for (i of range(1, ceiling)) if (i % 3 === 0 || i % 5 === 0) i];

console.log(values.reduce(
