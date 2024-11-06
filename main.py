import telebot
import config
from telebot import types
from affine import create_affine_note
import dotenv

#загрузим env-файл
dotenv.load_dotenv()

# создаём объект бота для взаимодействия с telegram api
bot = telebot.TeleBot(config.TELEGRAM_API_KEY)

# обработчик команды start
@bot.message_handler(commands=['start'])
def start_bot(message: types.Message):
  if str(message.from_user.id) != config.USER_ID:
    bot.send_message(message.chat.id, 'Некорректный пользователь!')
    return
  first_mess = f"Привет! Я бот для создания заметок в Affine."
  bot.send_message(message.chat.id, first_mess)


# обработчик остальных команд
@bot.message_handler()
def create_note(message: types.Message):
    if str(message.from_user.id) != config.USER_ID:
      bot.send_message(message.chat.id, 'Некорректный пользователь!')
        
    create_affine_note(message.text)
    bot.send_message(message.chat.id, 'Заметка успешно создана!')

if __name__ == '__main__':
  # включаем поллинг, чтобы получать обновления от telegram api
  bot.infinity_polling()