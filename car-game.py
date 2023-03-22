car_running = False
while True:
    car_command = input('> ').upper()
    if car_command == "START":
        if car_running:
            print('Car already running.')
        else:
            print('Car started...Ready to go!')
            car_running = True
    elif car_command == "STOP":
        if not car_running:
            print('Car already stopped')
        else:
            print('Car stopped.')
            car_running = False
    elif car_command == "QUIT":
        print('Exiting program...')
        break
    elif car_command == "HELP":
        print('START - Start the car.')
        print('STOP - Stop the car.')
        print('QUIT - Quit the application.')
    else:
        print("I don't understand that...")

