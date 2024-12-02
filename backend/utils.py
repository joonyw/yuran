import openai
import os
import urllib
from pathlib import Path
from moviepy.editor import ImageSequenceClip, AudioFileClip, CompositeVideoClip



def create_scenario(usr_input):
    client = openai.OpenAI(
    api_key = OPEN_API_KEY,
)
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "write a short scenario within less than 800 characters in length according to the following subject:" + usr_input},
    ]
    )
    return (response.choices[0].message.content)


def get_pic(resp):
    from openai import OpenAI
    client = openai.OpenAI(api_key = OPEN_API_KEY,)

    response = client.images.generate(
        model="dall-e-3",
        prompt=resp,
        size="1024x1024",
        quality="standard",
        n=1,
    )

    image_url = response.data[0].url
    urllib.request.urlretrieve(image_url, "generated_image.jpeg")
    return

# def speech(usr_input):

#     speech_file_path = Path(__file__).parent / "speech.mp3"
#     response = openai.audio.speech.create(
#     model="tts-1",
#     voice="alloy",
#     input=usr_input
#     )
#     response.stream_to_file(speech_file_path)

# def make_video(image_folder, audio_file, output_video, fps=0.5):
#     image_files = [os.path.join(image_folder, img) for img in sorted(os.listdir(image_folder)) if img.endswith(".jpg")]
#     clip = ImageSequenceClip(image_files, fps=fps)
#     audio = AudioFileClip(audio_file)
#     video = clip.set_audio(audio)

#     video = video.set_duration(audio.duration)

#     video.write_videofile("output.mp4", fps=fps, audio_codec="aac", audio_bitrate="192k")

    