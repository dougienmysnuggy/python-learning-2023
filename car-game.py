while True:
    car_command = input('> ').upper()
    if car_command == "START":
        print('Car started...Ready to go!')
    elif car_command == "STOP":
        print('Car stopped.')
    elif car_command == "QUIT":
        print('Exiting program...')
        break
    elif car_command == "HELP":
        print('START - Start the car.')
        print('STOP - Stop the car.')
        print('QUIT - Quit the application.')
    else:
        print("I don't understand that...")

