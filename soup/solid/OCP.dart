// Принцип открытости/закрытости в Dart
// FALSE
// class Shape {
//   final double width;
//   final double height;
//
//   Shape(this.width, this.height);
//
//   double get area => width * height;
// }
// Этот класс нарушает принцип открытости/закрытости, потому что он не открыт для расширения новыми формами. Если мы захотим добавить поддержку новых форм, нам придется модифицировать класс Shape.
// Чтобы следовать принципу открытости/закрытости, мы можем сделать класс Shape абстрактным и определить общий интерфейс для всех форм:
// TRUE
// abstract class Shape {
//   double get area;
// }
// 
// class Rectangle implements Shape {
//   final double width;
//   final double height;
// 
//   Rectangle(this.width, this.height);
// 
//   @override
//   double get area => width * height;
// }
// 
// class Circle implements Shape {
//   final double radius;
// 
//   Circle(this.radius);
// 
//   @override
//   double get area => circleArea(radius);
// }
// 
// class Triangle implements Shape {
//   final double base;
//   final double height;
// 
//   Triangle(this.base, this.height);
// 
//   @override
//   double get area => triangleArea(base, height);
// }