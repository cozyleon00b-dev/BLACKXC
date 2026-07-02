# 📘 BLACKXC — TUTORIAL LENGKAP / FULL TUTORIAL / ПОЛНОЕ РУКОВОДСТВО

---

## 🇬🇧 ENGLISH

### 📌 What is BLACKXC?
**BLACKXC** is an advanced bug hunting and security analysis tool with:
- Real DDOS Engine (HTTP Flood, SYN Flood, SSL Renegotiation)
- Cloudflare & Bot Bypass
- Vulnerability Scanner (SQLi, XSS, CSRF, etc.)
- Subdomain & Admin Panel Finder
- Data Dump Simulation (FBI/CIA)
- Role-Based Access (Member, VIP, Developer)

> ⚠️ **DISCLAIMER**: This tool is for **EDUCATIONAL PURPOSES ONLY**. Use only on systems you own or have explicit permission to test. The author is not responsible for any misuse.

---

### 🔧 Installation & Setup

#### 1. Clone Repository
```bash
git clone https://github.com/cozyleon00b-dev/BLACKXC.git
cd BLACKXC
```

#### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

#### 3. Decrypt Files (IMPORTANT!)
All source files are encrypted for security. You must decrypt them before running:
```bash
python encryptor.py
# Select: 2 (Decrypt All Files)
```

#### 4. Run BLACKXC
```bash
python main.py
```

---

### 🔑 Authentication Keys

| Role | Auth Key |
|------|----------|
| **Member** | `CozyStoreID` |

---

### 🛠️ Features by Role

| Feature | Member | VIP | Developer |
|---------|--------|-----|-----------|
| Free Tools (Ping, DNS, IP, Port) | ✅ | ✅ | ✅ |
| VIP Tools (Subdomain, SSL, Headers) | ❌ | ✅ | ✅ |
| Dump Data (FBI/CIA) | ✅ | ✅ | ✅ |
| Real DDOS Attack | ❌ | ✅ | ✅ |
| Cloudflare Bypass | ❌ | ✅ | ✅ |
| Bug Checker (Limited) | ✅ | ✅ | ✅ |
| Admin Panel | ❌ | ❌ | ✅ |

---

### 🔐 Encryption / Decryption Guide

All Python files in this repository are **encrypted** to protect the source code.

#### To Encrypt (before pushing to GitHub):
```bash
python encryptor.py
# Select: 1 (Encrypt All Files)
```

#### To Decrypt (before running or editing):
```bash
python encryptor.py
# Select: 2 (Decrypt All Files)
```

> ⚠️ **DO NOT** upload `master.key` or `secret.key` to GitHub — they are already in `.gitignore`.

---

### 📂 Folder Structure

```
BLACKXC/
├── main.py          # Main entry point
├── admin.py         # Admin Panel (Developer only)
├── tools.py         # All tools (Free, VIP, Developer)
├── dump.py          # Data Dump Engine
├── database.py      # Database handler
├── utils.py         # Utility functions
├── encryptor.py     # Encryption / Decryption tool
├── requirements.txt # Dependencies
├── modules/
│   ├── attack.py    # Real DDOS Engine
│   ├── bypass.py    # Cloudflare & Bot Bypass
│   └── checker.py   # Bug Checker (Vulnerability Scanner)
└── results/         # Generated reports (auto-created)
```

---

### 🧪 Quick Test

1. Run `python main.py`
2. Enter auth key: `Leoxdev` (Developer)
3. Select `[4] Real DDOS Attack`
4. Enter target URL (e.g., `https://httpbin.org/get`)
5. Select attack method and threads
6. Press Enter to stop attack

---

### 📜 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

### 👤 Author

