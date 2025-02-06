from PIL import Image, ImageFilter
from pydub import AudioSegment, effects
import os

UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def apply_image_filter(image_path, filter_type):
    try:
        img = Image.open(image_path)

        if filter_type == "grayscale":
            img = img.convert("L")
        elif filter_type == "blur":
            img = img.filter(ImageFilter.BLUR)
        elif filter_type == "edges":
            img = img.filter(ImageFilter.FIND_EDGES)
        elif filter_type == "contour":
            img = img.filter(ImageFilter.CONTOUR)

        filtered_path = os.path.join(UPLOAD_FOLDER, "filtered_" + os.path.basename(image_path))
        img.save(filtered_path)
        return filtered_path
    except Exception as e:
        print(f"Error applying image filter: {e}")
        return None

def apply_audio_filter(audio_path, filter_type):
    try:
        file_extension = audio_path.split(".")[-1].lower()

     
        temp_wav_path = audio_path.rsplit(".", 1)[0] + ".wav"
        if file_extension not in ["wav"]:
            audio = AudioSegment.from_file(audio_path, format=file_extension)
            audio.export(temp_wav_path, format="wav")
            audio_path = temp_wav_path

        audio = AudioSegment.from_wav(audio_path)

        
        if filter_type == "low_pass":
            filtered_audio = audio.low_pass_filter(300)
        elif filter_type == "high_pass":
            filtered_audio = audio.high_pass_filter(3000)
        elif filter_type == "reverse":
            filtered_audio = audio.reverse()
        elif filter_type == "speed_up":
            filtered_audio = effects.speedup(audio, playback_speed=1.5)
        elif filter_type == "slow_down":
            filtered_audio = effects.speedup(audio, playback_speed=0.7)
        else:
            return None

       
        output_path = os.path.join(UPLOAD_FOLDER, "filtered_" + os.path.basename(audio_path).replace(".wav", f".{file_extension}"))
        filtered_audio.export(output_path, format=file_extension)

        return output_path
    except Exception as e:
        print(f"Error applying audio filter: {e}")
        return None
