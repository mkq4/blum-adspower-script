from loguru import logger
import random
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, WebDriverException, TimeoutException
from browser import BrowserManager
from utils import get_numbers, Account

class TelegramBotAutomation:
    def __init__(self, serial_number):
        self.serial_number = serial_number
        self.browser_manager = BrowserManager(serial_number)
        self.browser_manager.start_browser()
        self.driver = self.browser_manager.driver
        
    def telegram_open(self):
        try:
            self.driver.get("https://web.telegram.org/k/")
            logger.info(f"Telegram open | sleeping 5 sec")
            time.sleep(5)
        except Exception as e:
            logger.error(f'Error | {e}')
    
    def go_to_links(self):
        try:
            #поиск группы
            search_chat_input = self.wait_for_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/input[1]')
            search_chat_input.click()
            search_chat_input.send_keys('@makaquich_soft_links')
            
            search_result = self.wait_for_element(By.XPATH, '//*[@id="search-container"]/div[2]/div[2]/div/div[1]/div/div[2]/ul/a/div[1]')
            search_result.click()
            sleeptime = random.randint(5, 12)
            logger.info(f'Group found | sleeping {sleeptime} sec')
            time.sleep(sleeptime)
            link = self.wait_for_element(By.CSS_SELECTOR, 'a[href="https://t.me/blum/app?startapp=ref_PWIYv6ZEQE"]')
            link.click()
            time.sleep(5)
        except Exception as e:
            logger.error(f'Error | {e}')
    
    def blum_process(self, account_number: int, accounts: list):
        try:
            iframe = self.wait_for_element(By.TAG_NAME, 'iframe')
            self.driver.switch_to.frame(iframe)
            self.wait_for_element(By.XPATH, '//*[@id="app"]/div[1]')
            logger.success(f'Blum launched')
            
            check_in_button = self.wait_for_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div/button')  # чек ин кнопка
            check_in_button.click()
            logger.success(f'Check-in success')
            time.sleep(5)
            
            daily_claim_btn = self.wait_for_element(By.XPATH, '//*[@id="app"]/div[1]/div[4]/div/div[2]/div[2]/div/button', timeout=20)
            self.driver.execute_script("arguments[0].click();", daily_claim_btn)
            logger.success(f'Daily claim success')
            time.sleep(6)
            
            daily_claim_btn = self.wait_for_element(By.XPATH, '//*[@id="app"]/div[1]/div[4]/div/div[2]/div[2]/div/button', timeout=20)
            self.driver.execute_script("arguments[0].click();", daily_claim_btn) 
            logger.success(f'Start farming success')
            time.sleep(2)
            
            games_available = self.wait_for_element(By.XPATH, '//*[@id="app"]/div[1]/div[5]/div[2]/div/div[2]') #сколько игр
            games_available_text = games_available.text if games_available else 0
            games_available_text = get_numbers(games_available_text)
            
            check_in_days = self.wait_for_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div/div/div[1]')  # чек ин дни
            check_in_days_text = check_in_days.text if check_in_days else 0
            check_in_days_text = get_numbers(check_in_days_text)
            
            meme_points = self.wait_for_element(By.XPATH, '//*[@id="app"]/div[1]/div[4]/div/div[1]/div[1]/div[2]')
            meme_points_text = meme_points.text if meme_points else 0
            meme_points_text = get_numbers(meme_points_text)
            
            blum_points = self.wait_for_element(By.XPATH, '//*[@id="app"]/div[1]/div[4]/div/div[2]/div[1]/div[2]')
            blum_points_text = blum_points.text if meme_points else 0
            blum_points_text = get_numbers(blum_points_text)
            
            logger.info(f'Account success | check-in {check_in_days_text} days | {games_available_text} tikets | {meme_points_text} meme points | {blum_points_text} blum points')
            
            
            account = Account(tikets=games_available_text, blum_balance=blum_points_text, meme_balance=meme_points_text, checkin_days=check_in_days_text, account_number=account_number)
            accounts.append(account)
            time.sleep(3)
            
        except Exception as e:
            logger.error(f'Error | {e}')
        finally:
            logger.info(f'Closing browser')
            time.sleep(2)
            self.browser_manager.close_browser()
    
    def wait_for_element(self, by, value, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((by, value))
        )
    
    def check_webdriver(self):
        self.driver.get("https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html")
        time.sleep(10000)