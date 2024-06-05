from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import pandas as pd

def get_last_button_label(browser):
    try:
        # Find all buttons of the specified type
        buttons = WebDriverWait(browser, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//button[@class='text-sm leading-5 w-10 h-10 rounded-full mx-1 pointer ease-in transition:all duration-300 bg-transparent md:hover:bg-primary-500 md:hover:text-white']"))
        )

        # Get the label of the last button
        last_button_label = buttons[-1].text.strip()

        return last_button_label
    except Exception as e:
        print(f"Error getting last button label: {str(e)}")
        return None

def count_buttons(browser):
    try:
        # Wait for at least one button of the specified type to be present
        buttons = WebDriverWait(browser, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//button[@class='text-sm leading-5 w-10 h-10 rounded-full mx-1 pointer ease-in transition:all duration-300 bg-transparent md:hover:bg-primary-500 md:hover:text-white']"))
        )

        # Print the count of matching buttons
        print(f"Number of buttons of the specified type: {len(buttons)}")

    except Exception as e:
        print(f"Error counting buttons: {str(e)}")

# Call this function after opening the page


'''def navigate_to_next_page(browser,page_number):
        try:
            
        # Wait for the second page button to be present
            button_xpath = f"//button[contains(@class, 'text-sm leading-5 w-10 h-10 rounded-full mx-1 pointer ease-in transition:all duration-300 bg-transparent md:hover:bg-primary-500 md:hover:text-white') and text()='{page_number}']"
            button = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, button_xpath)))
            browser.execute_script("arguments[0].scrollIntoView();", button)

        # Click the second page button
            button.click()
        except Exception as e:
                   print(f"Error navigating to the second page: {str(e)}")'''
def navigate_to_next_page(browser, page_number):
        # Wait for the page button to be present
        button_xpath = f"//button[contains(@class, 'text-sm leading-5 w-10 h-10 rounded-full mx-1 pointer ease-in transition:all duration-300 bg-transparent md:hover:bg-primary-500 md:hover:text-white') and text()='{page_number}']"
        button = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, button_xpath)))
        browser.execute_script("arguments[0].scrollIntoView();", button)
        #current_html = browser.page_source
        button.click()

        # Wait for the page to load (you may adjust the time as needed)
        #WebDriverWait(browser, 10).until(EC.staleness_of(button))
        #updated_html = browser.page_source
        #if current_html != updated_html:
            #print("HTML updated after clicking the button.")

def Get_instruments(input_text, periode_selection):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')  # Disable GPU acceleration to avoid potential issues
    options.add_argument('--window-size=1920,1080')  # Set a reasonable window size
    options.add_argument('--blink-settings=imagesEnabled=false')
     # Disable images loading
    browser = webdriver.Chrome(options=options)

    browser.get('https://www.casablanca-bourse.com/en/instruments')

    # Find the button element
    button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='autocomplete']"))
    )
    button.click()

    # Find the input field element
    input_field = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.XPATH, "//input[@aria-label='Ns:Tout les emetteurs']"))
    )

    # Clear any existing text in the input field
    input_field.clear()

    # Type the desired text into the input field
    input_field.send_keys(input_text)
    input_field.send_keys(Keys.ENTER)

    # Select the dropdown value
    select_dropdown = Select(WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.ID, 'range-date'))
    ))
    select_dropdown.select_by_value(periode_selection)

    # Click the 'Appliquer' button without waiting
    appliquer_button = browser.find_element(By.XPATH, "//button[text()='Apply']")
    appliquer_button.click()
    # Retrieve and return table data using BeautifulSoup
    stg_table=pd.DataFrame()
    data=pd.DataFrame()
    page_number=1
    n=int(get_last_button_label(browser))
    stg_table = retrieve_table_data_with_bs(browser, "//table[contains(@class, 'w-full')]")
    data = pd.concat([data, stg_table], ignore_index=True)
    for i in range(2,n+1):
        navigate_to_next_page(browser, i)
        stg_table = retrieve_table_data_with_bs(browser, "//table[contains(@class, 'w-full')]")
        data = pd.concat([data, stg_table], ignore_index=True)
        
        '''if i==5:
            navigate_to_next_page(browser, i)
            stg_table = retrieve_table_data_with_bs(browser, "//table[contains(@class, 'w-full')]")
            data = pd.concat([data, stg_table], ignore_index=True)
            break'''
    #navigate_to_next_page(browser, n)
    stg_table = retrieve_table_data_with_bs(browser, "//table[contains(@class, 'w-full')]")
    data = pd.concat([data, stg_table], ignore_index=True)
    return data

# Function to retrieve table data using BeautifulSoup
def retrieve_table_data_with_bs(browser, table_xpath):
    # Wait for a specific element in the table to be present (adjust the XPATH as needed)
    WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.XPATH, f"{table_xpath}//tbody/tr"))
    )

    # Get the page source
    page_source = browser.page_source

    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the table element
    table = soup.find('table', class_='w-full')

    # Check if the table is found
    if table:
        # Extract data from the table
        rows = table.find_all('tr')
        data = []

        for row in rows:
            # Extract data from each row
            cols = row.find_all(['td', 'th'])
            cols = [col.text.strip() for col in cols]
            data.append(cols)

        # Create a DataFrame from the extracted data
        df = pd.DataFrame(data[1:], columns=data[0])
        df=set_type(df)
        return df
    else:
        return None



def set_type(data):
    column = ['Number of securities traded','Trades volume','Capitalization']
    for i in column:
        data[i] = data[i].str.replace(' ', '')
    numeric_columns = ['Opening', 'Closing', 'Higher', 'Lower', 'Number of securities traded', 'Trades volume', 'Number of transactions', 'Capitalization']
    data[numeric_columns] = data[numeric_columns].apply(lambda x: pd.to_numeric(x.str.replace(',', '.'), errors='coerce'))