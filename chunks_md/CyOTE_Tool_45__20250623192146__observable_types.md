---
tool: CyOTE_Tool_45
section: observable_types
chunk_id: a158000a8151
timestamp: 2025-06-23 19:21:46
---

> **Summary:** # 👁 Observable Types   ## None (Host)  Presence or inspection of device firmware versions and status. Example on Windows: Querying BIOS version via WMI. Example on Linux: Reading firmware versions in /sys/class/dmi. Real-world scenario: Detect outdated RTU firmware vulnerable to exploitation.  ## No...

# 👁 Observable Types


## None (Host)

Presence or inspection of device firmware versions and status. Example on Windows: Querying BIOS version via WMI. Example on Linux: Reading firmware versions in /sys/class/dmi. Real-world scenario: Detect outdated RTU firmware vulnerable to exploitation.

## None (Host)

Modification of embedded firmware to alter device behavior. Example on Windows: Firmware rootkit modifying BIOS to persist malware. Example on Linux: UEFI firmware overwrite using fwupd. Real-world scenario: Attacker re-flashes PLC firmware to override safety logic.

## None (Host)

Presence and attributes of user accounts. Example on Windows: Listing local users with net user. Example on Linux: Parsing /etc/passwd. Real-world scenario: Suspicious new account added to DCS operator group.

## None (Host)

Authentication activity by user accounts. Example on Windows: Logon events in Security logs (Event ID 4624). Example on Linux: Auth log entries in /var/log/auth.log. Real-world scenario: Brute-force login attempts on ICS engineering workstation.

## None (Host)

Detection or modification of automated scheduled tasks. Example on Windows: Scheduled task created via schtasks. Example on Linux: Cron job inserted into /etc/crontab. Real-world scenario: Attacker installs periodic backdoor beacon task.

## None (Host)

Detection or modification of automated scheduled tasks. Example on Windows: Scheduled task created via schtasks. Example on Linux: Cron job inserted into /etc/crontab. Real-world scenario: Attacker installs periodic backdoor beacon task.

## None (Host)

Detection or modification of automated scheduled tasks. Example on Windows: Scheduled task created via schtasks. Example on Linux: Cron job inserted into /etc/crontab. Real-world scenario: Attacker installs periodic backdoor beacon task.

## None (Host)

Detection or modification of automated scheduled tasks. Example on Windows: Scheduled task created via schtasks. Example on Linux: Cron job inserted into /etc/crontab. Real-world scenario: Attacker installs periodic backdoor beacon task.

## None (Host)

Observation related to Process. Includes host-based indicators such as account, process, file, or service activity. Applicable to endpoint monitoring in both IT and ICS environments.

## None (Host)

Observation related to Process: OS API Execution. Includes host-based indicators such as account, process, file, or service activity. Applicable to endpoint monitoring in both IT and ICS environments.

## None (Host)

Creation of new system processes. Example on Windows: PowerShell spawning rundll32.exe. Example on Linux: Reverse shell initiated by netcat process. Real-world scenario: Malicious HMI application spawns unauthorized control processes.

## None (Host)

Observation related to Process: Process Metadata. Includes host-based indicators such as account, process, file, or service activity. Applicable to endpoint monitoring in both IT and ICS environments.

## None (Host)

Observation related to Process: Process Termination. Includes host-based indicators such as account, process, file, or service activity. Applicable to endpoint monitoring in both IT and ICS environments.

## None (Host)

Observation related to Module. Includes host-based indicators such as account, process, file, or service activity. Applicable to endpoint monitoring in both IT and ICS environments.

## None (Host)

Observation related to Module: Module Load. Includes host-based indicators such as account, process, file, or service activity. Applicable to endpoint monitoring in both IT and ICS environments.

## None (Host)

Observation related to Script. Includes host-based indicators such as account, process, file, or service activity. Applicable to endpoint monitoring in both IT and ICS environments.

## None (Host)

Observation related to Script: Script Execution. Includes host-based indicators such as account, process, file, or service activity. Applicable to endpoint monitoring in both IT and ICS environments.

## None (Host)

Observation related to Application Log. Includes host-based indicators such as account, process, file, or service activity. Applicable to endpoint monitoring in both IT and ICS environments.

## None (Host)

Observation related to Application Log: Application Log Content. Includes host-based indicators such as account, process, file, or service activity. Applicable to endpoint monitoring in both IT and ICS environments.

## None (Host)

Observation related to Drive. Includes host-based indicators such as account, process, file, or service activity. Applicable to endpoint monitoring in both IT and ICS environments.

## None (Host)

Observation related to Drive: Drive Creation. Includes host-based indicators such as account, process, file, or service activity. Applicable to endpoint monitoring in both IT and ICS environments.

## None (Host)

Observation related to Drive: Drive Modification. Includes host-based indicators such as account, process, file, or service activity. Applicable to endpoint monitoring in both IT and ICS environments.

## None (Host)

Observation related to Command. Includes host-based indicators such as account, process, file, or service activity. Applicable to endpoint monitoring in both IT and ICS environments.

## None (Host)

Execution of system-level commands or scripts. Example on Windows: cmd.exe runs base64-encoded payload. Example on Linux: Bash executes reverse shell via curl|bash. Real-world scenario: Remote operator executes PLC debug commands.

## None (Host)

Creation or modification of services that persist or execute on boot. Example on Windows: Malicious service registered via sc.exe. Example on Linux: New systemd unit file in /etc/systemd/system. Real-world scenario: Backdoor installed as ICS alarm monitoring service.

