# Speech & Text Language Translator

## Features
- Speech Recognition: Convert spoken words to text.
- Language Detection: Automatically detect the input language.
- Translation: Translate text into a specified language.
- Text-to-Speech: Speak out the translated text.
- Supports Multiple Languages: Uses `googletrans.LANGCODES` for language selection.

---

## Installation

Ensure you have Python installed (>=3.6). Install the required dependencies:

```sh
pip install googletrans==3.1.0a0 SpeechRecognition pyttsx3 langdetect
```

For speech recognition, you may also need:

```sh
pip install pyaudio
```

On Linux, install PortAudio before installing PyAudio:

```sh
sudo apt-get install portaudio19-dev
pip install pyaudio
```

## Example Usage

### Speech Translator

```python
import googletrans # googletrans==3.1.0a0
import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()
recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Wait for calibrations...")
    recognizer.adjust_for_ambient_noise(source, 1)
    print("Start speaking...")
    audio = recognizer.listen(source)
    print("Recorded successfully")
    speech = recognizer.recognize_google(audio)
    speech = speech.lower()
    print("Recognized Speech:", speech)

def trans():
    print("Translating...")
    print(googletrans.LANGCODES)
    language = input("Type the translation language code: ").lower()
    translator = googletrans.Translator()
    translation = translator.translate(text=speech, dest=language)
    print("Translation:", translation.text)
    engine.setProperty("rate", 120)
    engine.say(translation.text)
    engine.runAndWait()

trans()
```

### Text Translator

```python
from langdetect import detect
import googletrans

sentence = input("Enter the sentence: ")
print("Detected Language:", detect(sentence))

language = input("Type the translation language code: ").lower()

translator = googletrans.Translator()
translation = translator.translate(text=sentence, dest=language)
print("Translation:", translation.text)
print("Detected Translated Language:", detect(translation.text))
```

## Model Performance

- Speech recognition accuracy: Depends on microphone quality and background noise.
- Translation reliability: Uses Google Translate for high accuracy.
- Execution speed: Processes translations in real-time.

## Example Output

```plaintext
Wait for calibrations...
Start speaking...
Recorded successfully
Recognized Speech: "hello"
Translating...
Type the translation language code: fr
Translation: "bonjour"
```

```plaintext
Enter the sentence: "How are you?"
Detected Language: en
Type the translation language code: es
Translation: "¿Cómo estás?"
Detected Translated Language: es
```

## Future Enhancements

- Improve speech recognition accuracy.
- Add support for offline translations.
- Implement voice selection and accents in text-to-speech.
- Integrate machine learning for smarter translations.

## Author

Developed by Pavan Kalyan Manda

Website Developer | IoT & Embedded Systems Enthusiast | AI/ML Developer
