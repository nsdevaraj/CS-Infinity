
### **7. Interceptors, Pipes & Middleware**

- Using **Pipes** for validation and transformation
- Using **Interceptors** for logging, caching, etc.
- Middleware vs Guards vs Interceptors – when to use what?


# **Interceptors, Pipes & Middleware in NestJS**

NestJS provides **Pipes, Interceptors, and Middleware** to handle **validation, transformation, logging, caching**, and more. Understanding when to use **Middleware vs Guards vs Interceptors** is crucial for writing **clean and efficient** applications.

---

## **1. Pipes – Validation & Transformation**

Pipes are used for **data validation and transformation** before it reaches the controller.

### **🔹 Using Built-in Validation (`ValidationPipe`)**

```ts
import { Controller, Post, Body, UsePipes, ValidationPipe } from '@nestjs/common';
import { IsString, IsEmail } from 'class-validator';

class CreateUserDto {
  @IsString()
  name: string;

  @IsEmail()
  email: string;
}

@Controller('users')
export class UserController {
  @Post()
  @UsePipes(new ValidationPipe({ whitelist: true }))
  createUser(@Body() createUserDto: CreateUserDto) {
    return { message: 'User Created', data: createUserDto };
  }
}
```

🔹 **`whitelist: true`** removes unknown properties from incoming requests.

### **🔹 Custom Pipe for Data Transformation**

```ts
import { PipeTransform, Injectable, BadRequestException } from '@nestjs/common';

@Injectable()
export class ParseIntPipe implements PipeTransform {
  transform(value: any) {
    const parsedValue = parseInt(value, 10);
    if (isNaN(parsedValue)) {
      throw new BadRequestException('Invalid number');
    }
    return parsedValue;
  }
}
```

🔹 Apply it in a **route parameter**:

```ts
@Get(':id')
getUser(@Param('id', ParseIntPipe) id: number) { }
```

### **📌 Interview Tip:**

✅ **Know the difference between built-in (`ValidationPipe`) and custom pipes**.  
✅ **Be ready to explain how pipes are applied at the route, controller, and global level**.

---

## **2. Interceptors – Logging, Transformation & Caching**

Interceptors allow **modifying request/response** or performing **cross-cutting concerns** like logging, caching, and response transformation.

### **🔹 Logging Request/Response with Interceptors**

```ts
import { CallHandler, ExecutionContext, Injectable, NestInterceptor } from '@nestjs/common';
import { Observable } from 'rxjs';
import { tap } from 'rxjs/operators';

@Injectable()
export class LoggingInterceptor implements NestInterceptor {
  intercept(context: ExecutionContext, next: CallHandler): Observable<any> {
    console.log('Before request is handled');
    return next.handle().pipe(tap(() => console.log('After response is sent')));
  }
}
```

🔹 Apply at the **controller or globally**:

```ts
@UseInterceptors(LoggingInterceptor)
```

### **🔹 Response Transformation with Interceptors**

```ts
@Injectable()
export class TransformInterceptor implements NestInterceptor {
  intercept(context: ExecutionContext, next: CallHandler): Observable<any> {
    return next.handle().pipe(
      map((data) => ({ status: 'success', data })) // Wrap response in a standard format
    );
  }
}
```

### **📌 Interview Tip:**

✅ **Understand how interceptors modify responses globally**.  
✅ **Be ready to compare interceptors with middleware & guards**.

---

## **3. Middleware – Processing Requests Before Reaching Controllers**

Middleware runs **before the request hits the controller** (like in Express.js).

### **🔹 Example: Logging Middleware**

```ts
import { Injectable, NestMiddleware } from '@nestjs/common';

@Injectable()
export class LoggerMiddleware implements NestMiddleware {
  use(req: Request, res: Response, next: Function) {
    console.log(`Request... ${req.method} ${req.url}`);
    next();
  }
}
```

🔹 Apply middleware in **`app.module.ts`**:

```ts
import { MiddlewareConsumer, Module, NestModule } from '@nestjs/common';

@Module({})
export class AppModule implements NestModule {
  configure(consumer: MiddlewareConsumer) {
    consumer.apply(LoggerMiddleware).forRoutes('*'); // Apply to all routes
  }
}
```

### **📌 Interview Tip:**

✅ **Middleware is for request processing, logging, authentication, etc.**  
✅ **It runs before Guards, Interceptors, or Controllers.**

---

## **4. Middleware vs Guards vs Interceptors – When to Use What?**

|Feature|Runs On|Purpose|Use Case Examples|
|---|---|---|---|
|**Middleware**|Before controllers|Pre-processing requests|Logging, Authentication, Request Parsing|
|**Guards**|Before handlers|Authorization & Access Control|Role-based access, JWT authentication|
|**Interceptors**|Before & after controllers|Modifying requests & responses|Caching, Logging, Response Formatting|

### **📌 Interview Tip:**

✅ **Be ready to discuss real-world use cases** for each.  
✅ **Explain the order of execution: Middleware → Guards → Interceptors → Controllers → Response Interceptors**.

---

## **Key Takeaways for Interviews**

✅ **Pipes** are used for **validation and transformation** (e.g., `ValidationPipe`).  
✅ **Interceptors** modify **requests & responses** (e.g., logging, response formatting).  
✅ **Middleware** is used for **pre-processing requests** (e.g., authentication, logging).  
✅ **Understand when to use Middleware vs Guards vs Interceptors** for optimized performance.

🔥 **Pro Tip:** Be ready to **explain the execution flow** and **compare with Express.js middlewares**! 🚀



