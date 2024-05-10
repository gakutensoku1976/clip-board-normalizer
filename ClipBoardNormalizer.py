import json
import pyperclip
import keyboard
import time


def normalize_name(text, dictionary):
    for translate_item in dictionary["name_normalization"]["translate"]:
        text = text.translate(
            str.maketrans(translate_item["from"], translate_item["to"])
        )

    return text


def main():
    with open("normalize.json", "r", encoding="utf-8") as f:
        config = json.load(f)

        shortcut_key = config["shortcut_key"]
        print(f"ショートカットキー: {shortcut_key}")

        is_shortcut_pressed = False

        while True:
            time.sleep(0.01)

            if keyboard.is_pressed(shortcut_key) and not is_shortcut_pressed:
                is_shortcut_pressed = True
                clipboard_text = pyperclip.paste()

                if len(clipboard_text) == 0:
                    continue

                print(f"変換前: {clipboard_text}")

                for translate_item in config["text_normalization"]["translate"]:
                    clipboard_text = clipboard_text.translate(
                        str.maketrans(translate_item["from"], translate_item["to"])
                    )

                clipboard_text = f"【{clipboard_text}】"
                print(f"変換後: {clipboard_text}")

                pyperclip.copy(clipboard_text)

            elif not keyboard.is_pressed(shortcut_key):
                is_shortcut_pressed = False


if __name__ == "__main__":
    main()
