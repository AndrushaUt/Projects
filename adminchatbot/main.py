from aiogram import Bot, executor, types
from aiogram.dispatcher import Dispatcher
from aiogram.types.bot_command import BotCommand
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from random import choice
from time import sleep

"""
Создайте телеграм-бота со следующими inline-опциями:
* Сделать кого-то в чате админом
* Забанить/разбанить человека в чате
* Достать статистику по чату: сколько людей, сколько админов
* Заставить бота самого уйти из чата
А также чтобы по приходу нового пользователя в чат он ему задавал вопрос (на ваш выбор)
"""

abusive_language = ['6ля', '6лядь', '6лять', 'b3ъeб', 'cock', 'cunt', 'e6aль',
                    'ebal', 'eblan', 'eбaл', 'eбaть', 'eбyч',
                    'eбать', 'eбёт', 'eблантий', 'fuck', 'fucker', 'fucking',
                    'xyёв', 'xyй', 'xyя', 'xуе', 'xуй', 'xую',
                    'zaeb', 'zaebal', 'zaebali', 'zaebat', 'архипиздрит',
                    'ахуел', 'ахуеть', 'бздение', 'бздеть',
                    'бздех', 'бздецы', 'бздит', 'бздицы', 'бздло', 'бзднуть',
                    'бздун', 'бздунья', 'бздюха', 'бздюшка',
                    'бздюшко', 'бля', 'блябу', 'блябуду', 'бляд', 'бляди',
                    'блядина', 'блядище', 'блядки', 'блядовать',
                    'блядство', 'блядун', 'блядуны', 'блядунья', 'блядь',
                    'блядюга', 'блять', 'вафел', 'вафлёр',
                    'взъебка', 'взьебка', 'взьебывать', 'въеб', 'въебался',
                    'въебенн', 'въебусь', 'въебывать',
                    'выблядок', 'выблядыш', 'выеб', 'выебать', 'выебен',
                    'выебнулся', 'выебон', 'выебываться',
                    'выпердеть', 'высраться', 'выссаться', 'вьебен', 'гавно',
                    'гавнюк', 'гавнючка', 'гамно', 'гандон',
                    'гнид', 'гнида', 'гниды', 'говенка', 'говенный', 'говешка',
                    'говназия', 'говнецо', 'говнище',
                    'говно', 'говноед', 'говнолинк', 'говночист', 'говнюк',
                    'говнюха', 'говнядина', 'говняк',
                    'говняный', 'говнять', 'гондон', 'доебываться', 'долбоеб',
                    'долбоёб', 'долбоящер', 'дрисня',
                    'дрист', 'дристануть', 'дристать', 'дристун', 'дристуха',
                    'дрочелло', 'дрочена', 'дрочила',
                    'дрочилка', 'дрочистый', 'дрочить', 'дрочка', 'дрочун',
                    'е6ал', 'е6ут', 'мать', 'мать', 'ёбaн',
                    'ебaть', 'ебyч', 'ебал', 'ебало', 'ебальник', 'ебан',
                    'ебанамать', 'ебанат', 'ебаная', 'ёбаная',
                    'ебанический', 'ебанный', 'ебанныйврот', 'ебаное',
                    'ебануть', 'ебануться', 'ёбаную', 'ебаный',
                    'ебанько', 'ебарь', 'ебат', 'ёбат', 'ебатория', 'ебать',
                    'ебать-копать', 'ебаться', 'ебашить',
                    'ебёна', 'ебет', 'ебёт', 'ебец', 'ебик', 'ебин', 'ебись',
                    'ебическая', 'ебки', 'ебла', 'еблан',
                    'ебливый', 'еблище', 'ебло', 'еблыст', 'ебля', 'ёбн',
                    'ебнуть', 'ебнуться', 'ебня', 'ебошить',
                    'ебская', 'ебский', 'ебтвоюмать', 'ебун', 'ебут', 'ебуч',
                    'ебуче', 'ебучее', 'ебучий', 'ебучим',
                    'ебущ', 'ебырь', 'елда', 'елдак', 'елдачить', 'жопа',
                    'жопу', 'заговнять', 'задрачивать',
                    'задристать', 'задрота', 'зае6', 'заё6', 'заеб', 'заёб',
                    'заеба', 'заебал', 'заебанец', 'заебастая',
                    'заебастый', 'заебать', 'заебаться', 'заебашить',
                    'заебистое', 'заёбистое', 'заебистые',
                    'заёбистые', 'заебистый', 'заёбистый', 'заебись',
                    'заебошить', 'заебываться', 'залуп', 'залупа',
                    'залупаться', 'залупить', 'залупиться', 'замудохаться',
                    'запиздячить', 'засерать', 'засерун',
                    'засеря', 'засирать', 'засрун', 'захуячить', 'заябестая',
                    'злоеб', 'злоебучая', 'злоебучее',
                    'злоебучий', 'ибанамат', 'ибонех', 'изговнять',
                    'изговняться', 'изъебнуться', 'ипать', 'ипаться',
                    'ипаццо', 'Какдвапальцаобоссать', 'конча', 'курва',
                    'курвятник', 'лох', 'лошарa', 'лошара',
                    'лошары', 'лошок', 'лярва', 'малафья', 'манда',
                    'мандавошек', 'мандавошка', 'мандавошки', 'мандей',
                    'мандень', 'мандеть', 'мандища', 'мандой', 'манду',
                    'мандюк', 'минет', 'минетчик', 'минетчица',
                    'млять', 'мокрощелка', 'мокрощёлка', 'мразь', 'мудak',
                    'мудaк', 'мудаг', 'мудак', 'муде', 'мудель',
                    'мудеть', 'муди', 'мудил', 'мудила', 'мудистый', 'мудня',
                    'мудоеб', 'мудозвон', 'мудоклюй', 'хер',
                    'хуй', 'набздел', 'набздеть', 'наговнять', 'надристать',
                    'надрочить', 'наебать', 'наебет',
                    'наебнуть', 'наебнуться', 'наебывать', 'напиздел',
                    'напиздели', 'напиздело', 'напиздили', 'насрать',
                    'настопиздить', 'нахер', 'нахрен', 'нахуй', 'нахуйник',
                    'ебет', 'ебёт', 'невротебучий',
                    'невъебенно', 'нехира', 'нехрен', 'Нехуй', 'нехуйственно',
                    'ниибацо', 'ниипацца', 'ниипаццо',
                    'ниипет', 'никуя', 'нихера', 'нихуя', 'обдристаться',
                    'обосранец', 'обосрать', 'обосцать',
                    'обосцаться', 'обсирать', 'объебос', 'обьебос',
                    'однохуйственно', 'опездал', 'опизде',
                    'опизденивающе', 'остоебенить', 'остопиздеть',
                    'отмудохать', 'отпиздить', 'отпиздячить', 'отпороть',
                    'отъебись', 'охуевательский', 'охуевать', 'охуевающий',
                    'охуел', 'охуенно', 'охуеньчик', 'охуеть',
                    'охуительно', 'охуительный', 'охуяньчик', 'охуячивать',
                    'охуячить', 'очкун', 'падла', 'падонки',
                    'падонок', 'паскуда', 'педерас', 'педик', 'педрик',
                    'педрила', 'педрилло', 'педрило', 'педрилы',
                    'пездень', 'пездит', 'пездишь', 'пездо', 'пездят',
                    'пердануть', 'пердеж', 'пердение', 'пердеть',
                    'пердильник', 'перднуть', 'пёрднуть', 'пердун', 'пердунец',
                    'пердунина', 'пердунья', 'пердуха',
                    'пердь', 'переёбок', 'пернуть', 'пёрнуть', 'пи3д', 'пи3де',
                    'пи3ду', 'пиzдец', 'пидар', 'пидарaс',
                    'пидарас', 'пидарасы', 'пидары', 'пидор', 'пидорасы',
                    'пидорка', 'пидорок', 'пидоры', 'пидрас',
                    'пизда', 'пиздануть', 'пиздануться', 'пиздарваньчик',
                    'пиздато', 'пиздатое', 'пиздатый', 'пизденка',
                    'пизденыш', 'пиздёныш', 'пиздеть', 'пиздец', 'пиздит',
                    'пиздить', 'пиздиться', 'пиздишь', 'пиздища',
                    'пиздище', 'пиздобол', 'пиздоболы', 'пиздобратия',
                    'пиздоватая', 'пиздоватый', 'пиздолиз',
                    'пиздонутые', 'пиздорванец', 'пиздорванка',
                    'пиздострадатель', 'пизду', 'пиздуй', 'пиздун',
                    'пиздунья', 'пизды', 'пиздюга', 'пиздюк', 'пиздюлина',
                    'пиздюля', 'пиздят', 'пиздячить', 'писбшки',
                    'писька', 'писькострадатель', 'писюн', 'писюшка', 'хуй',
                    'хую', 'подговнять', 'подонки', 'подонок',
                    'подъебнуть', 'подъебнуться', 'поебать', 'поебень',
                    'поёбываает', 'поскуда', 'посрать', 'потаскуха',
                    'потаскушка', 'похер', 'похерил', 'похерила', 'похерили',
                    'похеру', 'похрен', 'похрену', 'похуй',
                    'похуист', 'похуистка', 'похую', 'придурок', 'приебаться',
                    'припиздень', 'припизднутый',
                    'припиздюлина', 'пробзделся', 'проблядь', 'проеб',
                    'проебанка', 'проебать', 'промандеть',
                    'промудеть', 'пропизделся', 'пропиздеть', 'пропиздячить',
                    'раздолбай', 'разхуячить', 'разъеб',
                    'разъеба', 'разъебай', 'разъебать', 'распиздай',
                    'распиздеться', 'распиздяй', 'распиздяйство',
                    'распроеть', 'сволота', 'сволочь', 'сговнять', 'секель',
                    'серун', 'серька', 'сестроеб', 'сикель',
                    'сила', 'сирать', 'сирывать', 'соси', 'спиздел',
                    'спиздеть', 'спиздил', 'спиздила', 'спиздили',
                    'спиздит', 'спиздить', 'срака', 'сраку', 'сраный',
                    'сранье', 'срать', 'срун', 'ссака', 'ссышь',
                    'стерва', 'страхопиздище', 'сука', 'суки', 'суходрочка',
                    'сучара', 'сучий', 'сучка', 'сучко',
                    'сучонок', 'сучье', 'сцание', 'сцать', 'сцука', 'сцуки',
                    'сцуконах', 'сцуль', 'сцыха', 'сцышь',
                    'съебаться', 'сыкун', 'трахае6', 'трахаеб', 'трахаёб',
                    'трахатель', 'ублюдок', 'уебать', 'уёбища',
                    'уебище', 'уёбище', 'уебищное', 'уёбищное', 'уебк',
                    'уебки', 'уёбки', 'уебок', 'уёбок', 'урюк',
                    'усраться', 'ушлепок', 'х_у_я_р_а', 'хyё', 'хyй', 'хyйня',
                    'хамло', 'хер', 'херня', 'херовато',
                    'херовина', 'херовый', 'хитровыебанный', 'хитрожопый',
                    'хуeм', 'хуе', 'хуё', 'хуевато',
                    'хуёвенький', 'хуевина', 'хуево', 'хуевый', 'хуёвый',
                    'хуек', 'хуёк', 'хуел', 'хуем', 'хуенч',
                    'хуеныш', 'хуенький', 'хуеплет', 'хуеплёт',
                    'хуепромышленник', 'хуерик', 'хуерыло', 'хуесос',
                    'хуесоска', 'хуета', 'хуетень', 'хуею', 'хуи', 'хуй',
                    'хуйком', 'хуйло', 'хуйня', 'хуйрик', 'хуище',
                    'хуля', 'хую', 'хуюл', 'хуя', 'хуяк', 'хуякать',
                    'хуякнуть', 'хуяра', 'хуясе', 'хуячить', 'целка',
                    'чмо', 'чмошник', 'чмырь', 'шалава', 'шалавой',
                    'шараёбиться', 'шлюха', 'шлюхой', 'шлюшка']

