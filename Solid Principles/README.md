# SOLID Principles using Python 3

Implementing a Sales application using the SOLID principles: Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, and Dependency Inversion. This repository is heavily inspired by [ArjanCodes's video](https://www.youtube.com/watch?v=pTB30aXS77U).

In short,
1. Single Responsibility<br />
    &nbsp;a module, class, or function must serve only one purpose.<br />
    &nbsp;&nbsp; &nbsp;&nbsp;e.g if you can extract functions within a function, then that means your function is capable of performing multiple duties

2. Open/Closed<br />
    &nbsp;Extend the functionality of an existing code, not refactor. <br />
    &nbsp;&nbsp; &nbsp;&nbsp;e.g. implement Abstract classes to specify methods needed by subclasses, then implement methods depending on the subclass's characteristic

3. Liskov Substitution<br />
   &nbsp;The ability of a subclass to perform actions of the super class without knowing the type of subclass.<br />
  &nbsp;&nbsp; &nbsp;&nbsp;e.g. Define a base class and methods that all of its subclasses have in common. 
         "If S is a subtype of T, then you should be able to substitute T with S."

4. Interface Segregation<br />
      &nbsp;Make interfaces (parent abstract classes) more specific, rather than generic.<br />
     &nbsp;&nbsp; &nbsp;&nbsp;e.g. Create more interfaces (classes) if needed and/or provide objects to constructors.

5. Dependency Inversion<br />
     &nbsp;Make classes depend on abstract classes rather than non-abstract classes.<br />
    &nbsp;&nbsp; &nbsp;&nbsp;e.g. Make classes inherit from abstract classes.
