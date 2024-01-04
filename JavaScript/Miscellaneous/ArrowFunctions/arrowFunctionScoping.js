/* As seen on: https://blog.webdevsimplified.com/2020-09/arrow-functions/
* "Now we can talk about the real power of arrow functions which is how they handle scoping of the this keyword. 
* In a normal function the this keyword is scoped based on the context of where the function is called.
* Arrow functions on the other hand scope the this keyword based on where the function is defined which works more like other programming languages.
* Here is a quick example.
*/

class Person {
  constructor(name) {
    this.name = name;
  }

  printNameArrow() {
    setTimeout(() => {
      console.log(`Arrow: ${this.name}`);
    }, 100);
  }

  printNameFunction() {
    setTimeout(function () {
      console.log(`Function: ${this.name}`);
    }, 100);
  }
}

const person = new Person("Kyle");
person.printNameArrow();    // Output: Arrow: Kyle
person.printNameFunction(); // Output: Function: undefined

/* GPT's explanation:
* In the printNameArrow method, an arrow function is used inside the setTimeout.
* Arrow functions do not bind their own this; instead, they inherit the this value from the enclosing execution context (in this case, the printNameArrow method).
* So, this.name refers to the name property of the Person instance, and you get the expected output "Arrow: Kyle".

* In contrast, in the printNameFunction method, a regular function is used inside the setTimeout.
* Regular functions, when used in this way, have their own this context, which is determined by how the function is called.
* In the context of the setTimeout callback, the this value is not the same as the Person instance, so this.name is undefined in this case.
*/
