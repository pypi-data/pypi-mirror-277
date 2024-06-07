import sys
import requests
from win10toast import ToastNotifier
       
        
from googletrans import Translator
translator = Translator()

def translate_text(text):
    translation = translator.translate(text)
    return translation.text
 
def meanings(text):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en_US/{text}"
    response = requests.get(url)
    data = response.json()
    if 'title' in data:
        return ""
    return data[0]['meanings'][0]['definitions'][0]['definition']
 
def detect_language(text):
    return translator.detect(text).lang   

def show_notification(title, message):
    toaster = ToastNotifier()
    toaster.show_toast(title, message, duration=10)
    


def main():
    try:
        text_to_translate = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else input("Enter the text to translate: ")
        translated_text = translate_text(text_to_translate)
        title= text_to_translate+"("+detect_language(text_to_translate)+")"
        translated_text =   translated_text + "\n" + meanings(translated_text)
        show_notification(title, translated_text)
    except:
        print("Error occurred")
        show_notification("Error", "Enter valid input")
        return 1

if __name__ == "__main__":
    main()
