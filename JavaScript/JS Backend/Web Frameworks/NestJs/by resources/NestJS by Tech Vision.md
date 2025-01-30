

reffered {

https://youtu.be/IdsBwplQAMw

https://youtu.be/2gtiffE3__U

}


### Nest JS

NestJS makes building robust applications straightforward by enforcing a structured, scalable  architecture with easy to test & decoupled code.

### **Misconception About NestJS**

Many believe **NestJS is only for building APIs**, but it actually supports three types of applications:

1. **HTTP Servers** – Use `NestFactory.create()` to build APIs and web servers with request endpoints.
2. **Microservices** – Use `NestFactory.createMicroservice()`, supporting protocols like TCP, NATS, and more for inter-service communication.
3. **Standalone Applications** – Use `NestFactory.createApplicationContext()` to build apps without network listeners, ideal for CLI tools and scheduled tasks.

Regardless of the type, **every NestJS app requires a root module**.


---


### **Creating a NestJS App**



With **Nest CLI**, you can rapidly set up and build your application, following best practices from the start.

#### **Step-by-Step Guide to Create a NestJS App:**

1. **Install Nest CLI Globally:** To get started, install the **Nest CLI** globally using npm:
    
    ```bash
    npm install -g @nestjs/cli
    ```
    
2. **Create a New Nest Application:** Once the CLI is installed, you can generate a new application using the `new` command:
    
    ```bash
    nest new podcast-app
    ```
    
    This will create a new directory with a NestJS app scaffold.
    
3. **Run the Application in Development Mode:** To start the app and begin working on it in development mode, use the following:
    
    ```bash
    cd podcast-app
    npm run start:dev
    ```
    
    The application will start on `localhost:3000`, and if you visit this URL, you'll receive a "Hello World" response.
    
4. **What Does the Generated Code Look Like?** The generated app includes a `main.ts` file, which is where the Nest app is created and the application starts listening on port 3000:
    
    ```typescript
    import { NestFactory } from '@nestjs/core';
    import { AppModule } from './app.module';
    
    async function bootstrap() {
      const app = await NestFactory.create(AppModule);
      await app.listen(3000);
    }
    bootstrap();
    ```
    
5. **App Module:** The **AppModule** is the root module of the application. Here's an example of the basic AppModule structure:
    
    ```typescript
    import { Module } from '@nestjs/common';
    
    @Module({
      imports: [],
      controllers: [],
      providers: [],
    })
    export class AppModule {}
    ```
    
    - The `@Module()` decorator defines the module.
    - The `imports` array is where you include other modules.
    - The `controllers` array is where you list your route handlers.
    - The `providers` array is where you define classes that can be injected as dependencies.
6. **NestJS Secret Weapon: The CLI:**
    
    - **Nest CLI** provides a lot of utility, such as creating modules, controllers, providers, and even test files with one simple command.
    - You can generate a new module with:
        
        ```bash
        nest generate module podcast
        ```
        
    - You can generate a controller:
        
        ```bash
        nest generate controller podcast
        ```
        

---


### **Modules in NestJS**

NestJS promotes a **modular architecture** that ensures scalability, maintainability, and separation of concerns. The framework encourages you to structure your code into **modules**, each encapsulating a specific set of features or domain.

#### **Root Module**

Every NestJS application has a **single root module**, typically called `AppModule`. This module is responsible for bootstrapping the entire application.

#### **Creating Modules**

Modules can be created using the **Nest CLI**. For example, running `nest generate module episode` creates an `episode` module. Similarly, you can generate other modules like `topics` and `config`.

```bash
nest generate module episode
```

#### **Module Dependencies**

Modules can **import** other modules. In the `AppModule`, all the generated modules (e.g., `EpisodeModule`, `TopicsModule`, `ConfigModule`) are listed in the `imports` array.

If you remove a module from this array, it’s no longer part of the application graph. However, you can import it into other modules to make it part of your app again.

```typescript
@Module({
  imports: [EpisodeModule, TopicsModule, ConfigModule],  // Root module imports others
  controllers: [],
  providers: [],
})
export class AppModule {}
```

#### **Modular Application Graph**

The `imports` array defines how modules are organized and interconnected in your application. For instance, if `ConfigModule` is imported into both `EpisodeModule` and `TopicsModule`, it becomes a shared module between them.

By structuring your app this way, you ensure that each module has a **clear responsibility**, making your app easier to scale and maintain.

This modular approach helps in organizing features efficiently, keeping your codebase **clean, flexible**, and **extensible**.

### **Modules in NestJS**

Modules are the **building blocks** of a NestJS application. You can visualize a Nest app as a **graph of interconnected modules**, with a **root module** at the top.

