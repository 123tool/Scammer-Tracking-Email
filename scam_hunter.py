import re
import socket

def analyze_header(header_text):
    print("\n[+] Menganalisis Jejak Digital Penipu...")
    
    # 1. Mencari Alamat IP Pengirim (Received from)
    ip_pattern = r'\[(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\]'
    ips = re.findall(ip_pattern, header_text)
    
    if ips:
        print(f"[*] IP Publik Terdeteksi: {ips[-1]}")
        print(f"[*] Lokasi Server: https://www.ip2location.com/{ips[-1]}")
    else:
        print("[-] IP tidak ditemukan. Header mungkin terenkripsi.")

    # 2. Mencari Domain Pengirim
    from_pattern = r'From:.*<.*@(.*)>'
    domain = re.search(from_pattern, header_text)
    if domain:
        target_domain = domain.group(1)
        print(f"[*] Domain Sumber: {target_domain}")
        
        # Cek Provider (MX Record)
        try:
            import dns.resolver
            answers = dns.resolver.resolve(target_domain, 'MX')
            for rdata in answers:
                print(f"[*] Email Provider (Lapor Ke Sini): {rdata.exchange}")
        except:
            print("[-] Gagal mengambil data MX.")

# Contoh Cara Pakai
if __name__ == "__main__":
    print("=== SCAMMER TRACKER PRO ===")
    header_input = input("Tempelkan Header Email di sini (lalu tekan Enter): ")
    analyze_header(header_input)
