---
tool: CyOTE_Tool_45
section: data_sources
chunk_id: 2bc4f1f6852b
timestamp: 2025-06-23 19:21:46
---

> **Summary:** # 🗃️ Data Sources   ## DS0001 - None  Computer software that provides low-level control for the hardware and device(s) of a host, such as BIOS or UEFI/EFI  ### Component: None  Changes made to firmware, which may include its settings, configurations, or underlying data. This can encompass alteration...

# 🗃️ Data Sources


## DS0001 - None

Computer software that provides low-level control for the hardware and device(s) of a host, such as BIOS or UEFI/EFI

### Component: None

Changes made to firmware, which may include its settings, configurations, or underlying data. This can encompass alterations to the Master Boot Record (MBR), Volume Boot Record (VBR), or other firmware components critical to system boot and functionality. Such modifications are often indicators of adversary activity, including malware persistence and system compromise. Examples: 

- Changes to Master Boot Record (MBR): Modifying the MBR to load malicious code during the boot process.
- Changes to Volume Boot Record (VBR): Altering the VBR to redirect boot processes to malicious locations.
- Firmware Configuration Changes: Modifying BIOS/UEFI settings such as disabling Secure Boot.
- Firmware Image Tampering: Updating firmware with a malicious or unauthorized image.
- Logs or Errors Indicating Firmware Changes: Logs showing unauthorized firmware updates or checksum mismatches.

This data component can be collected through the following measures:

- BIOS/UEFI Logs: Enable and monitor BIOS/UEFI logs to capture settings changes or firmware updates.
- Firmware Integrity Monitoring: Use tools or firmware security features to detect changes to firmware components.
- Endpoint Detection and Response (EDR) Solutions: Many EDR platforms can detect abnormal firmware activity, such as changes to MBR/VBR or unauthorized firmware updates.
- File System Monitoring: Monitor changes to MBR/VBR-related files using tools like Sysmon or auditd.
    - Windows Example (Sysmon): Monitor Event ID 7 (Raw disk access).
    - Linux Example (auditd): `auditctl -w /dev/sda -p wa -k firmware_modification`
- Network Traffic Analysis: Capture firmware updates downloaded over the network, particularly from untrusted sources. Use network monitoring tools like Zeek or Wireshark to analyze firmware-related traffic.
- Secure Boot Logs: Collect and analyze Secure Boot logs for signs of tampering or unauthorized configurations. Example: Use PowerShell to retrieve Secure Boot settings on Windows: `Confirm-SecureBootUEFI`
- Vendor-Specific Firmware Tools: Many hardware vendors provide tools for firmware integrity checks.Examples:
    - Intel Platform Firmware Resilience (PFR).
    - Lenovo UEFI diagnostics.

## DS0002 - None

A profile representing a user, device, service, or application used to authenticate and access resources

### Component: None

An attempt (successful and failed login attempts) by a user, service, or application to gain access to a network, system, or cloud-based resource. This typically involves credentials such as passwords, tokens, multi-factor authentication (MFA), or biometric validation.

*Data Collection Measures:*

- Host-Based Authentication Logs
    - Windows Event Logs
        - Event ID 4776  NTLM authentication attempt.
        - Event ID 4624  Successful user logon.
        - Event ID 4625  Failed authentication attempt.
        - Event ID 4648  Explicit logon with alternate credentials.
    - Linux/macOS Authentication Logs
        - `/var/log/auth.log`, `/var/log/secure`  Logs SSH, sudo, and other authentication attempts.
        - AuditD  Tracks authentication events via PAM modules.
        - macOS Unified Logs  `/var/db/diagnostics` captures authentication failures.
- Cloud Authentication Logs
    - Azure AD Logs
        - Sign-in Logs  Tracks authentication attempts, MFA challenges, and conditional access failures.
        - Audit Logs  Captures authentication-related configuration changes.
        - Microsoft Graph API  Provides real-time sign-in analytics.
    - Google Workspace & Office 365
        - Google Admin Console  `User Login Report` tracks login attempts and failures.
        - Office 365 Unified Audit Logs  Captures logins across Exchange, SharePoint, and Teams.
    - AWS CloudTrail & IAM
        - Tracks authentication via `AWS IAM AuthenticateUser` and `sts:GetSessionToken`.
        - Logs failed authentications to AWS Management Console and API requests.
- Container Authentication Monitoring
    - Kubernetes Authentication Logs
        - kubectl audit logs  Captures authentication attempts for service accounts and admin users.
        - Azure Kubernetes Service (AKS) and Google Kubernetes Engine (GKE)  Logs IAM authentication events.

## DS0003 - None

Automated tasks that can be executed at a specific time or on a recurring schedule running in the background (ex: Cron daemon, task scheduler, BITS)(Citation: Microsoft Tasks)

### Component: None

The establishment of a task or job that will execute at a predefined time or based on specific triggers.

*Data Collection Measures: *

- Windows Event Logs:
    - Event ID 4698 (Scheduled Task Created)  Detects the creation of new scheduled tasks.
    - Event ID 4702 (Scheduled Task Updated)  Identifies modifications to existing scheduled jobs.
    - Event ID 106 (TaskScheduler Operational Log)  Provides details about scheduled task execution.
- Sysmon (Windows):
    - Event ID 1 (Process Creation)  Detects the execution of suspicious tasks started by `schtasks.exe`, `at.exe`, or `taskeng.exe`.
- Linux/macOS Monitoring:
    - AuditD: Monitor modifications to `/etc/cron*`, `/var/spool/cron/`, and `crontab` files.
    - Syslog: Capture cron job execution logs from `/var/log/cron`.
    - OSQuery: Query the `crontab` and `launchd` tables for scheduled job configurations.
- Endpoint Detection and Response (EDR) Tools:
    - Track scheduled task creation and modification events.
