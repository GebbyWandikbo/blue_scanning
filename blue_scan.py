import socket

# Membuat socket TCP
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Membuat socket UDP
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Koneksi TCP
def conn_tcp():
    ipadd = input("Masukkan IP Tujuan: ")
    portadd = int(input("Masukkan Port Tujuan: "))
    tcp_socket.connect((ipadd, portadd))
    addr_tcp = tcp_socket.getpeername()
    print("Koneksi TCP berhasil ke", (ipadd, portadd))

# Koneksi UDP
def conn_udp():
    ipadd = input("Masukkan IP Tujuan: ")
    portadd = int(input("Masukkan Port Tujuan: "))
    udp_socket.sendto(b"Test", (ipadd, portadd))
    addr_udp = udp_socket.getpeername()
    print("Koneksi UDP berhasil ke", (ipadd, portadd))

def main():
    while True:
        print("[1] --- Scanning TCP Target")
        print("[2] --- Scanning UDP Target")
        print("[0] --- Exit")
        print("--------------------------------------------")
        
        pilihan = input("Pilih fitur sesuai nomor pilihan: ")
        
        if pilihan == "1":
            conn_tcp()
        elif pilihan == "2":
            conn_udp()
        elif pilihan == "0":
            print("Bye!!")
            break
        else:
            print("[Error] --- Masukkan nomor sesuai pilihan Anda")

if __name__ == "__main__":
    main()
