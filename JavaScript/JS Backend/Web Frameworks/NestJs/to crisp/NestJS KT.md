

## Intro:

* **progressive Node.js framework** for building efficient, scalable, and maintainable server-side applications.
* has built with TypeScript support, and inspired by Angular’s modular architecture & its dependency injection. 
* makes building robust applications straightforward by enforcing a structured, scalable architecture with easy to test & decoupled code.

## **Key Features** 

✅ **Modular Architecture** – Encourages separation of concerns using modules.  
✅ **Built-in Dependency Injection** – Improves code reusability and testability.  
✅ **Decorators@ & Metadata@(data)** – Uses TypeScript decorators (e.g., `@Controller()`, `@Injectable()`, `@Module()`).  
✅ **Express & Fastify Support** – Can be used with either Express.js or Fastify.  
✅ **Built-in Support for WebSockets, GraphQL, and Microservices**.  
✅ **Easy Integration with Databases** – Works well with TypeORM, Prisma, Sequelize, and Mongoose.  
✅ **Middleware & Guards** – Similar to Express middleware, but with added capabilities like Guards for authentication/authorization.  
✅ **Interceptors & Pipes** – Help in transforming and validating requests/responses.




---

### **Decorators in NestJS**

Decorators are **special functions** in NestJS that add **metadata** to classes, methods, and parameters, helping Nest manage dependencies, request handling, and module composition.

#### **1️⃣ What Are Decorators?**

✅ **Functions** that modify behavior.  
✅ Used on **classes** (`@Module()`), **methods** (`@Get()`), and **parameters**.  
✅ Enable **declarative programming** and **runtime reflection**.

#### **2️⃣ Example: Module Decorator**

```typescript
import { Module } from '@nestjs/common';

@Module({
  imports: [],        
  controllers: [],    
  providers: [],      
})
export class AppModule {}
```

- **`@Module()`** marks a class as a module and configures it.
- The `imports`, `controllers`, and `providers` define relationships.

#### **3️⃣ Example: Controller & Metadata**

```typescript
import { Controller, Get } from '@nestjs/common';

@Controller('users')  // Marks this as a controller for 'users' routes
export class UserController {
  @Get()  // Maps this method to a GET request
  getUsers() {
    return ['User1', 'User2'];
  }
}
```

#### **4️⃣ How Metadata Works?**

NestJS uses **Reflect Metadata** (`reflect-metadata` package) to store and retrieve metadata:

```typescript
import 'reflect-metadata';

class Example {
  @Reflect.metadata('role', 'admin')
  someMethod() {}
}

const role = Reflect.getMetadata('role', Example.prototype, 'someMethod');
console.log(role); // Output: "admin"
```

#### **5️⃣ Why Are Decorators Important?**

✅ Structure **controllers, services, and modules** efficiently.  
✅ Reduce **boilerplate code** by using metadata.  
✅ Enable **dependency injection, validation, and authorization**.

Decorators make NestJS highly **flexible, modular, and maintainable**! 🚀

---


### **Dependency Injection in NestJS**

**Dependency Injection (DI)** is a design pattern where dependencies are managed externally, allowing NestJS to inject them automatically.

#### **1️⃣ How DI Works in NestJS**

1. **Create a Provider** – A service class decorated with `@Injectable()`.
2. **Register in a Module** – Add it to the `providers` array.
3. **Inject into a Class** – Use the constructor to receive the dependency.

```typescript
@Injectable()
export class EpisodeService {
  // Service logic
}

@Controller('episode')
export class EpisodeController {
  constructor(private readonly episodeService: EpisodeService) {}
}
```

#### **2️⃣ Injecting Services Across Modules**

To inject a service from another module:

1. **Export** the service in its module:
    
    ```typescript
    @Module({
      providers: [ConfigService],
      exports: [ConfigService],
    })
    export class ConfigModule {}
    ```
    
2. **Import the module** where needed:
    
    ```typescript
    @Module({
      imports: [ConfigModule],
      controllers: [EpisodeController],
      providers: [EpisodeService],
    })
    export class EpisodeModule {}
    ```
    
3. **Inject the service** into a class:
    
    ```typescript
    constructor(
      private readonly episodeService: EpisodeService,
      private readonly configService: ConfigService
    ) {}
    ```
    

#### **3️⃣ Benefits of DI**

