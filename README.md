# py-obj-model

# Inheritance 体系

![Image.tiff](https://res.craft.do/user/full/ef363a0d-96e2-ce0d-d615-edb486d8a754/doc/4F3CC9C6-45D3-496F-A3A0-30E989B7058F/72BBE61F-A8DD-4938-A927-4BD6FAA30370_2/JsogQW5y5SIBosuP53W8ETB4dig6ROrPUmukRDFFf7kz/Image.tiff)

# Method-Based Model VS. Attribute-Based Model

在这个上下文中，方法指的是对象的行为，而属性则指的是对象的状态。基于方法的模型将方法调用视为程序执行的基本操作，而基于属性的模型将方法调用分成查找属性和调用结果两个步骤。

在基于方法的模型中，程序员定义对象的方法（或函数），然后通过调用这些方法来执行程序。例如，Python和JavaScript就是基于方法的编程语言，我们可以定义一个方法，然后通过调用这个方法来执行程序。

在基于属性的模型中，程序员定义对象的属性和值，然后通过查找这些属性来执行程序。这种模型通常用于描述数据结构和数据对象。例如，JSON就是一种基于属性的语言，我们可以定义一个对象，并指定该对象的属性和值。

在这段话中，作者将Smalltalk、Ruby和JavaScript归为基于方法的模型，而将Python和Lua归为基于属性的模型。这是因为Smalltalk、Ruby和JavaScript都是面向对象编程语言，这些语言强调对象的行为和方法调用，而Python和Lua则更注重对象的状态和属性。

总之，基于方法的模型和基于属性的模型是两种不同的编程范式，它们可以用于描述不同类型的程序。在实际编程中，程序员可以根据具体的应用场景选择适合的模型和语言。

## 但是Javascript中也可以实现类似基于属性的模型的方法调用吧？

是的，JavaScript中也可以实现一些基于属性的方式来进行方法调用。在JavaScript中，对象的方法实际上是对象的属性，它们可以被赋值、被传递给其他函数或对象，也可以通过对象属性的访问方式来调用。

例如，假设我们有一个名为`person`的对象，它有一个`name`属性和一个`greet`方法：

```javascript
const person = {
  name: "Alice",
  greet: function() {
    console.log("Hello, my name is " + this.name);
  }
};
```

我们可以通过以下方式来调用`greet`方法：

```javascript
person.greet(); // 输出：Hello, my name is Alice
```

这里的`person.greet()`实际上是通过访问`person`对象的`greet`属性来调用`greet`方法。在JavaScript中，对象属性可以是任意类型，包括函数，因此我们可以通过属性访问方式来调用对象的方法。

然而，与基于属性的模型不同，JavaScript中的方法调用仍然是通过函数调用来实现的。在JavaScript中，函数是一等公民，它们可以赋值、传递和返回，因此JavaScript中的方法调用更侧重于函数的语义和行为，而不是属性的查找和调用。

