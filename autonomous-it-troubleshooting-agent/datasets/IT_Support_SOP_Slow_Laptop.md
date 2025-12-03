# IT Support SOP - Slow Laptop Troubleshooting

## Document Information
- **Document Version:** 2.8
- **Last Updated:** December 2025
- **Department:** IT End User Support
- **Classification:** Internal Use Only
- **SOP ID:** IT-EUS-PERF-002

---

## Table of Contents
1. [Overview](#overview)
2. [Initial Assessment](#initial-assessment)
3. [Quick Fixes (5-10 minutes)](#quick-fixes-5-10-minutes)
4. [Intermediate Solutions (15-30 minutes)](#intermediate-solutions-15-30-minutes)
5. [Advanced Troubleshooting (30+ minutes)](#advanced-troubleshooting-30-minutes)
6. [Hardware vs Software Issues](#hardware-vs-software-issues)
7. [Prevention and Maintenance](#prevention-and-maintenance)
8. [Escalation Criteria](#escalation-criteria)

---

## Overview

### Purpose
This SOP provides systematic troubleshooting procedures for addressing slow laptop performance issues reported by end users.

### Scope
Applies to:
- Company-issued laptops (Windows 10/11, macOS)
- Performance degradation complaints
- Slow boot times
- Application lag and freezing
- General system sluggishness

### Common Causes of Slow Laptops
1. ⚠️ **Too many startup programs** (40% of cases)
2. ⚠️ **Insufficient RAM/memory** (25% of cases)
3. ⚠️ **Full hard drive** (15% of cases)
4. ⚠️ **Malware or viruses** (10% of cases)
5. ⚠️ **Outdated software/drivers** (5% of cases)
6. ⚠️ **Hardware failure** (5% of cases)

---

## Initial Assessment

### Step 1: Gather Information
Before starting troubleshooting, ask the user:

**Key Questions:**
1. ❓ When did you first notice the slowness?
   - Today/Recently/Gradually over time?
2. ❓ Is it always slow or only sometimes?
   - All the time / Morning only / When using specific apps?
3. ❓ Which applications are you using when it's slow?
   - Email / Browser / Office apps / Multiple programs?
4. ❓ Have you recently installed any new software?
5. ❓ When was the last time you restarted your laptop?
6. ❓ How much storage space is left on your laptop?

**Set Expectations:**
- Basic fixes: 5-10 minutes
- Intermediate: 15-30 minutes  
- Advanced: 30-60 minutes
- Some fixes require restart

---

### Step 2: Quick Visual Assessment

**Check Task Manager (Windows):**
1. Press **Ctrl + Shift + Esc** to open Task Manager
2. Click **More details** if needed
3. Check **Performance** tab

**Look for:**
- 🔴 **CPU** above 80% while idle = CPU bottleneck
- 🔴 **Memory** above 90% = RAM insufficient
- 🔴 **Disk** at 100% = Disk performance issue
- 🔴 **Network** high usage = Possible malware or sync issues

**Check Activity Monitor (macOS):**
1. Open **Spotlight** (Cmd + Space)
2. Type "Activity Monitor"
3. Check **CPU, Memory, Disk** tabs

---

## Quick Fixes (5-10 minutes)

### Fix 1: Restart the Laptop (Success Rate: 40%)
**The most effective first step!**

**Why this works:**
- Clears memory (RAM)
- Stops stuck processes
- Applies pending updates
- Resets network connections

**Steps:**
1. **Save all work** first
2. Close all applications
3. Click **Start** → **Power** → **Restart** (NOT Shut Down)
4. Wait for complete restart (2-5 minutes)
5. Test performance

**Important:** 
- ✅ Use "Restart" not "Shut Down"
- ✅ Wait for full restart before testing
- ❌ Don't just close the laptop lid

**If restart solves the issue:**
- Recommend restarting at least once per week
- Issue likely was memory leaks or stuck processes

---

### Fix 2: Close Unnecessary Programs

**Check what's running:**
1. Open **Task Manager** (Ctrl + Shift + Esc)
2. Go to **Processes** tab
3. Click **Memory** column to sort by usage

**Common memory hogs:**
- 🔴 Chrome/Edge with 20+ tabs (each tab = 50-100 MB)
- 🔴 Outlook with large mailboxes (500 MB+)
- 🔴 Teams if in multiple meetings/chats (200-300 MB)
- 🔴 Creative apps (Photoshop, video editors) (1 GB+)
- 🔴 Multiple Office documents open

**Quick action:**
1. Close browser tabs you're not using
2. Exit applications you're not actively using
3. Right-click tray icons and select "Exit" (not just closing windows)

**Pro tip:** 
- Keep only essential apps open
- Use OneNote or browser bookmarks instead of keeping everything open

---

### Fix 3: Disable Startup Programs

**Why this helps:**
Programs that start automatically slow down boot time and consume resources.

**Windows 10/11:**
1. Open **Task Manager** (Ctrl + Shift + Esc)
2. Click **Startup** tab
3. Look at **Startup impact** column
4. **Right-click** programs with "High" impact
5. Select **Disable**

**Safe to disable:**
- ✅ Spotify, iTunes
- ✅ Adobe Creative Cloud
- ✅ Microsoft OneDrive (if not critical)
- ✅ Zoom, Skype
- ✅ Gaming software (Steam, Discord)
- ✅ Printer utilities

**DO NOT disable:**
- ❌ Antivirus software (Symantec, McAfee, Windows Defender)
- ❌ VPN client (Cisco AnyConnect)
- ❌ Windows Security
- ❌ Graphics drivers

**After disabling:**
- Restart laptop
- Programs won't start automatically anymore
- You can still open them manually when needed

---

### Fix 4: Check for Windows Updates

**Outdated Windows = Security risks + Performance issues**

**Windows:**
1. Click **Start** → **Settings** (gear icon)
2. Select **Update & Security**
3. Click **Check for updates**
4. If updates available, click **Download and install**
5. Restart when prompted

**Important notes:**
- Updates can take 15-30 minutes
- Don't interrupt updates
- Plug in power adapter during updates
- Some updates require multiple restarts

**macOS:**
1. Click **Apple menu** → **System Preferences**
2. Select **Software Update**
3. Click **Update Now** if available
4. Enter admin password

---

### Fix 5: Free Up Disk Space

**Full disk = Slow computer!** Windows needs at least 20 GB free.

**Quick check:**
1. Open **File Explorer** (Windows + E)
2. Click **This PC**
3. Look at **Local Disk (C:)** bar
4. 🔴 Red bar = critically low space
5. 🟡 Yellow bar = low space warning

**Quick cleanup:**
1. Right-click **C: drive** → **Properties**
2. Click **Disk Cleanup**
3. Check these boxes:
   - ✅ Temporary files
   - ✅ Recycle Bin
   - ✅ Downloads folder (review first!)
   - ✅ Thumbnails
4. Click **Clean up system files**
5. Also check:
   - ✅ Windows Update Cleanup
   - ✅ Previous Windows installations
6. Click **OK** → **Delete Files**

**Expected results:**
- Should free 5-50 GB depending on usage
- Takes 5-15 minutes

---

## Intermediate Solutions (15-30 minutes)

### Fix 6: Run Antivirus/Malware Scan

**Malware can significantly slow down your computer.**

**Windows Defender (Built-in):**
1. Click **Start** → **Settings** → **Update & Security**
2. Select **Windows Security**
3. Click **Virus & threat protection**
4. Click **Quick scan** (10-15 min) or **Full scan** (30-60 min)
5. If threats found, click **Remove** or **Quarantine**

**Corporate Antivirus (Symantec, McAfee):**
1. Open antivirus from system tray
2. Run **Full System Scan**
3. Wait for completion
4. Follow remediation prompts

**Malwarebytes (If available):**
1. Open Malwarebytes
2. Click **Scan**
3. Review and remove threats

**Signs of malware:**
- 🚨 Unexpected pop-ups
- 🚨 Browser redirects
- 🚨 New toolbars in browser
- 🚨 Unknown programs running
- 🚨 Homepage changed without permission

---

### Fix 7: Optimize Hard Drive (Windows)

**Defragment HDD or Optimize SSD**

**Check drive type first:**
1. Open **Task Manager** → **Performance** tab
2. Select **Disk**
3. Look for **"SSD"** or **"HDD"** label

**For HDD (Traditional Hard Drives):**
1. Open **File Explorer** → **This PC**
2. Right-click **C: drive** → **Properties**
3. Go to **Tools** tab
4. Click **Optimize** under "Optimize and defragment drive"
5. Select **C: drive**
6. Click **Analyze** first
7. If over 10% fragmented, click **Optimize**
8. Takes 30-60 minutes

**For SSD (Solid State Drives):**
- Don't defragment SSDs!
- Instead, use **TRIM** (Windows does this automatically)
- Just click **Optimize** once - it's quick (1-2 minutes)

---

### Fix 8: Adjust Visual Effects for Performance

**Windows animations and effects consume resources.**

**Windows 10/11:**
1. Right-click **This PC** → **Properties**
2. Click **Advanced system settings** (left sidebar)
3. Under **Performance**, click **Settings**
4. Select **Adjust for best performance** (disables all effects)
   - OR select **Custom** and uncheck:
     - ❌ Animate windows when minimizing/maximizing
     - ❌ Animations in the taskbar
     - ❌ Fade or slide menus into view
     - ❌ Show shadows under windows
5. Keep these for usability:
   - ✅ Show thumbnails instead of icons
   - ✅ Smooth edges of screen fonts
6. Click **Apply** → **OK**

**Impact:** Small but noticeable improvement, especially on older laptops.

---

### Fix 9: Disable Background Apps

**Many apps run in background even when not in use.**

**Windows 10/11:**
1. Click **Start** → **Settings** → **Privacy**
2. Scroll down to **Background apps**
3. Toggle off apps you don't need running constantly:
   - Weather
   - News
   - Maps
   - Mail (if you use Outlook desktop app)
4. Keep enabled:
   - OneDrive (if used)
   - Antivirus
   - VPN

**Alternative method:**
1. **Settings** → **Apps** → **Startup**
2. Disable unnecessary apps

---

### Fix 10: Check for Driver Updates

**Outdated drivers, especially graphics, can cause slowness.**

**Windows Update method:**
1. **Settings** → **Update & Security** → **Windows Update**
2. Click **View optional updates**
3. Expand **Driver updates**
4. Install any available driver updates

**Device Manager method:**
1. Right-click **Start** → **Device Manager**
2. Expand **Display adapters**
3. Right-click your graphics card → **Update driver**
4. Select **Search automatically for drivers**
5. Restart if prompted

**Important drivers to update:**
- Graphics (NVIDIA, AMD, Intel)
- Network adapters
- Chipset

---

### Fix 11: Manage Browser Extensions

**Too many browser extensions slow down Chrome/Edge.**

**Google Chrome:**
1. Click **three dots** (⋮) → **More tools** → **Extensions**
2. Review all extensions
3. **Remove** unused ones
4. **Disable** ones you rarely use

**Common problematic extensions:**
- Ad blockers (multiple installed)
- VPNs and proxies
- Old toolbar extensions
- Coupon finders
- Weather/news extensions

**Recommendation:**
- Keep maximum 5-7 essential extensions
- Remove anything you haven't used in 3 months

---

## Advanced Troubleshooting (30+ minutes)

### Fix 12: Check RAM Usage and Upgrade Recommendations

**Insufficient RAM is a major cause of slowness.**

**Check current RAM:**
1. Open **Task Manager** → **Performance** → **Memory**
2. Look at **Total physical memory**

**RAM Requirements by usage:**
- 📊 **4 GB** = Basic web browsing only (outdated)
- 📊 **8 GB** = Standard office work, email, light multitasking
- 📊 **16 GB** = Recommended for most users, moderate multitasking
- 📊 **32 GB** = Power users, developers, designers, video editing

**Signs you need more RAM:**
- Memory usage consistently above 80%
- System uses lots of **Pagefile** (virtual memory)
- Lag when switching between applications
- Browser tabs freeze or crash

**Recommendation to users:**
- If RAM usage consistently > 80%, request upgrade ticket
- IT can install additional RAM in 15-30 minutes
- Typical upgrade: 8 GB → 16 GB

---

### Fix 13: Check Disk Health

**Failing hard drives cause severe slowness.**

**Windows - Check Disk Utility:**
1. Open **Command Prompt** as Administrator
2. Run: `chkdsk C: /f /r`
3. Type **Y** when asked to schedule on restart
4. Restart computer
5. Scan runs before Windows loads (30-60 min)

**Windows - S.M.A.R.T. Status:**
1. Open **Command Prompt** as Administrator
2. Run: `wmic diskdrive get status`
3. Should show: **"OK"**
4. If shows **"Pred Fail"** or **"Error"** = Drive failure imminent

**macOS - Disk Utility:**
1. Open **Disk Utility** (Applications → Utilities)
2. Select your drive
3. Click **First Aid**
4. Click **Run**

**Signs of failing drive:**
- 🚨 Frequent freezing
- 🚨 Files disappearing or corrupting
- 🚨 Clicking or grinding noises
- 🚨 Slow file operations
- 🚨 Frequent errors

**If drive is failing:**
- ⚠️ Back up data immediately!
- ⚠️ Submit hardware replacement ticket
- ⚠️ Do not attempt to fix failing drive yourself

---

### Fix 14: Clean Boot (Advanced)

**Starts Windows with minimal drivers and programs to identify conflicts.**

**Windows:**
1. Press **Win + R**, type `msconfig`, press Enter
2. Go to **Services** tab
3. Check **Hide all Microsoft services**
4. Click **Disable all**
5. Go to **Startup** tab
6. Click **Open Task Manager**
7. Disable all startup items
8. Close Task Manager
9. Click **OK** in System Configuration
10. **Restart**

**Testing after clean boot:**
- If laptop is fast now = Software conflict exists
- Re-enable services/startups one by one to find culprit
- If still slow = Likely hardware issue

**To restore normal boot:**
1. Run `msconfig` again
2. Select **Normal startup**
3. Click **OK** → Restart

---

### Fix 15: Windows Performance Troubleshooter

**Built-in Windows tool to diagnose issues.**

**Windows:**
1. **Control Panel** → **Troubleshooting**
2. Click **View all**
3. Run **Performance** troubleshooter
4. Follow on-screen recommendations
5. Also run:
   - System Maintenance
   - Search and Indexing

**What it fixes:**
- Unnecessary visual effects
- Power plan settings
- Unused desktop icons
- System file issues

---

### Fix 16: Reset / Reinstall Windows (Last Resort)

**When all else fails, fresh Windows install often solves persistent issues.**

**Prerequisite:**
- ⚠️ Backup all important files first!
- ⚠️ IT must perform this or user must have admin rights
- ⚠️ Takes 1-2 hours

**Windows 10/11 Reset:**
1. **Settings** → **Update & Security** → **Recovery**
2. Click **Get started** under "Reset this PC"
3. Choose:
   - **Keep my files** (recommended) - Removes apps but keeps personal files
   - **Remove everything** (nuclear option) - Clean slate
4. Follow prompts
5. Reinstall required applications after reset

**When to recommend this:**
- All troubleshooting steps failed
- System has accumulated years of software clutter
- Persistent malware issues
- User agrees to data backup and downtime

---

## Hardware vs Software Issues

### Software Issues (Can be fixed by user/IT support)
- ✅ Too many startup programs
- ✅ Full hard drive
- ✅ Malware/viruses
- ✅ Outdated software
- ✅ Corrupt system files
- ✅ Too many browser tabs/extensions

### Hardware Issues (Require replacement/upgrade)
- 🔧 Insufficient RAM (< 8 GB for modern Windows)
- 🔧 Old/failing hard drive (especially 5400 RPM HDDs)
- 🔧 Overheating (dust in vents, failed fan)
- 🔧 Aging processor (5+ years old)
- 🔧 Damaged components

### How to Identify Hardware Issues

**Temperature check:**
1. Download HWMonitor or Core Temp
2. Check CPU temperature
3. 🌡️ Normal: 40-60°C idle, 70-85°C under load
4. 🌡️ Hot: 90°C+ = Overheating issue

**Overheating symptoms:**
- Laptop very hot to touch (especially bottom)
- Fan running loud constantly
- Unexpected shutdowns
- Throttling (performance drops suddenly)

**Overheating fixes:**
1. Use laptop on hard, flat surface (not bed/couch)
2. Clean air vents with compressed air
3. Use cooling pad
4. If persists, submit repair ticket (fan may need replacement)

---

## Prevention and Maintenance

### Weekly Maintenance
- ✅ Restart laptop at least once
- ✅ Close unused applications and browser tabs
- ✅ Clear Downloads folder

### Monthly Maintenance
- ✅ Run Windows Update
- ✅ Run antivirus scan
- ✅ Check available disk space (keep 20%+ free)
- ✅ Review and uninstall unused programs

### Quarterly Maintenance
- ✅ Clear temp files and disk cleanup
- ✅ Review startup programs
- ✅ Update drivers
- ✅ Physically clean laptop (keyboard, vents)

### Best Practices
1. **Restart weekly** - Prevents memory leaks
2. **Keep disk 20% free** - Allows Windows to function properly
3. **Limit browser tabs** - Each tab uses 50-100 MB RAM
4. **Uninstall unused programs** - Frees space and resources
5. **Keep antivirus updated** - Prevents malware slowdowns
6. **Don't run too many programs simultaneously** - Especially on 8 GB RAM systems

---

## Escalation Criteria

### Escalate to IT Support if:
1. ⚠️ All quick and intermediate fixes attempted with no improvement
2. ⚠️ Disk health check shows drive failure
3. ⚠️ RAM usage consistently > 90% (may need hardware upgrade)
4. ⚠️ Laptop overheating with potential hardware damage
5. ⚠️ Persistent malware that antivirus can't remove
6. ⚠️ Blue Screen of Death (BSOD) errors
7. ⚠️ Hardware replacement needed (RAM, drive, fan)
8. ⚠️ Windows reinstall required

### Information to Provide
When creating support ticket, include:
- **Symptoms:** Specific slowness (boot time? app launch? general?)
- **Duration:** How long has it been slow?
- **Steps taken:** List all troubleshooting attempted
- **Task Manager screenshot:** Showing CPU, Memory, Disk usage
- **Available disk space:** How much free space on C: drive?
- **Last restart:** When was laptop last restarted?
- **Business impact:** High/Medium/Low urgency

---

## Contact Information

### IT Support Helpdesk
- **Phone:** 1-800-IT-HELP (1-800-484-3571)
- **Email:** itsupport@company.com
- **Chat:** https://support.company.com/chat
- **Ticket Portal:** https://support.company.com

### Expected Response Times
- **High Priority** (can't work): 1-2 hours
- **Medium Priority** (impaired work): 4-8 hours
- **Low Priority** (minor issue): 24 hours

### Hardware Replacement Requests
- Email: **hardware@company.com**
- Include: Asset tag, issue description, troubleshooting attempted
- Approval required for upgrades (RAM, SSD)

---

## Quick Reference Flowchart

```
Laptop slow? → START HERE

├─ When was last restart? > 7 days?
│  └─ YES → Restart laptop [40% success rate]
│
├─ Still slow? → Check Task Manager
│  ├─ Disk at 100%? → Run Disk Cleanup + Check disk health
│  ├─ Memory > 80%? → Close programs + Check RAM amount
│  └─ CPU > 80%? → Check for malware + Disable startups
│
├─ Still slow? → Try intermediate fixes
│  ├─ Run antivirus scan
│  ├─ Disable startup programs
│  ├─ Update Windows and drivers
│  └─ Clean browser extensions
│
└─ Still slow? → Escalate to IT Support
   └─ Provide: Screenshots, steps taken, business impact
```

---

## Success Metrics

**Target Resolution Rates:**
- Tier 1 (Quick fixes): 70% of cases resolved
- Tier 2 (Intermediate): Additional 20% resolved
- Tier 3 (Advanced / Hardware): Final 10% resolved

**Average Resolution Time:**
- Quick fixes: 10 minutes
- Intermediate: 25 minutes
- Advanced: 45 minutes
- Hardware replacement: 1-3 business days

---

## Appendix: Common Slow Laptop Scenarios

### Scenario 1: "Laptop slow every morning"
**Likely cause:** Overnight updates or backups running  
**Solution:** Schedule updates for end of day, check OneDrive/backup software

### Scenario 2: "Slow when opening Outlook"
**Likely cause:** Large mailbox (10 GB+)  
**Solution:** Archive old emails, reduce mailbox size to < 5 GB

### Scenario 3: "Browser tabs keep freezing"
**Likely cause:** Insufficient RAM, too many tabs  
**Solution:** Close tabs, use bookmarks, add more RAM

### Scenario 4: "Slow after Windows Update"
**Likely cause:** Update not fully installed or driver issue  
**Solution:** Restart again, roll back problem drivers

### Scenario 5: "Slow only with specific application"
**Likely cause:** App-specific issue, not system-wide  
**Solution:** Reinstall the application, check for app updates

---

## Document Revision History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | Mar 2021 | Initial SOP creation | IT Support Team |
| 2.0 | Sep 2022 | Added Windows 11 specific steps | R. Patel |
| 2.5 | Mar 2023 | Added hardware diagnostics | IT Support Team |
| 2.7 | Aug 2024 | Updated RAM requirements | L. Chen |
| 2.8 | Dec 2025 | Added prevention section and flowchart | M. Johnson |

---

**Document Classification:** Internal Use Only  
**Next Review Date:** June 2026  
**Compliance:** IT Service Management Standards v3.0

*For urgent performance issues impacting work, call IT Support at 1-800-IT-HELP*
