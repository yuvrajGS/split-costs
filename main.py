import PySimpleGUI as sg
import SplitCosts
from tkinter import Tk

def main():
    # Define the window's contents
    sg.theme('DarkAmber')
    layoutL = [
        [sg.Text("Input Receipt Items (Ex: chicken, 5.99):")],
        [sg.Multiline(size=(50,10),key='input')],
        [sg.Text("Split Costs:")],
        [sg.Multiline(size=(50,10),key='output')],
        [sg.Button("Exit"), sg.Button("Submit Input"), sg.Button("Run"), sg.Button("Copy")]
    ]
    
    def formatLR(name):
        return [
            sg.Listbox(['Submit Input'],size=(60,6),key=f'input-{name}', select_mode=sg.LISTBOX_SELECT_MODE_MULTIPLE, pad=(0,5))
        ]
    layoutR = [
        [sg.Text('Yuvraj Opt-out:')], formatLR('Yuvraj'), 
        [sg.Text('Meer Opt-out:')], formatLR("Meer"), 
        [sg.Text('Thenu Opt-out:')], formatLR("Thenu"), 
        [sg.Text('Cynthia Opt-out:')], formatLR("Cynthia"), 
        [sg.Text('Sarah Opt-out:')], formatLR("Sarah")
    ]
    layout = [
        [
            sg.Column(layoutL),
            sg.VSeperator(),
            sg.Column(layoutR)
        ]
    ]
    window = sg.Window("Split Costs", layout)


    # Event Loop to process "events" and get the "values" of the inputs
    optINS = ''
    while True:
        event, values = window.read()
        if (event == 'Exit' or event == sg.WIN_CLOSED):
            break
        if (event == 'Submit Input'):
            items = readIN(values['input'])
            window['input-Yuvraj'].update(items)
            window['input-Meer'].update(items)
            window['input-Thenu'].update(items)
            window['input-Cynthia'].update(items)
            window['input-Sarah'].update(items)
            window.refresh()
        if (event == 'Run'):
            finalCost, total, optINS = SplitCosts.run(values['input'],values['input-Yuvraj'],values['input-Meer'],values['input-Thenu'],values['input-Cynthia'],values['input-Sarah'])
            window['output'].update(f'Yuvraj: {finalCost[0]:.2f}\nMeer: {finalCost[1]:.2f}\nThenu: {finalCost[2]:.2f}\nCynthia: {finalCost[3]:.2f}\nSarah: {finalCost[4]:.2f}\nTotal: {total:.2f}')
        if (event == 'Copy'):
            copyToCliboard( '`' +values['output'] + '`' + optINS)
    window.close()
    return

def copyToCliboard(text):
    r = Tk()
    r.withdraw()
    r.clipboard_clear()
    r.clipboard_append(text)
    r.update()
    r.destroy()
    return

def readIN(input):
    checkL=[]
    itemList = input.split("\n")
    for itemIN in itemList:
        item = itemIN.split(",")
        checkL.append(item[0])
    return checkL

if __name__ == '__main__':
    main()