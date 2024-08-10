import whois
import subprocess
import re

# Validasi domain
def validasi_domain(domain):
    return re.match(r'^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', domain) is not None

# Informasi Domain
def domain():
    add = input("Masukkan Domain Target (contoh: example.com): ").strip()
    if not validasi_domain(add):
        print("[Error] --- Domain tidak valid.")
        return
    
    try:
        informasi = whois.whois(add)
        print("Ini adalah informasi dari domain yang ingin Anda cari")
        print("--------------------------------------------\n")
        print(informasi)
    except Exception as e:
        print(f"[Error] --- Terjadi kesalahan: {e}")

# Subdomain
def subdomain():
    add = input("Masukkan Domain Target (contoh: example.com): ").strip()
    if not validasi_domain(add):
        print("[Error] --- Domain tidak valid.")
        return
    
    try:
        # Menghapus skema dari domain yang dimasukkan jika ada
        domain = add.split("://")[-1]
        # Jalankan Sublist3r untuk mencari subdomain
        result = subprocess.run(['sublist3r', '-d', domain, '-v'], capture_output=True, text=True)
        # Filter hasil output untuk menghilangkan baris yang mengandung pesan error
        filtered_output = "\n".join(line for line in result.stdout.splitlines() if not any(
            keyword in line for keyword in ["Error:", "Searching now in", "Total Unique Subdomains Found"]
        ))
        print("Hasil Subdomain:")
        print(filtered_output)
    except FileNotFoundError:
        print("[Error] --- Sublist3r tidak ditemukan. Pastikan Sublist3r terinstal dengan benar.")
    except Exception as e:
        print(f"[Error] --- Terjadi kesalahan: {e}")

def main():
    while True:
        print("[1] --- Scanning Domain")
        print("[2] --- Scanning Subdomain")
        print("[0] --- Exit")
        print("--------------------------------------------")
        
        pilihan = input("Masukkan pilihan Anda: ").strip()
        
        if pilihan == "1":
            domain()
        elif pilihan == "2":
            subdomain()
        elif pilihan == "0":
            print("Bye!!")
            break
        else:
            print("[Error] --- Masukkan nomor sesuai pilihan Anda")

if __name__ == "__main__":
    main()
