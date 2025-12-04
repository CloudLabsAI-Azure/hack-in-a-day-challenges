# IT Support SOP - VPN Connection Issues

## Document Information
- **Document Version:** 3.2
- **Last Updated:** December 2025
- **Department:** IT Network Services
- **Classification:** Internal Use Only
- **SOP ID:** IT-NET-VPN-001

---

## Table of Contents
1. [Overview](#overview)
2. [VPN System Information](#vpn-system-information)
3. [Common VPN Error Codes](#common-vpn-error-codes)
4. [Troubleshooting Procedures](#troubleshooting-procedures)
5. [Platform-Specific Instructions](#platform-specific-instructions)
6. [Advanced Troubleshooting](#advanced-troubleshooting)
7. [Security and Best Practices](#security-and-best-practices)
8. [Escalation Procedures](#escalation-procedures)

---

## Overview

### Purpose
This Standard Operating Procedure (SOP) provides IT support staff and end-users with systematic troubleshooting steps for VPN (Virtual Private Network) connection issues.

### Scope
This document covers:
- Cisco AnyConnect VPN Client (primary)
- GlobalProtect VPN (for executives)
- Windows Built-in VPN (legacy)
- Mobile VPN (iOS and Android)

### VPN Importance
VPN access is critical for:
- Remote work and work-from-home scenarios
- Secure access to internal resources
- Protecting data on public networks
- Accessing file shares and internal applications
- Compliance with security policies

---

## VPN System Information

### Company VPN Details
- **VPN Type:** SSL VPN (Cisco AnyConnect)
- **VPN Gateway Address:** vpn.company.com
- **Backup Gateway:** vpn2.company.com
- **Authentication:** Active Directory credentials + MFA
- **Supported Platforms:** Windows 10/11, macOS 11+, iOS 14+, Android 10+

### Client Software Versions
| Platform | Client | Current Version | Download Link |
|----------|--------|-----------------|---------------|
| Windows | Cisco AnyConnect | 4.10.07073 | https://vpn.company.com/download |
| macOS | Cisco AnyConnect | 4.10.07073 | https://vpn.company.com/download |
| iOS | Cisco Secure Client | 5.0.02046 | App Store |
| Android | Cisco Secure Client | 5.0.02046 | Google Play Store |

### Network Requirements
- **Internet Connection:** Minimum 5 Mbps download, 1 Mbps upload
- **Ports Required:** TCP 443 (HTTPS), UDP 443 (DTLS)
- **DNS:** Must use company DNS when connected
- **Split Tunneling:** Enabled (only corporate traffic routes through VPN)

---

## Common VPN Error Codes

### Error Code Reference Table

| Error Code | Error Message | Common Cause | Quick Fix |
|------------|---------------|--------------|-----------|
| **ERROR-001** | "Connection attempt failed" | Internet connectivity issue | Check internet connection |
| **ERROR-002** | "Authentication failed" | Wrong username/password | Verify credentials, check CAPS LOCK |
| **ERROR-003** | "Certificate validation failed" | Expired or missing certificate | Update VPN client software |
| **ERROR-004** | "Unable to contact VPN server" | Firewall or network blocking | Check firewall settings |
| **ERROR-005** | "Connection timed out" | Network latency/instability | Try again, use backup gateway |
| **ERROR-006** | "Secure gateway rejected connection" | Account locked or disabled | Contact IT Support |
| **ERROR-007** | "MFA authentication failed" | MFA code expired/incorrect | Wait for new MFA code |
| **ERROR-008** | "No network adapter found" | VPN adapter disabled | Enable network adapter |
| **ERROR-009** | "License expired" | VPN license needs renewal | Contact IT Support |
| **ERROR-010** | "Maximum connections reached" | Too many concurrent sessions | Disconnect other VPN sessions |

---

## Troubleshooting Procedures

### TIER 1: Basic Troubleshooting (User Self-Service)
**Estimated Time:** 5-10 minutes  
**Success Rate:** ~70%

#### Step 1: Verify Internet Connection
1. Open a web browser
2. Navigate to **https://www.google.com** or **https://www.bing.com**
3. If page doesn't load:
   - Check Wi-Fi is connected
   - Check Ethernet cable is plugged in
   - Restart router/modem
   - Try mobile hotspot as alternative

**Decision Point:** ✅ Internet works → Continue to Step 2 | ❌ No Internet → Fix internet first

---

#### Step 2: Verify VPN Client is Installed
1. **Windows:** Check Start Menu → Search for "Cisco AnyConnect"
2. **macOS:** Check Applications folder → "Cisco AnyConnect Secure Mobility Client"
3. **Mobile:** Check app drawer for "Cisco Secure Client"

**If VPN client is missing:**
1. Download from: **https://vpn.company.com/download**
2. Run installer as Administrator (Windows) or with sudo (Mac)
3. Follow installation wizard
4. Restart computer after installation

---

#### Step 3: Check VPN Credentials
1. Verify you're using the correct credentials:
   - **Username:** firstname.lastname@company.com (or domain\username)
   - **Password:** Your current Active Directory password
2. Common mistakes:
   - ❌ Using old password (did you recently change it?)
   - ❌ CAPS LOCK is on
   - ❌ Extra spaces before/after username
   - ❌ Wrong domain (should be @company.com, not @gmail.com)

**Test your credentials:**
1. Go to **https://portal.office.com**
2. Try logging in with same credentials
3. If Office 365 login fails → Password is wrong, reset it
4. If Office 365 login works → Continue to Step 4

---

#### Step 4: Basic VPN Connection Attempt
1. Open Cisco AnyConnect client
2. Enter VPN address: **vpn.company.com**
3. Click **Connect**
4. Enter username and password
5. Complete MFA challenge (approve on phone or enter code)
6. Wait for connection (should take 10-30 seconds)

**Success indicators:**
- ✅ Green checkmark or "Connected" status
- ✅ Lock icon turns green/solid
- ✅ IP address shown in VPN client
- ✅ Can access internal resources (e.g., intranet)

---

#### Step 5: The "Turn It Off and On Again" Method
If connection fails, try this proven sequence:

**5A. Disconnect and Reconnect**
1. Click **Disconnect** in VPN client
2. Wait 10 seconds
3. Click **Connect** again
4. Re-enter credentials if prompted

**5B. Restart VPN Client**
1. Completely close VPN client (File → Exit)
2. Wait 5 seconds
3. Reopen VPN client
4. Try connecting again

**5C. Restart Computer**
1. Save all work
2. Close all applications
3. Restart computer (not just shut down)
4. After restart, try VPN connection

**Success Rate after restarts:** ~40% of issues resolved

---

### TIER 2: Intermediate Troubleshooting
**Estimated Time:** 15-20 minutes  
**Success Rate:** ~20%  
**Requires:** Basic technical knowledge

#### Step 6: Try Backup VPN Gateway
Sometimes the primary gateway is overloaded or experiencing issues.

1. Open Cisco AnyConnect
2. Instead of `vpn.company.com`, enter: **vpn2.company.com**
3. Click Connect
4. Enter credentials

**Regional Gateways (if applicable):**
- US East Coast: `vpn-east.company.com`
- US West Coast: `vpn-west.company.com`
- Europe: `vpn-eu.company.com`
- Asia Pacific: `vpn-apac.company.com`

---

#### Step 7: Check Firewall and Antivirus
Firewall or antivirus software may block VPN traffic.

**Windows Firewall:**
1. Open **Windows Security** (Windows key + I → Update & Security → Windows Security)
2. Click **Firewall & network protection**
3. Click **Allow an app through firewall**
4. Scroll to find **Cisco AnyConnect**
5. Ensure both **Private** and **Public** are checked
6. Click OK

**Third-Party Antivirus (Norton, McAfee, Kaspersky, etc.):**
1. Open your antivirus software
2. Look for "Firewall" or "Network Protection" settings
3. Add exception for **Cisco AnyConnect**
4. Whitelist these files:
   - `C:\Program Files (x86)\Cisco\Cisco AnyConnect\vpnagent.exe`
   - `C:\Program Files (x86)\Cisco\Cisco AnyConnect\vpnui.exe`

**Corporate Proxy:**
- If you're behind a corporate proxy, VPN may need proxy settings
- Contact IT Support for proxy configuration

---

#### Step 8: Clear VPN Cache and Preferences
Corrupted cache can cause persistent connection issues.

**Windows:**
1. Close Cisco AnyConnect
2. Open **Run** (Windows key + R)
3. Type: `%ProgramData%\Cisco\Cisco AnyConnect Secure Mobility Client\`
4. Delete these folders:
   - `Cache`
   - `Preferences`
5. Open **Run** again, type: `%LocalAppData%\Cisco\Cisco AnyConnect Secure Mobility Client\`
6. Delete all files in this folder
7. Restart computer
8. Try connecting again

**macOS:**
1. Close Cisco AnyConnect
2. Open **Finder** → **Go** → **Go to Folder...**
3. Type: `~/Library/Preferences/`
4. Delete any files starting with: `com.cisco.anyconnect`
5. Go to: `/opt/cisco/anyconnect/`
6. Delete the `profile` folder
7. Restart Mac
8. Try connecting again

---

#### Step 9: Update VPN Client Software
Outdated VPN client versions can have compatibility issues.

1. Open Cisco AnyConnect
2. Click the **gear icon** (⚙️) or **Settings**
3. Look for **About** or **Check for Updates**
4. If update is available, click **Download** and **Install**
5. Restart computer after update
6. Try connecting

**Manual Update:**
1. Download latest version from: **https://vpn.company.com/download**
2. Run installer (may need Admin rights)
3. Choose **Upgrade** or **Repair** option
4. Follow prompts
5. Restart computer

**Current Version Check:**
- Click **Help** → **About** in VPN client
- Current version should be: **4.10.07073** or newer
- If older than 4.9.x, definitely update

---

#### Step 10: Check Network Adapter Settings
VPN requires specific network adapters to be enabled and functioning.

**Windows:**
1. Open **Control Panel** → **Network and Sharing Center**
2. Click **Change adapter settings** (left sidebar)
3. Look for **Cisco AnyConnect Secure Mobility Client Virtual Miniport Adapter**
4. If it shows "Disabled":
   - Right-click → **Enable**
5. Right-click the adapter → **Properties**
6. Ensure these are checked:
   - ✅ Internet Protocol Version 4 (TCP/IPv4)
   - ✅ Internet Protocol Version 6 (TCP/IPv6)
7. Click OK

**Reset Network Adapters (Windows):**
```powershell
# Open Command Prompt as Administrator
# Run these commands:

netsh winsock reset
netsh int ip reset
ipconfig /release
ipconfig /renew
ipconfig /flushdns
```

After running these commands, restart your computer.

---

### TIER 3: Advanced Troubleshooting
**Estimated Time:** 20-30 minutes  
**Requires:** Advanced technical knowledge or IT support assistance  
**Success Rate:** ~10%

#### Step 11: Review VPN Logs
Logs provide detailed error information for diagnosis.

**Windows - Access Logs:**
1. Open **File Explorer**
2. Navigate to: `C:\ProgramData\Cisco\Cisco AnyConnect Secure Mobility Client\Logs`
3. Open the most recent log file (sorted by date)
4. Look for lines containing: `ERROR`, `FAILED`, `DENIED`

**macOS - Access Logs:**
1. Open **Terminal**
2. Run: `tail -f /opt/cisco/anyconnect/bin/vpnagentd.log`
3. Try connecting while watching the log
4. Look for error messages

**Common Log Errors:**
- `"SSL handshake failed"` → Certificate issue, update client
- `"Authentication rejected"` → Credentials invalid, reset password
- `"Adapter binding failed"` → Network adapter problem, reinstall client
- `"Host unreachable"` → Firewall blocking or gateway down

---

#### Step 12: Reinstall VPN Client (Clean Install)
If all else fails, completely remove and reinstall the VPN client.

**Windows - Complete Removal:**
1. Open **Control Panel** → **Programs and Features**
2. Find **Cisco AnyConnect Secure Mobility Client**
3. Right-click → **Uninstall**
4. Follow uninstallation wizard
5. After uninstall, delete these folders:
   - `C:\Program Files (x86)\Cisco\Cisco AnyConnect\`
   - `C:\ProgramData\Cisco\Cisco AnyConnect Secure Mobility Client\`
6. Restart computer
7. Download fresh installer from: **https://vpn.company.com/download**
8. Run installer as Administrator
9. Follow installation wizard
10. Restart computer again
11. Try connecting

**macOS - Complete Removal:**
1. Run the uninstaller: `/opt/cisco/anyconnect/bin/anyconnect_uninstall.sh`
2. Enter administrator password when prompted
3. Delete these folders:
   - `/opt/cisco/anyconnect/`
   - `~/Library/Preferences/com.cisco.anyconnect*`
4. Restart Mac
5. Download and install fresh copy

---

#### Step 13: Check for IP Address Conflicts
IP address conflicts can prevent VPN from establishing proper routing.

**Windows:**
1. Open **Command Prompt** (Win + R, type `cmd`)
2. Run: `ipconfig /all`
3. Look for "Cisco AnyConnect" adapter
4. Note the IP address
5. If IP is `169.254.x.x` → DHCP failure, need to troubleshoot network
6. If IP shows "Duplicate" or "Conflict" → Run: `ipconfig /release` then `ipconfig /renew`

**Test for Conflicts:**
```cmd
ping 10.0.0.1
# Should respond from VPN gateway, not local router
```

---

#### Step 14: MTU (Maximum Transmission Unit) Adjustment
MTU size mismatches can cause VPN connections to drop or fail.

**Windows - Check MTU:**
```cmd
netsh interface ipv4 show subinterfaces
```

**Adjust MTU if needed:**
```cmd
netsh interface ipv4 set subinterface "Ethernet" mtu=1400 store=persistent
```

**Optimal MTU for VPN:** 1400 bytes (default is 1500)

---

#### Step 15: DNS Resolution Issues
Sometimes VPN connects but you can't access internal resources due to DNS.

**Test DNS:**
```cmd
nslookup intranet.company.com
```

**If DNS fails:**
1. Open **Network Adapter Settings**
2. Right-click VPN adapter → **Properties**
3. Select **Internet Protocol Version 4 (TCP/IPv4)**
4. Click **Properties**
5. Select **Use the following DNS server addresses:**
   - Preferred DNS: `10.0.0.10`
   - Alternate DNS: `10.0.0.11`
6. Click OK

---

## Platform-Specific Instructions

### Windows 10/11 Specific Issues

#### Issue: "VPN Adapter Not Found"
**Solution:**
1. Open **Device Manager** (Win + X → Device Manager)
2. View → Show hidden devices
3. Expand **Network adapters**
4. Look for "Cisco AnyConnect Virtual Miniport Adapter for Windows x64"
5. If it has a yellow warning icon:
   - Right-click → **Update driver**
   - Choose **Browse my computer for drivers**
   - Navigate to: `C:\Program Files (x86)\Cisco\Cisco AnyConnect\`
   - Click **Next** and install

#### Issue: Windows 11 Compatibility
- Windows 11 requires VPN client version **4.10.04065** or newer
- Older versions will fail to connect
- Download latest from IT portal

---

### macOS Specific Issues

#### Issue: "Extension Blocked" on macOS
**Solution:**
1. Go to **System Preferences** → **Security & Privacy**
2. Click the **General** tab
3. Look for message: *"System software from Cisco was blocked from loading"*
4. Click **Allow**
5. Enter admin password
6. Restart Mac
7. Try connecting again

#### Issue: Keychain Access Prompts
If macOS repeatedly asks for keychain password:
1. Open **Keychain Access** app
2. Search for: `Cisco AnyConnect`
3. Right-click each item → **Get Info**
4. Go to **Access Control** tab
5. Select **Allow all applications to access this item**
6. Save changes

---

### Mobile (iOS/Android) Specific Issues

#### iOS VPN Setup
1. Download **Cisco Secure Client** from App Store
2. Open app
3. Tap **Connections** → **Add VPN Connection**
4. Enter:
   - **Description:** Company VPN
   - **Server Address:** vpn.company.com
5. Save
6. Tap **Connect**
7. Approve MFA on your phone

#### Android VPN Setup
1. Download **Cisco Secure Client** from Google Play
2. Open app
3. Tap **+** to add connection
4. Enter server: `vpn.company.com`
5. Tap **Connect**
6. Enter credentials
7. Complete MFA

#### Common Mobile Issues:
- **Battery Optimization:** Disable battery optimization for VPN app
- **Always-On VPN:** May conflict, disable it
- **Kill Switch:** If enabled, can prevent connection

---

## Security and Best Practices

### Security Requirements
- ✅ Always use VPN when working remotely
- ✅ Never share VPN credentials
- ✅ Disconnect VPN when not actively working
- ✅ Keep VPN client updated
- ✅ Report suspicious connection prompts to IT Security

### What VPN Does NOT Protect
- ❌ Does not make you anonymous online
- ❌ Does not replace antivirus software
- ❌ Does not prevent phishing attacks
- ❌ Does not protect against social engineering

### VPN Connection Best Practices
1. **Connect before accessing company resources**
2. **Disconnect when done** (reduces gateway load)
3. **Use primary gateway first** (vpn.company.com)
4. **Don't run multiple VPNs simultaneously** (conflicts)
5. **Report slow connections** to IT (may indicate issues)

### Performance Tips
- Close unnecessary applications while on VPN
- Pause cloud sync services (OneDrive, Dropbox) temporarily
- Use wired connection instead of Wi-Fi when possible
- Close browser tabs you're not using
- Avoid streaming video while on VPN

---

## Escalation Procedures

### When to Escalate to IT Support

Escalate if:
- ✋ All Tier 1 and Tier 2 steps have failed
- ✋ Error message is not in common error code table
- ✋ VPN connects but no access to any internal resources
- ✋ Multiple users reporting same issue (potential outage)
- ✋ Account lockout after VPN authentication attempts
- ✋ Urgent business need (executive, critical meeting)

### Information to Provide When Escalating

Create a ticket or call with this information:
1. **Your Details:**
   - Name
   - Employee ID
   - Department
   - Phone number
   - Email
2. **Issue Details:**
   - Exact error message (screenshot if possible)
   - When did issue start?
   - Can you connect from another location/network?
   - VPN client version (Help → About)
   - Operating system and version
3. **Troubleshooting Done:**
   - List of steps already attempted
   - Results of each step
4. **Business Impact:**
   - Urgent/High/Medium/Low
   - Are you unable to work?

---

## Contact Information

### IT Support Helpdesk
- **Phone (US):** 1-800-IT-HELP (1-800-484-3571)
- **Phone (International):** +1-555-484-3571
- **Email:** itsupport@company.com
- **Chat:** https://support.company.com/chat
- **Ticket Portal:** https://support.company.com

### Network Operations Center (NOC)
For VPN outages affecting multiple users:
- **Phone:** 1-800-NET-DOWN
- **Email:** noc@company.com
- **Status Page:** https://status.company.com

### Hours
- **Standard Support:** Monday-Friday, 7 AM - 7 PM EST
- **After-Hours Support:** Emergency only, 24/7
- **VPN Status Updates:** Check status page for outages

---

## Appendix A: VPN Connection Checklist

Use this checklist before calling IT Support:

- [ ] Internet connection is working (tested with web browser)
- [ ] VPN client is installed and updated
- [ ] Tried primary gateway (vpn.company.com)
- [ ] Tried backup gateway (vpn2.company.com)
- [ ] Verified username and password are correct
- [ ] Tested credentials on Office 365 portal
- [ ] CAPS LOCK is off
- [ ] Restarted VPN client
- [ ] Restarted computer
- [ ] Checked firewall allows VPN
- [ ] VPN adapter is enabled
- [ ] Cleared VPN cache
- [ ] No VPN adapter errors in Device Manager
- [ ] Reviewed VPN logs for errors
- [ ] Tried from different network (mobile hotspot)

**If all checked and still not working → Contact IT Support**

---

## Appendix B: Quick Reference - Error Messages

| Error Message | Translation | Fix |
|---------------|-------------|-----|
| "The VPN connection failed due to unsuccessful domain name resolution" | Can't find VPN server | Check internet, try backup gateway |
| "The secure gateway has rejected the connection attempt" | Authentication problem | Verify credentials, check account not locked |
| "Connection attempt has timed out" | Network too slow/unstable | Try different network, check internet speed |
| "AnyConnect was not able to establish a connection to the specified secure gateway" | Firewall blocking | Check firewall settings, contact IT if corporate network |
| "The certificate on the secure gateway is invalid" | Outdated VPN client | Update VPN client to latest version |
| "Reconnecting to VPN" (keeps looping) | Network unstable | Switch to wired connection, restart router |

---

## Document Revision History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | Jan 2022 | Initial SOP creation | Network Team |
| 2.0 | Jun 2023 | Added Tier 2/3 troubleshooting | J. Martinez |
| 2.5 | Dec 2023 | Added mobile instructions | IT Support |
| 3.0 | Jun 2024 | Updated for new VPN gateways | Network Team |
| 3.1 | Sep 2024 | Added Windows 11 specific issues | K. Thompson |
| 3.2 | Dec 2025 | Updated error codes and escalation procedures | M. Johnson |

---

**Document Classification:** Internal Use Only  
**Next Review Date:** June 2026  
**Compliance:** SOC 2, ISO 27001, NIST 800-171

*For VPN outages or emergency support, call 1-800-IT-HELP*
