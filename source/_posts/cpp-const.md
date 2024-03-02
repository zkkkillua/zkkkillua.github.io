---
title: "C++：const修饰符的常见用法"
date: 2020-09-30 10:09:10
categories: 
- "c++"
tags: 
- "c++"
---

### 1. const常量

```cpp
const int a = 10;
int const a = 10;

const int a;	// error 需要在创建时初始化
```

>  当以编译时初始化的方式定义一个const 对象时，编译器将在编译过程中把用到该变量的地方都替换成对应的值。
> 为了执行上述替换，编译器必须知道变量的初始值。
>
> 默认情况下， const 对象被设定为仅在文件内有效。
> 如果想只在一个文件中定义const，而在其他多个文件中声明并使用它。
>
> ```cpp
> // file_l.cc 定义并初始化了一个常量，该常量能被其他文件访问
> extern const int bufSize =fcn ();
> // file_l.h 头文件
> extern const int bufSize; // 与file_l.cc中定义的bufSize是同一个
> ```



### 2. const引用

const修饰引用表示不能通过引用修改值，如果引用的是常量，则引用必须也是const。

```cpp
int a = 10;
const int& r1 = a;		// const引用指向的可以不是常量，但是不能通过引用修改其值
int const & r2 = a;
int& const r3 = a;		// error 引用本身就不能修改指向，不需要再额外使用const修饰
```



### 3. const与指针

- 指向常量的指针：pointer to const

  ```cpp
  const int* p1 = &a;		// p1 is a pointer to int const
  int const* p2 = &a;		// p2 is a pointer to const int
  ```

  ```cpp
  const int a = 10;
  int b = 5;
  const int* p1 = &a;
  int const* p2 = &b;		// 指向常量的指针指向的可以不是常量，只是不能通过指针修改指向的值
  p1 = &b;				// 指向常量的指针可以改变指向
  ```

- 常量指针：const pointer

  ```cpp
  int* const p = &a;		// p is a const pointer to int
  ```
  
  ```cpp
  const int a = 10;
  int b = 5;
  int* const p1 = &a;			// error 常量只能被指向常量的指针指向
  const int* const p2 = &a;	// 指向常量的常量指针，既不能通过指针修改所指的值，也不能修改指向
  int* const p2 = &b;
  ```



### 4. const与普通函数

#### 4.1. const修饰返回值

##### 返回值是整型

const修饰返回值使得返回的是常量。

而常量的返回是受限的，比如如下代码的const是没有意义的：

```cpp
const int func(int a) {
	return a + 3;
}

int ret = func(3);		// ret == 6
ret = 5;				// ret == 5
```

虽然返回值类型是常量，但是因为被赋值给了其他的变量，所以返回值还是可以修改的（修改的是变量ret）。

##### 返回值是指向常量的指针

如果const修饰的返回值是指针类型，则结果有所不同。

```cpp
const int* func(int* p) {
	return p;
}

int a = 3;
// int *p = func(&a);		// error const int* -x> int*
const int *p = func(&a);
// *p = 5;					// error
```

##### 返回值为常量指针

同样，还有返回值类型为常量指针：

```cpp
int* const func(int* p) {
	return p;
}

int a = 3;
int *p = func(&a);
p = nullptr;
```

由于`int* const`限制的是返回的临时对象是常量指针，而常量指针是可以被赋值给其他非常量指针的，所以此处的const也没有作用。

##### 返回值为指向常量的引用

```cpp
const int& func(int& a) {
	return ++a;
}

int a = 3;
int &r = func(a);
// int& r = func(a);		// error const reference -x> reference
const int& r = func(a);		// r is a
```

返回值是指向常量的引用，不能传递给指向变量的引用。

#### 4.2. const修饰函数

const是可以修饰成员函数的，格式为`int A::func() const {}`，代表内部不会修改成员变量，可能修改静态成员变量，常对象仅能调用常成员函数。

而const是不能修饰普通的非类的成员的函数的，即没有`int func() const {}`的格式。

因为常成员函数的目的是避免修改成员变量，为常对象提供调用函数，而普通的函数如果想要避免修改其他变量，则在传入对象时规定为常量即可，所以不需要额外定义一种常函数。



### 5. const与成员函数

#### 5.1. const修饰返回值

同const修饰普通函数的返回值。

#### 5.2. const修饰成员函数（常成员函数）

```cpp
class A {
public:
	void func() const {
		// pval = 3;		// error
		// val = 3;			// error
		sval = 10;
	}
	int pval;
private:
	int val;
	static int sval;
};
int A::sval = 5;

int main()
{
	A a;
	a.func();				// sval = 10;

	return 0;
}
```

常成员函数无法修改成员变量，可以修改静态成员变量，无法调用非常成员函数，不论公有私有。

对象的this指针被声明为`A* const`类型，因此无法改变指向，在常成员函数中，this指针是`const A* const`类型，因此既无法改变指向，又无法改变this指针所指的值。

#### 5.3. const成员函数的重载

const是可以用于类成员函数的重载的。

非常量对象优先调用非常成员函数，常量对象只能调用常成员函数。

```cpp
class A {
public:
	void func() {
		cout << "func()" << endl;
	}
	void func() const {
		cout << "func() const" << endl;
	}
}

A a1;	a1.func();		// func();
const A a2;	a2.func();	// func() const;
```



### 6. constexpr

>C++ 11 新标准规定，允许将变量声明为constexpr类型以便由编译器来验证变量的值是否是一个常量表达式。

即声明为constexpr的变量和函数，代表它们是常量表达式，其值在编译期是可知的，用constexpr告知编译器可以进行优化。

而const是“只读”，不能被修改，编译器检查到修改const会直接报错。