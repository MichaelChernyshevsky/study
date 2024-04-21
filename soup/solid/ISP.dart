// Принцип разделения интерфейсов в Dart
// FALSE
// abstract class Vehicle {
//   void startEngine();
//   void stopEngine();
//   void accelerate();
//   void brake();
//   void turnLeft();
//   void turnRight();
// }
// TRUE
// abstract class Vehicle {
//   void startEngine();
//   void stopEngine();
//   void accelerate();
//   void brake();
// }
//
// abstract class TurnableVehicle {
//   void turnLeft();
//   void turnRight();
// }