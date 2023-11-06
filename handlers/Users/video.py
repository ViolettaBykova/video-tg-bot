from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import Command
from loader import dp, bot
from states import Dowload
import yt_dlp
import os

import yt_dlp

def sanitize_filename(filename):
    """
    Функция выполняет замену символов в названии файла, которые
    могут вызвать проблемы при сохранении на диск.
    """
    forbidden_chars = r'\/:*?"<>|'
    for char in forbidden_chars:
        filename = filename.replace(char, '_')
    return filename.strip()

async def download_video(url, chat_id):
    ydl_opts = { 
        'quiet': True,
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best'
    }

    try:
        os.makedirs(f"downloads/{chat_id}/", exist_ok=True)
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            video_title = sanitize_filename(info['title'])
            video_ext = info['ext']
            video_path = f"downloads/{chat_id}/{video_title}.{video_ext}"
            ydl_opts['outtmpl'] = video_path

            # Получение размера файла перед скачиванием
            if 'file_size' in info:
                file_size_bytes = info['file_size']
                file_size_mb = file_size_bytes / (1024 * 1024)  # MB

                if file_size_mb > 50:
                    return None, f"Файл слишком большой ({file_size_mb:.2f} MB). Не будет скачиваться."
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydld:
                ydld.download([url])
            
            return video_path, video_title
    except Exception as e:
        return None, str(e)

@dp.message_handler(state=Dowload.dowload)
async def download(message: types.Message, state: FSMContext):
    chat_id = message.chat.id
    await message.answer(text="Скачиваем...")
    video_url = message.text
    video_path, video_title = await download_video(video_url, chat_id)

    if video_path:
        try:
            with open(video_path, 'rb') as video_file:
                await bot.send_video(chat_id, video_file)
        except:
            await message.answer(text="Файл слишком большой")
        os.remove(video_path)
    else:
        await message.answer(text=f"Произошла ошибка при загрузке видео: {video_title}")

    await state.finish()

@dp.message_handler(Command('video'))
async def start_download(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}! Пожалуйста, отправь ссылку на видео, и я отправлю его тебе.(ограничение 50 мбфйт)")
    await Dowload.dowload.set()
