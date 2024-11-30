
[why jwt @KeeriPurswani](https://youtu.be/4o2AkDC8Z9c?si=kNWFaLd491m3hGv1)



1. **Inefficiency of Sessions**: Sessions can become inefficient due to increased user data storage on the server side, leading to scaling issues as the number of users grows.

2. **Complications with Multi-Server Management**: Managing sessions across multiple servers complicates load balancing and requires ensuring that all requests from the same user are directed to the same server.

3. **Sticky Sessions**: To handle user information effectively, sticky sessions are often implemented, meaning user data must reside on a specific server.

4. **Statefulness Issue**: The basic principle in distributed systems is to keep servers stateless. Storing sessions on the server side violates this principle.

5. **Use of Tokens**: Instead of storing session data on the server, all necessary information, including user ID and permissions, can be included in a self-contained token.

6. **Token Verification**: All servers must have the same key to verify the token, allowing any server to check its validity.

7. **Cryptographic Signing**: Tokens are cryptographically signed, ensuring that any tampering will cause verification to fail.

8. **Further Discussions on JWT**: There will be more detailed discussions on JSON Web Tokens (JWT) in the future, encouraging followers for more updates. 




