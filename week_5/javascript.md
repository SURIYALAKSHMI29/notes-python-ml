# JavaScript Notes

## Table of Contents
- [Events](#events)
- [Variables](#variables)
- [QuerySelector](#queryselector)
- [addEventListener](#addeventlistener)
- [Arrow Functions](#arrow-functions)
- [Intervals](#intervals)
- [Local Storage](#local-storage)
- [Small Features & Tips](#small-features--tips)
  - [Autofocus](#autofocus)
  - [Template Literals (String Literals)](#template-literals-string-literals)
  - [dataset](#dataset)

---

# Events

- JavaScript → Event-Driven programming
- Detection of events and actions that should be taken when an event is detected
- *EventListeners* → wait for certain events to occur, and then execute some code

```jsx
<button onclick="func()">Click Here</button>
````

* Whenever the button is clicked, the function func() is called

# Variables

### var

* Function-scoped or globally scoped (not block-scoped)
* Can be re-declared and updated
* Variables declared with *var* are hoisted(moved to the top) and **initialized as undefined**

  * only declarations are hoisted, not initializations (assignments)

  ```jsx
  console.log(name);    // undefined
  var name = "Suriya"; 

  // the above code is actually executed as,
  var name;   // Declared at the top
  console.log(name);
  name = "Suriya"
  ```

### let

* used to define a variable that is limited in scope to the current block such as function or loop
* Cannot be updated
* Hoisted, but not initialized with anything. Will get a reference error

```jsx
console.log(name);    // ReferenceError
let name = "Suriya";
```

### const

* used to define a value that will not change
* Hoisted, but not initialized (given a memory value)

# QuerySelector

### document.querySelector

* function searches for and return first element of the DOM (Document Object Model) that matches a given selector

* **Syntax**

  ```jsx
  document.querySelector(selector);
  ```

* If no matches found returns *null*

### document.querySelectorAll

* Returns all matching elements as a NodeList(like array)
* **Syntax**

  ```jsx
  document.querySelectorAll(selector)
  ```

```jsx
// multiple selectors
elements = document.querySelectorAll("h1, h2, .title");
```

> *selector* → .class, #id, tag or can even be a multiple selectors

# addEventListener

* Used to attach an event and function to an element

* **Syntax**

  ```jsx
  element.addEventListener(event, function);
  ```

* Takes 2 arguments

  * event → the event to listen for
  * function → the function to run when the event occurs

* Example

  ```jsx
  document.addEventListener('DOMContentLoaded', function() {
  	const button = document.querySelector('button');
  	button.onclick = count;   // attach function
  });
  ```

* Attached DOMContentLoaded event to the document → sometimes script runs even before the document is loaded which may results in element not found state

# Arrow Functions

* A shorter way to write functions in JavaScript

* Introduced in ES6 (ECMAScript 2015)

* Uses the **⇒** (arrow) syntax

  ```jsx
  (params) => {}
  ```

* No parentheses needed for a single parameter and No {} or return needed, if the value is returned implicitly

  ```jsx
  const square = x => x * x;
  console.log(square(5)); // 25
  ```

* Multiple Statements and Multiple parameters

  ```jsx
  const multiple = (a,b) => {
  	const c = a*b
  	return c;
  }
  multiple(2, 5); // returns 10
  ```

# Intervals

* Allows to run a function repeatedly at a specified time delay
* Implemented using the *setInterval()* function
* **Syntax**

  ```jsx
  let intervalId = setInterval(function, delayInMilliseconds);
  ```

  * *function* → the function to execute repeatedly
  * *delayInMilliseconds* → time between executions in ms (1000ms = 1 second)
  * *intervalId →* returned ID used to stop the interval later
* *clearInterval(intervalId)* stops the repeating execution

  * Must store the returned ID from *setInterval()* to clear it

```jsx
const intervalId = setInterval(() => {
    document.getElementById("counter").innerHTML += "<p>Hello</p>";
    no_of_times--;

    if(no_of_times==0){
        clearInterval(intervalId);
        submitButton.disabled = false;
    }
}, 1000);
```

# Local Storage

* When site is reloaded → all the information will be lost
* To store information on the user’s browser → Local storage can be used
* Information is stored as key-value pairs (similar to python dictionary)
* *localStorage.getItem(key)*: This function searches for an entry in local storage with a given key, and returns the value associated with that key.
* *localStorage.setItem(key, value)*:This function sets and entry in local storage, associating the key with a new value.

# Small Features & Tips

## Autofocus

* Automatically places the **cursor** inside an input field when the page loads
* Used inside the <input> or <textarea> elements in HTML

```jsx
<input type="text" id="name" placeholder="Enter your name" autofocus>
```

* When the page loads, the text cursor will be inside this input, ready for typing
* Only one element can have *autofocus* per page

## Template Literals (String Literals)

* Used for: Creating strings with variables or expressions easily and useful for multi-line strings
* **Syntax:** backticks(`) instead of quotes, and ${} for variables

## dataset

* A way to store custom data on HTML elements
* In HTML: Add custom attributes that start with *data-*

  * Attributes are completely valid HTML
  * e.g: data-color="red"
* In JavaScript: Access these attributes through the element’s .dataset object

  * converts kebab-case into camelCase in js
  * e.g: element.dataset.color.

```jsx
<div data-user-id="123"></div>

div.dataset.userId; // "123"
```
