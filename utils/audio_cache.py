import os
from db_connnector import imi_db_connector
def update_audio_cache(path: str = '') -> dict:
    audio_files = imi_db_connector.find({"type": "audio_info"})[0]["infos"]
    print(audio_files)
    for item in audio_files:
        if os.path.exists(path + audio_files[item]):
            continue
        else:
            with open(path + audio_files[item], 'wb') as f:
                f.write(imi_db_connector.get_file(audio_files[item], collection='audio'))
    return audio_files

if __name__ == '__main__':
    print(update_audio_cache(path='./resources/audio/'))