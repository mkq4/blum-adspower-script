from loguru import logger
from utils import read_accounts, rewrite_accounts
from bot import TelegramBotAutomation
from random import shuffle
def app():
    accounts = read_accounts()
    shuffle(accounts)
    all_accounts = []
    
    #стартуем наху
    for account in accounts:
        bot = TelegramBotAutomation(account)
        try:
            
            logger.info(f"Starting account | {account}")
            bot.telegram_open()
            bot.go_to_links()
            bot.blum_process(account_number=account, accounts=all_accounts)
            logger.info(f"Account end | {account}")
            
        except Exception as e:
            logger.error(f'Error | {e}')
    
    bot.browser_manager.close_browser()
    logger.info(f"---------- All {len(all_accounts)} accounts end ----------")
    for account in all_accounts:
        print(account)
    print(f"\n\nSoft creator - @mkqch (telegram) 🐒🦍")
app()