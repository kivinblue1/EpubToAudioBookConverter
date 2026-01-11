import os
import json

PROGRESS_EXTENSION = ".progress.json"

def get_progress_file_path(epub_file_path):
    base_path = os.path.splitext(epub_file_path)[0]
    return base_path + PROGRESS_EXTENSION

def load_progress(epub_file_path):
    progress_file = get_progress_file_path(epub_file_path)
    if os.path.exists(progress_file):
        try:
            with open(progress_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return {}
    return {}

def save_progress(epub_file_path, completed_chapters):
    progress_file = get_progress_file_path(epub_file_path)
    with open(progress_file, 'w', encoding='utf-8') as f:
        json.dump(completed_chapters, f, ensure_ascii=False, indent=2)

def mark_chapter_completed(epub_file_path, chapter_file_name):
    progress = load_progress(epub_file_path)
    if chapter_file_name not in progress:
        progress[chapter_file_name] = {
            "completed": True,
            "timestamp": os.path.getmtime(epub_file_path) if os.path.exists(epub_file_path) else None
        }
        save_progress(epub_file_path, progress)

def is_chapter_completed(epub_file_path, chapter_file_name):
    progress = load_progress(epub_file_path)
    return progress.get(chapter_file_name, {}).get("completed", False)

def reset_progress(epub_file_path):
    progress_file = get_progress_file_path(epub_file_path)
    if os.path.exists(progress_file):
        os.remove(progress_file)
