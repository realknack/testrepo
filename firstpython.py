command = ""
started = True
while True:
    command = input('> ').lower()
    if command == "start":
        if started:
            print("Car already started")
        else:
            started = True
            print("Car Started...")

    elif command == "stop":
        if not started:
            print("Car is already stopped...")
        else:
            started = False
            print("Car Stopped")
    elif command == "help":
        print("""
start -- to start the car
stop -- to stop the car
quite -- to quite
    """)
    elif command == "quit":
        break
    else:
        print("i dont understand its getting out of hand")
