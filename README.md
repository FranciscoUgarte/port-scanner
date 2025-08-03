# 🔎 Port Scanner (Python)

A simple command-line **Port Scanner** written in Python that checks which ports are open on a given host. It uses the `socket` module and can export results to a `.txt` file.

## 🚀 How to Use

### ✅ Requirements
- Python 3.x
- No external libraries required

### ▶️ Run the script

```bash
python port_scanner.py <host> --start <start_port> --end <end_port> --output <filename.txt>
```

### 📌 Example:

```bash
python port_scanner.py scanme.nmap.org --start 20 --end 100 --output scan_results.txt
```

### 🧪 Sample Output

```
📡 Scanning host: scanme.nmap.org
❌ Port 20 is CLOSED
✅ Port 22 is OPEN
✅ Port 80 is OPEN
⏱️ Scan completed in 3.42 seconds.
📁 Results saved to scan_results.txt
```

## 📄 Output

All results will be saved to a `.txt` file in the same directory.

## ⚠️ Disclaimer

> This tool is intended for **educational purposes only**.  
> Do not scan systems or networks without explicit permission.

