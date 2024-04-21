abstract class Animal {
  void speak();
}

class Dog extends Animal {
  @override
  void speak() {
    print('Гав!');
  }
}

class Cat extends Animal {
  @override
  void speak() {
    print('Мяу!');
  }
}

void main() {
  // Создаем объекты классов Dog и Cat
  Dog dog = Dog();
  Cat cat = Cat();

  // Заставляем объекты издавать звук
  dog.speak(); // Гав!
  cat.speak(); // Мяу!
}