✅ **Decouples logic** – Promotes clean and modular code.  
✅ **Easier to swap implementations** – Supports flexibility.  
✅ **Enhances testability** – Allows easy mocking of dependencies.  
✅ **Encourages maintainability** – Scales well with growing apps.

DI in NestJS ensures **better structure, scalability, and testability**! 🚀


---


### **Modules in NestJS**

NestJS follows a **modular architecture**, ensuring scalability and maintainability by grouping related features into **modules**.

#### **1️⃣ Root Module**

Every NestJS app has a **root module** (`AppModule`) that bootstraps the application.

#### **2️⃣ Creating a Module**

Use Nest CLI to generate modules:

```bash
nest generate module episode
```

#### **3️⃣ Module Structure & Dependencies**

Modules **import** other modules to structure the application:

```typescript
@Module({
  imports: [EpisodeModule, TopicsModule, ConfigModule], 
})
export class AppModule {}
```

- Modules not listed in `imports` are not part of the app.
- Shared modules (e.g., `ConfigModule`) can be reused across multiple modules.

#### **4️⃣ Key Characteristics**

✅ **Encapsulates Features** – Groups controllers, providers, and services.  
✅ **Encourages Reusability** – Modules can be imported elsewhere.  
✅ **Improves Maintainability** – Promotes a clean, scalable architecture.

By organizing modules efficiently, NestJS ensures a **structured and extensible** codebase. 🚀


![[../_imgs/Pasted image 20250130084338.png]]



---

### **Controllers in NestJS** 🚀

Controllers **handle incoming requests** and **return responses**. They act as request managers, directing traffic to services.

#### **1️⃣ Creating a Controller**

Generate a controller using Nest CLI:

```bash
nest generate controller episode
```

This creates `EpisodeController` inside `EpisodeModule`.

#### **2️⃣ Handling Requests**

Controllers use HTTP method decorators like `@Get()`, `@Post()`, and `@Put()`:

```typescript
@Controller('episode')
export class EpisodeController {
  @Get('featured')  
  findFeatured() {  
    return 'Featured episodes';  
  }  

  @Get(':id')  
  findById(@Param('id') id: string) {  
    return `Episode with ID: ${id}`;  
  }  
}
```

- `@Get('featured')` → Handles `/episode/featured`
- `@Get(':id')` → Captures URL parameter

#### **3️⃣ Delegating Logic to Services**

Controllers **shouldn’t contain business logic**. Instead, they delegate it to **services** for maintainability.

```typescript
constructor(private readonly episodeService: EpisodeService) {}
```

#### **4️⃣ Why Use Controllers?**

✅ **Defines routes** (`@Controller('route')`)  
✅ **Handles HTTP methods** (`@Get()`, `@Post()`, etc.)  
✅ **Processes parameters** (`@Param()`, `@Query()`, `@Body()`)  
✅ **Delegates logic to services**

Controllers **only manage requests**—services handle the real work! 🚀



---


### **Providers in NestJS** 🚀

Providers **encapsulate business logic** and are **injectable dependencies** in NestJS.

#### **1️⃣ Key Features**

✅ **`@Injectable()` Decorator** → Marks a class as a provider  
✅ **Encapsulates Logic** → Keeps controllers clean  
✅ **Dependency Injection (DI)** → Auto-injects where needed  
✅ **Singleton Pattern** → A single instance is shared

#### **2️⃣ Creating a Provider**

Generate a service (provider) using Nest CLI:

```bash
nest generate service user
```

#### **3️⃣ Using a Provider**

1️⃣ **Define the Service**

```typescript
@Injectable()
export class UserService {
  getUsers() {
    return ['John', 'Jane', 'Doe'];
  }
}
```

2️⃣ **Register in a Module**

```typescript
@Module({
  providers: [UserService],
  exports: [UserService], // Allows use in other modules
})
export class UserModule {}
```

3️⃣ **Inject into a Controller**

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

Providers **simplify dependency management**, making code **modular, reusable, and testable**. 🚀

---

### **NestJS Setup with CLI**

The **Nest CLI** simplifies application setup and development.

#### **1️⃣ Install & Create a Project**

```bash
npm install -g @nestjs/cli
nest new podcast-app
cd podcast-app
npm run start:dev  # Runs the app on localhost:3000
```

#### **2️⃣ Key Files & Structure**

