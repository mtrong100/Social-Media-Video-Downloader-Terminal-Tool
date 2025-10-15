import os
import sys
import subprocess
import platform
from colorama import Fore, Style, init
import yt_dlp as youtube_dlp

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
        return os.path.join(os.environ.get("USERPROFILE", ""), "Downloads")
    else:
        return os.path.join(os.path.expanduser("~"), "Downloads")

def has_cookie_file():
    return os.path.exists("cookies.txt")

def format_duration(duration):
    """Định dạng thời lượng từ giây sang phút:giây"""
    try:
        duration = int(duration)
        return f"{duration // 60}:{duration % 60:02d}"
    except Exception:
        return "Không xác định"

def format_file_size(size_bytes):
    try:
        size_mb = size_bytes / (1024 * 1024)
        return f"{size_mb:.2f} MB"
    except Exception:
        return "Không xác định"

def progress_hook(d):
    if d['status'] == 'downloading':
        percent = d.get('_percent_str', 'N/A').strip()
        speed = d.get('_speed_str', 'N/A')
        eta = d.get('_eta_str', 'N/A')
        sys.stdout.write(f"\r{Fore.YELLOW}📥 Đang tải: {percent} | {speed} | ETA: {eta}{Style.RESET_ALL}")
        sys.stdout.flush()
    elif d['status'] == 'finished':
        print(f"\n{Fore.GREEN}✅ Hoàn thành tải xuống!{Style.RESET_ALL}")

def add_metadata_to_mp4(file_path, info):
    """Thêm metadata cho file MP4 bằng ffmpeg CLI"""
    try:
        title = info.get("title", "")
        uploader = info.get("uploader", "")
        description = info.get("description", "")

        temp_file = file_path.replace(".mp4", "_meta.mp4")

        cmd = [
            "ffmpeg",
            "-i", file_path,
            "-c", "copy",
            "-metadata", f"title={title}",
            "-metadata", f"artist={uploader}",
            "-metadata", f"comment={description}",
            "-y", temp_file  # overwrite nếu tồn tại
        ]

        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        os.replace(temp_file, file_path)
        print(f"{Fore.GREEN}📄 Đã thêm metadata vào video MP4{Style.RESET_ALL}")

    except subprocess.CalledProcessError:
        print(f"{Fore.RED}⚠️ Lỗi khi chạy ffmpeg để thêm metadata!{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}⚠️ Lỗi khi thêm metadata: {e}{Style.RESET_ALL}")

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

    if has_cookie_file():
        ydl_opts['cookiefile'] = "cookies.txt"
        print(f"{Fore.GREEN}🔐 Đã phát hiện file cookies.txt{Style.RESET_ALL}")

    try:
        with youtube_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"{Fore.CYAN}🔍 Đang lấy thông tin video...{Style.RESET_ALL}")
            info = ydl.extract_info(url, download=False)
            title = info.get("title", "Không xác định")
            duration = info.get("duration", 0)

            print(f"\n{Fore.LIGHTGREEN_EX}📹 Thông tin video:{Style.RESET_ALL}")
            print(f"   {Fore.WHITE}Tiêu đề: {title}{Style.RESET_ALL}")
            print(f"   {Fore.WHITE}Thời lượng: {format_duration(duration)}{Style.RESET_ALL}")
            print(f"   {Fore.WHITE}Chất lượng: Tốt nhất{Style.RESET_ALL}")

            if ("x.com" in url or "twitter.com" in url) and not has_cookie_file():
                print(f"\n{Fore.YELLOW}⚠️ Video Twitter/X có thể cần cookies.txt{Style.RESET_ALL}")

            print(f"\n{Fore.YELLOW}🚀 Bắt đầu tải xuống...{Style.RESET_ALL}")
            ydl.download([url])

            filename = ydl.prepare_filename(info)
            file_path = os.path.join(folder, os.path.basename(filename))

            file_size = os.path.getsize(file_path) if os.path.exists(file_path) else 0

            print(f"\n{Fore.LIGHTGREEN_EX}📂 Tải xuống hoàn tất:{Style.RESET_ALL}")
            print(f"   {Fore.WHITE}Tên file: {os.path.basename(filename)}{Style.RESET_ALL}")
            print(f"   {Fore.WHITE}Kích thước: {format_file_size(file_size)}{Style.RESET_ALL}")
            print(f"   {Fore.WHITE}Vị trí lưu: {folder}{Style.RESET_ALL}")

            # ✅ Thêm metadata
            add_metadata_to_mp4(file_path, info)

    except Exception as e:
        print(f"{Fore.RED}❌ Lỗi: {e}{Style.RESET_ALL}")

def main():
    clear_terminal()
    print_banner()

    while True:
        url = input(f"{Fore.MAGENTA}📎 Nhập URL video (hoặc gõ 'exit' để thoát): {Style.RESET_ALL}").strip()
        if url.lower() in ['exit', 'quit']:
            print(f"{Fore.CYAN}👋 Tạm biệt! Cảm ơn bạn đã sử dụng tool.{Style.RESET_ALL}")
            break

        if not url:
            print(f"{Fore.RED}⚠️ URL không hợp lệ! Vui lòng nhập lại.{Style.RESET_ALL}")
            continue

        download_video(url)
        print(f"\n{Fore.LIGHTCYAN_EX}✨ Hoàn tất tải video!{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}------------------------------------------{Style.RESET_ALL}\n")

if __name__ == "__main__":
    main()
