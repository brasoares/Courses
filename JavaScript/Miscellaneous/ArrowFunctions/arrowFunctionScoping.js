/* As seen on: https://blog.webdevsimplified.com/2020-09/arrow-functions/
* "Now we can talk about the real power of arrow functions which is how they handle scoping of the this keyword. 
* In a normal function the this keyword is scoped based on the context of where the function is called.
* Arrow functions on the other hand scope the this keyword based on where the function is defined which works more like other programming languages.
* Here is a quick example.
*/

class Person {
  constructor(name) {
    this.name = name
  }
}

printNameArrow() {
  setTimeout(() => {
   console.log('Arrow: ${this.name}') 
  }, 100)
}

printNameFunction() {
  setTimeout(function () {
    console.log('Function: ${this.name}')
  }, 100)
}

const person = new Person("Kyle")
person.printNameArrow()
// Arrow: Kyle
person.printNameFunction()
// Function: 