Each module can depend on other modules, forming a structured architecture. For example:

- A **Product Module**
- An **Order Module** (which depends on Cart & Payment Modules)
- A **Shared Config Module** used across the app


![[../_imgs/Pasted image 20250130084338.png]]


![[../_imgs/Pasted image 20250130084402.png]]


#### **Key Characteristics of Modules:**

✅ **Defined as a Class** – Annotated with `@Module()` decorator  
✅ **Encapsulates Features** – Groups related providers, controllers & services  
✅ **Encourages Reusability** – Modules can be imported into other modules  
✅ **Improves Maintainability** – Promotes a scalable and modular architecture


---

### **Decorators in NestJS**

### **Understanding Decorators in NestJS**

Decorators are a key concept in **NestJS**, enabling the framework's flexibility and structure. At first, they may seem like magic, but they are simply **functions** that modify the behavior of classes, methods, or even method parameters. Decorators in NestJS are widely used to annotate classes and define their roles.

#### **What Are Decorators?**

A decorator is a **special function** that adds extra functionality to a **class**, **method**, or **parameter**. They are applied using the `@` symbol and can take **additional parameters** to control their behavior.

#### **Key Points About Decorators:**

- **Functions** that modify the behavior of the entity they are applied to.
- Can be applied to **classes**, **methods**, and **method parameters**.
- **Accept additional parameters** to customize their functionality.

#### **Example: Module Decorator**

In the `AppModule`, the **@Module** decorator is used to define a module. It is applied to the class to tell NestJS that this class is a module, and it configures how it behaves by taking a configuration object.

```typescript
import { Module } from '@nestjs/common';

@Module({
  imports: [],         // other modules imported into this module
  controllers: [],     // the controllers used in this module
  providers: [],       // services or providers used in this module
})
export class AppModule {}
```

- **@Module()** is a decorator that configures the `AppModule` by passing an object to it.
- The `imports`, `controllers`, and `providers` properties define relationships between modules, route handlers, and services.

#### **What Does This Mean?**

Decorators help **NestJS organize and structure your code** by providing metadata, which tells Nest how to manage dependencies, request handling, and module composition. They make the code **clear, modular, and easy to test**.



#### **What is a Decorator?**

A **decorator** is a **special function** that can be attached to:

- **Classes** (`@Module()`, `@Injectable()`)
- **Methods** (`@Get()`, `@Post()`)
- **Properties** (e.g., injecting dependencies)

It **modifies behavior** and **adds metadata** to the element it decorates.

#### **Think of Decorators Like Suits & Accessories**

A **plain class** is like a person in casual clothes. Adding a `@Module()` decorator is like **dressing it in a suit**, enabling it to **interact with other decorated classes** in the application module graph.

#### **Defining Relationships with Decorators**

Modules rely on **decorators**, a core concept in NestJS (and TypeScript), which allows defining metadata for classes. 

- Modules relate to each other via the `imports` array inside `@Module()`.
- Controllers and Providers are also defined inside modules using decorators.



---

### **Controllers in NestJS**

Controllers in NestJS are responsible for **handling incoming requests** and returning appropriate responses. Each controller is a class decorated with the `@Controller` decorator.

#### **Creating Controllers**

You can generate a controller using the Nest CLI:

```bash
nest generate controller episode
```

This command creates a controller file and adds it to the `EpisodeModule`. The generated controller manages a root path (e.g., `/episode`).

#### **Handling Requests**

Controllers contain methods decorated with HTTP method decorators like `@Get()`, `@Post()`, `@Put()`, etc. For example, to handle a GET request:

```typescript
@Get('featured')
findFeatured() {
  return 'Featured episodes';
}
```

Each method can also handle **URL parameters** (e.g., episode ID), **query parameters**, **request bodies**, or the entire request object using decorators like `@Param()`, `@Query()`, `@Body()`, and `@Req()`.

#### **Example: Handling URL Parameters**

To handle a GET request with a URL parameter:

```typescript
@Get(':id')
findById(@Param('id') id: string) {
  return `Episode with ID: ${id}`;
}
```

#### **Customizing Routes**

You can define custom routes for specific actions (e.g., `/episode/featured`), and NestJS does the routing for you. The controller methods are decorated with specific decorators that map to HTTP methods.

#### **Delegating Logic to Services**

Instead of returning mock data, controllers should delegate business logic to **services**, which are part of the **NestJS provider system**. This keeps controllers lightweight and focused on request handling.


### **Controllers in NestJS**

Controllers are the **entry point** for handling incoming requests. Think of them as wearing a **blue jacket** (watchman)—responsible for directing requests and returning responses.

