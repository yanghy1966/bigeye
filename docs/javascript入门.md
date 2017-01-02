# 参考资料
* [w3school](http://www.w3school.com.cn)
* [廖雪峰](http://www.liaoxuefeng.com/wiki/001434446689867b27157e896e74d51a89c25cc8b43bdb3000)
# 发展历史
- 诞生 于1995年
- 被ECMA-262所规范（语言核心）。它和Web浏览器没有任何关系
- DOM是一种宿主环境，Node和Adobe Flash都是它的一种实现
- 该语言的主要目的是描述DOM，提供API接口。当然也用来做服务器，如NODE
- 该语言的另一个作用是描述浏览器BOM

# 基本概念
* 注释。单行注释用//, 多行注释用 /* */
* 在JS中用分号分割语句，但分号是可选的，用换行符也是可以的，但最好用分号。
* 严格模式
  'use strict'; // 放在脚本第一行，可避免吴用全局变量
  
# 变量
* 变量声明。一般用var, 没有var表示全局变量。

 ```javascript
    var x = 2;
    global = 10;
 ```
 * 大小写敏感。
 * 变量名可用$，_符号
 * 一条语句可以声明多个变量，以逗号分隔。也可以横跨多行：
 
 ```javascript
    var name="Gates",
    age=56,
    job="CEO";
 ```
  
# 数据类型。具有动态类型
* 字符串
  使用单引号或双引号。字符串中可以嵌套引号
* 数字 
  只有一种数字类型，即浮点数。
* 布尔
   true，false
* 数组

- 声明方法1：
    var cars = new Array();
    cars[0] = "audi";
    cars[1] = "BMW";

- 声明方法2：
  
    var cars = new Array("audi","BMW");
- 声明 方法3：
    var cars = ["audo","BMW"];

- 声明方法4：
    var cars = [];
    cars.push('audo');
    cars.push('BMW');
    
* 对象

 - 由{}包括起来的代码块。里面由name:value来定义。应用十分广泛。
 - JS中，所有事物都是对象，字符串，数字，日期等。
 - JS中对象是拥有属性和方法的数据
  
 - 声明方法1：
    var person={firstname:"Bill", lastname:"Gates", id:5566};   
    
 - 声明方法2：
    var person={};
    person.firstname = "Bill";
    person.lastname = "Gates";
    person.id = 5566;
    person.sayhi = function(){console.log('hi'};
    
 - 引用方法1：
    name = person.lastname;
    
 - 引用方法2：
  
    name = person["lastname"];
    
 - 创建对象变量
  
  var x = new Number;
  var person = new Object;
  var carname = new String;
  
 -  创建对象
   
  
* Null
  cars = null; // 表示清空变量
* Undefined
- 表示变量不含值
  
# 流程控制
* if
  if ... else if ... else
  
* for
  for(var i = 0; i< cars.length ; i++){}
  for ( x in persion){ ... } // x是索引而不是具体元素
  for(var x of a){...} //遍历映射和集合，ES6新特性
  forEach()
  
  ```javascript
    var a = ['A', 'B', 'C'];
    a.forEach(function (element, index, array) {
    // element: 指向当前元素的值
    // index: 指向当前索引
    // array: 指向Array对象本身
    alert(element);
    });
  ```
  
* switch
  switch(n){ case1: ... break; ... default: ...}
  
* while
  while(...){...}

* do
  do{...}while( i< 5)
  
* break 跳出一层循环
* continue
* label
  label：语句
  label：{...}
  
* try/catch
  try{} catch(err) {}

* throw
  throw err

# Map映射
  JavaScript的对象有个小问题，就是键必须是字符串。但实际上Number或者其他数据类型作为键也是非常合理的。
  为了解决这个问题，最新的ES6规范引入了新的数据类型Map

  ```javascript
    var m = new Map([['Michael', 95], ['Bob', 75], ['Tracy', 85]]);
    m.get('Michael'); // 95
  ```
  初始化Map
  
  ```javascript
    var m = new Map(); // 空Map
    m.set('Adam', 67); // 添加新的key-value
    m.set('Bob', 59);
    m.has('Adam'); // 是否存在key 'Adam': true
    m.get('Adam'); // 67
    m.delete('Adam'); // 删除key 'Adam'
    m.get('Adam'); // undefined
  ```

# Set集合
   Set和Map类似，但不存在重复的键值
   var s = new Set([1,2,3,'4']);
   s.add(5); // 添加元素
   s.delete(3);

# iterable
   ES6引入的新类型，用于遍历Map,Set,Array

```javascript   
   var a = ['A', 'B', 'C'];
   var s = new Set(['A', 'B', 'C']);
   var m = new Map([[1, 'x'], [2, 'y'], [3, 'z']]);
   for (var x of a) { // 遍历Array
     alert(x);
   }
   for (var x of s) { // 遍历Set
     alert(x);
   }
  for (var x of m) { // 遍历Map
     alert(x[0] + '=' + x[1]);
  }
```

# 函数

* 函数内部可以定义函数

* 有名函数定义
  function abc(x){ ... ; return ...}
* arguments
  函数内部有一个变量叫arguments,并且它永远指向函数传入的所有参数
  
  ```javascript
   function foo(x) {
     alert(x); // 10
     for (var i=0; i<arguments.length; i++) {
         alert(arguments[i]); // 10, 20, 30
     }
   }
   foo(10, 20, 30);
  ```
  * rest参数. ES6支持

 ```javascript
  function foo(a, b, ...rest) {
    console.log('a = ' + a);
    console.log('b = ' + b);
    console.log(rest);
  }

  foo(1, 2, 3, 4, 5);
  // 结果:
  // a = 1
  // b = 2
  // Array [ 3, 4, 5 ]

  foo(1);
  // 结果:
  // a = 1
  // b = undefined
  // Array [] 

 ```
   
* 匿名函数


* 变量作用域
  - 变量提升
  JavaScript的函数定义有个特点，它会先扫描整个函数体的语句，把所有申明的变量“提升”到函数顶部：
  
  ```javascript
  'use strict';

  function foo() {
    var x = 'Hello, ' + y;
    alert(x);
    var y = 'Bob';
  }

  foo();
  
  ```
  - 全局作用域
    JavaScript默认有一个全局对象window，全局作用域的变量实际上被绑定到window的一个属性
    由于函数定义有两种方式，以变量方式var foo = function () {}定义的函数实际上也是一个全局变量，因此，顶层函数的定义也被视为一个全局   变量，并绑定到window对象：
  
  - 名字空间
  ```javascript
    // 唯一的全局变量MYAPP:
    var MYAPP = {};

    // 其他变量:
    MYAPP.name = 'myapp';
    MYAPP.version = 1.0;

    // 其他函数:
    MYAPP.foo = function () {
    return 'foo';
    };
  
  ```
  - let 申明块级作用域.ES6支持
  
  ```javascript
   'use strict';

   function foo() {
     var sum = 0;
     for (let i=0; i<100; i++) {
        sum += i;
     }
     i += 1; // SyntaxError
   }
  ```
  
* 方法
- 可以 在对象中绑定方法，也就是函数. 但在内部有this关键字。
  JavaScript的函数内部如果调用了this，那么这个this到底指向谁？
  答案是，视情况而定！
   如果以对象的方法形式调用，比如xiaoming.age()，该函数的this指向被调用的对象，也就是xiaoming，这是符合我们预期的。
   如果单独调用函数，比如getAge()，此时，该函数的this指向全局对象，也就是window。
   要指定函数的this指向哪个对象，可以用函数本身的apply方法，它接收两个参数，第一个参数就是需要绑定的this变量，第二个参数是Array，表    示函数本身的参数。

```javascript
   var xiaoming = {
      name: '小明',
      birth: 1990,
      age: function () {
          var y = new Date().getFullYear();
          return y - this.birth;
      }
  };
  
  xiaoming.age; // function xiaoming.age()
  xiaoming.age(); // 今年调用是25,明年调用就变成26了
  
```
* apply
  
```javascript
function getAge() {
    var y = new Date().getFullYear();
    return y - this.birth;
}

var xiaoming = {
    name: '小明',
    birth: 1990,
    age: getAge
};

xiaoming.age(); // 25
getAge.apply(xiaoming, []); // 25, this指向xiaoming, 参数为空

```

* 高阶函数
  一个函数可以接收另一个函数作为参数，这种函数就称之为高阶函数。
  
  ```javascript
  function add(x, y, f) {
    return f(x) + f(y);
  }
  
  ```
* map函数

```javascript
  function pow(x) {
    return x * x;
  }

  var arr = [1, 2, 3, 4, 5, 6, 7, 8, 9];
  arr.map(pow); // [1, 4, 9, 16, 25, 36, 49, 64, 81]

```

* reduce
再看reduce的用法。Array的reduce()把一个函数作用在这个Array的[x1, x2, x3...]上，这个函数必须接收两个参数，reduce()把结果继续和序列的下一个元素做累积计算，其效果就是：

[x1, x2, x3, x4].reduce(f) = f(f(f(x1, x2), x3), x4)


* filter
filter也是一个常用的操作，它用于把Array的某些元素过滤掉，然后返回剩下的元素。

```javascript
  var arr = [1, 2, 4, 5, 6, 9, 10, 15];
  var r = arr.filter(function (x) {
    return x % 2 !== 0;
  });
  arr; // [1, 5, 9, 15]

```

* 回调函数
filter()接收的回调函数，其实可以有多个参数。通常我们仅使用第一个参数，表示Array的某个元素。回调函数还可以接收另外两个参数，表示元素的位置和数组本身：

```javascript
  var arr = ['A', 'B', 'C'];
  var r = arr.filter(function (element, index, self) {
      console.log(element); // 依次打印'A', 'B', 'C'
      console.log(index); // 依次打印0, 1, 2
      console.log(self); // self就是变量arr
      return true;
  });
  
```




* sort排序
```javascript
  var arr = [10, 20, 1, 2];
  arr.sort(function (x, y) {
      if (x < y) {
          return -1;
      }
      if (x > y) {
          return 1;
      }
      return 0;
  }); // [1, 2, 10, 20]

```

* 闭包
  把函数作为返回值
  高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。
  
  ```javascript
    function lazy_sum(arr) {
    var sum = function () {
        return arr.reduce(function (x, y) {
            return x + y;
        });
    }
    return sum;
  }
    
  ```
  var f = lazy_sum([1, 2, 3, 4, 5]); // function sum()
  f(); // 15
  
  注意到返回的函数在其定义内部引用了局部变量arr，所以，当一个函数返回了一个函数后，其内部的局部变量还被新函数引用，所以，闭包用起来简单，实现起来可不容易。
  
  
  
  
* 箭头函数
箭头函数相当于匿名函数，并且简化了函数定义。箭头函数有两种格式，一种像上面的，只包含一个表达式，连{ ... }和return都省略掉了。还有一种可以包含多条语句，这时候就不能省略{ ... }和return：


* generator 产生器

```javascript
  function* fib(max) {
    var
        t,
        a = 0,
        b = 1,
        n = 1;
    while (n < max) {
        yield a;
        t = a + b;
        a = b;
        b = t;
        n ++;
    }
    return a;
  }
  
  fib(5); // fib {[[GeneratorStatus]]: "suspended", [[GeneratorReceiver]]: Window}
```
直接调用一个generator和调用函数不一样，fib(5)仅仅是创建了一个generator对象，还没有去执行它。

```javasript
  var f = fib(5);
f.next(); // {value: 0, done: false}
f.next(); // {value: 1, done: false}
f.next(); // {value: 1, done: false}
f.next(); // {value: 2, done: false}
f.next(); // {value: 3, done: true}

```

```javascript
  for (var x of fib(5)) {
    console.log(x); // 依次输出0, 1, 1, 2, 3
  }

```

因为generator可以在执行过程中多次返回，所以它看上去就像一个可以记住执行状态的函数，利用这一点，写一个generator就可以实现需要用面向对象才能实现的功能。例如，用一个对象来保存状态，得这么写：

```javascript
  var fib = {
    a: 0,
    b: 1,
    n: 0,
    max: 5,
    next: function () {
        var
            r = this.a,
            t = this.a + this.b;
        this.a = this.b;
        this.b = t;
        if (this.n < this.max) {
            this.n ++;
            return r;
        } else {
            return undefined;
        }
    }
  };

```

```javascript
  try {
    r1 = yield ajax('http://url-1', data1);
    r2 = yield ajax('http://url-2', data2);
    r3 = yield ajax('http://url-3', data3);
    success(r3);
  }
  catch (err) {
    handle(err);
  }

```

# 类/对象
# 常用库
# 浏览器环境DOM
* DOM文档对象模型，是对HTML的描述

  - DOM的最高节点是document变量，下面是html
  - html下面包括head和body
  
* DOM方法：

  - 添加（list.appendChild(js);insertBefore；）
  - 删除 （parent.removeChild(self)；）
  - 更新（1，p.innerHTML = 'ABC'; 2， p.innerText = '<script>alert("Hi")</script>'; 3，p.style.color = '#ff0000';）
  - 遍历
    
* 搜索方法

  - document.getElementById()和
  - document.getElementsByTagName()，以及CSS选择器
  - document.getElementsByClassName()。
  
* BOM浏览器对象模型

  - 提供和浏览器的接口
  - BOM的核心对象是window，全局变量都可以通过window.xxx来访问。
  - 用于描述窗口大小、位置、关系等
  
# 非浏览器环境
# 调试工具
