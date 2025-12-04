# IT Support FAQ - Password Reset Procedures

## Document Information
- **Document Version:** 2.1
- **Last Updated:** December 2025
- **Department:** IT Support Services
- **Classification:** Internal Use Only

---

## Table of Contents
1. [Overview](#overview)
2. [Password Requirements](#password-requirements)
3. [Self-Service Password Reset](#self-service-password-reset)
4. [Password Reset Methods](#password-reset-methods)
5. [Common Issues and Solutions](#common-issues-and-solutions)
6. [Account Lockout Procedures](#account-lockout-procedures)
7. [Security Best Practices](#security-best-practices)
8. [Contact Information](#contact-information)

---

## Overview

This document provides comprehensive instructions for resetting passwords for various company systems. Users should always attempt self-service options before contacting IT support.

### Supported Systems
- Windows Domain Accounts (Active Directory)
- Microsoft 365 / Office 365
- Company Email (Outlook)
- VPN Access
- Azure Portal
- Internal Applications (SharePoint, Teams, OneDrive)

---

## Password Requirements

All company passwords must meet the following criteria:

### Minimum Requirements
- **Length:** At least 12 characters
- **Complexity:** Must include three of the following:
  - Uppercase letters (A-Z)
  - Lowercase letters (a-z)
  - Numbers (0-9)
  - Special characters (!@#$%^&*)
- **History:** Cannot reuse last 10 passwords
- **Expiration:** Passwords expire every 90 days
- **Account Lockout:** Account locks after 5 failed attempts

### Password Strength Examples
✅ **Good passwords:**
- `Summ3r2025!Vacation`
- `Coffee&Morning$2025`
- `MyDog#Charlie123`

❌ **Bad passwords:**
- `Password123` (too common)
- `Summer2025` (no special characters)
- `12345678` (too simple)

---

## Self-Service Password Reset

### Prerequisites
Before using self-service password reset, you must:
1. Register security information (phone number and alternate email)
2. Set up multi-factor authentication (MFA)
3. Have access to your registered phone or email

### Step-by-Step: Register for Self-Service Password Reset

#### First-Time Setup
1. Go to **https://aka.ms/mfasetup**
2. Sign in with your current company credentials
3. Click **"Set it up now"** when prompted
4. Choose your verification method:
   - **Mobile app notification** (recommended)
   - **SMS text message**
   - **Phone call**
   - **Alternate email**
5. Follow the on-screen instructions to verify
6. Register at least TWO verification methods for backup

#### Important Notes
- Setup takes 5-10 minutes
- You'll need your mobile phone nearby
- Registration is required within 72 hours of account creation

---

## Password Reset Methods

### Method 1: Self-Service Password Reset Portal (PREFERRED)

**When to use:** You know your current password is expired or forgotten, and you have access to the internet.

#### Steps:
1. Go to **https://passwordreset.microsoftonline.com**
2. Enter your company email address (e.g., `firstname.lastname@company.com`)
3. Complete the CAPTCHA verification
4. Click **"Next"**
5. Choose your verification method:
   - Text code to registered mobile phone
   - Email code to alternate email address
   - Answer security questions
6. Enter the verification code you receive
7. Create a new password following the password requirements
8. Confirm your new password
9. Click **"Finish"**

**Expected Time:** 3-5 minutes

#### Success Message
You should see: *"Your password has been reset. You can now sign in with your new password."*

---

### Method 2: Windows Login Screen Reset

**When to use:** You're at your company laptop and have forgotten your password.

#### Steps:
1. At the Windows login screen, click **"I forgot my password"**
2. Or press **CTRL + ALT + DELETE** and select **"Change a password"**
3. Enter your username if prompted
4. Click **"Next"**
5. Choose verification method (text or email)
6. Enter the code you receive
7. Create your new password
8. Press **Enter** to log in with the new password

**Expected Time:** 3-5 minutes

---

### Method 3: While Signed Into Windows

**When to use:** You're already logged in but your password is about to expire or you want to change it.

#### Steps:
1. Press **CTRL + ALT + DELETE**
2. Select **"Change a password"**
3. Enter your old password
4. Enter your new password twice
5. Press **Enter**
6. You'll see a confirmation message: *"Your password has been changed"*

**Expected Time:** 1-2 minutes

---

### Method 4: Through Microsoft 365 Portal

**When to use:** You're already logged into Office 365 applications.

#### Steps:
1. Go to **https://portal.office.com**
2. Click your profile picture (top right corner)
3. Select **"My Account"**
4. Click **"Password"** in the left navigation
5. Click **"Change password"**
6. Enter your current password
7. Enter your new password twice
8. Click **"Submit"**

**Expected Time:** 2-3 minutes

---

### Method 5: Contact IT Support (Last Resort)

**When to use:** None of the self-service methods work, or your account is locked.

#### Steps:
1. Call IT Helpdesk: **1-800-IT-HELP (1-800-484-3571)**
   - Available: Monday-Friday, 7 AM - 7 PM EST
   - Saturday: 9 AM - 5 PM EST
   - Emergency support: 24/7
2. Or submit a ticket at: **https://support.company.com**
3. Or email: **itsupport@company.com**

#### Information to Provide:
- Full name
- Employee ID
- Department
- Work location
- Brief description of the issue
- Phone number where you can be reached

**Expected Response Time:** 
- High Priority: 1 hour
- Normal: 4 hours
- Low Priority: 24 hours

---

## Common Issues and Solutions

### Issue 1: "Your account has been locked"

**Cause:** Too many failed login attempts (5 or more).

**Solution:**
1. Wait 30 minutes for automatic unlock
2. OR call IT support for immediate unlock
3. Once unlocked, use self-service password reset

**Prevention:** Use password manager to avoid typos.

---

### Issue 2: "We didn't recognize that password"

**Possible Reasons:**
- Password recently changed and still syncing
- CAPS LOCK is on
- Using old password
- Typing error

**Solution:**
1. Check if CAPS LOCK is on
2. Verify you're using the most recent password
3. Wait 15 minutes if you just changed the password (sync time)
4. Try self-service password reset

---

### Issue 3: "Your password has expired"

**Cause:** Company policy requires password changes every 90 days.

**Solution:**
1. Click **"Update password"** or **"Change password"** link
2. Follow the on-screen prompts
3. Enter old password, then new password twice
4. Log in with new password

**Note:** You receive warning emails 14 days, 7 days, and 1 day before expiration.

---

### Issue 4: "Password doesn't meet requirements"

**Common Mistakes:**
- Not long enough (needs 12+ characters)
- Missing special characters or numbers
- Using common words or patterns
- Reusing recent passwords

**Solution:**
1. Review password requirements above
2. Use a passphrase: `ILove2Drink!Coffee`
3. Include numbers and special characters
4. Avoid dictionary words

---

### Issue 5: "We can't verify your identity"

**Cause:** Security info is not registered or outdated.

**Solution:**
1. Contact IT support immediately
2. Provide government-issued ID for verification
3. Update security information once reset
4. Register backup verification methods

---

### Issue 6: "New password can't be same as old password"

**Cause:** Attempting to reuse a password from your last 10 passwords.

**Solution:**
1. Create a completely new password
2. Don't modify your old password slightly (e.g., Password1 → Password2)
3. Use a password manager to generate unique passwords

---

### Issue 7: Password reset link expired

**Cause:** Password reset links expire after 60 minutes for security.

**Solution:**
1. Return to **https://passwordreset.microsoftonline.com**
2. Request a new password reset link
3. Complete the reset within 60 minutes

---

### Issue 8: Not receiving verification code

**Check These:**
1. **Phone issues:**
   - Verify the registered number is correct
   - Check for signal/reception
   - Wait up to 5 minutes for SMS delivery
   - Try "Call me" option instead
2. **Email issues:**
   - Check spam/junk folder
   - Verify alternate email is accessible
   - Check if email box is full
3. **General:**
   - Click "I didn't receive a code" to resend
   - Try a different verification method

---

## Account Lockout Procedures

### What Causes Account Lockout?
- 5 or more failed login attempts
- Using old/incorrect password repeatedly
- Multiple devices with cached old password
- Automated services using expired credentials

### How to Check If Your Account Is Locked
1. You'll see error: *"Your account has been locked for security reasons"*
2. Or error: *"Your account is temporarily locked to prevent unauthorized use"*

### Automatic Unlock
- Accounts automatically unlock after **30 minutes**
- No action required
- Just wait and try again

### Manual Unlock (Faster)
1. Call IT Support: **1-800-IT-HELP**
2. Verify your identity (Employee ID + last 4 of SSN)
3. IT will unlock your account immediately
4. Reset your password using self-service portal

### Preventing Lockouts
1. Use a password manager
2. Update password on all devices when changed
3. Disable auto-login on personal devices
4. Sign out of applications before password changes

---

## Security Best Practices

### DO's ✅
- ✅ Use unique passwords for each account
- ✅ Use a password manager (recommended: LastPass, 1Password, Bitwarden)
- ✅ Enable multi-factor authentication (MFA)
- ✅ Change password immediately if compromised
- ✅ Use passphrases: easier to remember, harder to crack
- ✅ Update security information regularly
- ✅ Log out of shared computers

### DON'Ts ❌
- ❌ Share your password with anyone (including IT staff)
- ❌ Write passwords on sticky notes
- ❌ Use the same password for work and personal accounts
- ❌ Save passwords in unsecured files (Excel, Word docs)
- ❌ Use personal information (birthdays, names)
- ❌ Store passwords in browser on shared computers
- ❌ Send passwords via email or chat

### Recommended Password Managers
Company-approved password managers:
1. **LastPass Business** (company-provided license)
2. **1Password Teams**
3. **Microsoft Authenticator** (built-in password manager)

### Multi-Factor Authentication (MFA)
MFA adds an extra layer of security:
- **What it is:** Requires phone verification after password
- **Why it matters:** Prevents 99.9% of account compromises
- **Required for:** All employees, contractors, and executives

---

## Password Change Schedule

### Regular Password Changes
- **Frequency:** Every 90 days
- **Warning notifications:** 14, 7, and 1 day before expiration
- **Grace period:** None - account locks on expiration

### Immediate Change Required
You MUST change your password immediately if:
- You suspect your password is compromised
- You received a phishing email and clicked links
- You shared your password (even accidentally)
- IT Security notifies you of suspicious activity
- You used your work password on a personal site that was breached

---

## Special Scenarios

### Remote Workers / VPN Users
If you're working remotely and your password expires:
1. Connect to company VPN first (use current password)
2. Once connected, change password through Windows (CTRL+ALT+DEL)
3. Disconnect and reconnect VPN with new password

**Important:** If VPN password is expired and you can't connect:
- Call IT Support immediately
- You may need to come to the office or use Remote Desktop

### Contractors and Temporary Employees
- Passwords expire every 60 days (not 90)
- Must register MFA within 24 hours of account creation
- Cannot use self-service reset - must contact IT sponsor

### Service Accounts
Service accounts (for applications, not people):
- Managed by IT Security team only
- 180-day expiration
- Require change management ticket
- Contact: **serviceaccounts@company.com**

### Executive Password Support
Executives have dedicated IT support:
- Email: **executivesupport@company.com**
- Phone: **1-800-VIP-HELP**
- Response time: 15 minutes

---

## Troubleshooting Decision Tree

```
Can't log in?
├─ Do you know your password?
│  ├─ YES → Is your account locked?
│  │  ├─ YES → Wait 30 min OR call IT Support
│  │  └─ NO → Check CAPS LOCK, try again
│  │
│  └─ NO → Is your password expired?
│     ├─ YES → Use self-service password reset
│     └─ NO → Use Method 1 (Self-Service Portal)
│
└─ Did you forget your username?
   └─ Contact IT Support with Employee ID
```

---

## Contact Information

### IT Support Helpdesk
- **Phone (US):** 1-800-IT-HELP (1-800-484-3571)
- **Phone (International):** +1-555-484-3571
- **Email:** itsupport@company.com
- **Chat:** https://support.company.com/chat
- **Portal:** https://support.company.com

### Hours of Operation
- **Monday-Friday:** 7:00 AM - 7:00 PM EST
- **Saturday:** 9:00 AM - 5:00 PM EST
- **Sunday:** Closed (Emergency support only)
- **24/7 Emergency Line:** 1-800-URGENT-IT

### Self-Service Resources
- **Password Reset Portal:** https://passwordreset.microsoftonline.com
- **Security Info Setup:** https://aka.ms/mfasetup
- **IT Knowledge Base:** https://kb.company.com
- **Video Tutorials:** https://training.company.com/password-help

---

## Frequently Asked Questions (FAQ)

### Q1: How long does it take for a password change to sync?
**A:** Typically 5-15 minutes. Wait 15 minutes before trying to log in to other applications.

### Q2: Can I reuse my old password?
**A:** No. The system blocks your last 10 passwords.

### Q3: Why do I need to change my password every 90 days?
**A:** This is an industry best practice and regulatory requirement to minimize security risks.

### Q4: What if I'm traveling and don't have access to my registered phone?
**A:** Use your backup verification method (alternate email or security questions). Always register multiple methods before traveling.

### Q5: Can IT support see my password?
**A:** No. IT staff cannot see your password. They can only reset it for you.

### Q6: Will changing my password log me out of my phone?
**A:** Yes, you'll need to re-enter your password on all devices (phone, tablet, laptop).

### Q7: Is my password change secure?
**A:** Yes. All password resets use encrypted connections (HTTPS) and multi-factor authentication.

### Q8: What happens if I enter the wrong password too many times?
**A:** After 5 failed attempts, your account locks for 30 minutes.

### Q9: Can I set my password to never expire?
**A:** No. For security reasons, all user accounts must change passwords every 90 days. Only service accounts have different policies.

### Q10: I changed my password but my phone keeps asking for the old one. Why?
**A:** Your device has the old password cached. Remove your work account from the device and add it back with the new password.

---

## Document Revision History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | Jan 2023 | Initial document creation | IT Security Team |
| 1.5 | Jun 2023 | Added self-service instructions | J. Smith |
| 2.0 | Jan 2024 | Updated for new MFA requirements | IT Security Team |
| 2.1 | Dec 2025 | Added troubleshooting decision tree | M. Johnson |

---

## Compliance and Security Notes

This document complies with:
- **SOC 2 Type II** security requirements
- **NIST 800-63B** password guidelines
- **GDPR** data protection standards
- **Company Security Policy v4.2**

**Document Classification:** Internal Use Only
**Distribution:** All Employees
**Next Review Date:** June 2026

---

*For additional support or to report security incidents, contact IT Security at security@company.com or call 1-800-SECURE-IT*
