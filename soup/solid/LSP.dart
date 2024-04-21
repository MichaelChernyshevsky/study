// Принцип подстановки Лисков в Dart
// class Animal {
//   void makeSound() {
//     // Издает звук
//   }
// }
// // Этот класс соответствует принципу подстановки Лисков, потому что любой объект типа Animal может использоваться в любом контексте, где используется объект типа Animal.
// // Например, мы можем создать функцию, которая принимает объект типа Animal:
// void makeAnimalSound(Animal animal) {
//   animal.makeSound();
// }
// FALSE
// class Animal {
//   void makeSound() {
//     // Издает звук
//   }
// }
// // 
// class Dog extends Animal {
//   void makeSound() {
//     // Издает звук собаки
//   }
// }
// // 
// class Cat extends Animal {
//   void makeSound() {
//     // Издает звук кошки
//   }
// }
// TRUE
// class Dog extends Animal {
//   @override
//   void makeSound() {
//     // Издает звук собаки
//   }

//   void bark() {
//     // Издает лай собаки
//   }
// }