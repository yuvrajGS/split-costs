import PySimpleGUI as sg
import main


sg.theme('DarkAmber')
layoutL = [
    [sg.Text("Input Receipt Items (Ex: chicken, 5.99):")],
    [sg.Multiline(size=(50,10),key='input')],
    [sg.Text("Split Costs:")],
    [sg.Multiline(size=(20,10),key='output')],
    [sg.Button("Exit"), sg.Button("Submit Input"), sg.Button("Run")]
]
def formatLR(name):
    return [
        sg.Text(f'{name} Opt-out:'),
        sg.Listbox(['Submit Input'],size=(20,5),key=f'input-{name}', select_mode=sg.LISTBOX_SELECT_MODE_MULTIPLE)
    ]
layoutR = [
    formatLR('Yuvraj'), formatLR("Meer"), formatLR("Thenu"), formatLR("Cynthia"), formatLR("Sarah")
]

layout = [
    [
        sg.Column(layoutL),
        sg.VSeperator(),
        sg.Column(layoutR)
    ]
]
window = sg.Window("Split Costs", layout)

def readIN(input):
    checkL=[]
    itemList = input.split("\n")
    for itemIN in itemList:
        item = itemIN.split(",")
        checkL.append(item[0])
    return checkL

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
        finalCost, total = main.main(values['input'],values['input-Yuvraj'],values['input-Meer'],values['input-Thenu'],values['input-Cynthia'],values['input-Sarah'])
        window['output'].update(f'Yuvraj: {finalCost[0]:.2f}\nMeer: {finalCost[1]:.2f}\nThenu: {finalCost[2]:.2f}\nCynthia: {finalCost[3]:.2f}\nSarah: {finalCost[4]:.2f}\nTotal: {total:.2f}')
window.close()
