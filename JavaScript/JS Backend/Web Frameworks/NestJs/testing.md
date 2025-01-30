
### **10. Testing in NestJS**

- Unit Testing with Jest
- E2E Testing with `@nestjs/testing`
- Mocking dependencies & Test-driven development (TDD)


# **Testing in NestJS**

Testing is a vital part of ensuring the **reliability** and **maintainability** of your NestJS applications. NestJS supports a range of testing strategies, including **unit testing** (for individual components) and **end-to-end (E2E) testing** (for the entire application). It also integrates well with **Jest** and **Vitest**, providing tools for mocking dependencies and supporting **Test-Driven Development (TDD)**.

---

## **1. Unit Testing with Jest & Vitest**

Unit testing focuses on testing individual components or services in isolation to ensure that each part of the application behaves as expected.

### **🔹 Setting Up Jest for Unit Testing**

NestJS uses **Jest** by default for testing. Jest provides powerful features like mocking, spies, and assertions.

1. **Install Jest Dependencies** (if not already installed):
    
    ```sh
    npm install --save-dev jest @nestjs/testing ts-jest @types/jest
    ```
    
2. **Basic Unit Test Example** (`user.service.ts`)
    
    ```ts
    import { Injectable } from '@nestjs/common';
    
    @Injectable()
    export class UserService {
      getUserById(id: string) {
        return { id, name: 'John Doe' };
      }
    }
    ```
    
    **Unit Test** (`user.service.spec.ts`)
    
    ```ts
    import { Test, TestingModule } from '@nestjs/testing';
    import { UserService } from './user.service';
    
    describe('UserService', () => {
      let service: UserService;
    
      beforeEach(async () => {
        const module: TestingModule = await Test.createTestingModule({
          providers: [UserService],
        }).compile();
    
        service = module.get<UserService>(UserService);
      });
    
      it('should return a user by ID', () => {
        expect(service.getUserById('1')).toEqual({ id: '1', name: 'John Doe' });
      });
    });
    ```
    
3. **Mocking Dependencies for Unit Testing**  
    Use **mock services** to isolate the unit under test from its dependencies.
    
    ```ts
    import { Injectable } from '@nestjs/common';
    
    @Injectable()
    export class UserService {
      constructor(private readonly userRepository: UserRepository) {}
    
      getUserById(id: string) {
        return this.userRepository.findById(id);
      }
    }
    ```
    
    **Mock Repository** (`user.service.spec.ts`)
    
    ```ts
    import { Test, TestingModule } from '@nestjs/testing';
    import { UserService } from './user.service';
    import { UserRepository } from './user.repository';
    
    const mockUserRepository = {
      findById: jest.fn().mockResolvedValue({ id: '1', name: 'John Doe' }),
    };
    
    describe('UserService', () => {
      let service: UserService;
    
      beforeEach(async () => {
        const module: TestingModule = await Test.createTestingModule({
          providers: [
            UserService,
            { provide: UserRepository, useValue: mockUserRepository },
          ],
        }).compile();
    
        service = module.get<UserService>(UserService);
      });
    
      it('should return a user by ID from the repository', () => {
        expect(service.getUserById('1')).resolves.toEqual({ id: '1', name: 'John Doe' });
        expect(mockUserRepository.findById).toHaveBeenCalledWith('1');
      });
    });
    ```
    

### **📌 Interview Tip:**

✅ Be ready to explain **Jest's mocking capabilities** and how you mock dependencies like repositories.  
✅ Know how to **test async code** using `mockResolvedValue` or `mockRejectedValue`.  
✅ Understand how **Jest's `beforeEach` and `afterEach`** hooks work for setup and teardown.

---

## **2. E2E Testing with `@nestjs/testing`**

End-to-end (E2E) tests ensure that the **entire application** (from the HTTP request to the response) works as expected, simulating real-world interactions.

### **🔹 Setting Up E2E Test Example**

E2E tests simulate requests to the application and validate the response. These tests can cover things like controllers, middleware, and guards.

