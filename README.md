# **Data Structures in Python: OOP and SOLID**

This repository contains implementations of data structures in Python, such as **Stack**, following **Object-Oriented Programming (OOP)** and **SOLID** principles to ensure the code is clean, modular, reusable, and scalable.

PS.: This repository is for study only, don't worry about overengineering

## **Main Objectives**
- **Apply Object-Oriented Programming (OOP)** principles such as encapsulation, inheritance, polymorphism, and composition.
- **Follow SOLID principles**, aiming for a well-structured, maintainable codebase.
- Implement popular data structures in a clear and efficient manner, including **Stack**, **Queue**, **Linked List**, and more.

## **Implemented Data Structures**
1. **Stack**
   - The stack follows the **LIFO (Last In, First Out)** principle, where the last element inserted is the first to be removed.
   - Implemented with a focus on **encapsulation**, **composition**, and **single responsibility**.

## **Applied Principles**

### **OOP Principles**
1. **Encapsulation**
   - All internal attributes are private (or protected) and can only be accessed or modified through specific methods (getters/setters).
   - Protects important data and prevents direct modification of attributes.

2. **Inheritance**
   - Inheritance is used to create classes that share common behaviors, reducing code redundancy.

3. **Polymorphism**
   - Methods with the same name but different behaviors are used to allow the code to be more flexible and reusable.

4. **Composition**
   - Instead of inheriting from other classes, classes contain other object instances to reuse functionalities and build more complex structures.

### **SOLID Principles**
1. **Single Responsibility Principle (SRP)**
   - Each class and method has a single responsibility, making it easier to maintain and avoiding mixed functionalities.

2. **Open for Extension, Closed for Modification (OCP)**
   - The code is open for extension but closed for modification. This is achieved with base classes and specific subclasses (e.g., Strategy design pattern).

3. **Liskov Substitution Principle (LSP)**
   - Derived classes can replace their base classes without altering the expected behavior, ensuring that subclasses do not break the system logic.

4. **Interface Segregation Principle (ISP)**
   - Smaller, more specific interfaces are preferred over large, generic interfaces, allowing classes to implement only the necessary methods.

5. **Dependency Inversion Principle (DIP)**
   - Dependencies are injected into classes rather than directly created, improving testability and flexibility.


## **Contributing**
Contributions are welcome! To suggest improvements or add new features:

1. Fork this repository.
2. Create a new branch (`git checkout -b my-new-feature`).
3. Make your changes and submit a pull request.

## **License**
This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for more details.

## Author

**Henrique Souza**