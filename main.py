import os
import platform
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pickle
from selenium.webdriver.common.keys import Keys

def initialize_driver(user_data_dir, profile_dir):
    options = webdriver.ChromeOptions()
    options.add_argument(f"user-data-dir={user_data_dir}")
    options.add_argument(f"profile-directory={profile_dir}")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument("--headless")  # Add this line to run Chrome in headless mode
    options.add_argument("--disable-gpu")  # Disable GPU acceleration (optional)
    options.add_argument("--window-size=1920,1080")  # Set window size (optional)

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver

def login_to_google(driver):
    google_login_button = driver.find_element(By.ID, 'google_login')
    google_login_button.click()

def select_simulator_and_language(driver, language, simulator):
    driver.execute_script("""
        var divs = document.querySelectorAll('.col-md-12');
        divs.forEach(function(div) {
            div.style.display = 'block';
        });
    """)
    
    testbench_language_dropdown = Select(driver.find_element(By.ID, 'testbenchLanguage'))
    testbench_language_dropdown.select_by_visible_text(language)
    simulator_dropdown = Select(driver.find_element(By.ID, 'simulator'))
    simulator_dropdown.select_by_visible_text(simulator)
    

def input_code(driver, tab_id, file_path):
    link = driver.find_element(By.XPATH, f'//*[@href="#{tab_id}"]')
    link.click()
    
    code = open(file_path, 'r').read()
    
    driver.execute_script(f"""
        var codeMirror = document.querySelector('#{tab_id} .CodeMirror').CodeMirror;
        codeMirror.setValue(arguments[0]);
    """, code)
    

def run_simulation(driver):
    run_button = driver.find_element(By.ID, 'runButton')
    run_button.click()
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CLASS_NAME, 'EXIT')))

def print_results(driver):
    stdout_elements = driver.find_elements(By.CLASS_NAME, 'STDOUT')
    command_elements = driver.find_elements(By.CLASS_NAME, 'COMMAND')
    stdout_text = "\n".join([element.text for element in stdout_elements])
    command_text = "\n".join([element.text for element in command_elements])
    
    print("STDOUT:")
    print(stdout_text)
    
    print("\nCOMMAND:")
    print(command_text)

def get_chrome_dir():
    system = platform.system()
    if system == "Windows":
        chrome_dir = os.path.join(os.getenv('LOCALAPPDATA'), "Google", "Chrome", "User Data")
    elif system == "Darwin":  # macOS
        chrome_dir = os.path.expanduser("~/Library/Application Support/Google/Chrome")
    elif system == "Linux":
        chrome_dir = os.path.expanduser("~/.config/google-chrome")
    else:
        raise Exception("Unsupported operating system")
    
    return chrome_dir

def main():

    user_data_dir = get_chrome_dir()

    # Change these variables according to your system
    #--------------------------------------------------

    profile_dir = "Profile 5" # Change this to your profile directory (should be in the user_data_dir) if encountered any error

    language = "SystemVerilog/Verilog"
    simulator = "Aldec Riviera Pro 2023.04"

    testbench_path= 'SystemVerilog/Lab3.3-svCode/testbench.sv'
    design_path = 'SystemVerilog/Lab3.3-svCode/design.sv'

    #--------------------------------------------------
    
    driver = initialize_driver(user_data_dir, profile_dir)
    driver.get('https://www.edaplayground.com')
    
    login_to_google(driver)
    select_simulator_and_language(driver, language, simulator)
    
    while True:
        input_code(driver, 'testbench0', testbench_path)
        input_code(driver, 'design0', design_path)
        
        run_simulation(driver)
        print_results(driver)

        key = input("Press q to quit, any other key to re-run: ")
        if key == 'q':
            break

    driver.quit()

if __name__ == "__main__":
    main()