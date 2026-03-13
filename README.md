# Brute Force Login Tool - Quick Start

## Setup

1. **Install dependencies:**

   ```bash
   pip install selenium webdriver-manager
   ```

2. **Prepare word lists:**
   - `usernames.txt` - one username per line
   - `password.txt` - one password per line

3. **Update target URL in script:**
   Edit `bruteforce_login.py` and change:
   ```python
   driver.get("https://your-target.com/login")
   ```

## Run

```bash
python bruteforce_login.py
```

## Stop

Press **Ctrl+C** to stop the script.

## Results

If successful, credentials are saved to `success.txt`

---

**Note:** Only use on systems you're authorized to test.
