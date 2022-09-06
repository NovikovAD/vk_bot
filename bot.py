# Импортируем библиотеку vk_api
import vk_api
# Достаём из неё longpoll
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api import VkApi
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import json

# Создаём переменную для удобства в которой хранится наш токен от группы

token="vk1.a.qezXB0DSmkusjxDVOVluGRSa7NIkEhULpiSYIJEWaq6uzpAovVWQ_TBrxsW-CtMjNji5mo9Yd4eZa2y6LlUjE_R5axbc8Mwi4THrK1Lls_a1wdVWqmrfsNtAssvhcF4tqxRAAHk1cN82Mwl3bumkglPSYXfKRinE7RM2daMEiuVsv8_hK2I7DEtyOPyyAb_X" # В ковычки вставляем аккуратно наш ранее взятый из группы токен.

# Подключаем токен и longpoll
bh = vk_api.VkApi(token = token)
give = bh.get_api()
longpoll = VkLongPoll(bh)

text_hs = "Хмм... Кажется мне нужно освежить мою память! Как хорошо, что на презентации Студенческого совета" \
          "12 сентября в 19:00 в Конгресс-центре будут представлены все составляющие Студенческого совета и ребята" \
          "лично смогут ответить на твои вопросы на ярмарке сразу после. Увидимся там!"

settings = dict(one_time=False, inline=True)

# Создадим функцию для ответа на сообщения в лс группы
def blasthack(id, text):
    bh.method('messages.send', {'user_id' : id, 'message' : text, 'random_id': 0})

keyboard1 = VkKeyboard(one_time=True)
keyboard1.add_button('Студенческие советы Высших школ/факуль', color=VkKeyboardColor.POSITIVE)
keyboard1.add_button('Общеуниверситетские проекты', color=VkKeyboardColor.POSITIVE)
keyboard1.add_line()
keyboard1.add_button('Студенческие объединения и общежития', color=VkKeyboardColor.POSITIVE)
keyboard1.add_button('Внешние связи и коммуникации', color=VkKeyboardColor.POSITIVE)

def sender(id, text):
    give.messages.send(user_id=id, message=text, random_id=0, keyboard=keyboard1.get_keyboard())



keyboard2 = VkKeyboard(**settings)
# pop-up кнопка
keyboard2.add_callback_button(label='Высшая школа экономики и бизнеса', color=VkKeyboardColor.SECONDARY, payload={"type": "my_own_100500_type_edit"})
keyboard2.add_line()
keyboard2.add_callback_button(label='Высшая школа финансов', color=VkKeyboardColor.SECONDARY, payload={"type": "my_own_100500_type_edit"})
keyboard2.add_line()
keyboard2.add_callback_button(label='Высшая инженерная школа «Новые материалы и технологии»', color=VkKeyboardColor.SECONDARY, payload={"type": "my_own_100500_type_edit"})
keyboard2.add_line()
keyboard2.add_callback_button(label='Факультет бизнеса «Капитаны»', color=VkKeyboardColor.SECONDARY, payload={"type": "my_own_100500_type_edit"})
keyboard2.add_line()
keyboard2.add_callback_button(label='Институт первая академия медиа', color=VkKeyboardColor.SECONDARY, payload={"type": "my_own_100500_type_edit"})
keyboard2.add_line()

keyboard3 = VkKeyboard(**settings)
# кнопка переключения назад, на 1ое меню.
keyboard3.add_callback_button('Назад', color=VkKeyboardColor.NEGATIVE, payload={"type": "my_own_100500_type_edit"})



# Слушаем longpoll(Сообщения)
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
      # Чтобы наш бот не слышал и не отвечал на самого себя
        if event.to_me:
            # Для того чтобы бот читал все с маленьких букв 
            message = event.text.lower()
            # Получаем id пользователя
            id = event.user_id

            if message == 'начать':
                sender(id, 'О чём ты хочешь узнать?')
            elif message == 'студенческие советы высших школ/факуль':
                    if event.object.payload['type'] == 'my_own_100500_type_edit':
                            last_id = give.messages.edit(
                                peer_id=event.obj.peer_id,
                                message='ola',
                                conversation_message_id=event.obj.conversation_message_id,
                                keyboard=(keyboard2 if f_toggle else keyboard3).get_keyboard())
                    f_toggle = not f_toggle
