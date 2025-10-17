# 🌀 SOCIAL MEDIA VIDEO DOWNLOADER

Tải video từ **YouTube, TikTok, Facebook, Instagram, Twitter/X**... với chất lượng tốt nhất.

---

## 📸 Screenshot
![Screenshot](https://i.postimg.cc/zvNbkkHj/Screenshot-2025-10-17-153439.png)

## 🚀 Tính năng

- Hỗ trợ tải video từ nhiều nền tảng phổ biến
- Tự động chọn **chất lượng tốt nhất**
- Hiển thị **tiến trình tải**
- Hỗ trợ **cookies.txt** cho các trang yêu cầu đăng nhập (như Twitter/X)
- Tự động lưu video vào **thư mục Downloads mặc định của hệ điều hành**

---

## 🧩 Yêu cầu cài đặt

### 1️⃣ Cài Python

Tải Python mới nhất tại: [https://www.python.org/downloads/](https://www.python.org/downloads/)

Trong quá trình cài đặt, hãy **tích chọn “Add Python to PATH”**.

### 2️⃣ Cài thư viện cần thiết

Mở terminal/cmd tại thư mục chứa `app.py` và chạy:

```bash
pip install yt-dlp colorama
```

---

## ⚙️ Cách sử dụng

1. Mở terminal trong thư mục chứa file `app.py`
2. Chạy lệnh:
   ```bash
   python app.py
   ```
3. Nhập **URL video** muốn tải
4. Tool sẽ:
   - Tự động chọn chất lượng cao nhất
   - Hiển thị tiến trình tải
   - Lưu file vào thư mục **Downloads**

---

## 🔐 (Tuỳ chọn) Sử dụng cookies.txt cho Twitter/X

Một số video trên Twitter/X yêu cầu **cookies** để tải.

Cách lấy file cookies.txt:

1. Cài extension trình duyệt **Get cookies.txt** [tại đây](https://github.com/mtrong100/Extension-Get-Cookies-With-YT-DLP-Format)
2. Vào trang **x.com** (hoặc **twitter.com**), đăng nhập
3. Export cookies và lưu file thành **cookies.txt** trong cùng thư mục với `app.py`

---

## 📁 Vị trí file tải về

- **Windows:** `C:\Users\<Tên người dùng>\Downloads`
- **Mac/Linux:** `~/Downloads`

---

## 🧰 Thông tin kỹ thuật

- **Ngôn ngữ:** Python 3
- **Thư viện:** yt-dlp, colorama
- **File chính:** `app.py`
- **Kiểu lưu:** MP4 (video tốt nhất + audio tốt nhất)

---

## 💡 Mẹo nhỏ

- Nếu tải video từ Twitter/X bị lỗi, hãy chắc chắn có `cookies.txt`
- Có thể đổi tên file sau khi tải nếu tiêu đề video quá dài

---

## ❤️ Cảm ơn bạn đã sử dụng!

Nếu thấy hữu ích, hãy ⭐ repo hoặc chia sẻ tool này!
