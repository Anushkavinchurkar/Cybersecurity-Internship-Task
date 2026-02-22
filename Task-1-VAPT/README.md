Task 1 – Vulnerability Assessment  (VA)


🧭 Objective
The objective of this task is to perform basic vulnerability assessment on a target system using Nmap. The goal is to identify open ports, detect running services, and gather operating system information to understand potential security risks.

🛠 Tools Used
Kali Linux
Nmap

🧪 Methodology
1️⃣ Service Version Detection
To identify running services and their versions:
nmap -sV 127.0.0.1
This command scans open ports and attempts to determine the service and version running on each port.

2️⃣ Operating System Detection
To detect operating system details:
nmap -O 127.0.0.1
This command performs OS fingerprinting to estimate the target system’s operating system.

🔎 Findings
Identified open ports on the target system.
Detected active services along with their versions.
Attempted OS detection through fingerprinting techniques.
Observed exposed services that may increase the system’s attack surface.

⚠️ Security Risk Analysis
The presence of open ports and exposed services can pose security risks such as:
Unauthorized access attempts
Exploitation of outdated service versions
Information disclosure during reconnaissance
Increased attack surface
If not properly secured using firewall rules, service hardening, and regular patch updates, these services could be targeted by attackers.

📊 Evidence
The following evidence is attached in this repository:
Nmap service version scan screenshot
OS detection screenshot
Vulnerability scan output
Detailed VAPT report (PDF)

✅ Conclusion
The Nmap scan successfully identified open ports, running services, and system information. This assessment demonstrates how reconnaissance techniques can reveal valuable information about a target system. Proper security measures such as closing unnecessary ports, updating services, and implementing firewall protections are recommended to reduce potential risks.