- SIEM & XDR Detection Rules:
    - Monitor for scheduled jobs created by unusual users.
    - Detect tasks executing scripts from non-standard directories.

### Component: None

Contextual data about a scheduled job, which may include information such as name, timing, command(s), etc.

### Component: None

Changes made to an existing scheduled job, including modifications to its execution parameters, command payload, or execution timing.

## DS0009 - None

Instances of computer programs that are being executed by at least one thread. Processes have memory space for process executables, loaded modules (DLLs or shared libraries), and allocated memory regions containing everything from user input to application-specific data structures(Citation: Microsoft Processes and Threads)

### Component: None

Calls made by a process to operating system-provided Application Programming Interfaces (APIs). These calls are essential for interacting with system resources such as memory, files, and hardware, or for performing system-level tasks. Monitoring these calls can provide insight into a process's intent, especially if the process is malicious.

*Data Collection Measures:*

- Endpoint Detection and Response (EDR) Tools:
    - Leverage tools to monitor API execution behaviors at the process level.
    - Example: Sysmon Event ID 10 captures API call traces for process access and memory allocation.
- Process Monitor (ProcMon):
    - Use ProcMon to collect detailed logs of process and API activity. ProcMon can provide granular details on API usage and identify malicious behavior during analysis.
- Windows Event Logs:
    - Use Event IDs from Windows logs for specific API-related activities:
        - Event ID 4688: A new process has been created (can indirectly infer API use).
        - Event ID 4657: A registry value has been modified (to monitor registry-altering APIs).
- Dynamic Analysis Tools:
    - Tools like Cuckoo Sandbox, Flare VM, or Hybrid Analysis monitor API execution during malware detonation.
- Host-Based Logs:
    - On Linux/macOS systems, leverage audit frameworks (e.g., `auditd`, `strace`) to capture and analyze system call usage that APIs map to.
- Runtime Monitors:
    - Runtime security tools like Falco can monitor system-level calls for API execution.
- Debugging and Tracing:
    - Use debugging tools like gdb (Linux) or WinDbg (Windows) for deep tracing of API executions in real time.

### Component: None

Refers to the event in which a new process (executable) is initialized by an operating system. This can involve parent-child process relationships, process arguments, and environmental variables. Monitoring process creation is crucial for detecting malicious behaviors, such as execution of unauthorized binaries, scripting abuse, or privilege escalation attempts.

*Data Collection Measures:*

- Endpoint Detection and Response (EDR) Tools:
    - EDRs provide process telemetry, tracking execution flows and arguments.
- Windows Event Logs:
    - Event ID 4688 (Audit Process Creation): Captures process creation with associated parent process.
- Sysmon (Windows):
    - Event ID 1 (Process Creation): Provides detailed logging
- Linux/macOS Monitoring:
    - AuditD (execve syscall): Logs process creation.
    - eBPF/XDP: Used for low-level monitoring of system calls related to process execution.
    - OSQuery: Allows SQL-like queries to track process events (process_events table).
    - Apple Endpoint Security Framework (ESF): Monitors process creation on macOS.
- Network-Based Monitoring:
    - Zeek (Bro) Logs: Captures network-based process execution related to remote shells.
    - Syslog/OSSEC: Tracks execution of processes on distributed systems.
- Behavioral SIEM Rules:
    - Monitor process creation for uncommon binaries in user directories.
    - Detect processes with suspicious command-line arguments. 

### Component: None

Contextual data about a running process, which may include information such as environment variables, image name, user/owner, etc.

### Component: None

The exit or termination of a running process on a system. This can occur due to normal operations, user-initiated commands, or malicious actions such as process termination by malware to disable security controls.

*Data Collection Measures:*

- Endpoint Detection and Response (EDR) Tools:
    - Monitor process termination events.
- Windows Event Logs:
    - Event ID 4689 (Process Termination)  Captures when a process exits, including process ID and parent process.
    - Event ID 7036 (Service Control Manager)  Monitors system service stops.
- Sysmon (Windows):
    - Event ID 5 (Process Termination)  Detects when a process exits, including parent-child relationships.
- Linux/macOS Monitoring:
    - AuditD (`execve`, `exit_group`, `kill` syscalls)  Captures process termination via command-line interactions.
    - eBPF/XDP: Monitors low-level system calls related to process termination.
    - OSQuery: The processes table can be queried for abnormal exits.

## DS0011 - None

Executable files consisting of one or more shared classes and interfaces, such as portable executable (PE) format binaries/dynamic link libraries (DLL), executable and linkable format (ELF) binaries/shared libraries, and Mach-O format binaries/shared libraries(Citation: Microsoft LoadLibrary)(Citation: Microsoft Module Class)

### Component: None

When a process or program dynamically attaches a shared library, module, or plugin into its memory space. This action is typically performed to extend the functionality of an application, access shared system resources, or interact with kernel-mode components.

*Data Collection Measures:*

- Event Logging (Windows):
    - Sysmon Event ID 7: Logs when a DLL is loaded into a process.
    - Windows Security Event ID 4688: Captures process creation events, often useful for correlating module loads.
    - Windows Defender ATP: Can provide visibility into suspicious module loads.
- Event Logging (Linux/macOS):
    - AuditD (`execve` and `open` syscalls): Captures when shared libraries (`.so` files) are loaded.
    - Ltrace/Strace: Monitors process behavior, including library calls (`dlopen`, `execve`).
    - MacOS Endpoint Security Framework (ESF): Monitors library loads (`ES_EVENT_TYPE_NOTIFY_DYLD_INSERT_LIBRARIES`).
- Endpoint Detection & Response (EDR): 
    - Provide real-time telemetry on module loads and process injections.
    - Sysinternals Process Monitor (`procmon`): Captures loaded modules and their execution context.
