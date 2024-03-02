---
title: "为什么函数返回对象时没有调用复制构造函数？"
date: 2020-09-30 15:07:02
categories: 
- "c++"
tags: 
- "c++"
---

### 1. 复制构造函数被调用的三种情况

1. 使用已有的对象创建新的对象。

   ```cpp
   A a1(a);
   A a2 = a;
   ```

2. 函数的参数类型是对象。

   ```cpp
   void func(A a);
   ```

3. 函数返回值的类型是对象。

   ```cpp
   A func();
   ```

### 2. 示例代码

```cpp
#include <iostream>

using namespace std;

class A {
public:
	A() { cout << "constructor" << endl; }
	~A() { cout << "destructor" << endl; }
	A(const A& a) { cout << "copy constructor" << endl; }
};

A func() {
	A a;
	cout << "func()" << endl;
	return a;
}

int main()
{
    A a = func();
	
	cout << "return" << endl;
	return 0;
}
```

运行结果为：

```
constructor		// A a = func()调用func中A a
func()
return			// main结束
destructor		// 析构a
```

而相较预期的结果少了`func()`返回值的临时对象的复制构造函数，和用函数返回值生成`A a`对象的复制构造函数。

### 3. 原因

产生这个问题的原因是编译器进行了返回值优化RVO，减少了不必要对象的构造，提高效率。

以下内容摘自[维基百科](https://zh.wikipedia.org/wiki/%E8%BF%94%E5%9B%9E%E5%80%BC%E4%BC%98%E5%8C%96)：

> **返回值优化**（Return value optimization，缩写为**RVO**）是C++的一项编译优化技术。即删除保持函数返回值的临时对象。这可能会省略两次复制构造函数，即使复制构造函数有副作用。

