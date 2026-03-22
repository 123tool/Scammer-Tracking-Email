## 🚀 Fitur
- **IP Extraction**: Mengambil IP pengirim dari email header.
- **MX Lookup**: Mengetahui provider email penipu untuk pelaporan (abuse report).
- **Geo-Tracking Link**: Menghasilkan link pelacakan lokasi IP otomatis.

## 📲 Instalasi (Termux)
```bash
pkg update && pkg upgrade
pkg install python
pip install dnspython requests
git clone [https://github.com/123tool/Scammer-Tracking-Email.git](https://github.com/123tool/Scammer-Tracking-Email.git)
cd Scammer-Tracking-Email
python scam_hunter.py

Atau

git init
git add .
git commit -m "Initial release: Scammer Investigation Tool"
git branch -M main
git remote add origin https://github.com/123tool/Scammer-Tracking-Email.git
git push -u origin main
