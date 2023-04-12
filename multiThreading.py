import threading
import time

class AsyncWrite(threading.Thread):
    def __init__(self, text, out):
        threading.Thread.__init__(self)
        self.text = text
        self.out = out

    def run(self):
        with open(self.out, "a") as file:
            file.write(self.text + "\n")
        time.sleep(2)
        print(f"Finished Background File Write to {self.out}")

    
def Main():
    message = input("Enter a string to store: ")
    background = AsyncWrite(message, "out.txt")
    background.start()
    print(f"The program can continue while it writes in another thread")
    print(f"100 + 400 = {100+400}")

    background.join()
    print(f"Waited until thread was complete")


if __name__ == "__main__":
    Main()