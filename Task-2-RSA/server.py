import socket
import ast


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    for d in range(2, phi):
        if (e * d) % phi == 1:
            return d
    return None

def power(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp //= 2
        base = (base * base) % mod
    return result



print("----- RSA KEY GENERATION -----")
p = int(input("Enter prime number p: "))
q = int(input("Enter prime number q: "))
n = p * q
phi = (p - 1) * (q - 1)

while True:
    e = int(input("Enter e (1 < e < phi and gcd(e, phi) = 1): "))
    if 1 < e < phi and gcd(e, phi) == 1:
        break
    else:
        print("Invalid e. Try again.")

d = mod_inverse(e, phi)
if d is None:
    print("Modular inverse not found.")
    exit()
q = int(input("Enter prime number q: "))
n = p * q
phi = (p - 1) * (q - 1)


print("\nPublic Key (e, n):", (e, n))
print("Private Key (d, n):", (d, n))



server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("127.0.0.1", 12345))
server_socket.listen(1)

print("\nServer waiting for client connection...")

conn, addr = server_socket.accept()
print("Client connected from:", addr)


conn.send(f"{e},{n}".encode())

data = conn.recv(4096).decode()
cipher_list = ast.literal_eval(data)

print("Encrypted message received:", cipher_list)

decrypted_chars = [chr(power(c, d, n)) for c in cipher_list]
decrypted_message = "".join(decrypted_chars)

print("Decrypted message:", decrypted_message)

conn.close()
server_socket.close()
