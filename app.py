import os
import sys
from colorama import Fore, Style, init
import yt_dlp as youtube_dlp
import platform

# Khởi tạo colorama
init(autoreset=True)

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    banner = f"""
{Fore.CYAN + Style.BRIGHT}🌀 SOCIAL MEDIA VIDEO DOWNLOADER{Style.RESET_ALL}
{Fore.LIGHTCYAN_EX}Tải video từ YouTube, TikTok, Facebook, Instagram...{Style.RESET_ALL}
"""
    print(banner)

def get_download_folder():
    """Trả về thư mục Downloads mặc định"""
    if platform.system() == "Windows":
        downloads = os.path.join(os.environ.get("USERPROFILE", ""), "Downloads")
    else:
        downloads = os.path.join(os.path.expanduser("~"), "Downloads")
    
    return downloads

def has_cookie_file():
    """Kiểm tra xem file cookies.txt có tồn tại không"""
    return os.path.exists("cookies.txt")

def format_duration(duration):
    """Định dạng thời lượng từ giây sang phút:giây"""
    if not duration:
        return "Không xác định"
    
    try:
        duration = int(duration)
        minutes = duration // 60
        seconds = duration % 60
        return f"{minutes}:{seconds:02d}"
    except (ValueError, TypeError):
        return "Không xác định"

def format_file_size(size_bytes):
    """Định dạng kích thước file"""
    if not size_bytes:
        return "Không xác định"
    
    try:
        size_mb = size_bytes / (1024 * 1024)
        return f"{size_mb:.2f} MB"
    except (ValueError, TypeError):
        return "Không xác định"

def progress_hook(d):
    """Hiển thị tiến trình tải"""
    if d['status'] == 'downloading':
        percent = d.get('_percent_str', 'N/A').strip()
        speed = d.get('_speed_str', 'N/A')
        eta = d.get('_eta_str', 'N/A')
        sys.stdout.write(f"\r{Fore.YELLOW}📥 Đang tải: {percent} | {speed} | ETA: {eta}{Style.RESET_ALL}")
        sys.stdout.flush()
    elif d['status'] == 'finished':
        print(f"\n{Fore.GREEN}✅ Hoàn thành tải xuống!{Style.RESET_ALL}")

def download_video(url):
    folder = get_download_folder()

    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4',
        'outtmpl': os.path.join(folder, '%(title)s.%(ext)s'),
        'progress_hooks': [progress_hook],
        'noplaylist': True,
        'quiet': True,
        'ignoreerrors': True,
    }

    # Thêm cookies.txt nếu tồn tại
    if has_cookie_file():
        ydl_opts['cookiefile'] = "cookies.txt"
        print(f"{Fore.GREEN}🔐 Đã phát hiện file cookies.txt{Style.RESET_ALL}")

    try:
        with youtube_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"{Fore.CYAN}🔍 Đang lấy thông tin video...{Style.RESET_ALL}")
            info = ydl.extract_info(url, download=False)
            title = info.get("title", "Không xác định")
            duration = info.get('duration', 0)
            
            print(f"\n{Fore.LIGHTGREEN_EX}📹 Thông tin video:{Style.RESET_ALL}")
            print(f"   {Fore.WHITE}Tiêu đề: {title}{Style.RESET_ALL}")
            print(f"   {Fore.WHITE}Thời lượng: {format_duration(duration)}{Style.RESET_ALL}")
            print(f"   {Fore.WHITE}Chất lượng: Tốt nhất{Style.RESET_ALL}")
            
            # Cảnh báo cho Twitter/X nếu không có cookies
            if ("x.com" in url or "twitter.com" in url) and not has_cookie_file():
                print(f"\n{Fore.YELLOW}⚠️  Cảnh báo: Video Twitter/X có thể cần cookies.txt để tải{Style.RESET_ALL}")
                print(f"{Fore.YELLOW}   Tạo file cookies.txt trong thư mục tool để tải video Twitter/X{Style.RESET_ALL}")
            
            print(f"\n{Fore.YELLOW}🚀 Bắt đầu tải xuống...{Style.RESET_ALL}")
            ydl.download([url])
            
            # Hiển thị thông tin file sau khi tải xong
            filename = ydl.prepare_filename(info)
            file_path = os.path.join(folder, os.path.basename(filename))
            
            file_size = 0
            if os.path.exists(file_path):
                try:
                    file_size = os.path.getsize(file_path)
                except OSError:
                    file_size = 0
            
            print(f"\n{Fore.LIGHTGREEN_EX}📂 Tải xuống hoàn tất:{Style.RESET_ALL}")
            print(f"   {Fore.WHITE}Tên file: {os.path.basename(filename)}{Style.RESET_ALL}")
            print(f"   {Fore.WHITE}Kích thước: {format_file_size(file_size)}{Style.RESET_ALL}")
            print(f"   {Fore.WHITE}Vị trí lưu: {folder}{Style.RESET_ALL}")
            
    except Exception as e:
        error_msg = str(e)
        if ("x.com" in url or "twitter.com" in url) and "cookies" in error_msg.lower():
            print(f"\n{Fore.RED}❌ Lỗi Twitter/X: Cần file cookies.txt để tải video{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}💡 Hướng dẫn:{Style.RESET_ALL}")
            print(f"{Fore.WHITE}1. Sử dụng extension 'Get cookies.txt' trên trình duyệt{Style.RESET_ALL}")
            print(f"{Fore.WHITE}2. Export cookies từ twitter.com hoặc x.com{Style.RESET_ALL}")
            print(f"{Fore.WHITE}3. Lưu file thành cookies.txt trong thư mục tool{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}❌ Lỗi: {error_msg}{Style.RESET_ALL}")

def main():
    clear_terminal()
    print_banner()

    url = input(f"{Fore.MAGENTA}📎 Nhập URL video: {Style.RESET_ALL}").strip()
    if not url:
        print(f"{Fore.RED}⚠️ URL không hợp lệ!{Style.RESET_ALL}")
        return

    download_video(url)
    
    print(f"\n{Fore.LIGHTCYAN_EX}✨ Cảm ơn đã sử dụng tool!{Style.RESET_ALL}")

if __name__ == "__main__":
    main()