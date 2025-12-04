# IT Support SOP - Printer Issues and Troubleshooting

## Document Information
- **Document Version:** 3.1
- **Last Updated:** December 2025
- **Department:** IT End User Support
- **Classification:** Internal Use Only
- **SOP ID:** IT-EUS-PRINT-003

---

## Table of Contents
1. [Overview](#overview)
2. [Printer Types and Identification](#printer-types-and-identification)
3. [Common Printer Issues](#common-printer-issues)
4. [Quick Troubleshooting Steps](#quick-troubleshooting-steps)
5. [Issue-Specific Solutions](#issue-specific-solutions)
6. [Print Quality Problems](#print-quality-problems)
7. [Connection and Network Issues](#connection-and-network-issues)
8. [Driver Installation and Updates](#driver-installation-and-updates)
9. [Print Queue Management](#print-queue-management)
10. [Escalation and Support](#escalation-and-support)

---

## Overview

### Purpose
This SOP provides comprehensive troubleshooting procedures for printer-related issues across all company printing devices.

### Scope
Covers:
- Network printers (office MFPs)
- USB-connected local printers
- Wireless printers
- Print servers and print queues
- Mobile printing issues

### Common Printer Problems (By Frequency)
1. 📊 **Printer offline/not found** (35%)
2. 📊 **Paper jams** (25%)
3. 📊 **Print quality issues** (20%)
4. 📊 **Stuck print jobs** (10%)
5. 📊 **Driver problems** (5%)
6. 📊 **Other** (5%)

### Average Resolution Time
- Basic issues: 5-10 minutes
- Intermediate: 15-25 minutes
- Complex/Hardware: 30+ minutes or technician dispatch

---

## Printer Types and Identification

### Network Printers (Most Common)
**Characteristics:**
- Connected to company network via Ethernet
- Shared by multiple users
- Usually located in common areas
- Managed through print server
- Examples: HP LaserJet Pro, Xerox WorkCentre, Canon imageRUNNER

**How to identify:**
- Look for Ethernet cable connected to printer
- Check printer LCD screen for IP address
- Printer name format: `FLOOR-LOCATION-MODEL` (e.g., `3F-East-HPM605`)

---

### USB Printers (Local)
**Characteristics:**
- Connected directly to one computer via USB
- Personal use, not shared
- Common for home offices or executives

**How to identify:**
- USB cable from printer to computer
- Shows as "Local printer" in devices

---

### Wireless Printers
**Characteristics:**
- Connected via Wi-Fi
- Can be shared or personal
- Requires proper network configuration

**How to identify:**
- No physical cables
- Wi-Fi icon on printer display
- Network settings show SSID

---

### Multi-Function Printers (MFPs)
**Features:**
- Print, Copy, Scan, Fax
- Usually network-connected
- Larger office machines

**Special notes:**
- Each function may have separate issues
- Scan-to-email may require separate configuration

---

## Common Printer Issues

### Issue Categories and Quick Diagnosis

| Symptom | Likely Cause | Quick Test |
|---------|--------------|------------|
| "Printer not found" / Offline | Network/connection issue | Can you ping the printer? |
| Blank pages printing | Toner/ink empty or not installed | Check toner levels |
| Partial printouts / Cut-off text | Wrong paper size or scaling | Check print preview |
| Smudged or faded prints | Low toner or dirty components | Print test page |
| Paper jams | Wrong paper type, worn rollers | Open and inspect |
| Nothing happens when printing | Print queue stuck or paused | Check print queue |
| Prints but wrong content | Wrong document sent | Check print history |
| Error codes on display | Hardware or firmware issue | Note error code |

---

## Quick Troubleshooting Steps

### STEP 1: The Universal Printer Fix (Success Rate: 50%)
**Turn it off and back on - for both printer AND computer**

**Printer restart:**
1. Press **Power** button on printer (wait for shutdown)
2. Wait **30 seconds**
3. Turn printer back **on**
4. Wait for initialization (1-2 minutes)
5. Look for "Ready" status on display

**Computer restart:**
1. Save all work
2. **Restart** computer (not just logoff)
3. Wait for complete restart
4. Try printing again

**Why this works:**
- Clears error states
- Resets network connection
- Clears memory/buffer
- Reconnects print services

---

### STEP 2: Check Physical Basics
**Before diving into software, check hardware:**

**Power and Connections:**
- ✅ Is printer powered on? (look for lights/display)
- ✅ Power cable securely connected?
- ✅ For network printers: Ethernet cable connected?
- ✅ For USB printers: USB cable connected at both ends?
- ✅ Any error messages on printer display?

**Paper:**
- ✅ Paper loaded in tray?
- ✅ Paper guides adjusted to paper size?
- ✅ Paper not crumpled or stuck?
- ✅ Tray fully closed?

**Consumables:**
- ✅ Toner/ink cartridges installed?
- ✅ Protective tape removed from new cartridges?
- ✅ Sufficient toner/ink remaining?

---

### STEP 3: Check Printer Status

**Windows 10/11:**
1. Open **Settings** → **Devices** → **Printers & scanners**
2. Find your printer in the list
3. Click on it
4. Look at status:
   - ✅ **"Ready"** = Good
   - ⚠️ **"Offline"** = Connection problem
   - ⚠️ **"Paused"** = Manually paused
   - ⚠️ **"Error"** = Check printer display
   - ⚠️ **"Driver unavailable"** = Need driver update

**Quick status check:**
- Click **Open queue**
- Look for stuck jobs
- Check if printer is set to "Use Printer Offline" (should be unchecked)

---

### STEP 4: Print Test Page
**Confirms printer hardware is functioning:**

**From printer (preferred method):**
1. Press **Menu** or **Settings** button on printer
2. Navigate to **Reports** or **Information**
3. Select **Configuration Page** or **Test Page**
4. Press **OK** or **Print**

**If test page prints correctly:**
- ✅ Printer hardware works
- ✅ Issue is with computer/network/driver

**If test page fails or blank:**
- ❌ Printer hardware problem
- ❌ Check toner/ink
- ❌ May need technician

---

## Issue-Specific Solutions

### Issue 1: Printer Shows "Offline"

**CAUSE:** Computer can't communicate with printer.

**SOLUTION A: Set Printer Online (Windows)**
1. **Control Panel** → **Devices and Printers**
2. Right-click your printer
3. **Uncheck** "Use Printer Offline"
4. Try printing again

**SOLUTION B: Restart Print Spooler Service**
1. Press **Win + R**, type `services.msc`, press Enter
2. Find **Print Spooler**
3. Right-click → **Restart**
4. Wait 10 seconds
5. Try printing again

**SOLUTION C: Remove and Re-add Printer**
1. **Settings** → **Devices** → **Printers & scanners**
2. Click your printer → **Remove device**
3. Click **Add a printer or scanner**
4. Wait for detection
5. Select your printer from list
6. Click **Add device**

**For Network Printers - Check IP Address:**
1. Print configuration page from printer
2. Note the IP address (e.g., 192.168.1.100)
3. Open **Command Prompt**
4. Type: `ping 192.168.1.100` (use actual printer IP)
5. If "Request timed out" = Network issue
6. If replies received = Network OK, likely driver/software issue

---

### Issue 2: Paper Jams

**IMPORTANT:** Never force paper out - can damage printer!

**STEP-BY-STEP PAPER JAM REMOVAL:**

1. **Power off** printer (prevents damage)
2. **Open all access doors:**
   - Front cover
   - Rear access panel
   - Top scanner lid
   - Duplexer unit (for two-sided printers)
3. **Locate the jammed paper:**
   - Printer display may show location
   - Look in all paper paths
4. **Remove paper carefully:**
   - Pull in direction of paper path
   - Use both hands for large sheets
   - Remove all fragments (even small pieces)
5. **Check for obstacles:**
   - Paper clips, staples
   - Torn paper pieces
   - Foreign objects
6. **Close all doors firmly**
7. **Power on** printer
8. **Try printing** test page

**PREVENTION TIPS:**
- ✅ Use correct paper type (20-24 lb for most printers)
- ✅ Don't overfill paper tray (max line indicator)
- ✅ Fan paper before loading (prevents static cling)
- ✅ Adjust paper guides to fit paper snugly
- ✅ Remove damaged or wrinkled sheets
- ✅ Don't mix paper types in same tray

**COMMON JAM LOCATIONS:**
- **Input tray:** Paper not feeding properly
- **Duplexer:** Two-sided printing mechanism
- **Fuser area:** Paper stuck in heating unit (HOT! Wait to cool)
- **Output tray:** Paper not exiting properly

**IF JAMS PERSIST:**
- Worn pickup rollers (common after 50k+ pages)
- Wrong paper type
- Submit maintenance ticket

---

### Issue 3: Blank Pages Printing

**CAUSE:** Usually toner/ink related.

**CHECK 1: Toner/Ink Levels**
1. Check printer display for toner status
2. Or print configuration page (shows toner levels)
3. If low/empty:
   - Replace cartridge
   - Shake cartridge gently to distribute remaining toner (temporary fix)

**CHECK 2: Protective Tape on New Cartridge**
- New toner cartridges have orange/yellow protective tape
- MUST be removed before installation
- Remove cartridge, check for tape, remove if present

**CHECK 3: Print Head Issues (Inkjet)**
1. Run **Print Head Cleaning** utility:
   - **Control Panel** → **Devices and Printers**
   - Right-click printer → **Printing Preferences**
   - Find **Maintenance** or **Tools** tab
   - Click **Clean Print Heads**
2. Run 2-3 times if necessary
3. Print nozzle check pattern to verify

**CHECK 4: Driver Setting**
- Open print dialog
- Check print settings
- Ensure **not set to "Draft mode" with "Save Toner" enabled**

---

### Issue 4: Print Job Stuck in Queue

**SYMPTOM:** Document shows "Printing" but nothing happens.

**SOLUTION 1: Cancel and Restart**
1. Open **Devices and Printers**
2. Double-click your printer to open queue
3. Right-click stuck job → **Cancel**
4. If it won't cancel, proceed to Solution 2

**SOLUTION 2: Clear Print Queue (Command)**
**Windows:**
1. Open **Command Prompt** as Administrator
2. Run these commands:
   ```cmd
   net stop spooler
   del /Q /F /S "%windir%\System32\spool\PRINTERS\*.*"
   net start spooler
   ```
3. All print jobs will be cleared
4. Try printing again

**SOLUTION 3: PowerShell Method**
```powershell
Stop-Service -Name Spooler -Force
Remove-Item -Path "C:\Windows\System32\spool\PRINTERS\*" -Force
Start-Service -Name Spooler
```

**SOLUTION 4: Restart Print Spooler (GUI)**
1. **Win + R**, type `services.msc`
2. Find **Print Spooler**
3. Right-click → **Stop**
4. Navigate to: `C:\Windows\System32\spool\PRINTERS\`
5. Delete all files in folder
6. Back to Services, right-click **Print Spooler** → **Start**

---

### Issue 5: Printer Not Found / Can't Detect

**FOR NETWORK PRINTERS:**

**CHECK 1: Verify Printer is On Network**
1. Get printer IP address from printer display
   - Press **Menu** → **Network** → **TCP/IP**
   - Note IP address (e.g., 192.168.10.50)
2. From computer, open **Command Prompt**
3. Ping printer: `ping 192.168.10.50`
4. If successful: Can see printer on network
5. If fails: Network connectivity issue

**CHECK 2: Add Printer by IP Address (Manual)**
1. **Settings** → **Devices** → **Printers & scanners**
2. Click **Add a printer or scanner**
3. Wait, then click **"The printer that I want isn't listed"**
4. Select **"Add a printer using a TCP/IP address or hostname"**
5. **Device type:** TCP/IP Device
6. **Hostname or IP address:** Enter printer IP (e.g., 192.168.10.50)
7. **Port name:** Auto-fills
8. **Uncheck** "Query the printer"
9. Click **Next**
10. Select printer manufacturer and model
11. Click **Next**, then **Finish**

**FOR USB PRINTERS:**

**CHECK 1: USB Connection**
1. Unplug USB cable from computer
2. Wait 10 seconds
3. Plug into **different USB port** (preferably USB 3.0)
4. Wait for Windows to detect
5. Check **Device Manager** for any yellow exclamation marks

**CHECK 2: USB Port Issues**
1. Try different USB cable (if available)
2. Test USB port with another device (flash drive)
3. Avoid USB hubs - connect directly to computer

---

### Issue 6: Printing Very Slow

**CAUSE:** Network issues, large files, or printer settings.

**CHECK 1: Document Complexity**
- Large PDFs with images = slower
- High-resolution graphics = slower
- Print a simple text document to compare

**CHECK 2: Print Quality Settings**
1. Open **Print** dialog
2. Click **Preferences** or **Properties**
3. Check quality setting:
   - **Draft:** Fast but lower quality
   - **Normal:** Balance (recommended)
   - **Best/High:** Slow but best quality
4. For internal documents, use **Draft** or **Normal**

**CHECK 3: Network Congestion**
- Large print jobs can take time over network
- Check if others are printing simultaneously
- Wait for queue to clear

**CHECK 4: Printer Memory**
- Some printers have limited memory
- Large/complex documents may cause slowdowns
- Check if printer display shows "Processing" or "Memory low"
- Contact IT if consistent issue

---

## Print Quality Problems

### Streaks or Lines on Printouts

**CAUSE:** Dirty drums, scratched drum, or toner issue.

**FIX 1: Clean Printer**
1. Power off printer
2. Remove toner cartridge
3. Look for blue or green cleaning tab (HP printers)
4. Gently pull tab all the way out, then push back in
5. For other brands: Gently wipe drum with lint-free cloth
6. Reinstall cartridge
7. Print cleaning page (printer menu)

**FIX 2: Replace Toner/Drum**
- If cleaning doesn't help, toner or drum may be damaged
- Check page count - drums typically last 20-50k pages
- Submit supply replacement request

---

### Faded or Light Printouts

**CAUSE:** Low toner, toner save mode, or dirty optics.

**FIX 1: Check Toner Level**
- Print configuration page (shows percentage)
- If below 10%, replace toner

**FIX 2: Disable Toner Save Mode**
1. Open **Printer Properties**
2. Look for **EconoMode** or **Toner Save**
3. **Disable** it
4. Click **OK**

**FIX 3: Shake Toner Cartridge**
1. Remove toner cartridge
2. Gently shake side-to-side 5-6 times
3. Reinstall
4. Try printing (temporary fix)

---

### Smudged or Smeared Prints

**CAUSE:** Fuser unit issue or wrong paper type.

**FIX 1: Check Paper Type**
- Using correct paper weight (20-24 lb)?
- Not using glossy photo paper in laser printer?
- Paper damp or humid?

**FIX 2: Clean Fuser Rollers**
1. Run cleaning page from printer menu
2. Most printers have built-in cleaning cycle
3. Menu → Maintenance → Cleaning

**FIX 3: Fuser Replacement**
- If smudging persists, fuser may be worn
- Fusers last ~50-100k pages
- Requires technician replacement

---

### Spots or Dots on Prints

**CAUSE:** Dirty scanner glass (for copies) or drum issues.

**FIX FOR COPYING:**
1. Lift scanner lid
2. Clean glass with glass cleaner and soft cloth
3. Also clean white backing (ADF lid)
4. Wipe dry
5. Try copying again

**FIX FOR PRINTING:**
- Print cleaning page
- Replace toner if issue persists

---

## Connection and Network Issues

### Wireless Printer Connection Setup

**INITIAL SETUP:**
1. **On Printer:**
   - Press **Wireless** or **Network** button
   - Select **Wireless Setup Wizard**
   - Choose your **Wi-Fi network** (usually: Company-WiFi or Corp-Wireless)
   - Enter Wi-Fi password if prompted
   - Wait for connection confirmation
2. **On Computer:**
   - Add printer as described in "Printer Not Found" section
   - Use printer's IP address shown on display

**TROUBLESHOOTING WIRELESS:**
- Ensure printer and computer on same network
- Check Wi-Fi signal strength on printer
- Restart wireless router
- Forget network on printer and reconnect

---

### Print Server Issues

**Company printers often connect through print server.**

**CHECK PRINT SERVER STATUS:**
1. Open web browser
2. Go to: http://printserver.company.com (or https://printserver/)
3. Look for your printer in list
4. Check status indicator

**IF PRINT SERVER UNAVAILABLE:**
- Try direct IP printing (bypass server)
- Contact IT Support - may be server outage

---

## Driver Installation and Updates

### Installing Printer Drivers

**METHOD 1: Windows Update (Preferred)**
1. **Settings** → **Update & Security** → **Windows Update**
2. Click **View optional updates**
3. Expand **Driver updates**
4. Check box for your printer
5. Click **Download and install**

**METHOD 2: Manufacturer Website**
1. Visit manufacturer's support site:
   - HP: support.hp.com
   - Canon: usa.canon.com/support
   - Xerox: support.xerox.com
   - Epson: epson.com/support
2. Enter printer model number
3. Download driver for your OS (Windows 10/11)
4. Run installer
5. Follow prompts

**METHOD 3: IT Software Center**
- Many companies provide drivers through software portal
- Check your company's IT self-service portal

---

### Updating Printer Drivers

**WHEN TO UPDATE:**
- After Windows major updates
- Printer not working after OS upgrade
- New features not available
- Manufacturer recommends update

**HOW TO UPDATE:**
1. **Device Manager** method:
   - Right-click **Start** → **Device Manager**
   - Expand **Printers** or **Print queues**
   - Right-click your printer → **Update driver**
   - Choose **Search automatically for drivers**
2. **Manual update:**
   - Download latest driver from manufacturer
   - Run installer (may say "Upgrade" or "Repair")

---

## Print Queue Management

### Viewing Print Queue

**Windows:**
1. **Settings** → **Devices** → **Printers & scanners**
2. Click your printer → **Open queue**

**OR:**
1. **Control Panel** → **Devices and Printers**
2. Double-click your printer

### Managing Print Jobs

**PAUSE A PRINT JOB:**
- Right-click job → **Pause**
- Useful if you need to print something urgent first

**CANCEL A PRINT JOB:**
- Right-click job → **Cancel**
- May take a moment to clear

**PRIORITIZE A PRINT JOB:**
- Pause all other jobs
- Leave only urgent job active

### Print Spooler Service

**WHAT IT DOES:**
- Manages print jobs
- Queues documents
- Communicates with printer

**COMMON ISSUES:**
- Service crashes = Can't print anything
- Service hung = Jobs stuck in queue

**HOW TO RESTART:**
- See "Issue 4: Print Job Stuck in Queue" above

---

## Mobile Printing

### iOS (iPhone/iPad)

**USING AIRPRINT:**
1. Open document/photo/email
2. Tap **Share** icon (square with arrow)
3. Scroll and tap **Print**
4. Tap **Select Printer**
5. Choose your printer (must be AirPrint compatible)
6. Set options (copies, range, etc.)
7. Tap **Print**

**TROUBLESHOOTING:**
- iPhone and printer must be on same Wi-Fi network
- Not all printers support AirPrint
- Restart both devices if printer not found

---

### Android

**USING GOOGLE CLOUD PRINT (or Manufacturer App):**
1. Install printer app (HP Smart, Canon Print, Epson iPrint)
2. Open app and add printer
3. Select document to print
4. Tap **Print**

**OR Built-in Android Printing:**
1. Open document
2. Tap **⋮** (three dots) → **Print**
3. Select printer
4. Tap **Print**

---

### Email to Print (Enterprise Feature)

**SOME COMPANY PRINTERS HAVE EMAIL ADDRESSES:**
1. Get printer email from IT (e.g., 3F-East-Printer@company.com)
2. Email document as attachment to that address
3. Document prints automatically
4. Check with IT if available for your printer

---

## Escalation and Support

### When to Escalate to IT Support

**ESCALATE IF:**
- ⚠️ Tried all basic troubleshooting with no success
- ⚠️ Hardware issue (paper jams persist, mechanical noise)
- ⚠️ Need toner/ink replacement (if not self-service)
- ⚠️ Printer firmware update needed
- ⚠️ Network printer can't be found by anyone
- ⚠️ Printer shows hardware error codes
- ⚠️ Physical damage to printer
- ⚠️ Need new printer driver installed
- ⚠️ Multiple users affected (potential outage)

### Information to Provide

**When creating ticket, include:**
1. **Printer details:**
   - Printer name/location
   - Model number
   - IP address (if known)
   - Connection type (network/USB/wireless)
2. **Issue description:**
   - Specific problem
   - Error messages (exact text or screenshot)
   - When issue started
   - Frequency (always/sometimes)
3. **Troubleshooting attempted:**
   - List steps already tried
   - Results of each step
4. **Business impact:**
   - Urgency level (High/Medium/Low)
   - How many users affected
   - Critical documents waiting to print

---

### Printer Supplies Requests

**TO REQUEST TONER/INK:**
- Email: supplies@company.com
- Portal: https://supplies.company.com
- Include: Printer model, toner part number, location

**EXPECTED DELIVERY:**
- Stock items: 1-2 business days
- Special order: 3-5 business days
- Emergency: Contact IT Support

---

### Hardware Repair/Replacement

**FOR PRINTER REPAIRS:**
- Email: facilities@company.com
- Include: Asset tag, issue description, location
- Technician dispatch: 1-3 business days

**FOR PRINTER REPLACEMENT:**
- Manager approval required
- Submit request through IT asset portal
- Typical wait: 5-10 business days

---

## Contact Information

### IT Support Helpdesk
- **Phone:** 1-800-IT-HELP (1-800-484-3571)
- **Email:** itsupport@company.com
- **Chat:** https://support.company.com/chat
- **Portal:** https://support.company.com

### Print Services Team
- **Email:** printservices@company.com
- **Phone:** ext. 5432
- **For:** Network printer issues, driver installation, print server problems

### Facilities (Hardware Issues)
- **Email:** facilities@company.com
- **Phone:** ext. 6789
- **For:** Physical printer repairs, paper jams requiring disassembly, hardware replacement

---

## Quick Reference Guide

### 5-Minute Printer Troubleshooting Checklist

- [ ] Is printer powered on?
- [ ] Does printer display show "Ready"?
- [ ] Is paper loaded?
- [ ] Is toner/ink installed and sufficient?
- [ ] Restart printer (30 seconds off, then on)
- [ ] Restart computer
- [ ] Check if printer shows offline → Set online
- [ ] Print test page from printer itself
- [ ] Check for stuck print jobs → Clear queue
- [ ] Try printing simple text document

**If all checked and still not working → Contact IT Support**

---

## Common Error Codes

| Error Code | Meaning | Solution |
|------------|---------|----------|
| 13.XX.XX | Paper jam | Clear jam, restart printer |
| 49.XXXX | Firmware error | Power cycle, update firmware |
| 50.X | Fuser error | Power cycle, may need fuser replacement |
| 10.XXXX | Supply memory error | Reinstall cartridge, check chip contacts |
| 59.X | Motor error | Power cycle, contact IT if persists |
| 79.XXXX | Critical error | Power cycle, disconnect USB/network, reconnect |

---

## Document Revision History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | May 2021 | Initial printer SOP | IT Support Team |
| 2.0 | Nov 2022 | Added wireless and mobile printing | L. Martinez |
| 2.5 | May 2023 | Expanded troubleshooting steps | IT Support Team |
| 3.0 | Oct 2024 | Added Windows 11 instructions | R. Thompson |
| 3.1 | Dec 2025 | Added print quality and error codes | M. Johnson |

---

**Document Classification:** Internal Use Only  
**Next Review Date:** June 2026  
**Compliance:** IT Service Management Standards v3.0

*For urgent printing issues during business hours, call IT Support at 1-800-IT-HELP*
