import requests

text = (
    "These were to have an enormous impact, not only because they were associated with "
    "Constantine, but also because, as in so many other areas, the decisions taken by "
    "Constantine (or in his name) were to have great significance for centuries to come. "
    "One of the main issues was the shape that Christian churches were to take, since there "
    "was not, apparently, a tradition of monumental church buildings when Constantine decided "
    "to help the Christian church build a series of truly spectacular structures."
)

response = requests.get("http://localhost:8880/v1/audio/voices")
voices = response.json()["voices"]
samples_dir = "samples"

# Generate audio
for voice in voices:
    response = requests.post(
        "http://localhost:8880/v1/audio/speech",
        json={
            "model": "kokoro",
            "input": text,
            "voice": voice,
            "response_format": "mp3",  # Supported: mp3, wav, opus, flac
            "speed": 1.0,
        },
    )

    # Save audio
    with open(f"{samples_dir}/{voice}.mp3", "wb") as f:
        f.write(response.content)