#### **Key Features of Controllers:**

✅ **Defined with `@Controller()`** – Specifies a root path for the controller  
✅ **Handles HTTP Requests** – Methods inside the controller use HTTP verb decorators like `@Get()`, `@Post()`, `@Put()`, etc.  
✅ **Defines Routes** – Each method can take a sub-route as a parameter  
✅ **Delegates Business Logic** – Controllers **shouldn’t contain business logic**; instead, they delegate it to services
Controllers **only handle requests and responses**—everything else is passed to **services**

#### **Example:**

```typescript
@Controller('products')  
export class ProductController {  
  @Get()  
  getAllProducts() {  
    return 'Returning all products';  
  }  

  @Post()  
  createProduct() {  
    return 'Creating a new product';  
  }  
}
```

* we can also create custom decorators on our own

----

**Providers in NestJS**

- **Overview**: In NestJS, _providers_ are classes that can be injected into other components like controllers or services. They serve as a backbone for functionality such as business logic, data fetching, or utility functions.
    
- **Using the `@Injectable()` Decorator**: The `@Injectable()` decorator is used to define a class as a provider, making it available for dependency injection. This allows it to be injected wherever it's needed in other classes, like controllers or other services.
    
    ```typescript
    import { Injectable } from '@nestjs/common';
    
    @Injectable()
    export class EpisodeService {
      // Service logic here
    }
    ```
    
- **Generating Providers Using Nest CLI**: You can create services (which are providers) using the Nest CLI. To generate a service, use the following command:
    
    ```bash
    nest generate service episode
    ```
    
    This command creates the `episode.service.ts` file, the corresponding test file, and automatically adds the service to the `providers` array in the module.
    
- **Incorporating Providers into Modules**: Once a provider is generated, it must be registered in the module’s `providers` array to make it accessible within the module. If you add the provider manually, ensure it's correctly listed in the `providers` array.
    
    ```typescript
    import { Module } from '@nestjs/common';
    import { EpisodeService } from './episode.service';
    
    @Module({
      providers: [EpisodeService],
    })
    export class EpisodeModule {}
    ```
    
- **Service Example**: A typical service might look like this. It could contain methods like `findAll()`, `findFeatured()`, `findOne()`, and `create()`. These methods manage the business logic, typically interacting with a database or in-memory data.
    
    ```typescript
    import { Injectable } from '@nestjs/common';
    
    @Injectable()
    export class EpisodeService {
      private episodes = [
        { id: 1, title: 'Episode 1', featured: true },
        { id: 2, title: 'Episode 2', featured: false },
      ];
    
      async findAll() {
        return this.episodes;
      }
    
      async findFeatured() {
        return this.episodes.filter(episode => episode.featured);
      }
    
      async findOne(id: number) {
        return this.episodes.find(episode => episode.id === id);
      }
    
      async create(createEpisodeDto: CreateEpisodeDto) {
        const newEpisode = { id: Date.now(), ...createEpisodeDto };
        this.episodes.push(newEpisode);
        return newEpisode;
      }
    }
    ```
    
    In this case, the `create()` method takes a `CreateEpisodeDto` (a Data Transfer Object) to define the shape of the incoming data.
    
- **Asynchronous Methods**: Although the methods in the above example are not interacting with a database, they are marked as `async`. In a real-world application, you would typically make these methods asynchronous to interact with a database.
    
    ```typescript
    async findAll() {
      // Normally, here you'd fetch data from a database
      return this.episodes;
    }
    ```
    
- **DTOs (Data Transfer Objects)**: When receiving data, methods like `create()` often require a DTO to define the expected structure. A `CreateEpisodeDto` might look like this:
    
    ```typescript
    export class CreateEpisodeDto {
      readonly title: string;
      readonly featured: boolean;
    }
    ```
    
    In the `EpisodeService`, this DTO ensures that incoming data matches the structure and types expected by the application, providing a validation layer.
    


This approach ensures that services encapsulate core business logic, and by leveraging dependency injection, you can easily reuse them across various parts of your application, keeping your code modular and maintainable.
### **Providers in NestJS**

Providers are the **core of business logic** in NestJS. They are simply **classes that can be injected** into other classes as dependencies.

#### **Key Features of Providers:**

✅ **Defined with `@Injectable()`** – Marks a class as a provider  
✅ **Encapsulates Business Logic** – Keeps controllers clean by handling data processing  
✅ **Uses Dependency Injection (DI)** – Automatically injected where needed  
✅ **Follows the Singleton Pattern** – A single instance is shared across the application

#### **How It Works:**

