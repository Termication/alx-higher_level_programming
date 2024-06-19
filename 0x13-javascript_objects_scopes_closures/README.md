# 0x13. JavaScript - Objects, Scopes and Closures

## Why JavaScript Programming is Amazing

JavaScript is one of the most popular and versatile programming languages in the world. It's the backbone of web development, enabling dynamic and interactive experiences on websites. Here are some reasons why JavaScript is amazing:

1. **Versatility**: JavaScript can be used for front-end, back-end (with Node.js), and even mobile app development.
2. **Community and Ecosystem**: A vast community and rich ecosystem of libraries and frameworks (like React, Angular, and Vue) make development faster and easier.
3. **Asynchronous Programming**: JavaScript's support for asynchronous programming through callbacks, promises, and async/await enhances performance and responsiveness.
4. **Event-Driven**: JavaScript is designed to handle events, making it ideal for creating interactive user interfaces.
5. **Easy to Learn**: JavaScript has a relatively low barrier to entry, making it accessible to beginners while still being powerful enough for experts.

## How to Create an Object in JavaScript

Creating an object in JavaScript can be done in several ways. Here are a few common methods:

### Using Object Literals

```javascript
let person = {
    name: 'John',
    age: 30,
    greet: function() {
        console.log('Hello, ' + this.name);
    }
};

## Using the new Keyword with a Constructor Function

```javascript

function Person(name, age) {
    this.name = name;
    this.age = age;
    this.greet = function() {
        console.log('Hello, ' + this.name);
    };
}

let person = new Person('John', 30);
```
## Using ES6 Classes

```javascript

class Person {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }

    greet() {
        console.log('Hello, ' + this.name);
    }
}

let person = new Person('John', 30);
```
**What this Means**

The this keyword in JavaScript refers to the object it belongs to. Its value depends on the context in which it is used:

    -Global Context: this refers to the global object (window in browsers).
    -Method Context: Inside a method, this refers to the owner object.
    -Function Context: In a function, this refers to the global object (or undefined in strict mode).
    -Arrow Functions: this retains the value from the enclosing lexical context.

### Example

```javascript

let person = {
    name: 'John',
    greet: function() {
        console.log('Hello, ' + this.name); // 'this' refers to the 'person' object
    }
};

person.greet();
```
### What undefined Means

undefined is a primitive value that indicates a variable has been declared but not yet assigned a value. It is also the default return value of functions that do not explicitly return a value.
Example

```javascript

let x;
console.log(x); // undefined

function doNothing() {}
console.log(doNothing()); // undefined
```
## Why Variable Type and Scope is Important

Understanding variable type and scope is crucial in JavaScript to avoid bugs and unexpected behavior.
### Variable Types

    -Primitive Types: String, Number, Boolean, Null, Undefined, Symbol, BigInt
    -Reference Types: Objects (including arrays and functions)

### Variable Scope

    -Global Scope: Variables declared outside any function are in the global scope.
    -Function Scope: Variables declared inside a function are local to that function.
    -Block Scope: Variables declared with let or const inside a block ({}) are only accessible within that block.

### Example

```javascript

let globalVar = 'I am global';

function scopeExample() {
    let localVar = 'I am local';
    console.log(globalVar); // Accessible
    console.log(localVar);  // Accessible
}

scopeExample();
console.log(localVar); // Uncaught ReferenceError: localVar is not defined
```
## What is a Closure

A closure is a function that has access to its own scope, the scope of the outer function, and the global scope. This allows for the creation of functions with private variables.
### Example

```javascript

function outerFunction(outerVariable) {
    return function innerFunction(innerVariable) {
        console.log('Outer Variable: ' + outerVariable);
        console.log('Inner Variable: ' + innerVariable);
    };
}

const closureExample = outerFunction('outside');
closureExample('inside');
```
## What is a Prototype

Prototypes are the mechanism by which JavaScript objects inherit features from one another. Every JavaScript object has a prototype, which is another object from which it inherits properties and methods.
Example

```javascript

function Person(name) {
    this.name = name;
}

Person.prototype.greet = function() {
    console.log('Hello, ' + this.name);
};

let person = new Person('John');
person.greet();
```
## How to Inherit an Object from Another

Inheritance in JavaScript can be achieved using prototypes or ES6 classes.
Using Prototypes

```javascript

function Animal(name) {
    this.name = name;
}

Animal.prototype.speak = function() {
    console.log(this.name + ' makes a noise.');
};

function Dog(name) {
    Animal.call(this, name);
}

Dog.prototype = Object.create(Animal.prototype);
Dog.prototype.constructor = Dog;

Dog.prototype.bark = function() {
    console.log(this.name + ' barks.');
};

let dog = new Dog('Rex');
dog.speak();
dog.bark();
```
### Using ES6 Classes

```javascript

class Animal {
    constructor(name) {
        this.name = name;
    }

    speak() {
        console.log(this.name + ' makes a noise.');
    }
}

class Dog extends Animal {
    bark() {
        console.log(this.name + ' barks.');
    }
}

let dog = new Dog('Rex');
dog.speak();
dog.bark();
```
