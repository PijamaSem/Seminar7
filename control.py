import gui

def start():
    global mode
    data = open('contats.txt', 'r')
    last_id = data.readlines()[0]
    last_id = int(last_id)+1
    mode = gui.mode()
    while mode != 'x':
        if mode == 'w':
            contact_data = gui.get_data()
            data = open('contats.txt', 'a')
            data.writelines(f'{str(last_id)}; {contact_data[1]}; {contact_data[2]}; {contact_data[3]}\n')
            last_id = int(last_id) + 1
            data.close()
        mode = gui.mode()
        if mode == 'r':
            data = open('contats.txt', 'r')
            #data.readlines()
            for line in data.readlines():
                print(line)
            mode = gui.mode()
        else:
            print('Не верный ввод')
            mode = gui.mode()