1. **Create a Service (Provider)**

```typescript
@Injectable()
export class UserService {
  getUsers() {
    return ['John', 'Jane', 'Doe'];
  }
}
```

2. **Register It in a Module**

```typescript
@Module({
  providers: [UserService],
  exports: [UserService] // Allows other modules to use it
})
export class UserModule {}
```

3. **Inject It into a Controller**

* Controller inject done in constructor

```typescript
@Controller('users')
export class UserController {
  constructor(private readonly userService: UserService) {}

  @Get()
  getUsers() {
    return this.userService.getUsers();
  }
}
```

Think of **providers as skilled freelancers**, and **NestJS as an agency** that places them wherever they’re needed. By using providers, you're leveraging **Dependency Injection** and the **Singleton pattern** for better maintainability and testability.



---

### Dependency Injection

**Dependency Injection in NestJS**

- **What is Dependency Injection (DI)?**
    
    - Dependency Injection is a design pattern used to manage the dependencies of objects. Instead of creating instances of dependencies inside a class, you let an external source (NestJS in this case) manage the instantiation and injection of dependencies.
- **How DI Works in NestJS:**
    
    1. **Create a Provider**: In NestJS, a provider is a class decorated with the `@Injectable()` decorator. Providers can be injected into other classes (e.g., controllers or other services).
    2. **Declare the Provider in a Module**: The provider must be added to the `providers` array in the module. This makes it available to be injected into other components within the module.
    3. **Inject the Provider into a Class**: To inject a provider into a class, add it as a constructor parameter, and NestJS will handle the injection automatically at runtime.
    
    ```typescript
    import { Injectable } from '@nestjs/common';
    
    @Injectable()
    export class EpisodeService {
      // Methods to manage episodes
    }
    
    @Controller('episode')
    export class EpisodeController {
      constructor(private readonly episodeService: EpisodeService) {}
    }
    
    ```
    
- **Example Walkthrough**:
    
    - You have an `EpisodeController` that needs to use the `EpisodeService` class. Instead of manually creating an instance of `EpisodeService` in the controller, NestJS injects it automatically at runtime.
    - To tell NestJS to inject the service into the controller, you simply define the constructor like this:
    
    ```typescript
    constructor(private readonly episodeService: EpisodeService) {}
    ```
    
    NestJS will create an instance of `EpisodeService` and inject it into the `episodeService` parameter.
    
- **Injecting Services from Other Modules**:
    
    - If you need to inject a service from another module (e.g., a `ConfigService` from a `ConfigModule`), you will:
        1. Create the service in the new module.
        2. Export the service from the module.
        3. Import the module containing the service into the current module.
        4. Inject the service into your class as usual.
    
    Example of creating and injecting a `ConfigService`:
    
    1. **Generate ConfigService** using CLI:
        
        ```bash
        nest g service config
        ```
        
    2. **Modify the `ConfigModule`**:
        
        ```typescript
        @Module({
          providers: [ConfigService],
          exports: [ConfigService],  // Exporting the service
        })
        export class ConfigModule {}
        ```
        
    3. **Inject `ConfigService` into `EpisodeController`**:
        
        ```typescript
        import { ConfigService } from './config.service';
        
        @Controller('episodes')
        export class EpisodeController {
          constructor(
            private readonly episodeService: EpisodeService,
            private readonly configService: ConfigService
          ) {}
        }
        ```
        
    4. **Ensure `EpisodeModule` Imports `ConfigModule`**:
        
        ```typescript
        @Module({
          imports: [ConfigModule],  // Importing the config module
          controllers: [EpisodeController],
          providers: [EpisodeService],
        })
        export class EpisodeModule {}
        ```
        
- **Benefits of Dependency Injection**:
    
    - It ensures **clean code** by decoupling classes from the logic of creating their dependencies.
    - Makes it easier to **swap out implementations** of dependencies (e.g., switching between in-memory and database storage).
    - Encourages **modular architecture** by promoting reusable, maintainable components.
    - **Easier testing** as you can mock dependencies when testing components.

---

This pattern of Dependency Injection not only simplifies the code structure but also makes it easy to manage and test the components in your application.





---


![[../_imgs/Pasted image 20250130091415.png]]



### **Middleware in NestJS**

Middleware acts like an **airport security checkpoint** for incoming requests—it processes them before they reach controllers.

#### **How Middleware Works:**

1. **Intercepts Requests** before they reach a route handler.
2. **Performs Preprocessing**, such as:
    - Logging requests
    - Authentication checks
    - Modifying request objects
    - Validating input
3. **Passes Control** to the next middleware or the controller.

