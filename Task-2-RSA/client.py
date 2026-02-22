import socket

def power(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp //= 2
        base = (base * base) % mod
    return result

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("127.0.0.1", 12345))

key_data = client_socket.recv(1024).decode()
e, n = map(int, key_data.split(","))

print("Public key received:", (e, n))

msg = input("Enter message: ")

msg_ascii = [ord(c) for c in msg]
cipher_list = [power(c, e, n) for c in msg_ascii]

print("Encrypted message:", cipher_list)

client_socket.send(str(cipher_list).encode())

client_socket.close()

