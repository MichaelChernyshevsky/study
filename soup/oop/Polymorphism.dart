abstract class Shape {
  void draw();
}

class Circle extends Shape {
  final double radius;

  Circle(this.radius);

  @override
  void draw() {
    print('Рисуем круг радиусом $radius');
  }
}

class Rectangle extends Shape {
  final double width;
  final double height;

  Rectangle(this.width, this.height);

  @override
  void draw() {
    print('Рисуем прямоугольник шириной $width и высотой $height');
  }
}

void main() {
  // Создаем объекты классов Circle и Rectangle
  Circle circle = Circle(10);
  Rectangle rectangle = Rectangle(20, 30);

  // Рисуем объекты
  circle.draw(); // Рисуем круг радиусом 10
  rectangle.draw(); // Рисуем прямоугольник шириной 20 и высотой 30
}
