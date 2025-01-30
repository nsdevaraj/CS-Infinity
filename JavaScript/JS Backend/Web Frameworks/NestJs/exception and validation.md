
### **6. Exception Handling & Validation**

- Custom Exception Filters
- Built-in Exception Handling (`HttpException`, `NotFoundException`)
- Request Validation (`class-validator`, `class-transformer`)
- Error handling best practices



# **Exception Handling & Validation in NestJS**

Handling exceptions and validating requests are crucial for building **robust** and **secure** NestJS applications. NestJS provides **built-in exception handling**, **custom exception filters**, and **request validation** mechanisms.

---

## **1. Built-in Exception Handling (`HttpException`, `NotFoundException`)**

NestJS provides **predefined exceptions** like `HttpException`, `NotFoundException`, and more.

### **🔹 Throwing Built-in Exceptions**

```ts
import { Controller, Get, Param, NotFoundException } from '@nestjs/common';

@Controller('users')
export class UserController {
  private users = [{ id: 1, name: 'John Doe' }];

  @Get(':id')
  getUser(@Param('id') id: number) {
    const user = this.users.find((u) => u.id === Number(id));
    if (!user) {
      throw new NotFoundException(`User with ID ${id} not found`);
    }
    return user;
  }
}
```

### **📌 Interview Tip:**

✅ Be ready to explain how **NestJS handles exceptions globally** without needing `try/catch`.  
✅ Mention that **NestJS automatically sends structured error responses**.

---

## **2. Custom Exception Filters**

For **custom error handling**, create an **exception filter**.

### **🔹 Creating a Custom Exception (`custom-exception.ts`)**

```ts
import { HttpException, HttpStatus } from '@nestjs/common';

export class CustomException extends HttpException {
  constructor(message: string) {
    super({ error: message, statusCode: HttpStatus.BAD_REQUEST }, HttpStatus.BAD_REQUEST);
  }
}
```

### **🔹 Creating an Exception Filter (`exception.filter.ts`)**

```ts
import { ExceptionFilter, Catch, ArgumentsHost, HttpException } from '@nestjs/common';

@Catch(HttpException)
export class CustomExceptionFilter implements ExceptionFilter {
  catch(exception: HttpException, host: ArgumentsHost) {
    const ctx = host.switchToHttp();
    const response = ctx.getResponse();
    const status = exception.getStatus();
    
    response.status(status).json({
      statusCode: status,
      message: exception.message,
      timestamp: new Date().toISOString(),
    });
  }
}
```

### **🔹 Applying the Exception Filter**

1️⃣ **At Controller Level:**

```ts
import { UseFilters } from '@nestjs/common';

@UseFilters(CustomExceptionFilter)
```

2️⃣ **Globally (Best Practice):**

```ts
import { APP_FILTER } from '@nestjs/core';

providers: [{ provide: APP_FILTER, useClass: CustomExceptionFilter }]
```

### **📌 Interview Tip:**

✅ Explain how `@Catch()` works to **intercept and format errors**.  
✅ Mention that **custom exception filters help in logging & formatting responses**.

---

## **3. Request Validation (`class-validator`, `class-transformer`)**

### **🔹 Installing Dependencies**

```sh
npm install class-validator class-transformer
```

### **🔹 Creating a DTO for Validation (`create-user.dto.ts`)**

```ts
import { IsString, IsEmail, IsNotEmpty } from 'class-validator';

export class CreateUserDto {
  @IsString()
  @IsNotEmpty()
  name: string;

  @IsEmail()
  email: string;
}
```

### **🔹 Applying Validation in Controller**

```ts
import { Controller, Post, Body, UsePipes, ValidationPipe } from '@nestjs/common';

@Controller('users')
export class UserController {
  @Post()
  @UsePipes(new ValidationPipe()) // Apply validation
  createUser(@Body() createUserDto: CreateUserDto) {
    return { message: 'User Created Successfully', data: createUserDto };
  }
}
```

### **📌 Interview Tip:**

✅ Explain how `ValidationPipe` **automatically validates and transforms DTOs**.  
✅ Highlight that `class-validator` prevents **invalid data from reaching the service layer**.

---

## **4. Error Handling Best Practices**

✅ **Always use DTOs** to enforce data validation.  
✅ **Use Exception Filters** to handle errors globally.  
✅ **Log errors** using a logging library (`winston`, `pino`).  
✅ **Never expose stack traces in production**.  
✅ **Use meaningful HTTP status codes** (`400`, `404`, `500`).

---

## **Key Takeaways for Interviews**

✅ **NestJS provides built-in exception handling** (`HttpException`, `NotFoundException`).  
✅ **Custom Exception Filters** allow structured error responses.  
✅ **DTOs with `class-validator` ensure data integrity**.  
✅ **Global Exception Handling improves maintainability**.

🔥 **Pro Tip:** Be ready to compare **NestJS exception handling with Express.js**, where errors need manual handling with `try/catch`! 🚀



