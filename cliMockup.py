import time

def menu():
    print("__      __   _   _                _____ _                 _       _             ")
    time.sleep(0.05)
    print("\ \    / /  | | (_)              / ____(_)               | |     | |            ")
    time.sleep(0.05)
    print(" \ \  / /__ | |_ _ _ __   __ _  | (___  _ _ __ ___  _   _| | __ _| |_ ___  _ __ ")
    time.sleep(0.05)
    print("  \ \/ / _ \| __| | '_ \ / _` |  \___ \| | '_ ` _ \| | | | |/ _` | __/ _ \| '__|")
    time.sleep(0.05)
    print("   \  / (_) | |_| | | | | (_| |  ____) | | | | | | | |_| | | (_| | || (_) | |   ")
    time.sleep(0.05)
    print("    \/ \___/ \__|_|_| |_|\__, | |_____/|_|_| |_| |_|\__,_|_|\__,_|\__\___/|_|   ")
    time.sleep(0.05)
    print("                          __/ |                                                 ")
    time.sleep(0.05)
    print("                         |___/                                                  ")
    time.sleep(0.05)

    print("Menu:\n1. Select data files\n2. Generate data files\n3. Exit")
    inp = int(input("> "))

def main():
    menu()

main()