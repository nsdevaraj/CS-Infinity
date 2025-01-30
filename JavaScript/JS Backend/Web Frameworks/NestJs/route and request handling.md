

### **3. Routing & Request Handling**

- Handling different HTTP methods (`GET`, `POST`, `PUT`, `DELETE`)
- Route parameters, query parameters, and body parsing
- Middleware (`NestMiddleware`)
- Guards (`CanActivate`, `AuthGuards`)



## **3. Routing & Request Handling in NestJS**

### **1. Handling Different HTTP Methods (`GET`, `POST`, `PUT`, `DELETE`)**

NestJS provides decorators to handle various HTTP methods inside controllers.

- **GET** – Fetch data
- **POST** – Create data
- **PUT/PATCH** – Update data
- **DELETE** – Remove data

Example:

```ts
@Controller('users')
export class UsersController {
  @Get() // GET /users
  getUsers() {
    return 'List of users';
  }

  @Post() // POST /users
  createUser(@Body() userData: any) {
    return `User ${userData.name} created!`;
  }

  @Put(':id') // PUT /users/:id
  updateUser(@Param('id') id: string, @Body() userData: any) {
    return `User ${id} updated`;
  }

  @Delete(':id') // DELETE /users/:id
  deleteUser(@Param('id') id: string) {
    return `User ${id} deleted`;
  }
}
```

**📌 Interview Tip:** Be ready to explain when to use **PUT vs PATCH** (PUT replaces the entire resource, PATCH modifies specific fields).

---

### **2. Route Parameters, Query Parameters & Body Parsing**

- **Route Parameters (`@Param()`)** – Extract dynamic values from URL
    
    ```ts
    @Get(':id') // GET /users/123
    getUser(@Param('id') id: string) {
      return `User ID: ${id}`;
    }
    ```
    
- **Query Parameters (`@Query()`)** – Extract optional data from URL
    
    ```ts
    @Get() // GET /users?role=admin
    getUsers(@Query('role') role: string) {
      return `Users with role: ${role}`;
    }
    ```
    
- **Body Parsing (`@Body()`)** – Extract data from request body
    
    ```ts
    @Post() // POST /users
    createUser(@Body() userData: any) {
      return `User created with name: ${userData.name}`;
    }
    ```
    

**📌 Interview Tip:** Be prepared to explain **the difference between route params and query params** (params for required values, query params for optional filters).

---

### **3. Middleware (`NestMiddleware`)**

Middleware functions run **before the request reaches the controller**. Used for **logging, authentication, request transformation, etc.**

- Create a middleware:
    
    ```ts
    @Injectable()
    export class LoggerMiddleware implements NestMiddleware {
      use(req: Request, res: Response, next: Function) {
        console.log(`Incoming request: ${req.method} ${req.url}`);
        next(); // Pass to next handler
      }
    }
    ```
    
- Apply middleware in a module:
    
    ```ts
    export class AppModule {
      configure(consumer: MiddlewareConsumer) {
        consumer.apply(LoggerMiddleware).forRoutes('users');
      }
    }
    ```
    

**📌 Interview Tip:** Explain when to use **Middleware vs Guards vs Interceptors** (Middleware for global request processing, Guards for authentication, Interceptors for response modification).

---

### **4. Guards (`CanActivate`, `AuthGuards`)**

Guards **control access** to routes by implementing `CanActivate`.

- Example: **Auth Guard using JWT**
    
    ```ts
    @Injectable()
    export class AuthGuard implements CanActivate {
      canActivate(context: ExecutionContext): boolean {
        const request = context.switchToHttp().getRequest();
        return request.headers.authorization ? true : false;
      }
    }
    ```
    
- Apply guard to a controller or route:
    
    ```ts
    @UseGuards(AuthGuard)
    @Get()
    getSecureData() {
      return 'Protected data';
    }
    ```
    

**📌 Interview Tip:** Explain how **Guards work in NestJS** and how they differ from Middleware (Middleware runs before Guards, Guards determine access).

---

## **Key Takeaways for Interviews**

✅ **HTTP Methods** – Know when to use `GET`, `POST`, `PUT`, `DELETE`.  
✅ **Routing Parameters** – `@Param()`, `@Query()`, `@Body()` for extracting data.  
✅ **Middleware** – Runs before controllers, used for logging/auth.  
✅ **Guards** – Handles authentication/authorization, implemented with `CanActivate`.

🔥 **Pro Tip:** Be prepared to answer **how Middleware, Guards, and Interceptors differ** in real-world applications! 🚀

