# Brute Force Login Tool

A Python-based penetration testing tool for credential dictionary attack on web login forms using Selenium WebDriver.

## ⚠️ Legal Notice

This tool is for **authorized penetration testing and educational purposes only**. Unauthorized access to computer systems is illegal. Only use this on systems you own or have explicit written permission to test.

## Features

- **Headless Chrome automation** - Fast, no GUI overhead
- **Dictionary-based attacks** - Test multiple username/password combinations
- **Automated success detection** - Recognizes successful login by URL/page content
- **Progress tracking** - Shows real-time attempt count and status
- **Result logging** - Saves successful credentials to `success.txt`

## Requirements

- Python 3.8+
- Google Chrome (installed locally)
- Selenium WebDriver
- webdriver-manager (optional, for auto-downloading ChromeDriver)

## Installation

```bash
pip install selenium webdriver-manager
```

Ensure Google Chrome is installed on your system.

## File Structure

```
├── bruteforce_login.py    # Main script
├── usernames.txt          # List of usernames (one per line)
├── password.txt           # List of passwords (one per line)
├── success.txt            # Output file with found credentials
└── README.md              # This file
```

## Usage

### 1. Prepare Word Lists

Create `usernames.txt`:

```
admin
administrator
root
user1
test
```

Create `password.txt`:

```
password123
admin
1234567890
qwerty
```

### 2. Update Target URL

Edit the script and change the login URL:

```python
driver.get("https://your-target-site.com/login")
```

### 3. Run the Script

```bash
python bruteforce_login.py
```

## Output

The script displays:

- ✅ Loaded password/username counts
- 📝 Current attempt (username/password pair)
- URL after login attempt
- ❌ Failed attempts
- 🎉 SUCCESS when credentials are found

**Output file:** If successful, credentials are saved to `success.txt`

## Configuration

### Speed Options

**Faster (less reliable):**

```python
time.sleep(0.1)  # Reduce from 0.5
WebDriverWait(driver, 3)  # Reduce from 5
```

**Slower (more reliable):**

```python
time.sleep(2)  # Increase for slow servers
WebDriverWait(driver, 15)  # Wait longer for page load
```

### Disable/Enable Headless Mode

```python
# Headless (no browser window - FASTER)
options.add_argument("--headless=new")

# Non-headless (see the browser - SLOWER but useful for debugging)
# options.add_argument("--headless=new")
```

## Performance Tips

1. **Headless mode** is orders of magnitude faster
2. **Reduce sleep time** to 0.1-0.5s if the target server is fast
3. **Reduce wait timeout** to 3-5s for responsive sites
4. **Filter word lists** - remove unlikely combinations first
5. **Try common credentials first** - reorder lists by probability
6. **Use multi-threading** - test multiple logins in parallel (advanced)

## Troubleshooting

### Script hangs at "Starting Chrome browser..."

**Solution:** Check internet connection (for ChromeDriver download). If offline, ensure ChromeDriver is already installed.

```bash
# Check Chrome installation
where chrome.exe

# Try running with explicit ChromeDriver path
python -c "from selenium import webdriver; webdriver.Chrome()"
```

### "Element not found" errors

The login form fields might have different names. Inspect the webpage HTML:

```bash
# Check the actual field names in your target:
# Open browser → Right-click → Inspect → Find <input> tags
```

Update the script if needed:

```python
email_field = driver.find_element(By.NAME, "email")  # Change "email" if different
password_field = driver.find_element(By.NAME, "password")  # Change "password" if different
```

### Getting rate-limited

If the server blocks repeated requests:

- Increase `time.sleep()` value
- Add random delays between attempts
- Use proxy rotation (advanced)

### Chrome crashes or closes

Ensure Chrome has enough resources. Reduce the number of parallel operations or increase wait times.

## How It Works

1. **Initialize** - Loads usernames and passwords from text files
2. **Launch Chrome** - Opens a headless Chrome browser
3. **Loop** - For each password/username combination:
   - Navigate to login page
   - Wait for form to load
   - Fill username and password fields
   - Submit the form
   - Check if login was successful (by URL or page content)
4. **Detect Success** - If "dashboard" or "welcome" appears, credentials found
5. **Save Results** - Write credentials to `success.txt`
6. **Exit** - Close browser and terminate

## Ethical Considerations

- Only use on systems you're authorized to test
- Get written permission from the system owner
- Use lowest effective privileges
- Document all testing activities
- Report vulnerabilities responsibly
- Consider the impact on the organization

## Support

For issues, check:

1. Chrome is installed: `where chrome.exe`
2. Python packages: `pip list | grep selenium`
3. Target URL is correct in the script
4. Login form field names match the HTML

## License

For educational and authorized penetration testing use only.

---

**Created:** March 2026  
**Last Updated:** March 14, 2026
