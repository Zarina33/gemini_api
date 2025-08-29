import google.generativeai as genai
import json
import os

# Set your Gemini API key from an environment variable for security
genai.configure(api_key=os.environ.get('YOUR_GEMINI_API_KEY'))

def translate_to_kyrgyz(text_to_translate):
    """
    Translates a given text from English to Kyrgyz using the Gemini 1.5 Flash API.
    """
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # The prompt specifically asks the model to translate only the provided text to Kyrgyz.
        prompt = f"Текстти англис тилинен кыргыз тилине котор. Баштапкы форматын сакта.\n\nText: \"\"\"{text_to_translate}\"\"\""
        
        response = model.generate_content(prompt)
        
        return response.text
    except Exception as e:
        return f"Которгон учурда ката кетти: {e}"

def process_file_and_translate_values(file_path):
    """
    Reads a JSON file, extracts text values, and translates them to Kyrgyz.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            
            # This is the key part: we are iterating through the conversations
            # list and replacing the 'value' field with its Kyrgyz translation.
            if "conversations" in data:
                print("Оригиналдуу маалыматтар:")
                print(json.dumps(data, indent=2, ensure_ascii=False))
                
                for conversation in data["conversations"]:
                    if "value" in conversation:
                        english_text = conversation["value"]
                        kyrgyz_translation = translate_to_kyrgyz(english_text)
                        
                        # Update the 'value' field with the translated text
                        conversation["value"] = kyrgyz_translation
                
                print("\nКоторулган маалыматтар:")
                print(json.dumps(data, indent=2, ensure_ascii=False))
            else:
                print("Файл 'conversations' ачкычын камтыбайт.")
                
    except FileNotFoundError:
        print(f"Ката: '{file_path}' файлы табылган жок.")
    except json.JSONDecodeError:
        print(f"Ката: '{file_path}' файлы жарактуу JSON файлы эмес.")
    except Exception as e:
        print(f"Күтүлбөгөн ката кетти: {e}")

if __name__ == "__main__":
    file_name = "input.json" # Change this to your file name if needed
    process_file_and_translate_values(file_name)