**cozyleon00b-dev**  
GitHub: [cozyleon00b-dev](https://github.com/cozyleon00b-dev)

---

---

## 🇮🇩 BAHASA INDONESIA

### 📌 Apa itu BLACKXC?
**BLACKXC** adalah alat bug hunting dan analisis keamanan canggih dengan fitur:
- Mesin DDOS Nyata (HTTP Flood, SYN Flood, SSL Renegotiation)
- Bypass Cloudflare & Bot
- Pemindai Kerentanan (SQLi, XSS, CSRF, dll.)
- Pencari Subdomain & Panel Admin
- Simulasi Dump Data (FBI/CIA)
- Akses Berbasis Peran (Member, VIP, Developer)

> ⚠️ **DISCLAIMER**: Alat ini untuk **TUJUAN EDUKASI SAJA**. Gunakan hanya di sistem yang Anda miliki atau memiliki izin eksplisit. Penulis tidak bertanggung jawab atas penyalahgunaan.

---

### 🔧 Instalasi & Persiapan

#### 1. Clone Repository
```bash
git clone https://github.com/cozyleon00b-dev/BLACKXC.git
cd BLACKXC
```

#### 2. Install Dependensi
```bash
pip install -r requirements.txt
```

#### 3. Dekripsi File (PENTING!)
Semua file sumber dienkripsi demi keamanan. Anda harus mendekripsi sebelum menjalankan:
```bash
python encryptor.py
# Pilih: 2 (Decrypt All Files)
```

#### 4. Jalankan BLACKXC
```bash
python main.py
```

---

### 🔑 Kunci Autentikasi

| Peran | Kunci Auth |
|-------|------------|
| **Member** | `CozyStoreID` |

---

### 🛠️ Fitur Berdasarkan Peran

| Fitur | Member | VIP | Developer |
|-------|--------|-----|-----------|
| Tools Gratis (Ping, DNS, IP, Port) | ✅ | ✅ | ✅ |
| Tools VIP (Subdomain, SSL, Headers) | ❌ | ✅ | ✅ |
| Dump Data (FBI/CIA) | ✅ | ✅ | ✅ |
| Serangan DDOS Nyata | ❌ | ✅ | ✅ |
| Bypass Cloudflare | ❌ | ✅ | ✅ |
| Bug Checker (Terbatas) | ✅ | ✅ | ✅ |
| Panel Admin | ❌ | ❌ | ✅ |

---

### 🔐 Panduan Enkripsi / Dekripsi

Semua file Python di repositori ini **dienkripsi** untuk melindungi kode sumber.

#### Untuk Enkripsi (sebelum push ke GitHub):
```bash
python encryptor.py
# Pilih: 1 (Encrypt All Files)
```

#### Untuk Dekripsi (sebelum menjalankan atau mengedit):
```bash
python encryptor.py
# Pilih: 2 (Decrypt All Files)
```

> ⚠️ **JANGAN** upload `master.key` atau `secret.key` ke GitHub — sudah ada di `.gitignore`.

---

### 📂 Struktur Folder

```
BLACKXC/
├── main.py          # Entry point utama
├── admin.py         # Panel Admin (Developer only)
├── tools.py         # Semua tools (Free, VIP, Developer)
├── dump.py          # Mesin Dump Data
├── database.py      # Handler database
├── utils.py         # Fungsi utilitas
├── encryptor.py     # Alat Enkripsi / Dekripsi
├── requirements.txt # Dependensi
├── modules/
│   ├── attack.py    # Mesin DDOS Nyata
│   ├── bypass.py    # Bypass Cloudflare & Bot
│   └── checker.py   # Bug Checker (Pemindai Kerentanan)
└── results/         # Laporan yang dihasilkan (otomatis)
```

---

### 🧪 Uji Cepat

1. Jalankan `python main.py`
2. Masukkan kunci auth: `Leoxdev` (Developer)
3. Pilih `[4] Real DDOS Attack`
4. Masukkan URL target (contoh: `https://httpbin.org/get`)
5. Pilih metode serangan dan jumlah thread
6. Tekan Enter untuk menghentikan serangan

---

### 📜 Lisensi

Proyek ini dilisensikan di bawah **MIT License** — lihat file [LICENSE](LICENSE) untuk detail.

---

### 👤 Penulis

**cozyleon00b-dev**  
GitHub: [cozyleon00b-dev](https://github.com/cozyleon00b-dev)

---

---

## 🇷🇺 РУССКИЙ

### 📌 Что такое BLACKXC?
**BLACKXC** — это продвинутый инструмент для баг-хантинга и анализа безопасности с функциями:
- Реальный DDOS-движок (HTTP Flood, SYN Flood, SSL Renegotiation)
- Обход Cloudflare и ботов
- Сканер уязвимостей (SQLi, XSS, CSRF и др.)
- Поиск субдоменов и админ-панелей
- Симуляция дампов данных (FBI/CIA)
- Доступ на основе ролей (Member, VIP, Developer)

> ⚠️ **ПРЕДУПРЕЖДЕНИЕ**: Этот инструмент предназначен **ТОЛЬКО ДЛЯ ОБРАЗОВАТЕЛЬНЫХ ЦЕЛЕЙ**. Используйте только на системах, которыми вы владеете или имеете явное разрешение. Автор не несёт ответственности за неправомерное использование.

---

### 🔧 Установка и настройка

#### 1. Клонирование репозитория
```bash
git clone https://github.com/cozyleon00b-dev/BLACKXC.git
cd BLACKXC
```

#### 2. Установка зависимостей
```bash
pip install -r requirements.txt
```

#### 3. Дешифровка файлов (ВАЖНО!)
Все исходные файлы зашифрованы для безопасности. Вы должны расшифровать их перед запуском:
```bash
python encryptor.py
# Выберите: 2 (Decrypt All Files)
```

#### 4. Запуск BLACKXC
```bash
python main.py
```

---

### 🔑 Ключи аутентификации

| Роль | Ключ |
|------|------|
| **Member** | `CozyStoreID` |

---

### 🛠️ Функции по ролям

| Функция | Member | VIP | Developer |
|---------|--------|-----|-----------|
| Бесплатные инструменты (Ping, DNS, IP, Port) | ✅ | ✅ | ✅ |
| VIP-инструменты (Subdomain, SSL, Headers) | ❌ | ✅ | ✅ |
| Дамп данных (FBI/CIA) | ✅ | ✅ | ✅ |
| Реальная DDOS-атака | ❌ | ✅ | ✅ |
| Обход Cloudflare | ❌ | ✅ | ✅ |
| Bug Checker (ограниченный) | ✅ | ✅ | ✅ |
| Админ-панель | ❌ | ❌ | ✅ |

---

### 🔐 Руководство по шифрованию / дешифрованию

Все Python-файлы в этом репозитории **зашифрованы** для защиты исходного кода.

#### Для шифрования (перед отправкой в GitHub):
```bash
python encryptor.py
# Выберите: 1 (Encrypt All Files)
```

#### Для дешифровки (перед запуском или редактированием):
```bash
python encryptor.py
# Выберите: 2 (Decrypt All Files)
```

> ⚠️ **НЕ** загружайте `master.key` или `secret.key` в GitHub — они уже в `.gitignore`.

---

### 📂 Структура папок

```
BLACKXC/
├── main.py          # Главная точка входа
├── admin.py         # Админ-панель (только Developer)
├── tools.py         # Все инструменты (Free, VIP, Developer)
├── dump.py          # Движок дампов данных
├── database.py      # Обработчик базы данных
├── utils.py         # Вспомогательные функции
├── encryptor.py     # Инструмент шифрования / дешифрования
├── requirements.txt # Зависимости
├── modules/
│   ├── attack.py    # Реальный DDOS-движок
│   ├── bypass.py    # Обход Cloudflare и ботов
│   └── checker.py   # Bug Checker (сканер уязвимостей)
└── results/         # Сгенерированные отчёты (создаются автоматически)
```

---

### 🧪 Быстрый тест

1. Запустите `python main.py`
2. Введите ключ авторизации: `Leoxdev` (Developer)
3. Выберите `[4] Real DDOS Attack`
4. Введите URL цели (например: `https://httpbin.org/get`)
5. Выберите метод атаки и количество потоков
6. Нажмите Enter для остановки атаки

---

### 📜 Лицензия

Этот проект лицензирован под **MIT License** — подробности в файле [LICENSE](LICENSE).

---

### 👤 Автор

**cozyleon00b-dev**  
GitHub: [cozyleon00b-dev](https://github.com/cozyleon00b-dev)

---

## 📌 Ссылки / Links / Tautan

- **GitHub**: https://github.com/cozyleon00b-dev/BLACKXC
- **Issues**: https://github.com/cozyleon00b-dev/BLACKXC/issues
- **License**: MIT (see LICENSE file)

---

**© 2026 cozyleon00b-dev — BLACKXC. All Rights Reserved.**

---

## 🚀 **CARA UPLOAD `Tutorial.md` KE GITHUB**

### ✅ **CARA 1 — LEWAT WEB GITHUB**
1. Buka repo lo: `https://github.com/cozyleon00b-dev/BLACKXC`
2. Klik **"Add file"** → **"Create new file"**
3. Kasih nama: `Tutorial.md`
4. **PASTE** semua isi di atas
5. Klik **"Commit new file"**

### ✅ **CARA 2 — LEWAT GIT (CMD)**
```cmd
cd C:\Users\asus\Downloads\Project Besar\BLACKXC
notepad Tutorial.md
# Paste semua isi di atas, simpan

git add Tutorial.md
git commit -m "Add Tutorial.md — 3 Languages"
git push
```

**© 2026 cozyleon00b-dev — BLACKXC. All Rights Reserved.**