- **`main.ts`** – Bootstraps the app:
    
    ```typescript
    import { NestFactory } from '@nestjs/core';
    import { AppModule } from './app.module';
    
    async function bootstrap() {
      const app = await NestFactory.create(AppModule);
      await app.listen(3000);
    }
    bootstrap();
    ```
    
- **`app.module.ts`** – The root module defining imports, controllers, and providers:
    
    ```typescript
    import { Module } from '@nestjs/common';
    
    @Module({ imports: [], controllers: [], providers: [] })
    export class AppModule {}
    ```
    

#### **3️⃣ CLI Shortcuts for Rapid Development**

- Generate a **module**:
    
    ```bash
    nest generate module podcast
    ```
    
- Generate a **controller**:
    
    ```bash
    nest generate controller podcast
    ```
    
- Generate a **service**:
    
    ```bash
    nest g service podcast
    ```
    

Nest CLI accelerates development by scaffolding the structure and enforcing best practices. 🚀





---



![[../_imgs/Pasted image 20250130091415.png]]


---

### **Middleware in NestJS** 🛂

Middleware acts like **airport security**, processing requests **before** they reach controllers.

#### **How It Works:**

- **Intercepts** requests before route handlers
- **Preprocesses** data (logging, auth checks, modifying requests)
- **Passes Control** to the next handler or controller

#### **Example: Logging Middleware**

```typescript
@Injectable()
export class LoggerMiddleware implements NestMiddleware {
  use(req: Request, res: Response, next: NextFunction) {
    console.log(`Request... ${req.method} ${req.url}`);
    next();
  }
}
```

#### **Applying Middleware**

```typescript
export class AppModule implements NestModule {
  configure(consumer: MiddlewareConsumer) {
    consumer.apply(LoggerMiddleware).forRoutes('users');
  }
}
```

#### **Key Takeaways:**

✅ **Pre-request processing**  
✅ **Can be applied globally or to specific routes**  
✅ **Common use cases**: Logging, Authentication, Input validation

---

### **Guards in NestJS** 🔒

Guards act as **security checkpoints**, controlling access based on conditions like authentication or roles.

#### **How It Works:**

