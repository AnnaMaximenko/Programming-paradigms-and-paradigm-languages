let numbers = [1, 3, 57, 4, 2, 4];

function sort_imp(numbers) {
  for (let index = 1; index < numbers.length; index++) {
    let number = numbers[index];
    position = index;
    while (position > 0 && numbers[position - 1] < number) {
      numbers[position] = numbers[position - 1];
      position -= 1;
    }
    numbers[position] = number;
  }
  return numbers;
}

function sort_dec(numbers) {
  numbers.sort((a, b) => b - a);
  return numbers;
}

console.log(sort_imp(numbers));
console.log(sort_dec(numbers));