## None (Host)

Creation or modification of services that persist or execute on boot. Example on Windows: Malicious service registered via sc.exe. Example on Linux: New systemd unit file in /etc/systemd/system. Real-world scenario: Backdoor installed as ICS alarm monitoring service.

## None (Host)

Creation or modification of services that persist or execute on boot. Example on Windows: Malicious service registered via sc.exe. Example on Linux: New systemd unit file in /etc/systemd/system. Real-world scenario: Backdoor installed as ICS alarm monitoring service.

## None (Host)

Creation or modification of services that persist or execute on boot. Example on Windows: Malicious service registered via sc.exe. Example on Linux: New systemd unit file in /etc/systemd/system. Real-world scenario: Backdoor installed as ICS alarm monitoring service.

## None (Host)

Observation related to File. Includes host-based indicators such as account, process, file, or service activity. Applicable to endpoint monitoring in both IT and ICS environments.

## None (Host)

Observation related to File: File Access. Includes host-based indicators such as account, process, file, or service activity. Applicable to endpoint monitoring in both IT and ICS environments.

## None (Host)

Detection of new files created on disk. Example on Windows: New DLL dropped in System32. Example on Linux: Web shell uploaded to /var/www/html. Real-world scenario: Exploit payload written to PLC config directory.

## None (Host)

Observation related to File: File Deletion. Includes host-based indicators such as account, process, file, or service activity. Applicable to endpoint monitoring in both IT and ICS environments.

## None (Host)

Observation related to File: File Metadata. Includes host-based indicators such as account, process, file, or service activity. Applicable to endpoint monitoring in both IT and ICS environments.

## None (Host)

Observation related to File: File Modification. Includes host-based indicators such as account, process, file, or service activity. Applicable to endpoint monitoring in both IT and ICS environments.

## None (Host)

Changes to Windows Registry keys or values. Example: Autorun value added to HKCU\Software\Microsoft\Windows\CurrentVersion\Run. Real-world scenario: ICS software persistence via registry run key.

## None (Host)

Changes to Windows Registry keys or values. Example: Autorun value added to HKCU\Software\Microsoft\Windows\CurrentVersion\Run. Real-world scenario: ICS software persistence via registry run key.

## None (Host)

Changes to Windows Registry keys or values. Example: Autorun value added to HKCU\Software\Microsoft\Windows\CurrentVersion\Run. Real-world scenario: ICS software persistence via registry run key.

## None (Host)

Observation related to Logon Session. Includes host-based indicators such as account, process, file, or service activity. Applicable to endpoint monitoring in both IT and ICS environments.

## None (Host)

Observation related to Logon Session: Logon Session Creation. Includes host-based indicators such as account, process, file, or service activity. Applicable to endpoint monitoring in both IT and ICS environments.

## None (Host)

Observation related to Logon Session: Logon Session Metadata. Includes host-based indicators such as account, process, file, or service activity. Applicable to endpoint monitoring in both IT and ICS environments.

## None (Network)

Network observable related to Network Traffic. Covers connection behavior, flow metadata, and content patterns. Used in anomaly detection for ICS protocol misuse or lateral movement.

## None (Network)

Creation of new network connections between hosts. Example on Windows: Outbound TCP to known C2 IP via svchost.exe. Example on Linux: SSH connection to nonstandard port. Real-world scenario: Unauthorized ICS device opens connection to external IP.

## None (Network)

Raw content within network sessions. Example: Extracted payload from Modbus TCP session. Real-world scenario: Sensitive control commands seen in cleartext ICS protocol stream.

## None (Network)

Network observable related to Network Traffic: Network Traffic Flow. Covers connection behavior, flow metadata, and content patterns. Used in anomaly detection for ICS protocol misuse or lateral movement.

## None (Network)

Network observable related to Network Share. Covers connection behavior, flow metadata, and content patterns. Used in anomaly detection for ICS protocol misuse or lateral movement.

## None (Network)

Network observable related to Network Share: Network Share Access. Covers connection behavior, flow metadata, and content patterns. Used in anomaly detection for ICS protocol misuse or lateral movement.

## None (Host)

Observation related to Asset. Includes host-based indicators such as account, process, file, or service activity. Applicable to endpoint monitoring in both IT and ICS environments.

## None (Host)

Observation related to Asset: Asset Inventory. Includes host-based indicators such as account, process, file, or service activity. Applicable to endpoint monitoring in both IT and ICS environments.

## None (Host)

Observation related to Asset: Software. Includes host-based indicators such as account, process, file, or service activity. Applicable to endpoint monitoring in both IT and ICS environments.

## None (Host)

Observation related to Operational Databases. Includes host-based indicators such as account, process, file, or service activity. Applicable to endpoint monitoring in both IT and ICS environments.

## None (Host)

Observation related to Operational Databases: Device Alarm. Includes host-based indicators such as account, process, file, or service activity. Applicable to endpoint monitoring in both IT and ICS environments.

## None (Host)

Observation related to Operational Databases: Process History/Live Data. Includes host-based indicators such as account, process, file, or service activity. Applicable to endpoint monitoring in both IT and ICS environments.

## None (Host)

Observation related to Operational Databases: Process/Event Alarm. Includes host-based indicators such as account, process, file, or service activity. Applicable to endpoint monitoring in both IT and ICS environments.