#### **Example Middleware for Logging Requests:**

```typescript
@Injectable()
export class LoggerMiddleware implements NestMiddleware {
  use(req: Request, res: Response, next: NextFunction) {
    console.log(`Request... ${req.method} ${req.url}`);
    next(); // Pass control to the next handler
  }
}
```

#### **Applying Middleware in a Module:**

```typescript
export class AppModule implements NestModule {
  configure(consumer: MiddlewareConsumer) {
    consumer.apply(LoggerMiddleware).forRoutes('users');
  }
}
```

#### **Key Takeaways:**

✅ **Middleware runs before controllers**  
✅ **Can be applied globally or to specific routes**  
✅ **Used for logging, authentication, and request transformations**  
✅ **Avoid unnecessary middleware—NestJS provides built-in tools for request handling**


---


### Guards

**Guards in NestJS**

1. **Purpose of Guards**:
    
    - Guards are used for **access control** in NestJS applications. They are typically used to protect routes from unauthorized access, such as ensuring that only authenticated users can access specific resources.
    - A guard is a class with the `@Injectable()` decorator and implements the `CanActivate` interface.
2. **Implementing a Guard**:
    
    - The guard must implement the `canActivate()` method, which decides if a request should be allowed or rejected.
    - The `canActivate()` method receives an **execution context** that can be used to extract the `request` object and other relevant properties to perform checks (e.g., validate headers or check for valid tokens).
3. **Basic Guard Example**:
    
    - A simple guard that checks for a valid API key in the request header:
        
        ```typescript
        import { Injectable, CanActivate, ExecutionContext } from '@nestjs/common';
        import { Observable } from 'rxjs';
        
        @Injectable()
        export class ApiKeyGuard implements CanActivate {
          canActivate(
            context: ExecutionContext,
          ): boolean | Promise<boolean> | Observable<boolean> {
            const request = context.switchToHttp().getRequest();
            const apiKey = request.headers['x-api-key'];
        
            // If API key is valid, grant access, otherwise reject
            return apiKey === 'valid-api-key'; 
          }
        }
        ```
        
4. **Applying Guards**:
    
    - Guards can be applied to **entire controllers** or **individual route handlers**.
    - To apply a guard to a whole controller, use the `@UseGuards()` decorator on the controller class:
        
        ```typescript
        @UseGuards(ApiKeyGuard)
        @Controller('episodes')
        export class EpisodesController {
          // All routes in this controller will require the API key
        }
        ```
        
5. **Applying Guards to Specific Handlers**:
    
    - You can also apply a guard to specific route handlers if you only want to restrict access to certain endpoints:
        
        ```typescript
        @Controller('episodes')
        export class EpisodesController {
          @Post()
          @UseGuards(ApiKeyGuard)
          create() {
            // Only this route will require the API key
          }
        }
        ```
        
6. **Outcome**:
    
    - Once the guard is applied, requests to the protected routes will be checked. If the request does not meet the guard’s condition (e.g., no valid API key), the request will be rejected, and the client will receive an error response.
7. **Advanced Authentication**:
    
    - For more complex use cases like implementing an entire authentication flow, including user login, token issuance, and route protection, NestJS provides several utilities to build and secure authentication mechanisms.

In summary, guards offer a simple but effective way to handle authentication and authorization in NestJS. They can be applied at various levels, from entire controllers to specific route handlers, and help ensure only valid requests are processed.


### **Guards in NestJS**

Guards are **security checkpoints** in the request lifecycle, determining whether a request can proceed based on specific conditions like authentication, roles, or custom logic.

#### **How Guards Work:**

1. **Intercept Requests** before they reach the controller.
2. **Inspect the Execution Context** to check user roles, authentication, etc.
3. **Return `true` or `false`** to allow or deny access.

#### **Example: Authentication Guard**

```typescript
@Injectable()
export class AuthGuard implements CanActivate {
  canActivate(context: ExecutionContext): boolean {
    const request = context.switchToHttp().getRequest();
    return request.headers.authorization === 'valid-token'; // Example logic
  }
}
```

#### **Applying a Guard to a Route:**

```typescript
@Controller('profile')
@UseGuards(AuthGuard)
export class ProfileController {
  @Get()
  getProfile() {
    return 'User profile data';
  }
}
```

#### **Key Takeaways:**

✅ **Guards decide if a request is allowed or denied**  
✅ **Executed before the route handler**  
✅ **Can be applied globally, at the controller, or method level**  
✅ **Used for authentication, role-based access, or any custom logic**


---


### **Interceptors in NestJS**

Interceptors are **powerful middleware-like components** that run **before and after** a request reaches the route handler, giving full control over the **request-response lifecycle**.

