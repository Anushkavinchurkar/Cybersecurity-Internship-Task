# Task 2 – RSA Encryption & Secure Communication

## 📌 Objective
To implement RSA encryption and decryption for secure communication between a client and server using Python.

---

## 🛠 Technologies Used
- Python
- Socket Programming
- RSA Algorithm

---

## 🔐 Description

In this task, RSA cryptographic algorithm was implemented to ensure secure message transmission between client and server.

The server generates:
- Public Key (e, n)
- Private Key (d, n)

The client:
- Receives public key
- Encrypts message
- Sends encrypted data to server

The server:
- Decrypts message using private key

---

## 🧪 Sample Execution

Server Output:
Public Key (e, n): (5, 247)  
Private Key (d, n): (173, 247)  
Encrypted message received: [130, 79]  
Decrypted message: hi  

Client Output:
Public key received: (5, 247)  
Encrypted message: [130, 79]  

---

## ✅ Outcome
Successfully implemented RSA encryption and demonstrated secure message exchange between client and server.