1. **Controller Test** (`user.controller.ts`)
    
    ```ts
    import { Controller, Get, Param } from '@nestjs/common';
    import { UserService } from './user.service';
    
    @Controller('users')
    export class UserController {
      constructor(private readonly userService: UserService) {}
    
      @Get(':id')
      getUserById(@Param('id') id: string) {
        return this.userService.getUserById(id);
      }
    }
    ```
    
2. **E2E Test Setup** (`user.controller.spec.ts`)
    
    ```ts
    import { Test, TestingModule } from '@nestjs/testing';
    import { INestApplication } from '@nestjs/common';
    import * as request from 'supertest';
    import { UserController } from './user.controller';
    import { UserService } from './user.service';
    
    describe('UserController (e2e)', () => {
      let app: INestApplication;
    
      beforeAll(async () => {
        const moduleFixture: TestingModule = await Test.createTestingModule({
          controllers: [UserController],
          providers: [
            UserService,
            {
              provide: UserService,
              useValue: { getUserById: jest.fn().mockResolvedValue({ id: '1', name: 'John Doe' }) },
            },
          ],
        }).compile();
    
        app = moduleFixture.createNestApplication();
        await app.init();
      });
    
      it('/users/:id (GET)', () => {
        return request(app.getHttpServer())
          .get('/users/1')
          .expect(200)
          .expect({ id: '1', name: 'John Doe' });
      });
    
      afterAll(async () => {
        await app.close();
      });
    });
    ```
    
3. **Running E2E Tests**  
    Run E2E tests with:
    
    ```sh
    npm run test:e2e
    ```
    

### **📌 Interview Tip:**

✅ Be ready to explain **how `supertest` is used** for making HTTP requests in E2E tests.  
✅ Understand how to **mock services in E2E tests** and isolate components.  
✅ Highlight the difference between **unit tests and E2E tests** in terms of scope and dependencies.

---

## **3. Mocking Dependencies & Test-Driven Development (TDD)**

Mocking is crucial for isolating components and avoiding hitting real databases or external APIs during tests. **Test-Driven Development (TDD)** focuses on writing tests **before the code**.

### **🔹 Mocking Services in Unit Tests**

You can mock **third-party libraries** or **external services** using Jest’s mock functions (`jest.fn()`), or **manual mocks**.

For instance, in an **HTTP call mock**:

```ts
const mockHttpService = {
  get: jest.fn().mockResolvedValue({ data: 'mock data' }),
};
```

### **🔹 Test-Driven Development (TDD)**

In TDD, you:

1. **Write the test** first (the test will fail).
2. **Write just enough code** to make the test pass.
3. **Refactor** the code and tests to make sure they are clean.

Example:

```ts
describe('Add User (TDD)', () => {
  it('should create a new user', async () => {
    const user = { name: 'John Doe' };
    await expect(service.addUser(user)).resolves.toHaveProperty('id');
  });
});
```

Then implement just enough code to pass the test.

### **📌 Interview Tip:**

✅ Be prepared to explain **mocking strategies** and when to use **manual mocks** or **jest.fn()**.  
✅ Highlight how **TDD improves code quality** by focusing on test cases first.  
✅ Understand that **unit tests should mock external services** (e.g., databases, APIs) to isolate the unit under test.

---

## **Key Takeaways for Interviews**

✅ **Unit Testing** with Jest allows for isolated testing of components, while **E2E Testing** simulates real-world requests to test the entire flow.  
✅ **Mocking dependencies** is essential for unit tests to ensure components are tested in isolation.  
✅ **TDD** helps improve code design and guarantees that all code changes pass predefined tests.  
✅ **Jest and Vitest** are widely used for testing in NestJS; Vitest can be a faster alternative for smaller projects.

🔥 **Pro Tip:** Be prepared to discuss **unit testing best practices**, including **mocking**, **spying on function calls**, and **test isolation**. Also, explain how **E2E testing** ensures that everything in the application integrates well. 🚀