#### **What Can Interceptors Do?**

✅ **Modify requests before they reach the handler**  
✅ **Transform responses before sending them to the client**  
✅ **Handle logging, caching, or response mapping**  
✅ **Measure execution time for performance monitoring**

#### **Example: Logging Interceptor**

```typescript
@Injectable()
export class LoggingInterceptor implements NestInterceptor {
  intercept(context: ExecutionContext, next: CallHandler): Observable<any> {
    console.log('Before handling request...');
    const now = Date.now();
    
    return next.handle().pipe(
      tap(() => console.log(`After... ${Date.now() - now}ms`))
    );
  }
}
```

#### **Applying an Interceptor to a Controller:**

```typescript
@Controller('users')
@UseInterceptors(LoggingInterceptor)
export class UserController {
  @Get()
  getUsers() {
    return ['John', 'Jane', 'Doe'];
  }
}
```

#### **Key Takeaways:**

✅ **Runs both before & after the request handler**  
✅ **Can modify or transform requests & responses**  
✅ **Useful for logging, caching, and performance tracking**  
✅ **Applied globally, per controller, or per route**


---

### **Pipes in NestJS**

1. **Purpose of Pipes**:
    
    - Pipes in NestJS are used to **validate** or **transform** incoming data before it is handed over to the route handler.
    - They help ensure the data is in the expected format and meet necessary criteria, preventing errors from entering the handler logic.
2. **Built-in Pipes**:
    
    - **Validation Example**:
        - Use the `ParseIntPipe` to validate that a query parameter is an integer.
        - Example:
            
            ```typescript
            @Get()
            findAll(@Query('limit', ParseIntPipe) limit: number) {
              // limit will be validated as integer
            }
            ```
            
    - **Transformation Example**:
        - Use `DefaultValuePipe` to set a default value if a parameter is missing.
        - Example:
            
            ```typescript
            @Get()
            findAll(@Query('limit', new DefaultValuePipe(10)) limit: number) {
              // limit will default to 10 if not provided
            }
            ```
            
3. **Custom Pipes**:
    
    - If built-in pipes don't meet your needs, you can create custom pipes by implementing the `PipeTransform` interface.
    - **Custom Pipe Example**: A pipe that ensures a number is strictly positive:
        
        ```typescript
        import { PipeTransform, Injectable, BadRequestException } from '@nestjs/common';
        
        @Injectable()
        export class IsStrictlyPositivePipe implements PipeTransform {
          transform(value: any) {
            if (value <= 0) {
              throw new BadRequestException('Value must be strictly positive');
            }
            return value;
          }
        }
        ```
        
    - You can use this custom pipe like so:
        
        ```typescript
        @Get()
        findAll(@Query('limit', IsStrictlyPositivePipe) limit: number) {
          // will validate that 'limit' is positive
        }
        ```
        
4. **Validation with DTOs**:
    
    - DTOs (Data Transfer Objects) allow you to structure incoming data, and you can apply validation rules to them using the `class-validator` package.
    - Install the necessary libraries:
        
        ```bash
        npm install class-validator class-transformer
        ```
        
    - **Example DTO with Validation**:
        
        ```typescript
        import { IsString, IsOptional, IsBoolean, IsDate } from 'class-validator';
        import { Type } from 'class-transformer';
        
        export class CreateEpisodeDto {
          @IsString()
          name: string;
        
          @IsBoolean()
          @IsOptional()
          featured: boolean;
        
          @IsDate()
          @Type(() => Date)
          publishedAt: Date;
        }
        ```
        
    - **Controller with Validation Pipe**:
        
        ```typescript
        @Post()
        create(@Body(ValidationPipe) createEpisodeDto: CreateEpisodeDto) {
          // automatically validates using class-validator decorators
        }
        ```
        
5. **Date Transformation**:
    
    - If you send a `date` as a string, you can transform it into a JavaScript `Date` object using the `@Transform` decorator from `class-transformer`.
    - Example of transforming a date string into a `Date` instance:
        
        ```typescript
        @IsDate()
        @Transform(({ value }) => new Date(value))
        publishedAt: Date;
        ```
        
6. **Rejecting Invalid Requests**:
    
    - Pipes can be used to prevent requests from being processed if the validation fails.
    - **Example**: If the client sends a `publishedAt` property with the wrong format or missing, you can reject the request early by using a combination of validation and transformation.

By leveraging pipes, NestJS ensures that data is correctly validated and transformed before it reaches the business logic, making the code more robust and secure.

### **Pipes in NestJS**