- Memory Forensics:
    - Volatility Framework (`malfind`, `ldrmodules`): Detects injected DLLs and anomalous module loads.
    - Rekall Framework: Useful for kernel-mode module detection.
- SIEM and Log Analysis:
    - Centralized log aggregation to correlate suspicious module loads across the environment.
    - Detection rules using correlation searches and behavioral analytics.

## DS0012 - None

A file or stream containing a list of commands, allowing them to be launched in sequence(Citation: Microsoft PowerShell Logging)(Citation: FireEye PowerShell Logging)(Citation: Microsoft AMSI)

### Component: None

The execution of a text file that contains code via the interpreter.

*Data Collection Measures:*

- Windows Event Logs:
    - Event ID 4104 (PowerShell Script Block Logging)  Captures full command-line execution of PowerShell scripts.
    - Event ID 4688 (Process Creation)  Detects script execution by tracking process launches (`powershell.exe`, `wscript.exe`, `cscript.exe`).
    - Event ID 5861 (Script Execution)  Captures script execution via Windows Defender AMSI logging.
- Sysmon (Windows):
    - Event ID 1 (Process Creation)  Monitors script execution initiated by scripting engines.
    - Event ID 11 (File Creation)  Detects new script files written to disk before execution.
- Endpoint Detection and Response (EDR) Tools:
    - Track script execution behavior, detect obfuscated commands, and prevent malicious scripts.
- PowerShell Logging:
    - Enable Module Logging: Logs all loaded modules and cmdlets.
    - Enable Script Block Logging: Captures complete PowerShell script execution history.
- SIEM Detection Rules:
    - Detect script execution with obfuscated, encoded, or remote URLs.
    - Alert on script executions using `-EncodedCommand` or `iex(iwr)`.

## DS0015 - None

Events collected by third-party services such as mail servers, web applications, or other appliances (not by the native OS or platform)(Citation: Confluence Logs)

### Component: None

Application Log Content refers to logs generated by applications or services, providing a record of their activity. These logs may include metrics, errors, performance data, and operational alerts from web, mail, or other applications. These logs are vital for monitoring application behavior and detecting malicious activities or anomalies. Examples: 

- Web Application Logs: These logs include information about requests, responses, errors, and security events (e.g., unauthorized access attempts).
- Email Application Logs: Logs contain metadata about emails sent, received, or blocked (e.g., sender/receiver addresses, message IDs).
- SaaS Application Logs: Activity logs include user logins, configuration changes, and access to sensitive resources.
- Cloud Application Logs: Logs detail control plane activities, including API calls, instance modifications, and network changes.
- System/Application Monitoring Logs: Logs provide insights into application performance, errors, and anomalies.

This data component can be collected through the following measures:

Configure Application Logging

- Enable logging within the application or service.
- Examples:
    - Web Servers: Enable access and error logs in NGINX or Apache.
    - Email Systems: Enable audit logging in Microsoft Exchange or Gmail.

Centralized Log Management

- Use log management solutions like Splunk, or a cloud-native logging solution.
- Configure the application to send logs to a centralized system for analysis.

Cloud-Specific Collection

- Use services like AWS CloudWatch, Azure Monitor, or Google Cloud Operations Suite for cloud-based applications.
- Ensure logging is enabled for all critical resources (e.g., API calls, IAM changes).

SIEM Integration

- Integrate application logs with a SIEM platform (e.g., Splunk, QRadar) for real-time correlation and analysis.
- Use parsers to standardize log formats and extract key fields like timestamps, user IDs, and error codes.

## DS0016 - None

A non-volatile data storage device (hard drive, floppy disk, USB flash drive) with at least one formatted partition, typically mounted to the file system and/or assigned a drive letter(Citation: Sysmon EID 9)

### Component: None

The activity of assigning a new drive letter or creating a mount point for a data storage device, such as a USB, network share, or external hard drive, enabling access to its content on a host system. Examples: 

