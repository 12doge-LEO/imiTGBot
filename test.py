from db_connnector import imi_db_connector
import time

filename = 'meow2.mp3'

data = {
    "time": time.time(),
    "name": "meow",
    "type": "audio",
}

audio_info ={
    "type" : "audio_info",
    "infos":{
        "meow1":"meow2.mp3"
    }
}

# print(imi_db_connector.insert(audio_info))
# with open('./test.mp3','wb') as f:
#     f.write(data)

def upload_audio(file_name:str='',name:str=''):
    audio_info = list(imi_db_connector.find({"type":"audio_info"}))
    if len(audio_info) == 0:
        audio_info_data = {
            "type": "audio_info",
            "infos": {

            }
        }
        try:
            imi_db_connector.insert(audio_info_data)
        except Exception as e:
            print(e)
    else:
        print(audio_info[0]["infos"])
        audio_info[0]["infos"][name] = file_name
        imi_db_connector.update({"type":"audio_info"},audio_info[0])

    try:
        imi_db_connector.insert_file(file_name,id=name,collection="audio")
    except Exception as e:
        print(e)

if __name__ == '__main__':
    upload_audio("./meow3.mp3","meow3")