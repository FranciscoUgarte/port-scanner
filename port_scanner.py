import socket
import argparse
import time

def scan_ports(host, ports, output_file):
    print(f"📡 Scanning host: {host}")
    results = []

    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((host, port))

            if result == 0:
                status = f"✅ Port {port} is OPEN"
            else:
                status = f"❌ Port {port} is CLOSED"

            print(status)
            results.append(status)
            sock.close()
        except socket.error as err:
            error_msg = f"Error: {err}"
            print(error_msg)
            results.append(error_msg)
            break

    # Guardar en archivo de texto
    with open(output_file, "w") as f:
        f.write(f"Scan results for {host}:\n")
        f.write("\n".join(results))
        f.write(f"\n\nCompleted in {time.time() - start_time:.2f} seconds.")

    print(f"\n📁 Results saved to {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple Port Scanner with log output")
    parser.add_argument("host", help="IP address or domain to scan")
    parser.add_argument("--start", type=int, default=1, help="Start port (default: 1)")
    parser.add_argument("--end", type=int, default=1024, help="End port (default: 1024)")
    parser.add_argument("--output", default="scan_results.txt", help="Output file name")

    args = parser.parse_args()
    target_ports = list(range(args.start, args.end + 1))

    start_time = time.time()
    scan_ports(args.host, target_ports, args.output)
