# 参考资料
* [w3school](http://www.w3school.com.cn)
# 发展历史


# 基本概念
* 注释。单行注释用//, 多行注释用 /* */
* 在JS中用分号分割语句，但分号是可选的，用换行符也是可以的，但最好用分号。

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
  - 声明方法1：
    var person={firstname:"Bill", lastname:"Gates", id:5566};   
  - 声明方法2：
    var person={};
    person.firstname = "Bill";
    person.lastname = "Gates";
    person.id = 5566;
  - 引用方法1：
    name = person.lastname;
  - 引用方法2：
    name = person["lastname"];
  - 声明对象变量
  var x = new Number;
  var person = new Object;
  var carname = new String;
  
* Null
  cars = null; // 表示清空变量
* Undefined
  - 表示变量不含值
# 流程控制
# 函数

# 类/对象
# 常用库
# 浏览器环境

# 非浏览器环境
# 调试工具