- **Intercepts** requests before they reach controllers
- **Checks execution context** (e.g., user roles, tokens)
- **Returns `true` or `false** to allow/deny access

#### **Example: Auth Guard**

```typescript
@Injectable()
export class AuthGuard implements CanActivate {
  canActivate(context: ExecutionContext): boolean {
    const request = context.switchToHttp().getRequest();
    return request.headers.authorization === 'valid-token';
  }
}
```

#### **Applying Guards**

```typescript
@Controller('profile')
@UseGuards(AuthGuard)
export class ProfileController {
  @Get() getProfile() {
    return 'User profile data';
  }
}
```

#### **Key Takeaways:**

✅ **Controls access** based on conditions  
✅ **Applied globally, on controllers, or route handlers**  
✅ **Used for**: Authentication, Role-based access, Custom logic

---

### **Interceptors in NestJS** 🎬

Interceptors provide control over the **request-response lifecycle**, running both **before and after** the route handler.

#### **What They Can Do:**

✅ Modify requests before reaching the handler  
✅ Transform responses before sending them to the client  
✅ Handle logging, caching, or performance monitoring

#### **Example: Logging Interceptor**

```typescript
@Injectable()
export class LoggingInterceptor implements NestInterceptor {
  intercept(context: ExecutionContext, next: CallHandler): Observable<any> {
    const now = Date.now();
    return next.handle().pipe(
      tap(() => console.log(`Request processed in ${Date.now() - now}ms`))
    );
  }
}
```

#### **Key Takeaways:**

✅ Runs **before & after** the handler  
✅ Modifies requests/responses  
✅ Useful for logging, caching, and performance tracking

---

### **Pipes in NestJS** 💧

Pipes **validate** or **transform** incoming data before reaching the handler.

#### **What They Do:**

✅ **Validate** data against rules  
✅ **Transform** data types (e.g., string to number)  
✅ **Throw exceptions** if invalid

#### **Example: Built-in Validation Pipe**

```typescript
@Get(':id')
getUser(@Param('id', ParseIntPipe) id: number) {
  return `User ID: ${id}`;
}
```

#### **Creating a Custom Pipe**

```typescript
@Injectable()
export class ToUpperCasePipe implements PipeTransform {
  transform(value: any) {
    return typeof value === 'string' ? value.toUpperCase() : value;
  }
}
```

#### **Built-in Pipes:**

- `ValidationPipe`: Validates DTOs
- `ParseIntPipe`: Converts strings to numbers
- `ParseUUIDPipe`: Validates UUID
- `DefaultValuePipe`: Sets default values

#### **Key Takeaways:**

✅ Ensures **data integrity** before the controller  
✅ Prevents **invalid data** from breaking the app  
✅ Custom and built-in pipes available

---

### **Error Handling in NestJS** ⚠️

1. **Default Error Response**:
    
    - NestJS returns a 500 Internal Server Error for unhandled errors.
2. **Custom Error Handling**:
    
    - Use `HttpException` or predefined exceptions like `NotFoundException` (404), `ForbiddenException` (403), `UnauthorizedException` (401).
    
    **Example**:
    
    ```typescript
    throw new NotFoundException('Episode not found');
    ```
    
    Returns:
    
    ```json
    {
      "statusCode": 404,
      "message": "Episode not found",
      "error": "Not Found"
    }
    ```
    
3. **Customizing Error Responses**:
    
    - Exception filters allow global customization for error handling, e.g., modifying error format or logging.
    
    **Example** (Custom filter):
    
    ```typescript
    @Catch()
    export class AllExceptionsFilter implements ExceptionFilter {
      catch(exception: any, host: ArgumentsHost) {
        const response = host.switchToHttp().getResponse<Response>();
        response.status(exception.getStatus()).json({
          statusCode: exception.getStatus(),
          message: exception.message,
          error: exception.name,
        });
      }
    }
    ```
    
4. **Advanced Customization**:
    
    - Customize error handling using exception filters for better control over the response.

---

### **Exception Filters in NestJS** 🛠️

Exception filters handle errors centrally, providing **consistent error responses**.

#### **How They Work:**

1. **Catch exceptions** from guards, interceptors, pipes, or route handlers.
2. **Define custom error handling** to avoid exposing sensitive information.

#### **Creating a Custom Filter**:

```typescript
@Catch(HttpException)
export class HttpExceptionFilter implements ExceptionFilter {
  catch(exception: HttpException, host: ArgumentsHost) {
    const response = host.switchToHttp().getResponse<Response>();
    response.status(exception.getStatus()).json({
      statusCode: exception.getStatus(),
      message: exception.message,
      timestamp: new Date().toISOString(),
    });
  }
}
```

#### **Global Application**:

```typescript
app.useGlobalFilters(new HttpExceptionFilter());
```

#### **Benefits**:

✅ Centralized error handling  
✅ Customizable responses  
✅ Enhanced security by hiding sensitive info


---

### **Testing in NestJS** 🧪

1. **Generated Test Files**:
    
    - NestJS CLI generates test files for components, ready to be populated with tests.
2. **Testing Controller**:
    
    - NestJS provides utilities for creating a test module, typically starting with wiring tests for controllers and services.
    
    **Example**:
    
    ```typescript
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
    
3. **Mocking Services**:
    
    - Mock providers to simulate real service behavior for isolated tests.
    
    **Example**:
    
    ```typescript
    const mockEpisodeService = {
      findOne: jest.fn().mockResolvedValue({ id: 1, title: 'Episode 1' }),
    };
    ```
    
4. **Testing Controller Handlers**:
    
    - Test controller methods to ensure they work as expected with mocked services.
    
    **Example**:
    
    ```typescript
    it('should return an episode', async () => {
      const result = await controller.findOne(1);
      expect(result).toEqual({ id: 1, title: 'Episode 1' });
    });
    ```
    
5. **Testing Negative Scenarios**:
    
    - Simulate errors like `null` returns or thrown exceptions to ensure proper error handling.
    
    **Example**:
    
    ```typescript
    it('should throw an error if episode not found', async () => {
      mockEpisodeService.findOne.mockResolvedValue(null);
      await expect(controller.findOne(999)).rejects.toThrowError('Episode not found');
    });
    ```
    
6. **Benefits of Dependency Injection (DI)**:
    
    - DI allows easy mocking of services, improving testability and isolating components for unit testing.
7. **Error Handling**:
    
    - Ensure controllers return meaningful error responses, using NestJS's built-in error handling or custom exception filters.

By using these strategies, each part of your NestJS application can be tested in isolation with full control over dependencies.
