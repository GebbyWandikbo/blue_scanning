import whois
import subprocess
import re

# Validasi domain
def validasi_domain(domain):
    return re.match(r'^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', domain) is not None

# Informasi Domain
def domain():
    add = input("Enter Your Domain Target (Example: example.com): ").strip()
    if not validasi_domain(add):
        print("[Error] --- Domain Is Not Valid.")
        return
    
    try:
        informasi = whois.whois(add)
        print("Here Is The Information Of Your Domain Target")
        print("--------------------------------------------\n")
        print(informasi)
    except Exception as e:
        print(f"[Error] --- Theres Someting Wrong: {e}")

# Subdomain
def subdomain():
    add = input("Enter Your Domain Target (Example: example.com): ").strip()
    if not validasi_domain(add):
        print("[Error] --- Domain Is Not valid.")
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
        print("Result Of Your Subdomain:")
        print(filtered_output)
    except FileNotFoundError:
        print("[Error] --- Sublist3r Is not fund. Make sure Sublist3r is installed.")
    except Exception as e:
        print(f"[Error] --- Theres Someting Wrong: {e}")

def main():
    while True:
        print("[1] --- Scanning Domain")
        print("[2] --- Scanning Subdomain")
        print("[0] --- Exit")
        print("--------------------------------------------")
        
        pilihan = input("Enter your choice: ").strip()
        
        if pilihan == "1":
            domain()
        elif pilihan == "2":
            subdomain()
        elif pilihan == "0":
            print("Bye!!")
            break
        else:
            print("[Error] --- Select The Number By The Options")

if __name__ == "__main__":
    main()
