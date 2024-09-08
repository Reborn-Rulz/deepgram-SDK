from deepgram import DeepgramClient, PrerecordedOptions

DEEPGRAM_API_KEY = "ae2f547355449dbc097e07b2ca082605cd68f9ee"

AUDIO_URL = {
    "url": "https://static.deepgram.com/examples/Bueller-Life-moves-pretty-fast.wav"
}

def main():
    try:
        deepgram = DeepgramClient(DEEPGRAM_API_KEY)

        options = PrerecordedOptions(
            model="nova-2",
            language="en",
        )

        response = deepgram.listen.prerecorded.v("1").transcribe_url(AUDIO_URL, options)
        print(response.to_json(indent=4))

    except Exception as e:
        print(f"Exception: {e}")

if __name__ == "__main__":
    main()