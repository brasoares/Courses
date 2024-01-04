// If there is only one parameter for the function: just leave out the parenthesis, if necessary (preference, readability and so on might influence in such a decision):

// Traditional:
function isPositive(number) {
  return number >= 0
}

// Single parameter way with an arrow function:
const isPositive = number => {
  return number >= 0
}

// As seen on: https://blog.webdevsimplified.com/2020-09/arrow-functions/