storage = MemoryStorage()
bot = Bot(token='5657467049:AAG2o0O6Hv0iD7WTSwoFq7Aowyk7BAPyTks')
dp = Dispatcher(bot, storage=storage)

data = dict()


class FSMCommands(StatesGroup):
    ban_user = State()
    unban_user = State()
    new_admin = State()


async def admin_checker(chat: int, user: int) -> bool:
    for admin in (await bot.get_chat_administrators(chat_id=chat)):
        if admin["user"]["id"] == user:
            return True
    return False


@dp.message_handler(commands="start")
async def command_start(message: types.Message):
    await bot.set_my_commands(
        [BotCommand("ban", 'ban user'), BotCommand('start', 'запустить бота'),
         BotCommand('unban', 'разбанить юзера'),
         BotCommand('pidor_start', 'активировать пидор-бота'),
         BotCommand('get_stat', 'получить статистику чата'),
         BotCommand('bot_leave_chat', 'кикнуть бота'),
         BotCommand('set_new_admin', 'сделать нового админа'),
         BotCommand('clear_pinned_messages', 'очистить закрепы'),
         BotCommand('ping_all', 'пингануть всех')])
    await message.answer("Всем привет, я ЧатАдминБот")


@dp.message_handler(content_types=types.ContentType.NEW_CHAT_MEMBERS)
async def some_handler(message: types.Message):
    for user in message.new_chat_members:
        data[user["username"]] = user['id']
    await message.answer("Привет я бот, представьтесь теперь вы пожалуйста")


