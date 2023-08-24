import time


def animate_text(text, delay=0.2):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()  # Print a newline at the end


if __name__ == "__main__":
    name = "Murali ❤"
    animate_text(name)
