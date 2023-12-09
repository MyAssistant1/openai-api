from openai import OpenAI
client = OpenAI(api_key="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")

audio_file = open("Record (online-voice-recorder.com).mp3", "rb")
transcript = client.audio.translations.create(
  model="whisper-1", 
  file=audio_file, 
  response_format="text"
)

print(transcript)