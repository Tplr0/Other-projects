from mcstatus import JavaServer
import socket
import os
import time
import threading
from tqdm import tqdm

# Global flag to stop loading bar
done_loading = False

# ANSI color codes
Green = "\033[92m"
RESET = "\033[0m"

def ensure_server_file():
    if not os.path.exists("server.txt"):
        with open("server.txt", "w") as f:
            pass

def get_server_address():
    user_input = input("Enter Minecraft server IP (leave blank to load from server.txt): ").strip()
    if " " in user_input:
        print("You entered multiple IPs. Please enter only one.")
        return get_server_address()
    if user_input:
        save_if_not_exists(user_input)
        return user_input
    else:
        with open("server.txt", "r") as file:
            lines = [line.strip() for line in file if line.strip()]
            if not lines:
                print("server.txt is empty.")
                exit()
            print("Available saved servers:")
            for i, line in enumerate(lines, 1):
                print(f"{i}. {line}")
            choice = input("Select server number: ").strip()
            if choice.isdigit() and 1 <= int(choice) <= len(lines):
                return lines[int(choice) - 1]
            else:
                print("Invalid choice.")
                exit()

def save_if_not_exists(ip):
    if " " in ip:
        print("Invalid server address: contains spaces. Please check your input.")
        return

    with open("server.txt", "r") as file:
        existing_ips = [line.strip() for line in file if line.strip()]

    if ip not in existing_ips:
        save = input(f"'{ip}' is not in server.txt. Save it? (y/n): ").strip().lower()
        if save == 'y':
            with open("server.txt", "a") as file:
                file.write(ip + "\n")
            print("Saved.")

def detect_server_type(ip):
    ip = ip.lower()
    if "aternos.me" in ip:
        return "Aternos (Free-hosted)"
    elif "hypixel.net" in ip:
        return "Hypixel (Public / Premium)"
    elif "minehut" in ip:
        return "Minehut (Free-hosted)"
    elif "cubecraft" in ip:
        return "CubeCraft (Public)"
    elif "mcplayhd" in ip or "gportal" in ip:
        return "Hosted (Community / Rented)"
    else:
        return "Custom / Unknown"

def loading_bar():
    with tqdm(
        total=100,
        desc=f"{Green}🌐 Connecting{RESET}",
        ncols=70,
        bar_format=f"{Green}{{l_bar}}{{bar}}{RESET} | {{n_fmt}}/{{total_fmt}} [{{elapsed}}<{{remaining}}, {{rate_fmt}}]"
    ) as bar:
        for _ in range(100):
            if done_loading:
                bar.n = bar.total  # instantly set bar to 100%
                bar.refresh()      # force redraw
                break
            time.sleep(0.03)
            bar.update(1)

def check_server_status(address):
    global done_loading
    try:
        server = JavaServer.lookup(address)
        status = server.status()
        done_loading = True  # moved up BEFORE printing

        server_type = detect_server_type(address)

        print("\n--- Server Status ---")
        print(f"✅ Server Online: Yes")
        print(f"🏷️ Server Type: {server_type}")
        print(f"IP: {address}")
        print(f"Version: {status.version.name}")
        print(f"Players: {status.players.online}/{status.players.max}")
        print(f"MOTD: {status.description}")
        print(f"Latency: {status.latency:.2f} ms")
    except (socket.timeout, ConnectionRefusedError, Exception) as e:
        done_loading = True  # also here for errors
        print("\n--- Server Status ---")
        print(f"❌ Server Online: No")
        print(f"Reason: {e}")

if __name__ == "__main__":
    ensure_server_file()
    server_ip = get_server_address()

    status_thread = threading.Thread(target=check_server_status, args=(server_ip,))
    status_thread.start()

    loading_bar()

    status_thread.join()
