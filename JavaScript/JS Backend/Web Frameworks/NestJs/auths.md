

### **5. Authentication & Authorization**

- Implementing **JWT Authentication** (`@nestjs/passport`, `passport-jwt`)
- Role-based access control (RBAC)
- API key authentication
- OAuth with NestJS (`passport-google-oauth20`, etc.)



# **Authentication & Authorization in NestJS**

Authentication (**who you are**) and Authorization (**what you can access**) are critical in securing NestJS applications. NestJS supports various authentication strategies, including **JWT, API keys, OAuth**, and **role-based access control (RBAC)**.

---

## **1. Implementing JWT Authentication (`@nestjs/passport`, `passport-jwt`)**

### **🔹 Installing Dependencies**

```sh
npm install @nestjs/passport passport passport-jwt @nestjs/jwt jsonwebtoken
```

### **🔹 Setting Up JWT Auth Module (`auth.module.ts`)**

```ts
import { Module } from '@nestjs/common';
import { JwtModule } from '@nestjs/jwt';
import { PassportModule } from '@nestjs/passport';
import { AuthService } from './auth.service';
import { JwtStrategy } from './jwt.strategy';

@Module({
  imports: [
    PassportModule.register({ defaultStrategy: 'jwt' }),
    JwtModule.register({
      secret: 'super-secret-key', // Use env variables in production!
      signOptions: { expiresIn: '1h' },
    }),
  ],
  providers: [AuthService, JwtStrategy],
  exports: [AuthService],
})
export class AuthModule {}
```

### **🔹 Creating JWT Strategy (`jwt.strategy.ts`)**

```ts
import { Injectable } from '@nestjs/common';
import { PassportStrategy } from '@nestjs/passport';
import { ExtractJwt, Strategy } from 'passport-jwt';

@Injectable()
export class JwtStrategy extends PassportStrategy(Strategy) {
  constructor() {
    super({
      jwtFromRequest: ExtractJwt.fromAuthHeaderAsBearerToken(),
      secretOrKey: 'super-secret-key',
    });
  }

  async validate(payload: any) {
    return { userId: payload.sub, username: payload.username };
  }
}
```

### **🔹 Generating JWT Token in Auth Service (`auth.service.ts`)**

```ts
import { Injectable } from '@nestjs/common';
import { JwtService } from '@nestjs/jwt';

@Injectable()
export class AuthService {
  constructor(private readonly jwtService: JwtService) {}

  async login(user: any) {
    const payload = { username: user.username, sub: user.id };
    return { access_token: this.jwtService.sign(payload) };
  }
}
```

### **🔹 Protecting Routes with `@UseGuards(AuthGuard('jwt'))`**

```ts
import { Controller, Get, UseGuards } from '@nestjs/common';
import { AuthGuard } from '@nestjs/passport';

@Controller('profile')
export class ProfileController {
  @UseGuards(AuthGuard('jwt'))
  @Get()
  getProfile() {
    return { message: 'Protected Profile Data' };
  }
}
```

### **📌 Interview Tip:**

✅ Be ready to explain **how JWT authentication works** and why we use `passport-jwt`.  
✅ Know the **difference between session-based authentication and token-based authentication (JWT)**.

---

## **2. Role-Based Access Control (RBAC) in NestJS**

RBAC ensures that only users with specific roles can access certain routes.

### **🔹 Creating a Role Guard (`roles.guard.ts`)**

```ts
import { Injectable, CanActivate, ExecutionContext } from '@nestjs/common';
import { Reflector } from '@nestjs/core';

@Injectable()
export class RolesGuard implements CanActivate {
  constructor(private reflector: Reflector) {}

  canActivate(context: ExecutionContext): boolean {
    const requiredRoles = this.reflector.get<string[]>('roles', context.getHandler());
    if (!requiredRoles) {
      return true;
    }
    const { user } = context.switchToHttp().getRequest();
    return requiredRoles.some((role) => user.roles?.includes(role));
  }
}
```

### **🔹 Creating a Roles Decorator (`roles.decorator.ts`)**

```ts
import { SetMetadata } from '@nestjs/common';

export const Roles = (...roles: string[]) => SetMetadata('roles', roles);
```

