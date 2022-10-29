import PySimpleGUI as sg
from keywords import python_keywords
from builtin import built_in
from constants import constants
from methods import string_methods 
from methods import list_methods
from methods import mutable_sequence_types

combo_keywords = [x for x in python_keywords.keys()]
combo_builtin = [x for x in built_in.keys()]
combo_consts = [x for x in constants.keys()]
combo_strings = [x for x in string_methods.keys()]

tab1_layout = [

sg.vtop(
[
    sg.T("Keyword:",font='Helvetica',),
    
    sg.Combo(
        combo_keywords,
        font='Helvetica 12', 
        enable_events=True,
        size=(15,30), 
        key="-word"),
    
]),
[sg.HorizontalSeparator(),],
[
    sg.T(
        size=(45,20),
        key='ml',
        font='Helvetica 12',),
],
[sg.HorizontalSeparator(),],
[
    sg.T(
        "Utility      ",
        font='Helvetica',), 
    sg.T(
        "⭐⭐⭐⭐⭐",
        key='util',
        text_color='yellow',
        font='Helvetica 20'),
    sg.T("Popularity",font='Helvetica',), 
    sg.T(
        "⭐⭐⭐⭐⭐",
        key='pop',
        text_color='yellow',
        font='Helvetica 20'),
    sg.T("Difficulty  ",font='Helvetica',),
    sg.T(
        "⭐⭐⭐⭐⭐", 
        key="dif",
        text_color='yellow',
        font='Helvetica 20')
],
]    

tab2_layout = [
    [
        sg.T("Strings:",font='Helvetica',),
        sg.Combo(
            combo_strings, 
            enable_events=True,
            size=(20,30),
            font='Helvetica', 
            key="-strword")
    ],
    [sg.HorizontalSeparator(),],
    [
        sg.T("",
            size=(40,10),
            key='strml',
            font='Helvetica', )
    ],
    [sg.HorizontalSeparator(),],
    [
        sg.T("Arguments  ",font='Helvetica',),
        sg.T("", key="strarg",font='Helvetica',)
    ]
]    

tab3_layout = [
sg.vtop(
[
    sg.T("Built-In:",font='Helvetica'),
    sg.Combo(
        combo_builtin, 
        enable_events=True,
        size=(15,30), 
        key="-bword")
]),
[sg.HorizontalSeparator(),],
[
    sg.T("",size=(40,10),font='Helvetica',key='bml'),
],
[sg.HorizontalSeparator(),],
[
    sg.T("Utility      ",font='Helvetica'), 
    sg.T(
        "⭐⭐⭐⭐⭐",
        key='butil',
        text_color='yellow',
        font='Helvetica 20'),
    sg.T("Popularity",font='Helvetica'), 
    sg.T(
        "⭐⭐⭐⭐⭐",
        key='bpop',
        text_color='yellow',font='Helvetica 20'),
    sg.T("Difficulty  ",font='Helvetica'),
    sg.T(
        "⭐⭐⭐⭐⭐", 
        key="bdif",
        text_color='yellow',
        font='Helvetica 20')
]
]

tab4_layout = [
    sg.vtop(
[
    sg.T(
        "Constants:",
        font='Helvetica'),
    sg.Combo(
        combo_consts,
        default_value=combo_consts[1],
        enable_events=True,
        size=(15,40), 
        key="-cword",
        font='Helvetica')
]),
[
    sg.T(
        size=(45,15),
        key='cml', 
        font='Helvetica'),
],
[
    sg.T("Utility      ",font='Helvetica'), 
    sg.T(
        "⭐⭐⭐⭐⭐",
        key='cutil', 
        text_color='yellow',
        font='Helvetica 20'),
    sg.T("Popularity",font='Helvetica'), 
    sg.T(
        "⭐⭐⭐⭐⭐",
        key='cpop',
        text_color='yellow',
        font='Helvetica 20'),
        sg.T("Difficulty  ",font='Helvetica'),
    sg.T(
        "⭐⭐⭐⭐⭐",
        text_color='yellow', 
        key="cdif",
        font='Helvetica 20')
]]

layout2 = [
[
sg.TabGroup([
[
    sg.Tab(
        'Keywords', 
        tab1_layout, 
        tooltip='Keywords are functions like "def"'
    ), 
    sg.Tab(
        'Methods', 
        tab2_layout
    ),
    sg.Tab(
        "Built-in",
        tab3_layout
    ),
    sg.Tab(
        "Constants",
        tab4_layout
    )
]
], tooltip='TIP2')]]  


def main():

    window = sg.Window("python3", layout2)
    
    while True:
        event, values = window.read()
        
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == "-word":
            x = values["-word"]
            window['ml'].update(python_keywords[f"{x}"][0])
            window["dif"].update(python_keywords[f"{x}"][1])
            window["util"].update(python_keywords[f"{x}"][2])
            window["pop"].update(python_keywords[f"{x}"][3])


        if event == "-bword":
            x = values["-bword"]
            

            window['bml'].update(built_in[f"{x}"][0])
            window["bdif"].update(built_in[f"{x}"][1])
            window["butil"].update(built_in[f"{x}"][2])
            window["bpop"].update(built_in[f"{x}"][3])


        if event == "-cword":
            x = values["-cword"]

            window['cml'].update(constants[f"{x}"][0])
            window["cdif"].update(constants[f"{x}"][1])
            window["cutil"].update(constants[f"{x}"][2])
            window["cpop"].update(constants[f"{x}"][3])

        if event == "-strword":
            x = values["-strword"]

            window['strml'].update(string_methods[f"{x}"]["description"][0])
            window["strarg"].update(string_methods[f"{x}"]["args"][0:])

main()