@dp.message_handler(commands="ban")
async def get_user_id_for_unban(message: types.Message):
    if await admin_checker(message.chat.id, message.from_user.id):
        await FSMCommands.ban_user.set()
        await message.answer("Напишите его имя пользователя")


@dp.message_handler(state=FSMCommands.ban_user)
async def ban_user(message: types.Message, state: FSMContext):
    if message.text.lower() == 'отмена':
        await message.answer("Процесс бана отменен")
        await state.finish()
        return
    if message.text[1:len(message.text)] not in data.keys():
        await message.answer("В чате нет такого пользователя")
    else:
        await bot.ban_chat_member(chat_id=message.chat.id,
                                  user_id=int(
                                      data[message.text[1:len(message.text)]]))
        await message.answer("Пользователь забанен")
    await state.finish()


@dp.message_handler(commands="unban")
async def get_user_id_for_ban(message: types.Message):
    if await admin_checker(message.chat.id, message.from_user.id):
        await FSMCommands.unban_user.set()
        await message.answer("Напишите его имя пользователя")


@dp.message_handler(state=FSMCommands.unban_user)
async def unban_user(message: types.Message, state: FSMContext):
    if message.text.lower() == 'отмена':
        await message.answer("Процесс разбана отменен")
        await state.finish()
        return
    if message.text[1:len(message.text)] not in data.keys():
        await message.answer("В чате нет такого пользователя")
    else:
        await bot.unban_chat_member(chat_id=message.chat.id,
                                    user_id=data[
                                        message.text[1:len(message.text)]])
        await message.answer("Пользователь разбанен")
    await state.finish()