### **🔹 Applying Role-Based Protection**

```ts
import { Controller, Get, UseGuards } from '@nestjs/common';
import { Roles } from './roles.decorator';
import { RolesGuard } from './roles.guard';
import { AuthGuard } from '@nestjs/passport';

@Controller('admin')
@UseGuards(AuthGuard('jwt'), RolesGuard)
export class AdminController {
  @Roles('admin')
  @Get()
  getAdminData() {
    return { message: 'Admin Access Granted' };
  }
}
```

### **📌 Interview Tip:**

✅ Know the difference between **role-based access (RBAC) and permission-based access**.  
✅ Be prepared to explain **how Guards work in NestJS**.

---

## **3. API Key Authentication**

API Key authentication is useful for **machine-to-machine communication** (e.g., third-party integrations).

### **🔹 Creating an API Key Guard (`api-key.guard.ts`)**

```ts
import { Injectable, CanActivate, ExecutionContext } from '@nestjs/common';

@Injectable()
export class ApiKeyGuard implements CanActivate {
  canActivate(context: ExecutionContext): boolean {
    const request = context.switchToHttp().getRequest();
    const apiKey = request.headers['x-api-key'];
    return apiKey === process.env.API_KEY; // Store API key in environment variables
  }
}
```

### **🔹 Applying API Key Authentication**

```ts
import { Controller, Get, UseGuards } from '@nestjs/common';
import { ApiKeyGuard } from './api-key.guard';

@Controller('external')
@UseGuards(ApiKeyGuard)
export class ExternalController {
  @Get()
  getExternalData() {
    return { message: 'API Key Authenticated' };
  }
}
```

### **📌 Interview Tip:**

✅ Know when to use **API keys vs JWT authentication**.  
✅ API keys are **static** and should be **rotated periodically** for security.

---

## **4. OAuth with NestJS (`passport-google-oauth20`)**

OAuth is used for **social login (Google, Facebook, GitHub, etc.)**.

### **🔹 Installing Google OAuth Package**

```sh
npm install passport-google-oauth20
```

### **🔹 Implementing Google Strategy (`google.strategy.ts`)**

```ts
import { Injectable } from '@nestjs/common';
import { PassportStrategy } from '@nestjs/passport';
import { Strategy, VerifyCallback } from 'passport-google-oauth20';

@Injectable()
export class GoogleStrategy extends PassportStrategy(Strategy, 'google') {
  constructor() {
    super({
      clientID: process.env.GOOGLE_CLIENT_ID,
      clientSecret: process.env.GOOGLE_CLIENT_SECRET,
      callbackURL: 'http://localhost:3000/auth/google/callback',
      scope: ['email', 'profile'],
    });
  }

  async validate(accessToken: string, refreshToken: string, profile: any, done: VerifyCallback) {
    return done(null, { profile, accessToken });
  }
}
```

### **🔹 Creating Google Auth Controller (`auth.controller.ts`)**

```ts
import { Controller, Get, UseGuards, Req } from '@nestjs/common';
import { AuthGuard } from '@nestjs/passport';

@Controller('auth')
export class AuthController {
  @Get('google')
  @UseGuards(AuthGuard('google'))
  googleLogin() {
    return { message: 'Redirecting to Google...' };
  }

  @Get('google/callback')
  @UseGuards(AuthGuard('google'))
  googleCallback(@Req() req) {
    return req.user;
  }
}
```

### **📌 Interview Tip:**

✅ Know how **OAuth differs from JWT** (OAuth is third-party authentication, JWT is self-contained).  
✅ Explain **OAuth flow (Authorization Code, Access Token, Refresh Token)**.

---

## **Key Takeaways for Interviews**

✅ **JWT Authentication** – Secure, stateless authentication.  
✅ **Role-Based Access Control (RBAC)** – Restrict access based on user roles.  
✅ **API Key Authentication** – Best for external API integrations.  
✅ **OAuth with Google** – Allows social login.

🔥 **Pro Tip:** Be prepared to **compare authentication strategies** and discuss **when to use API keys, JWT, and OAuth** in real-world applications! 🚀