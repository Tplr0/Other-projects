# Minecraft Server Pinger

**Ping Status Monitor for Minecraft Servers**
This Python project allows you to ping Minecraft servers and check their availability and basic metadata. It was built as a lightweight utility tool to monitor server responsiveness using Python libraries.

---

## **Features**

* Ping any Minecraft server using its IP address
* Display latency and connection status
* Optionally view server metadata (MOTD, player count, etc.)
* Terminal-based tool with simple execution

---

## **Prerequisites**

To run this project, you’ll need:

* Python 3.6 or newer
* `mcstatus` library (for pinging Minecraft servers)

Install the required library:

```bash
pip install mcstatus
```

---

## **Getting Started**

*Clone the Repository:*

```
git clone https://github.com/yourusername/minecraft-server-pinger.git
cd minecraft-server-pinger
```

*Run the Script:*

```
python ping_server.py
```

---

## **Usage**

* Edit `ping_server.py` to input your server IP or pass it as an argument (if supported)
* Run from command line and observe latency stats
* Use this tool to monitor uptime or troubleshoot server issues

---

## **Troubleshooting**

* `ModuleNotFoundError`: Install missing libraries using `pip`
* `ConnectionRefusedError`: Ensure server IP is correct and online
* Python errors: Confirm you're using a compatible Python version

---

## **Acknowledgments**

This project was created as a Python utility for learning and personal use. It uses the open-source [mcstatus](https://github.com/Dinnerbone/mcstatus) library. Please use it responsibly—this code is shared for educational purposes only and is not intended for abuse or unauthorized server monitoring.
