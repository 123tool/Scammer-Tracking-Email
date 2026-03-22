## 🚀 Fitur
- **IP Extraction**: Mengambil IP pengirim dari email header.
- **MX Lookup**: Mengetahui provider email penipu untuk pelaporan (abuse report).
- **Geo-Tracking Link**: Menghasilkan link pelacakan lokasi IP otomatis.

## 📲 Instalasi (Termux)
```bash
pkg update && pkg upgrade
pkg install python
pip install dnspython requests
git clone [https://github.com/username/scammer-tracker.git](https://github.com/username/scammer-tracker.git)
cd scammer-tracker
python scam_hunter.py

Atau

git init
git add .
git commit -m "Initial release: Scammer Investigation Tool"
git branch -M main
git remote add origin https://github.com/USERNAME_KAMU/NAMA_REPO.git
git push -u origin main
