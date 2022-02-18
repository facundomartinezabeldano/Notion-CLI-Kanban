import os

def clean_screen_and_print_logo():
    with open(os.path.join("src","userdata.json"), "r", encoding="utf8") as f:
        for line in f:
            print(line)
    return

clean_screen_and_print_logo()
