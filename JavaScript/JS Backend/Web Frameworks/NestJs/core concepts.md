


### **2. Core Concepts**

- **Modules** – Organizing your app into feature modules
- **Controllers** – Handling incoming requests
- **Providers & Services** – Business logic layer
- **Dependency Injection** – How NestJS handles dependencies
- **Decorators** – Understanding `@Module()`, `@Injectable()`, `@Controller()`, etc.



### **2. Core Concepts of NestJS**

#### **1. Modules – Organizing Your App into Feature Modules**

- In NestJS, applications are **modular** by design.
- A **module** is a class annotated with `@Module()`, grouping related components (controllers, services, providers).
- Helps in organizing code, improving maintainability, and promoting reusability.
- Every NestJS app has a **root module (`AppModule`)**, and you can create feature modules using:
    
    ```sh
    nest g module users
    ```
    
- Example:
    
    ```ts
    @Module({
      imports: [],
      controllers: [UsersController],
      providers: [UsersService],
    })
    export class UsersModule {}
    ```
    

---

#### **2. Controllers – Handling Incoming Requests**

- Controllers handle incoming HTTP requests and define routes.
- Decorated with `@Controller()` and route handlers (`@Get()`, `@Post()`, etc.).
- Example:
    
    ```ts
    @Controller('users')
    export class UsersController {
      @Get()
      getAllUsers() {
        return 'Returning all users';
      }
    
      @Post()
      createUser(@Body() userData: any) {
        return `User ${userData.name} created!`;
      }
    }
    ```
    
- Controllers delegate business logic to **services/providers**.

---

#### **3. Providers & Services – Business Logic Layer**

- **Services** contain business logic and data-handling operations.
- Marked with `@Injectable()` to allow **dependency injection**.
- Registered inside `providers` array in a module.
- Example:
    
    ```ts
    @Injectable()
    export class UsersService {
      getUsers() {
        return [{ id: 1, name: 'John Doe' }];
      }
    }
    ```
    

---

#### **4. Dependency Injection – How NestJS Handles Dependencies**

- **Dependency Injection (DI)** is a design pattern where dependencies are **automatically injected** rather than being manually instantiated.
- Enhances testability, modularity, and maintainability.
- NestJS automatically resolves dependencies using the `providers` array in `@Module()`.
- Example:
    
    ```ts
    @Injectable()
    export class UsersService {
      constructor(private readonly databaseService: DatabaseService) {}
    }
    ```
    

---

#### **5. Decorators – Understanding `@Module()`, `@Injectable()`, `@Controller()`, etc.**

- **Decorators** are **metadata annotations** that NestJS uses to define components.
- Common decorators:
    
    |Decorator|Purpose|
    |---|---|
    |`@Module()`|Defines a module|
    |`@Injectable()`|Marks a class as a provider/service|
    |`@Controller()`|Defines a controller|
    |`@Get()`, `@Post()`|Maps HTTP routes to handler methods|
    |`@Body()`, `@Param()`|Extracts request data|
    

---

### **Key Takeaway for Interviews**

- **Modules** help organize an app into **reusable components**.
- **Controllers** handle **incoming HTTP requests**.
- **Providers/Services** contain **business logic** and are **injectable**.
- **Dependency Injection (DI)** improves **code reusability** and **testability**.
- **Decorators** define NestJS components and their behavior.

🔥 **Pro Tip:** Be ready to explain **how DI works**, **why modular architecture is useful**, and **difference between a controller and a provider**! 🚀


