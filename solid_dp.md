# SOLID Principles and Design Patterns in Pizza Restaurant

This document explains how the applied design patterns in the Pizza Restaurant project align with the SOLID principles. Each principle is discussed with examples and patterns used to maintain scalability, flexibility, and maintainability in the system.

## **Single Responsibility Principle (SRP)**

### **Definition**
A class should have one and only one reason to change, meaning it should have only one responsibility.

### **How it is Applied**
- **Factory Pattern**: Separates pizza creation logic, ensuring that each pizza class (e.g., `MargheritaPizza`, `PepperoniPizza`) is solely responsible for defining its own properties.
- **Decorator Pattern**: Ensures that the base `Pizza` class only defines core properties (e.g., name, base cost), while toppings (e.g., `CheeseTopping`, `OlivesTopping`) are managed independently.
- **InventoryManager (Singleton)**: Dedicated to inventory management tasks, like checking stock and decrementing quantities, without overlapping with order processing or payment logic.

## **Open-Closed Principle (OCP)**

### **Definition**
Software entities should be open for extension but closed for modification.

### **How it is Applied**
- **Decorator Pattern**: New toppings can be added as independent classes (e.g., `MushroomsTopping`) without modifying the existing base `Pizza` class or other topping implementations.
- **Strategy Pattern**: Adding new payment methods is as simple as creating a new subclass of `PaymentMethod` (e.g., `GooglePayPayment`) without altering the existing codebase.

## **Liskov Substitution Principle (LSP)**

### **Definition**
Objects of a superclass should be replaceable with objects of its subclass without breaking the application.

### **How it is Applied**
- **Factory Pattern**: Any subclass of `Pizza` (e.g., `MargheritaPizza`, `PepperoniPizza`) can be used interchangeably with the base `Pizza` type in the system.
- **Decorator Pattern**: Toppings like `CheeseTopping` or `OlivesTopping` are interchangeable and can wrap any `Pizza` object, preserving the functionality of the system.

**Example**: A `PepperoniPizza` object can replace a `Pizza` reference, and the system will still function correctly without any changes to the logic.

## **Interface Segregation Principle (ISP)**

### **Definition**
Clients should not be forced to depend on methods they do not use.

### **How it is Applied**
- **Strategy Pattern**: The `PaymentMethod` interface defines only the necessary method (`process_payment`) for payment processing. Subclasses like `PayPalPayment` and `CreditCardPayment` implement this method without any additional, irrelevant functionality.

### **Benefits**
This approach ensures that each payment class implements only the required behavior, avoiding bloated interfaces.

## **Dependency Inversion Principle (DIP)**

### **Definition**
High-level modules should not depend on low-level modules but on abstractions.

### **How it is Applied**
- **Strategy Pattern**: The `PaymentContext` class interacts with the abstract `PaymentMethod` interface rather than concrete payment implementations. This allows seamless integration of new payment methods (e.g., `BitcoinPayment`).
- **Singleton Pattern**: The `InventoryManager` is a singleton, ensuring that all parts of the system depend on a single instance, reducing tight coupling and ensuring consistency.

## **Conclusion**
By leveraging design patterns such as Factory, Decorator, Strategy, and Singleton, the Pizza Restaurant project adheres to the SOLID principles. This design approach ensures:

- **Maintainability**: Clear separation of concerns allows for easier debugging and updates.
- **Scalability**: New features can be added (e.g., new pizzas, toppings, or payment methods) with minimal changes to existing code.
- **Extensibility**: The system can adapt to future requirements without significant rewrites.

These principles collectively enhance the robustness and longevity of the system, making it easier to manage and extend as the business evolves.