Pipes are **data validation and transformation tools** that process incoming request data **before it reaches the route handler**.

#### **What Do Pipes Do?**

✅ **Validate incoming data** to ensure it meets expected rules  
✅ **Transform data types** (e.g., convert strings to numbers)  
✅ **Throw exceptions if data is invalid**, preventing handler execution

#### **Example: Using a Built-in Validation Pipe**

```typescript
@Controller('users')
export class UserController {
  @Get(':id')
  getUser(@Param('id', ParseIntPipe) id: number) {
    return `User ID: ${id}`;
  }
}
```

🛠️ Here, `ParseIntPipe` ensures that the `id` is always converted to a number.

#### **Creating a Custom Pipe**

```typescript
@Injectable()
export class ToUpperCasePipe implements PipeTransform {
  transform(value: any) {
    return typeof value === 'string' ? value.toUpperCase() : value;
  }
}
```

Applying it to a route:

```typescript
@Get()
getUser(@Query('name', ToUpperCasePipe) name: string) {
  return `User: ${name}`;
}
```

#### **Built-in Pipes in NestJS:**

🔹 `ValidationPipe` – Validates DTOs using class-validator  
🔹 `ParseIntPipe` – Converts strings to numbers  
🔹 `ParseUUIDPipe` – Ensures valid UUID format  
🔹 `DefaultValuePipe` – Assigns a default value if none is provided
etc.. 
#### **Key Takeaways:**

✅ **Pipes ensure data integrity before it reaches the controller**  
✅ **They prevent invalid data from breaking the app**  
✅ **NestJS provides built-in pipes, but you can create custom ones**


---

### Error and Exceptions


**Error Handling in NestJS**

1. **Default Error Response**:
    
    - NestJS automatically returns a 500 Internal Server Error if there’s an unhandled error during the request processing.
    - This behavior is helpful, but it’s often not enough for good user experience.
2. **Custom Error Handling**:
    
    - NestJS offers built-in support for better error handling with HTTP exceptions.
    - You can use the `HttpException` class to throw custom errors with messages and status codes.
    - You can use  predefined exceptions like:
        - `NotFoundException` (404)
        - `ForbiddenException` (403)
        - `UnauthorizedException` (401)
3. **Usage of HTTP Exceptions/ PredifnedExceptions**:
    
    - When throwing an exception like `NotFoundException`, NestJS automatically converts the error into a structured JSON response with the correct HTTP status.
    
    **Example**:
    
    ```typescript
    import { HttpException, NotFoundException } from '@nestjs/common';
    
    throw new NotFoundException('Episode not found');
    throw new HttpException('Episode not found', HttpStatus.NOT_FOUND);
    ```
    
    This would return a JSON response with:
    
    ```json
    {
      "statusCode": 404,
      "message": "Episode not found",
      "error": "Not Found"
    }
    ```
    
4. **Customizing Error Handling**:
    
    - You can customize how errors are handled globally using **exception filters**.
    - Exception filters allow you to modify the response before it reaches the client, making it possible to return custom error formats or log errors in specific ways.
    
    **Example** (Creating a custom exception filter):
    
    ```typescript
    import { ExceptionFilter, Catch, ArgumentsHost } from '@nestjs/common';
    import { Response } from 'express';
    
    @Catch()
    export class AllExceptionsFilter implements ExceptionFilter {
      catch(exception: any, host: ArgumentsHost) {
        const response = host.switchToHttp().getResponse<Response>();
        const status = exception.getStatus();
        response
          .status(status)
          .json({
            statusCode: status,
            message: exception.message,
            error: exception.name,
          });
      }
    }
    ```
    
5. **Advanced Customization**:
    
    - Beyond standard HTTP exceptions, NestJS allows deep customization. You can hook into the request lifecycle to perform actions before or after route handlers are executed.
    - This gives you flexibility in how errors are handled across the entire application.
6. **NestJS Flexibility**:
    
    - While NestJS provides useful default behaviors (e.g., HTTP exceptions), it’s also extremely flexible, allowing you to implement custom behavior for error handling, logging, and response formatting based on specific needs.

By leveraging these built-in mechanisms and customizing them using exception filters, you can enhance the error handling in your NestJS applications, ensuring better communication with the frontend and more robust backend error management.


### **Exception Filters in NestJS**

Exception filters are classes that allow **centralized handling of errors** throughout the application, ensuring consistent and secure error responses.

#### **How Exception Filters Work:**

1. **Catch exceptions** thrown by any part of the request handling process—**guards, interceptors, pipes, or route handlers**.
2. **Define custom error handling** to ensure consistent responses and avoid exposing sensitive information.

