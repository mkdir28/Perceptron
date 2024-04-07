
def readfile(file):
    data = list()
    with open(file, 'r') as files:
        for line in files:
            data.append(line.strip().split(','))
    return data


def main():
    training_data = input("Please, provide path to file with training data");
    test_data = input("Please, provide path to file with test data");
    learning_rate = input("Please, provide learning rate");
    epochs = input("Please, provide number of epochs");


    menu = {}
    menu['1'] = "Enter new observations"
    menu['2'] = "Exiting the program"

    while True:
        options = sorted(menu.keys())

        for enter in options:
            print(enter, menu[enter])
        choose = input("Please, choose an option: ")

        if choose == '1':
        elif choose == '2':
            break

        else:
            print("Unknown option was chosen!")




if __name__ == '__main__':
    main()