@dp.message_handler(commands="bot_leave_chat")
async def leave_chat(message: types.Message):
    if await admin_checker(message.chat.id, message.from_user.id):
        await message.answer("Всем пока, до новых встреч!")
        await bot.leave_chat(chat_id=message.chat.id)


@dp.message_handler(commands="get_stat")
async def get_stat(message: types.Message):
    if await admin_checker(message.chat.id, message.from_user.id):
        print((await bot.get_chat_administrators(message.chat.id)))
        await message.answer(
            f"Статистика\nКоличество участников: {await bot.get_chat_member_count(chat_id=message.chat.id)}\nКоличество админов:{len(await bot.get_chat_administrators(chat_id=message.chat.id))}")


@dp.message_handler(commands="set_new_admin")
async def get_user_id_for_new_admin(message: types.Message):
    if await admin_checker(message.chat.id, message.from_user.id):
        await FSMCommands.new_admin.set()
        await message.answer("Напишите его имя пользователя")


@dp.message_handler(state=FSMCommands.new_admin)
async def set_admin(message: types.Message, state: FSMContext):
    if message.text.lower() == 'отмена':
        await message.answer("Процесс добавления нового админа отменен")
        await state.finish()
        return
    if message.text[1:len(message.text)] not in data.keys():
        await message.answer("В чате нет такого пользователя")
    else:
        await bot.promote_chat_member(chat_id=message.chat.id,
                                      user_id=data[
                                          message.text[1:len(message.text)]],
                                      can_manage_chat=True,
                                      can_change_info=True,
                                      can_delete_messages=True,
                                      can_manage_video_chats=True,
                                      can_promote_members=True,
                                      can_pin_messages=True,
                                      can_edit_messages=True,
                                      can_post_messages=True,
                                      can_restrict_members=True,
                                      can_invite_users=True)
        await message.answer("Новый админ добавлен")
        await state.finish()


@dp.message_handler(commands='clear_pinned_messages')
async def unpin(message: types.Message):
    if await admin_checker(message.chat.id, message.from_user.id):
        await bot.unpin_all_chat_messages(message.chat.id)
        await message.answer("Все закрепы очищены")


@dp.message_handler(commands='start_pidor')
async def pidor(message: types.Message):
    await message.answer("Узнаем кто пидор сегодня")
    sleep(2.5)
    await message.answer("Все гей-списки проверены")
    sleep(2.5)
    await message.answer("Вся вышка опрошена")
    sleep(2.5)
    await message.answer("Мнения соседей учтены")
    sleep(2.5)
    await message.answer("Владимир Владимирович подтвердил")
    sleep(2.5)
    await message.answer(f"Пидор обнаружен @{choice(list(data.keys()))}")


@dp.message_handler(commands="ping_all")
async def ping_all(message: types.Message):
    if await admin_checker(message.chat.id, message.from_user.id):
        index = 0
        usernames: str = ""
        for user_name in data.keys():
            if index % 5 == 4:
                await message.answer(usernames)
                usernames = ""
            usernames += ('@' + user_name + ' ')
            index += 1
        if len(usernames) != 0:
            await message.answer(usernames)


@dp.message_handler()
async def collect_all_messages(message: types.Message):
    for word in message.text.split():
        if word in abusive_language:
            await bot.delete_message(message.chat.id, message.message_id)
            return


executor.start_polling(dp, skip_updates=True)