- USB Drive Insertion: A USB drive is plugged in and automatically assigned the letter `E:\` on a Windows machine.
- Network Drive Mapping: A network share `\\server\share` is mapped to the drive `Z:\`.
- Virtual Drive Creation: A virtual disk is mounted on `/mnt/virtualdrive` using an ISO image or a virtual hard disk (VHD).
- Cloud Storage Mounting: Google Drive is mounted as `G:\` on a Windows machine using a cloud sync tool.
- External Storage Integration: An external HDD or SSD is connected and assigned `/mnt/external` on a Linux system.

This data component can be collected through the following measures:

Windows Event Logs

- Relevant Events:
    - Event ID 98: Logs the creation of a volume (mount or new drive letter assignment).
    - Event ID 1006: Logs removable storage device insertions.
- Configuration: Enable "Removable Storage Events" in the Group Policy settings:
`Computer Configuration > Administrative Templates > System > Removable Storage Access`

Linux System Logs

- Command-Line Monitoring: Use `dmesg` or `journalctl` to monitor mount events.

- Auditd Configuration: Add audit rules to track mount points.
- Logs can be reviewed in /var/log/audit/audit.log.

macOS System Logs

- Unified Logs: Monitor system logs for mount activity:
- Command-Line Tools: Use `diskutil list` to verify newly created or mounted drives.

Endpoint Detection and Response (EDR) Tools

- EDR solutions can log removable drive usage and network-mounted drives. Configure EDR policies to alert on suspicious drive creation events.

SIEM Tools

- Centralize logs from multiple platforms into a SIEM (e.g., Splunk) to correlate and alert on suspicious drive creation activities.

### Component: None

The alteration of a drive letter, mount point, or other attributes of a data storage device, which could involve reassignment, renaming, permissions changes, or other modifications. Examples: 

- Drive Letter Reassignment: A USB drive previously assigned `E:\` is reassigned to `D:\` on a Windows machine.
- Mount Point Change: On a Linux system, a mounted storage device at `/mnt/external` is moved to `/mnt/storage`.
- Drive Permission Changes: A shared drive's permissions are modified to allow write access for unauthorized users or processes.
- Renaming of a Drive: A network drive labeled "HR_Share" is renamed to "Shared_Resources."
- Modification of Cloud-Integrated Drives: A cloud storage mount such as Google Drive is modified to sync only specific folders.

This data component can be collected through the following measures:

Windows Event Logs

- Relevant Events:
    - Event ID 98: Indicates changes to a volume (e.g., drive letter reassignment).
    - Event ID 1006: Logs permission modifications or changes to removable storage.
- Configuration: Enable "Storage Operational Logs" in the Event Viewer:
`Applications and Services Logs > Microsoft > Windows > Storage-Tiering > Operational`

Linux System Logs

- Auditd Configuration: Add audit rules to track changes to mounted drives: `auditctl -w /mnt/ -p w -k drive_modification`
- Command-Line Monitoring: Use `dmesg` or `journalctl` to observe drive modifications.

macOS System Logs

- Unified Logs: Collect mount or drive modification events: `log show --info | grep "Volume modified"`
- Command-Line Monitoring: Use `diskutil` to track changes:

Endpoint Detection and Response (EDR) Tools

- Configure policies in EDR solutions to monitor and log changes to drive configurations or attributes.

SIEM Tools

- Aggregate logs from multiple systems into a centralized platform like Splunk to correlate events and alert on suspicious drive modification activities.


## DS0017 - None

A directive given to a computer program, acting as an interpreter of some kind, in order to perform a specific task(Citation: Confluence Linux Command  Line)(Citation: Audit OSX)

### Component: None

Command Execution involves monitoring and capturing the execution of textual commands (including shell commands, cmdlets, and scripts) within an operating system or application. These commands may include arguments or parameters and are typically executed through interpreters such as `cmd.exe`, `bash`, `zsh`, `PowerShell`, or programmatic execution. Examples: 

- Windows Command Prompt
    - dir  Lists directory contents.
    - net user  Queries or manipulates user accounts.
    - tasklist  Lists running processes.
- PowerShell
    - Get-Process  Retrieves processes running on a system.
    - Set-ExecutionPolicy  Changes PowerShell script execution policies.
    - Invoke-WebRequest  Downloads remote resources.
- Linux Shell
    - ls  Lists files in a directory.
    - cat /etc/passwd  Reads the user accounts file.
    - curl http://malicious-site.com  Retrieves content from a malicious URL.
- Container Environments
    - docker exec  Executes a command inside a running container.
    - kubectl exec  Runs commands in Kubernetes pods.
- macOS Terminal
    - open  Opens files or URLs.
    - dscl . -list /Users  Lists all users on the system.
    - osascript -e  Executes AppleScript commands.

This data component can be collected through the following measures:

Enable Command Logging

- Windows:
    - Enable PowerShell logging: `Set-ExecutionPolicy Bypass`, `Set-ItemProperty -Path "HKLM:\SOFTWARE\Policies\Microsoft\Windows\PowerShell\ScriptBlockLogging" -Name EnableScriptBlockLogging -Value 1`
    - Enable Windows Event Logging:
        - Event ID 4688: Tracks process creation, including command-line arguments.
        - Event ID 4104: Logs PowerShell script block execution.
- Linux/macOS:
    - Enable shell history logging in `.bashrc` or `.zshrc`: `export HISTTIMEFORMAT="%d/%m/%y %T "`, `export PROMPT_COMMAND='history -a; history -w'`
    - Use audit frameworks (e.g., `auditd`) to log command executions. Example rule to log all `execve` syscalls: `-a always,exit -F arch=b64 -S execve -k cmd_exec`
- Containers:
    - Use runtime-specific tools like Dockers --log-driver or Kubernetes Audit Logs to capture exec commands.

Integrate with Centralized Logging

- Collect logs using a SIEM (e.g., Splunk) or cloud-based log aggregation tools like AWS CloudWatch or Azure Monitor. Example Splunk Search for Windows Event 4688:
`index=windows EventID=4688 CommandLine=*`

Use Endpoint Detection and Response (EDR) Tools

- Monitor command executions via EDR solutions 

Deploy Sysmon for Advanced Logging (Windows)

- Use Sysmon's Event ID 1 to log process creation with command-line arguments

## DS0019 - None

A computer process that is configured to execute continuously in the background and perform system tasks, in some cases before any user has logged in(Citation: Microsoft Services)(Citation: Linux Services Run Levels)

### Component: None

The registration of a new service or daemon on an operating system.

*Data Collection Measures:*

- Windows Event Logs
    - Event ID 4697 - Captures the creation of a new Windows service.
    - Event ID 7045 - Captures services installed by administrators or adversaries.
    - Event ID 7034 - Could indicate malicious service modification or exploitation.
- Sysmon Logs
    - Sysmon Event ID 1 - Process Creation (captures service executables).
    - Sysmon Event ID 4 - Service state changes (detects service installation).
    - Sysmon Event ID 13 - Registry modifications (captures service persistence changes).
- PowerShell Logging
    - Monitor `New-Service` and `Set-Service` PowerShell cmdlets in Event ID 4104 (Script Block Logging).
- Linux/macOS Collection Methods
    - AuditD & Syslog Daemon Logs (`/var/log/syslog`, `/var/log/messages`, `/var/log/daemon.log`)
    - AuditD Rules:
        - `auditctl -w /etc/systemd/system -p wa -k service_creation`
        - Detects changes to `systemd` service configurations.
- Systemd Journals (`journalctl -u <service_name>`)
    - Captures newly created systemd services.
- LaunchDaemons & LaunchAgents (macOS)
    - Monitor `/Library/LaunchDaemons/` and `/Library/LaunchAgents/` for new plist files.

### Component: None

Contextual data about a service/daemon, which may include information such as name, service executable, start type, etc.

### Component: None

Changes made to an existing service or daemon, such as modifying the service name, start type, execution parameters, or security configurations.

*Data Collection Measures: *

- Windows Event Logs
    - Event ID 7040 - Detects modifications to the startup behavior of a service.
    - Event ID 7045 - Can capture changes made to existing services.
    - Event ID 7036 - Tracks when services start or stop, potentially indicating malicious tampering.
    - Event ID 4697 - Can detect when an adversary reinstalls a service with different parameters.
- Sysmon Logs
    - Sysmon Event ID 13 - Detects changes to service configurations in the Windows Registry (e.g., `HKLM\SYSTEM\CurrentControlSet\Services\`).
    - Sysmon Event ID 1 - Can track execution of `sc.exe` or `PowerShell Set-Service`.
- PowerShell Logging
    - Event ID 4104 (Script Block Logging) - Captures execution of commands like `Set-Service`, `New-Service`, or `sc config`.
    - Command-Line Logging (Event ID 4688) - Tracks usage of service modification commands:
        - `sc config <service_name> start= auto`  
        - `sc qc <service_name>`  
- Linux/macOS Collection Methods
    - Systemd Journals (`journalctl -u <service_name>`) Tracks modifications to systemd service configurations.
    - Daemon Logs (`/var/log/syslog`, `/var/log/messages`, `/var/log/daemon.log`) Captures changes to service state and execution parameters.
    - AuditD Rules for Service Modification 
        - Monitor modifications to `/etc/systemd/system/` for new or altered service unit files: `auditctl -w /etc/systemd/system/ -p wa -k service_modification`
        - Track execution of `systemctl` or `service` commands: `auditctl -a always,exit -F arch=b64 -S execve -F a0=systemctl -F key=service_mod`
    - OSQuery for Linux/macOS Monitoring
        - Query modified services using OSQuerys `processes` or `system_info` tables: `SELECT * FROM systemd_units WHERE state != 'running';`
    - macOS Launch Daemon/Agent Modification
        - Monitor for changes in:
            - `/Library/LaunchDaemons/`
            - `/Library/LaunchAgents/`
        - Track modifications to `.plist` files indicating persistence attempts.

## DS0022 - None

A computer resource object, managed by the I/O system, for storing data (such as images, text, videos, computer programs, or any wide variety of other media).(Citation: Microsoft File Mgmt)

### Component: None

To events where a file is opened or accessed, making its contents available to the requester. This includes reading, executing, or interacting with files by authorized or unauthorized entities. Examples include logging file access events (e.g., Windows Event ID 4663), monitoring file reads, and detecting unusual file access patterns. Examples: 

- File Read Operations: A user opens a sensitive document (e.g., financial_report.xlsx) on a shared drive.
- File Execution: A script or executable file is accessed and executed (e.g., malware.exe is run from a temporary directory).
- Unauthorized File Access: An unauthorized user attempts to access a protected configuration file (e.g., `/etc/passwd` on Linux or `System32` files on Windows).
- File Access Patterns: Bulk access to multiple files in a short time (e.g., mass access to documents on a file server).
- File Access via Network: Files on a network share are accessed remotely (e.g., logs of SMB file access).

This data component can be collected through the following measures:

Windows

- Windows Event Logs: Event ID 4663: Captures file system auditing details, including who accessed the file, access type, and file name.
- Sysmon:
    - Event ID 11: Logs file creation time changes.
    - Event ID 1 (process creation): Can provide insight into files executed.
- PowerShell: Commands to monitor file access in real-time: `Get-WinEvent -FilterHashtable @{LogName='Security'; ID=4663}`

Linux

- Auditd: Monitor file access events using audit rules: `auditctl -w /path/to/file -p rwxa -k file_access`
- View logs: `ausearch -k file_access`
- Inotify: Use inotify to track file access on Linux: `inotifywait -m /path/to/watch -e access`

macOS

- Unified Logs: Monitor file access using the macOS Unified Logging System.
- FSEvents: File System Events can track file accesses: `fs_usage | grep open`

Network Devices

- SMB/CIFS Logs: Monitor file access over network shares using logs from SMB or CIFS protocol.
- NAS Logs: Collect logs from network-attached storage systems for file access events.

SIEM Integration

- Collect file access logs from all platforms (Windows, Linux, macOS) and centralize in a SIEM for correlation and analysis.

### Component: None

A new file is created on a system or network storage. This action often signifies an operation such as saving a document, writing data, or deploying a file. Logging these events helps identify legitimate or potentially malicious file creation activities. Examples include logging file creation events (e.g., Sysmon Event ID 11 or Linux auditd logs). 

This data component can be collected through the following measures:

Windows

- Sysmon: Event ID 11: Logs file creation events, capturing details like the file path, hash, and creation time.
- Windows Event Log: Enable "Object Access" auditing in Group Policy to track file creation under Event ID 4663.
- PowerShell: Real-time monitoring of file creation:`Get-WinEvent -FilterHashtable @{LogName='Security'; ID=4663}`

Linux

- Auditd: Use audit rules to monitor file creation: `auditctl -w /path/to/directory -p w -k file_creation`
- View logs: `ausearch -k file_creation`
- Inotify: Monitor file creation with inotifywait: `inotifywait -m /path/to/watch -e create`

macOS

- Unified Logs: Use the macOS Unified Logging System to capture file creation events.
- FSEvents: Use File System Events to monitor file creation: `fs_usage | grep create`

Network Devices

- NAS Logs: Monitor file creation events on network-attached storage devices.
- SMB Logs: Collect logs of file creation activities over SMB/CIFS protocols.

SIEM Integration

- Forward logs from all platforms (Windows, Linux, macOS) to a SIEM for central analysis and alerting.

### Component: None

Refers to events where files are removed from a system or storage device. These events can indicate legitimate housekeeping activities or malicious actions such as attackers attempting to cover their tracks. Monitoring file deletions helps organizations identify unauthorized or suspicious activities.

This data component can be collected through the following measures:

Windows

- Sysmon: Event ID 23: Logs file deletion events, including details such as file paths and responsible processes.
- Windows Event Log: Enable "Object Access" auditing to monitor file deletions.
- PowerShell: `Get-WinEvent -FilterHashtable @{LogName='Security'; ID=4663} | Where-Object {$_.Message -like '*DELETE*'}`

Linux

- Auditd: Use audit rules to capture file deletion events: `auditctl -a always,exit -F arch=b64 -S unlink -S rename -S rmdir -k file_deletion`
- Query logs: `ausearch -k file_deletion`
- Inotify: Use inotifywait to monitor file deletions: `inotifywait -m /path/to/watch -e delete`

macOS

- Endpoint Security Framework (ESF): Monitor events like ES_EVENT_TYPE_AUTH_UNLINK to capture file deletion activities.
- FSEvents: Track file deletion activities in real-time: `fs_usage | grep unlink`

SIEM Integration

- Forward file deletion logs to a SIEM for centralized monitoring and correlation with other events.


### Component: None

contextual information about a file, including attributes such as the file's name, size, type, content (e.g., signatures, headers, media), user/owner, permissions, timestamps, and other related properties. File metadata provides insights into a file's characteristics and can be used to detect malicious activity, unauthorized modifications, or other anomalies. Examples: 

- File Ownership and Permissions: Checking the owner and permissions of a critical configuration file like /etc/passwd on Linux or C:\Windows\System32\config\SAM on Windows.
- Timestamps: Analyzing the creation, modification, and access timestamps of a file.
- File Content and Signatures: Extracting the headers of an executable file to verify its signature or detect packing/obfuscation.
- File Attributes: Analyzing attributes like hidden, system, or read-only flags in Windows.
- File Hashes: Generating MD5, SHA-1, or SHA-256 hashes of files to compare against threat intelligence feeds.
- File Location: Monitoring files located in unusual directories or paths, such as temporary or user folders.

This data component can be collected through the following measures:

Windows

- Sysinternals Tools: Use `AccessEnum` or `PSFile` to retrieve metadata about file access and permissions.
- Windows Event Logs: Enable object access auditing and monitor events like 4663 (Object Access) and 5140 (A network share object was accessed).
- PowerShell: Use Get-Item or Get-ChildItem cmdlets: `Get-ChildItem -Path "C:\Path\To\Directory" -Recurse | Select-Object Name, Length, LastWriteTime, Attributes`

Linux

- File System Commands: Use `ls -l` or stat to retrieve file metadata: `stat /path/to/file`
- Auditd: Configure audit rules to log metadata access: `auditctl -w /path/to/file -p wa -k file_metadata`
- Filesystem Integrity Tools: Tools like tripwire or AIDE (Advanced Intrusion Detection Environment) can monitor file metadata changes.

macOS

- FSEvents: Use FSEvents to track file metadata changes.
- Endpoint Security Framework (ESF): Capture metadata-related events via ESF APIs.
- Command-Line Tools: Use ls -l or xattr for file attributes: `ls -l@ /path/to/file`

SIEM Integration

- Forward file metadata logs from endpoint or network devices to a SIEM for centralized analysis.

### Component: None

Changes made to a file, including updates to its contents, metadata, access permissions, or attributes. These modifications may indicate legitimate activity (e.g., software updates) or unauthorized changes (e.g., tampering, ransomware, or adversarial modifications). Examples: 

- Content Modifications: Changes to the content of a configuration file, such as modifying `/etc/ssh/sshd_config` on Linux or `C:\Windows\System32\drivers\etc\hosts` on Windows.
- Permission Changes: Altering file permissions to allow broader access, such as changing a file from `644` to `777` on Linux or modifying NTFS permissions on Windows.
- Attribute Modifications: Changing a file's attributes to hidden, read-only, or system on Windows.
- Timestamp Manipulation: Adjusting a file's creation or modification timestamp using tools like `touch` in Linux or timestomping tools on Windows.
- Software or System File Changes: Modifying system files such as `boot.ini`, kernel modules, or application binaries.

This data component can be collected through the following measures:

Windows

- Event Logs: Enable file system auditing to monitor file modifications using Security Event ID 4670 (File System Audit) or Sysmon Event ID 2 (File creation time changed).
- PowerShell: Use Get-ItemProperty or Get-Acl cmdlets to monitor file properties: `Get-Item -Path "C:\path\to\file" | Select-Object Name, Attributes, LastWriteTime`

Linux

- File System Monitoring: Use tools like auditd with rules to monitor file modifications: `auditctl -w /path/to/file -p wa -k file_modification`
- Inotify: Use inotifywait to watch for real-time changes to files or directories: `inotifywait -m /path/to/file`

macOS

- Endpoint Security Framework (ESF): Monitor file modification events using ESF APIs.
- Audit Framework: Configure audit rules to track file changes.
- Command-Line Tools: Use fs_usage to monitor file activities: `fs_usage -w /path/to/file`

SIEM Tools

- Collect logs from endpoint agents (e.g., Sysmon, Auditd) and file servers to centralize file modification event data.

## DS0024 - None

A Windows OS hierarchical database that stores much of the information and settings for software programs, hardware devices, user preferences, and operating-system configurations(Citation: Microsoft Registry)

### Component: None

The removal of a registry key within the Windows operating system.

*Data Collection Measures:*

- Windows Event Logs
    - Event ID 4658 - Registry Key Handle Closed: Captures when a handle to a registry key is closed, which may indicate deletion.
    - Event ID 4660 - Object Deleted: Logs when a registry key is deleted.
- Sysmon (System Monitor) for Windows
    - Sysmon Event ID 12 - Registry Key Deleted: Logs when a registry key is removed.
    - Sysmon Event ID 13 - Registry Value Deleted: Captures removal of specific registry values.
- Endpoint Detection and Response (EDR) Solutions
    - Monitor registry deletions for suspicious behavior.

### Component: None

Changes made to an existing registry key or its values. These modifications can include altering permissions, modifying stored data, or updating configuration settings.

*Data Collection Measures:*

- Windows Event Logs
    - Event ID 4657 - Registry Value Modified: Logs changes to registry values, including modifications to startup entries, security settings, or system configurations.
- Sysmon (System Monitor) for Windows
    - Sysmon Event ID 13 - Registry Value Set: Captures changes to specific registry values.
    - Sysmon Event ID 14 - Registry Key & Value Renamed: Logs renaming of registry keys, which may indicate evasion attempts.
- Endpoint Detection and Response (EDR) Solutions
    - Monitor registry modifications for suspicious behavior.

## DS0028 - None

Logon occurring on a system or resource (local, domain, or cloud) to which a user/device is gaining access after successful authentication and authorization(Citation: Microsoft Audit Logon Events)

### Component: None

The successful establishment of a new user session following a successful authentication attempt. This typically signifies that a user has provided valid credentials or authentication tokens, and the system has initiated a session associated with that user account. This data is crucial for tracking authentication events and identifying potential unauthorized access. Examples: 

- Windows Systems
    - Event ID: 4624
        - Logon Type: 2 (Interactive) or 10 (Remote Interactive via RDP).
        - Account Name: JohnDoe
        - Source Network Address: 192.168.1.100
        - Authentication Package: NTLM
- Linux Systems
    - /var/log/utmp or /var/log/wtmp:
        - Log format: login user [tty] from [source_ip]
        - User: jane
        - IP: 10.0.0.5
        - Timestamp: 2024-12-28 08:30:00
- macOS Systems
    - /var/log/asl.log or unified logging framework:
        - Log: com.apple.securityd: Authentication succeeded for user 'admin'
- Cloud Environments
    - Azure Sign-In Logs:
        - Activity: Sign-in successful
        - Client App: Browser
        - Location: Unknown (Country: X)
- Google Workspace
    - Activity: Login
        - Event Type: successful_login
        - Source IP: 203.0.113.55

This data component can be collected through the following measures:

- Windows Systems
    - Event Logs: Monitor Security Event Logs using Event ID 4624 for successful logons.
    - PowerShell Example: `Get-EventLog -LogName Security -InstanceId 4624`
- Linux Systems
    - Log Files: Monitor `/var/log/utmp`, `/var/log/wtmp`, or `/var/log/auth.log` for logon events.
    - Tools: Use `last` or `who` commands to parse login records.
- macOS Systems
    - Log Sources: Monitor `/var/log/asl.log` or Apple Unified Logs using the `log show` command.
    - Command Example: `log show --predicate 'eventMessage contains "Authentication succeeded"' --info`
- Cloud Environments
    - Azure AD: Use Azure Monitor to analyze sign-in logs. Example CLI Query: `az monitor log-analytics query -w <workspace_id> --analytics-query "AzureActivity | where ActivityStatus == 'Success' and OperationName == 'Sign-in'"`
    - Google Workspace: Enable and monitor Login Audit logs from the Admin Console.
    - Office 365: Use Audit Log Search in Microsoft 365 Security & Compliance Center for login-related events.
- Network Logs
    - Sources: Network authentication mechanisms (e.g., RADIUS or TACACS logs).
- Enable EDR Monitoring: 
    - EDR tools monitor logon session activity, including the creation of new sessions.
    - Configure alerts for: Suspicious logon types (e.g., Logon Type 10 for RDP or Type 5 for Service). Logons from unusual locations, accounts, or devices.
    - Leverage EDR telemetry for session attributes like source IP, session duration, and originating process.

### Component: None

Contextual data about a logon session, such as username, logon type, access tokens (security context, user SIDs, logon identifiers, and logon SID), and any activity associated within it

## DS0029 - None

Data transmitted across a network (ex: Web, DNS, Mail, File, etc.), that is either summarized (ex: Netflow) and/or captured as raw data in an analyzable format (ex: PCAP)

### Component: None

The initial establishment of a network session, where a system or process initiates a connection to a local or remote endpoint. This typically involves capturing socket information (source/destination IP, ports, protocol) and tracking session metadata. Monitoring these events helps detect lateral movement, exfiltration, and command-and-control (C2) activities.

*Data Collection Measures:*

- Windows:
    - Event ID 5156  Filtering Platform Connection - Logs network connections permitted by Windows Filtering Platform (WFP).
    - Sysmon Event ID 3  Network Connection Initiated - Captures process, source/destination IP, ports, and parent process.
- Linux/macOS:
    - Netfilter (iptables), nftables logs - Tracks incoming and outgoing network connections.
    - AuditD (`connect` syscall) - Logs TCP, UDP, and ICMP connections.
    - Zeek (`conn.log`) - Captures protocol, duration, and bytes transferred.
- Cloud & Network Infrastructure:
    - AWS VPC Flow Logs / Azure NSG Flow Logs - Logs IP traffic at the network level in cloud environments.
    - Zeek (conn.log) or Suricata (network events) - Captures packet metadata for detection and correlation.
- Endpoint Detection & Response (EDR):
    - Detect anomalous network activity such as new C2 connections or data exfiltration attempts.

### Component: None

The full packet capture (PCAP) or session data that logs both protocol headers and payload content. This allows analysts to inspect command and control (C2) traffic, exfiltration, and other suspicious activity within network communications. Unlike metadata-based logs, full content analysis enables deeper protocol inspection, payload decoding, and forensic investigations.

*Data Collection Measures:*

- Network Packet Capture (Full Content Logging)
    - Wireshark / tcpdump / tshark
        - Full packet captures (PCAP files) for manual analysis or IDS correlation. `tcpdump -i eth0 -w capture.pcap`
    - Zeek (formerly Bro)
        - Extracts protocol headers and payload details into structured logs. `echo "redef Log::default_store = Log::ASCII;" > local.zeek | zeek -Cr capture.pcap local.zeek`
    - Suricata / Snort (IDS/IPS with PCAP Logging)
        - Deep packet inspection (DPI) with signature-based and behavioral analysis. `suricata -c /etc/suricata/suricata.yaml -i eth0 -l /var/log/suricata`
- Host-Based Collection
    - Sysmon Event ID 22  DNS Query Logging, Captures DNS requests made by processes, useful for detecting C2 domains.
    - Sysmon Event ID 3  Network Connection Initiated, Logs process-to-network connection relationships.
    - AuditD (Linux)  syscall=connect, Monitors outbound network requests from processes. `auditctl -a always,exit -F arch=b64 -S connect -k network_activity`
- Cloud & SaaS Traffic Collection
    - AWS VPC Flow Logs / Azure NSG Flow Logs / Google VPC Flow Logs, Captures metadata about inbound/outbound network traffic.
    - Cloud IDS (AWS GuardDuty, Azure Sentinel, Google Chronicle), Detects malicious activity in cloud environments by analyzing network traffic patterns.

### Component: None

Summarized network packet data that captures session-level details such as source/destination IPs, ports, protocol types, timestamps, and data volume, without storing full packet payloads. This is commonly used for traffic analysis, anomaly detection, and network performance monitoring.

*Data Collection Measures:*

- Network Flow Logs (Metadata Collection)
    - NetFlow 
        - Summarized metadata for network conversations (no packet payloads).
    - sFlow (Sampled Flow Logging)
        - Captures sampled packets from switches and routers.
        - Used for real-time traffic monitoring and anomaly detection.
    - Zeek (Bro) Flow Logs
        - Zeek logs session-level details in logs like conn.log, http.log, dns.log, etc.
- Host-Based Collection
    - Sysmon Event ID 3  Network Connection Initiated
        - Logs process-level network activity, useful for detecting malicious outbound connections.
    - AuditD (Linux)  syscall=connect
        - Monitors system calls for network connections. `auditctl -a always,exit -F arch=b64 -S connect -k network_activity`
- Cloud & SaaS Flow Monitoring
    - AWS VPC Flow Logs
        - Captures metadata for traffic between EC2 instances, security groups, and internet gateways.
    - Azure NSG Flow Logs / Google VPC Flow Logs
        - Logs ingress/egress traffic for cloud-based resources.

## DS0033 - None

A storage resource (typically a folder or drive) made available from one host to others using network protocols, such as Server Message Block (SMB) or Network File System (NFS)(Citation: Microsoft NFS Overview)

### Component: None

Opening a network share, which makes the contents available to the requestor (ex: Windows EID 5140 or 5145)

*Data Collection Measures:*

- Windows:
    - Event ID 5140  Network Share Object Access Logs every access attempt to a network share.
    - Event ID 5145  Detailed Network Share Object Access Captures granular access control information, including the requesting user, source IP, and access permissions.
    - Sysmon Event ID 3  Network Connection Initiated Helps track SMB connections to suspicious or unauthorized network shares.
    - Enable Audit Policy for Network Share Access: `auditpol /set /subcategory:"File Share" /success:enable /failure:enable`
    - Enable PowerShell Logging to Detect Unauthorized SMB Access: `Set-ExecutionPolicy RemoteSigned`
    - Restrict Network Share Access with Group Policy (GPO): `Computer Configuration ? Windows Settings ? Security Settings ? Local Policies ? User Rights Assignment` Set "Access this computer from the network" to restrict unauthorized accounts.
- Linux/macOS:
    - AuditD (`open`, `read`, `write`, `connect` syscalls) Detects access to NFS, CIFS, and SMB network shares.
    - Lsof (`lsof | grep nfs` or `lsof | grep smb`) Identifies active network share connections.
    - Mount (`mount | grep nfs` or `mount | grep cifs`) Lists currently mounted network shares.
    - Enable AuditD for SMB/NFS Access: `auditctl -a always,exit -F arch=b64 -S open -F path=/mnt/share -k network_share_access`
    - Monitor Active Network Shares Using Netstat: `netstat -an | grep :445`
- Endpoint Detection & Response (EDR):
    - Detects abnormal network share access behavior, such as unusual account usage, large file transfers, or encrypted file activity.

## DS0039 - None

Data sources with information about the set of devices found within the network, along with their current software and configurations

### Component: None

This includes sources of current and expected devices on the network, including the manufacturer, model, and necessary identifiers (e.g., IP and hardware addresses)

### Component: None

This includes sources of current and expected software or application programs deployed to a device, along with information on the version and patch level for vendor products, full source code for any application programs, and unique identifiers (e.g., hashes, signatures).

## DS0040 - None

Operational databases contain information about the status of the operational process and associated devices, including any measurements, events, history, or alarms that have occurred

### Component: None

This includes alarms associated with unexpected device functions, such as shutdowns, restarts, failures, or configuration changes

### Component: None

This includes any data stores that maintain historical or real-time events and telemetry recorded from various sensors or devices

### Component: None

This includes a list of any process alarms or alerts produced to indicate unusual or concerning activity within the operational process (e.g., increased temperature/pressure)