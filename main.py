from bot.bot_body import imiBot
import time
def main():
    imi_bot = imiBot()
    imi_bot.init()
    imi_bot.start()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
    while True:
        time.sleep(1)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
