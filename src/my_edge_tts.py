import asyncio
import edge_tts


def load_voices(language_prefix=None):
    voices = asyncio.run(edge_tts.list_voices())
    if language_prefix:
        voices = [
            voice for voice in voices
            if voice.get("Locale", "").lower().startswith(language_prefix.lower())
        ]
    return [voice["ShortName"] for voice in voices]


async def _generate_mp3_async(
        input_text_file_path,
        output_mp3_file_path,
        voice,
        playback_rate_percentage=100,
        volume_percentage=100,
        pitch_hz=0,
        max_retries=3
):
    with open(input_text_file_path, "r", encoding="utf-8") as f:
        text = f.read()

    rate = f"+{playback_rate_percentage - 100}%" if playback_rate_percentage >= 100 else f"{playback_rate_percentage - 100}%"
    volume = f"+{volume_percentage - 100}%" if volume_percentage >= 100 else f"{volume_percentage - 100}%"
    pitch = f"+{pitch_hz}Hz" if pitch_hz >= 0 else f"{pitch_hz}Hz"

    last_error = None
    for attempt in range(max_retries):
        try:
            communicate = edge_tts.Communicate(text, voice, rate=rate, volume=volume, pitch=pitch)
            await communicate.save(output_mp3_file_path)
            return True
        except (asyncio.LimitOverrunError, asyncio.TimeoutError, ConnectionError, OSError) as e:
            last_error = e
            if attempt < max_retries - 1:
                await asyncio.sleep(2 ** attempt)
                continue
            raise RuntimeError(f"Failed after {max_retries} attempts: {e}")
    raise last_error


def generate_mp3_file(
        input_text_file_path,
        output_mp3_file_path,
        voice,
        playback_rate_percentage=100,
        volume_percentage=100,
        pitch_hz=0,
        command='tts'
):
    if command not in ('playback', 'tts'):
        print("invalid command")
        return False

    try:
        asyncio.run(_generate_mp3_async(
            input_text_file_path,
            output_mp3_file_path,
            voice,
            playback_rate_percentage,
            volume_percentage,
            pitch_hz
        ))
        print("File generated successfully.")
        return True
    except Exception as e:
        print(f"Error generating audio: {e}")
        return False
