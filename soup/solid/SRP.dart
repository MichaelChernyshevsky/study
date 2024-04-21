// Чтобы следовать принципу единственной ответственности, мы можем разделить класс Order на два класса:
//
// Order - класс для хранения информации об заказе.
// OrderProcessor - класс для обработки заказа.
// 
// class Order {
//   String id;
//   String customerName;
//   List<dynamic> products;
//   double totalPrice;
//   Order(
//       this.id, this.customerName, this.products, this.totalPrice);
// }
// 
// class OrderProcessor {
//   void process(Order order) {
//     // Обработать заказ
//   }
// }