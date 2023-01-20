import sys
import json
import clipboard

PATH_DATA = "clipboard.json"


def save_data(file_path, data):
    with open(file_path, "w") as f:
        json.dump(data, f)


def load_data(file_path):
    try:
        with open(file_path, "r") as f:
            data = json.load(f)
            return data
    except:
        return {}


if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_data(PATH_DATA)

    if command == "save":
        # Save whatever is in clipboard
        key = input("Enter a key: ")
        data[key] = clipboard.paste()
        save_data(PATH_DATA, data)
        print("Saved")

    elif command == "load":
        key = input("Enter the key you wanna load: ")
        if key in data:
            clipboard.copy(data[key])
            print("Data Copied in your clipboard")
        else:
            print("Key does not exist")

    elif command == "list":
        print("list")
        print(data)
    else:
        print("Unknown Command")

