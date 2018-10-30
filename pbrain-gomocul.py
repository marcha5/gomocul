#!/usr/bin/env python3

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
        command = sys.stdin.readline().strip()
        if ' ' in command:
            command, param_1 = command.split(' ')
            if command == 'INFO':
                continue
            if ',' in param_1:
                param_1, param_2 = param_1.split(',')
                if str.isnumeric(param_1) and str.isnumeric(param_2):
                    param_1 = int(param_1)
                    param_2 = int(param_2)
                    try:
                        choice[command](param_1, param_2)
                    except Exception as e:
                        print("Unknown command !", e)
                else:
                    print("Unknown command !")
            else:
                try:
                    if str.isnumeric(param_1):
                        param_1 = int(param_1)
                        choice[command](param_1)
                    else:
                        print("Unknown command !")
                except:
                    print("Unknown command !")
        else:
            try:
                choice[command]()
            except Exception as e:
                print('Unknown command !', e)

main()