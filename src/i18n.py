TRANSLATIONS = {
    "en": {
        "epub_file_path": "EPUB File Path:",
        "browse": "Browse",
        "language_prefix": "Language prefix (e.g., en, ru, fr):",
        "refresh_voices": "Refresh Voices",
        "voice": "Voice:",
        "output_directory": "Output Directory Path:",
        "output_file_name": "Output File Name:",
        "single_mp3_file": "Single MP3 file",
        "playback_speed": "Playback Speed Percentage:",
        "volume": "Volume Percentage:",
        "pitch": "Pitch Hz:",
        "book_title": "Book title:",
        "select_all": "Select All",
        "chapter_list": "Chapter List:",
        "unselect_all": "Unselect All",
        "selected_chapter_text": "Selected Chapter Text:",
        "generate": "Generate",
        "updating_voices": "Updating voices list...",
        "voices_loaded": "Voices list updated.",
        "no_voices_error": "Failed to load voices for prefix: {prefix}. Check internet connection or prefix.",
        "deleting_chapter_list": "Deleting chapter list...",
        "filling_chapter_list": "Filling chapter list...",
        "loading": "Loading...",
        "loaded": "Loaded.",
        "selecting": "Selecting...",
        "selection_done": "Selection done.",
        "generating": "Generating {index}/{total} : {file}",
        "audio_book_created": "Audio book successfully created!",
        "language": "Language:",
        "completed": "Completed",
        "chapter_completed": "Chapter completed: {chapter}",
        "chapter_failed": "Chapter failed: {chapter}",
        "progress_reset": "Progress reset",
    },
    "ru": {
        "epub_file_path": "Путь к EPUB файлу:",
        "browse": "Обзор",
        "language_prefix": "Префикс языка (например, en, ru, fr):",
        "refresh_voices": "Обновить голоса",
        "voice": "Голос:",
        "output_directory": "Путь к выходной директории:",
        "output_file_name": "Имя выходного файла:",
        "single_mp3_file": "Один MP3 файл",
        "playback_speed": "Процент скорости воспроизведения:",
        "volume": "Процент громкости:",
        "pitch": "Высота тона (Hz):",
        "book_title": "Название книги:",
        "select_all": "Выбрать все",
        "chapter_list": "Список глав:",
        "unselect_all": "Отменить выбор",
        "selected_chapter_text": "Текст выбранной главы:",
        "generate": "Создать",
        "updating_voices": "Обновление списка голосов...",
        "voices_loaded": "Список голосов обновлен.",
        "no_voices_error": "Не удалось загрузить голоса для префикса: {prefix}. Проверьте подключение к интернету или префикс.",
        "deleting_chapter_list": "Удаление списка глав...",
        "filling_chapter_list": "Заполнение списка глав...",
        "loading": "Загрузка...",
        "loaded": "Загружено.",
        "selecting": "Выбор...",
        "selection_done": "Выбор завершен.",
        "generating": "Генерация {index}/{total} : {file}",
        "audio_book_created": "Аудиокнига успешно создана!",
        "language": "Язык:",
        "completed": "Готово",
        "chapter_completed": "Глава завершена: {chapter}",
        "chapter_failed": "Глава не удалась: {chapter}",
        "progress_reset": "Прогресс сброшен",
    }
}

CURRENT_LANGUAGE = "ru"

def set_language(lang):
    global CURRENT_LANGUAGE
    if lang in TRANSLATIONS:
        CURRENT_LANGUAGE = lang

def _(key):
    return TRANSLATIONS.get(CURRENT_LANGUAGE, TRANSLATIONS["en"]).get(key, key)

def get_language():
    return CURRENT_LANGUAGE
