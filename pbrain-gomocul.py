import sys
from comunication_protocol import function_obj

choice = {
    'START': function_obj.start,
    'TURN': function_obj.turn,
    'BEGIN': function_obj.begin,
    'BOARD': function_obj.board,
    'INFO': function_obj.info,
    'END': function_obj.end,
    'ABOUT': function_obj.about,
    'RESTART': function_obj.restart
}


def main():
    command = ''
    while command != 'END':
        command = sys.stdin.readline().strip('\r\n').upper()
        if ' ' in command:
            command = command.split(' ')
            if command[0] == 'INFO':
                continue
            if ',' in command:
                param_1 = command[1]
                param_2 = command[2]
                if str.isnumeric(param_1) and str.isnumeric(param_2):
                    param_1 = int(param_1)
                    param_2 = int(param_2)
                    try:
                        choice[command[0]](param_1, param_2)
                    except Exception as e:
                        print("Unknown command ! 1", e)
                        sys.stdout.flush()
                else:
                    print("Unknown command ! 2")
                    sys.stdout.flush()
            else:
                try:
                    if str.isnumeric(command[1]):
                        param_1 = int(command[1])
                        choice[command[0]](param_1)
                    else:
                        print("Unknown command ! 3")
                        sys.stdout.flush()
                except:
                    print("Unknown command ! 4")
                    sys.stdout.flush()
        else:
            try:
                choice[command]()
            except Exception as e:
                print('Unknown command ! 5', e)
                sys.stdout.flush()

main()