#### **Creating a Custom Exception Filter:**

```typescript
@Catch(HttpException)
export class HttpExceptionFilter implements ExceptionFilter {
  catch(exception: HttpException, host: ArgumentsHost) {
    const response = host.switchToHttp().getResponse<Response>();
    const status = exception.getStatus();
    const message = exception.message;

    response.status(status).json({
      statusCode: status,
      message: message,
      timestamp: new Date().toISOString(),
    });
  }
}
```

#### **Applying the Exception Filter Globally:**

```typescript
import { AppModule } from './app.module';

async function bootstrap() {
  const app = await NestFactory.create(AppModule);
  app.useGlobalFilters(new HttpExceptionFilter());
  await app.listen(3000);
}
bootstrap();
```

#### **Benefits of Exception Filters:**

✅ **Centralized Error Handling** – Consistently manage errors across the app  
✅ **Customizable Responses** – Tailor error responses to fit your needs  
✅ **Security** – Prevent the leakage of sensitive details in error messages

In conclusion, exception filters provide a robust way to handle and log errors while maintaining **stability and security** in your app, ensuring **clean and consistent error messaging** for clients.


---

### Tests in Nest js

**Testing in NestJS**

1. **Generated Test Files**:
    
    - NestJS CLI generates test files for components like controllers and services. These files are ready to be populated with relevant tests for your application logic.
2. **Testing Controller**:
    
    - Nest provides testing utilities to create a module for testing purposes.
    - The initial test code checks if the wiring is happening correctly, but it might fail since the module doesn’t know how to inject the services (like the `EpisodeService` or `ConfigService`).
    
    **Example**:
    
    ```typescript
    import { Test, TestingModule } from '@nestjs/testing';
    import { EpisodeController } from './episode.controller';
    import { EpisodeService } from './episode.service';
    
    describe('EpisodeController', () => {
      let controller: EpisodeController;
      let service: EpisodeService;
    
      beforeEach(async () => {
        const module: TestingModule = await Test.createTestingModule({
          controllers: [EpisodeController],
          providers: [EpisodeService],
        }).compile();
    
        controller = module.get<EpisodeController>(EpisodeController);
        service = module.get<EpisodeService>(EpisodeService);
      });
    
      it('should be defined', () => {
        expect(controller).toBeDefined();
      });
    });
    ```
    
3. **Mocking Services for Tests**:
    
    - Instead of using the actual service, you can mock the provider. This allows you to simulate the service behavior without the need for real implementations.
    
    **Example**:
    
    ```typescript
    const mockEpisodeService = {
      findOne: jest.fn().mockResolvedValue({ id: 1, title: 'Episode 1' }),
    };
    
    const module: TestingModule = await Test.createTestingModule({
      controllers: [EpisodeController],
      providers: [
        {
          provide: EpisodeService,
          useValue: mockEpisodeService,
        },
      ],
    }).compile();
    ```
    
4. **Testing the Controller Handlers**:
    
    - After mocking the services, you can test controller methods, ensuring that the controller behaves as expected.
    
    **Example**:
    
    ```typescript
    it('should return an episode when found', async () => {
      const result = await controller.findOne(1);
      expect(result).toEqual({ id: 1, title: 'Episode 1' });
      expect(mockEpisodeService.findOne).toHaveBeenCalledWith(1);
    });
    ```
    
5. **Testing Negative Scenarios**:
    
    - You can also test negative scenarios, like when a service method returns `null` or throws an error.
    - Mocking the return value of the service to `null` helps simulate the case where an episode is not found, and you can ensure that the controller handles errors appropriately.
    
    **Example**:
    
    ```typescript
    it('should throw an error if episode is not found', async () => {
      mockEpisodeService.findOne.mockResolvedValue(null);
      try {
        await controller.findOne(999);
      } catch (e) {
        expect(e).toBeInstanceOf(Error);
        expect(e.message).toBe('Episode not found');
      }
    });
    ```
    
6. **Benefits of Dependency Injection for Testing**:
    
    - DI improves testability by allowing you to isolate components and control what is injected into them, which makes unit testing easier.
    - You can swap out real service implementations with mock objects, giving you full control over the dependencies during tests.
7. **Error Handling and Response**:
    
    - When an error is thrown in a request handler, you should ensure that it returns a useful error response to the client.
    - NestJS provides mechanisms to handle errors gracefully, which you can explore further by using built-in error handling or custom exception filters to provide meaningful error messages in the response.


This structured approach to testing ensures that each part of your NestJS application can be tested in isolation, with mock dependencies, and also allows you to handle both positive and negative test cases effectively.

---

### Error handling in NestJS

