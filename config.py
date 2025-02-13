# ---------------------------------------------#
# Configuration
# ---------------------------------------------#
# Recheck time in seconds to recheck all accounts (60 seconds = 1 minute and 0 means no recheck)
AccountsRecheckTime = 10

# Adds a random delay to the AccountsRecheckTime interval to make it more unpredictable and less detectable.
# Set it to 0 to disable the random delay.
# For example, if set to 120, the bot will introduce a random delay between 1 and 120 seconds each time it rechecks.
MaxRandomDelay = 10

# Accounts will be checked in the order they are listed
AccountList = [
    {
        "account_name": "Account 1",  # A custom name for the account (not important, just for logs)
        "Authorization": "Bearer 1725293331814ROaCY0Ip0oQ0HvvudhP6o4y5HNEYY0uaDbuv1pNmq4bedfzuc2E9VsgTIMHivpKT5658610961",  # To get the token, refer to the README.md file
        "UserAgent": "Mozilla/5.0 (Linux; Android 13; K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/127.0.6533.103 Mobile Safari/537.36",  # Refer to the README.md file to obtain a user agent
        "Proxy": {},  # You can use proxies to avoid getting banned. Use {} for no proxy
        # Example of using a proxy:
        # "Proxy": {
        #   "https": "https://10.10.1.10:3128",
        #   "http": "http://user:pass@10.10.1.10:3128/"
        # },
        "config": {
            "auto_tap": True,  # Enable auto tap by setting it to True, or set it to False to disable
            "auto_free_tap_boost": True,  # Enable auto free tap boost by setting it to True, or set it to False to disable
            "auto_get_daily_cipher": True,  # Enable auto get daily cipher by setting it to True, or set it to False to disable
            "auto_get_daily_task": True,  # Enable auto-get daily tasks by setting it to True, or set it to False to disable
            "auto_get_task": True,  # Enable auto get (Youtube/Twitter and ...) task to True, or set it to False to disable
            "auto_finish_mini_game": False,  # Enable auto finish mini game by setting it to True, or set it to False to disable
            "auto_claim_daily_combo": True,  # Enable auto claim daily combo by setting it to True, or set it to False to disable
            "auto_daily_combo_enable": False,  # Enable auto daily combo by setting it to True, or set it to False to disable
            "auto_daily_combo_max_price": 5_000_000,  # Maximum price of combo for purchase
            "auto_playground_games": True,  # Enable auto playground games by setting it to True, or set it to False to disable
            # If you have over 5 accounts, disable the auto_playground_games feature or use a proxy for each account.
            "auto_upgrade": False,  # Enable auto-upgrade by setting it to True, or set it to False to disable
            "auto_upgrade_start": 2_000_000,  # Start buying upgrades when the balance is greater than this amount
            "auto_upgrade_min": 100_000,  # Stop buying upgrades when the balance is less than this amount
            # This feature will ignore the auto_upgrade_start and auto_upgrade_min.
            # By changing it to True, the bot will find the overall best card and then wait for the best card to be available (based on cooldown or price).
            # When the best card is available, the bot will buy it and then wait for the next best card to be available.
            # This feature will stop buying upgrades when the balance is less than the price of the best card.
            "wait_for_best_card": False,  # Recommended to keep it True for high-level accounts
            "enable_parallel_upgrades": False,  # Enable parallel card upgrades. This will buy cards in parallel if the best card is on cooldown. It should speed up the profit.
            "parallel_upgrades_max_price_per_hour": 6000,  # Cards with less than X coins per 1k will be bought
            "show_num_buy_options": 0,  # Number of card buy options to show in the logs, ranked by best value, 0 disables this.
            "max_promo_games_per_round": 3,  # Maximum number of promo games to play in a single round, 0 disables this.
        },
        # If you have enabled Telegram bot logging,
        # you can add your chat ID below to receive logs in your Telegram account.
        # You can obtain your chat ID by messaging @chatIDrobot.
        # Example: "telegram_chat_id": "12345678".
        # If you do not wish to use this feature for this account, leave it empty.
        # This feature is optional and is required to enable the telegramBotLogging feature below.
        "telegram_chat_id": "",  # String - you can get it from https://t.me/chatIDrobot
    },
    # {
    #     "account_name": "Account 2",  # A custom name for the account (not important, just for logs)
    #     "Authorization": "Bearer TOKEN_HERE",  # To get the token, refer to the README.md file
    #     "UserAgent": "Your UserAgent",  # Refer to the README.md file to obtain a user agent
    #     "Proxy": {},  # You can use proxies to avoid getting banned. Use {} for no proxy
    #     # Example of using a proxy:
    #     # "Proxy": {
    #     #   "https": "https://10.10.1.10:3128",
    #     #   "http": "http://user:pass@10.10.1.10:3128/"
    #     # },
    #     "config": {
    #         "auto_tap": True,  # Enable auto tap by setting it to True, or set it to False to disable
    #         "auto_free_tap_boost": True,  # Enable auto free tap boost by setting it to True, or set it to False to disable
    #         "auto_get_daily_cipher": True,  # Enable auto get daily cipher by setting it to True, or set it to False to disable
    #         "auto_get_daily_task": True,  # Enable auto-get daily tasks by setting it to True, or set it to False to disable
    #         "auto_get_task": True,  # Enable auto get (Youtube/Twitter and ...) task to True, or set it to False to disable
    #         "auto_finish_mini_game": False,  # Enable auto finish mini game by setting it to True, or set it to False to disable
    #         "auto_daily_combo_enable": False,  # Enable auto daily combo by setting it to True, or set it to False to disable
    #         "auto_daily_combo_max_price": 5_000_000,  # Maximum price of combo for purchase
    #         "auto_playground_games": True,  # Enable auto playground games by setting it to True, or set it to False to disable
    #         # If you have over 5 accounts, disable the auto_playground_games feature or use a proxy for each account.
    #         "auto_upgrade": True,  # Enable auto-upgrade by setting it to True, or set it to False to disable
    #         "auto_upgrade_start": 2_000_000,  # Start buying upgrades when the balance is greater than this amount
    #         "auto_upgrade_min": 100_000,  # Stop buying upgrades when the balance is less than this amount
    #         # This feature will ignore the auto_upgrade_start and auto_upgrade_min.
    #         # By changing it to True, the bot will find the overall best card and then wait for the best card to be available (based on cooldown or price).
    #         # When the best card is available, the bot will buy it and then wait for the next best card to be available.
    #         # This feature will stop buying upgrades when the balance is less than the price of the best card.
    #         "wait_for_best_card": True,  # Recommended to keep it True for high-level accounts
    #         "enable_parallel_upgrades": True,  # Enable parallel card upgrades. This will buy cards in parallel if the best card is on cooldown. It should speed up the profit.
    #         "parallel_upgrades_max_price_per_hour": 6000,  # Cards with less than X coins per 1k will be bought
    #         "show_num_buy_options": 0,  # Number of card buy options to show in the logs, ranked by best value, 0 disables this.
    #         "max_promo_games_per_round": 3,  # Maximum number of promo games to play in a single round, 0 disables this.
    #     },
    #     # If you have enabled Telegram bot logging,
    #     # you can add your chat ID below to receive logs in your Telegram account.
    #     # You can obtain your chat ID by messaging @chatIDrobot.
    #     # Example: "telegram_chat_id": "12345678".
    #     # If you do not wish to use this feature for this account, leave it empty.
    #     # This feature is optional and is required to enable the telegramBotLogging feature below.
    #     "telegram_chat_id": "",  # String - you can get it from https://t.me/chatIDrobot
    # },
]

# ---------------------------------------------#
# Telegram Logging
# By enabling this feature, you will receive logs in your Telegram account.
# To use this feature, you need to create a bot and obtain the token from @BotFather.
# Note: Only important logs are sent to Telegram, feel free to include more logs as needed.
# You can also use this feature to receive logs from a bot running on a server.
# If you don't want to use this feature, set "is_active" to False and leave "bot_token" and "uid" fields empty.
# This feature is optional, and you can disable it by setting "is_active" to False.
telegramBotLogging = {
    "is_active": False,  # Set it to True if you want to use it, and make sure to fill out the below fields
    "bot_token": "",  # HTTP API access token from https://t.me/BotFather ~ Start your bot after creating it
    # Configure the what you want to receive logs from the bot
    "messages": {
        "general_info": True,  # General information
        "account_info": True,  # Account information
        "http_errors": False,  # HTTP errors
        "other_errors": False,  # Other errors
        "daily_cipher": True,  # Daily cipher
        "daily_task": False,  # Daily task
        "upgrades": True,  # Upgrades
    },
}

ConfigFileVersion = 1
