import logging
import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update,InputMediaAudio
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext,CallbackQueryHandler
from utils import update_audio_cache
# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

class imiBot():
    def __init__(self):
        self.token = "1872215428:AAFEGNxBPGfskxE2sjWAo6jQczgCqo6_Vms"


    def _start(self,update:Update,_:CallbackContext) -> None:

        user = update.effective_user
        update.message.reply_markdown_v2(
            fr'Hi {user.mention_markdown_v2()}\!',
        )

    def _help_command(self,update: Update, _: CallbackContext) -> None:
        """Send a message when the command /help is issued."""
        update.message.reply_text('Help!')

    def _boats(self,update: Update, _: CallbackContext) -> None:
        """Echo the user message."""
        update.message.reply_text("没有哦")

    def _echo(self,update: Update, _: CallbackContext) -> None:
        """Echo the user message."""
        update.message.reply_text("宁在说什么捏")

    def _meow(self,update: Update, _:CallbackContext) -> None:
        audios = update_audio_cache("../resources/audio/")
        keyboard = []
        for item in audios:
            keyboard.append([
                InlineKeyboardButton(f"{item}",callback_data=audios[item])
            ])
        reply_markup = InlineKeyboardMarkup(keyboard)

        update.message.reply_text('喵喵喵？:', reply_markup=reply_markup)



    def _button(self,update: Update, _: CallbackContext) -> None:
        query = update.callback_query
        query.message.reply_audio(audio=open('../resources/audio/' + query.data, 'rb'))
        query.answer()


    def run(self) -> None:
        updater = Updater(self.token)

        dispatcher = updater.dispatcher

        dispatcher.add_handler(CommandHandler("start",self._start))
        dispatcher.add_handler(CommandHandler("help",self._help_command))
        dispatcher.add_handler(CommandHandler("boats",self._boats))
        dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, self._echo))

        dispatcher.add_handler(CommandHandler('meow', self._meow))
        dispatcher.add_handler(CallbackQueryHandler(self._button))

        updater.start_polling()

        updater.idle()

if __name__ == '__main__':
    imi_bot = imiBot()

    imi_bot.run()