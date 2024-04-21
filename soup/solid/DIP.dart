// Принцип инверсии зависимости в Dart
// 
// Вместо того чтобы классы зависели от конкретных реализаций, они должны зависеть от абстракций.
// class MySQLConnection {
//   void connect() {
//     // Реализация подключения к MySQL
//   }
// }
//
// class DatabaseManager {
//   final MySQLConnection connection;
//
//   DatabaseManager(this.connection);
//
//   void connect() {
//     connection.connect();
//   }
// }
// Если мы захотим изменить базу данных на PostgreSQL, нам придется изменить `DatabaseManager`. Вместо этого, мы можем создать абстрактный класс или интерфейс `DatabaseConnection`.
// abstract class DatabaseConnection {
//   void connect();
// }
//
// class MySQLConnection implements DatabaseConnection {
//   @override
//   void connect() {
//     // Реализация подключения к MySQL
//   }
// }
//
// class PostgreSQLConnection implements DatabaseConnection {
//   @override
//   void connect() {
//     // Реализация подключения к PostgreSQL
//   }
// }
//
// class DatabaseManager {
//   final DatabaseConnection connection;
//
//   DatabaseManager(this.connection);
//
//   void connect() {
//     connection.connect();
//   }
// }