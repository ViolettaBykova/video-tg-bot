from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp, Command

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Список команд: ",
            "/start - Начать диалог",
            "/help - Получить справку",
            "/video - это команда для скачивания видео и отправка вам video сообщением",
            "/how_to_dzen - Инструкция как скачать видео с dzen")

    await message.answer("\n".join(text))

@dp.message_handler(Command('how_to_dzen'))
async def bot_help(message: types.Message):
    text = ("Инструкция как скачать видео с дзен: ",
            "1 - Вам нужно зайти в просмотр кода страницы (ctrl + u) либо правой кнопкой мыши в окне браузера и этот пунк будет почти в конце",
            "либо можете добавить в начале url -> view-source:  (https://dzen.ru/video/watch/adf-> view-source:https://dzen.ru/adf",
            "2 - Сделать поиск по странице (ctrl + f)  с фразой .m3u найти первое совпадение и скопировать эту ссылку",
            "3 - Вставить ссылку в бота",
            "4 - Ссылка будет похожа на  - https://cdn.dzen.ru/vod/converted-video/vod-content/90/99/29/21/65/68/14/90/01/9f6469c5-5725-4589-a1fa-4ce8756ae9ad/kaltura/desc_9eefbfeabc775bc271d48cc2aa653519/3157535482317786832/ysign1=7be90fd6e998c8408cd6a15fbcc4d53713aebea4ed344b19bdb6585e38ab822a,abcID=967,from=zen,pfx,sfx,ts=6555f263/master.m3u8?vsid=uk19n315c0m0k9pp6"
            )

    await message.answer("\n".join(text))