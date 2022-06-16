'''
Peinan Wang 
CS 5001 Spring 2022
Final Project

gui_functions.py
'''


from tkinter import *
from tkinter import ttk
from graphing_functions import create_graph


WIDTH = 450
HEIGHT = 250
LABEL_LENGTH = 450
FULL_WINDOW = 1.0

X_POSITION = 0.5
Y_LABEL_0 = 0.3
Y_LABEL_1 = 0.6
Y_LABEL_2 = 0.1
Y_LABEL_3 = 0.6

Y_BUTTON_0 = 0.8
Y_BUTTON_1 = 0.2
Y_BUTTON_2 = 0.3
Y_BUTTON_3 = 0.4
Y_BUTTON_4 = 0.7
Y_BUTTON_5 = 0.8

TITLE = "Demographic Profile of Vancouver"

GUI_LABEL_0 = "The demographic profile of Vancouver has changed a lot!\n\n"\
              + "We have compared the demographic data of the 22 "\
              + "neighbourhoods in Vancouver, and analyzed their demographic "\
              + "trends by comparing data CENSUS 2006 and CENSUS 2016."
GUI_LABEL_1 = "Click START to explore the demographoc data"
GUI_LABEL_2 = "Please select the type demographic data you would "\
               + "like to check:"
GUI_LABEL_3 = "Click EXIT to quit the program or CONTINUE to keep exploring"

GUI_BUTTON_O = "START"
GUI_BUTTON_1 = "  Total Population of Each Neighbourhood  "
GUI_BUTTON_2 = "Immigrant Population of Each Neighbourhood"
GUI_BUTTON_3 = "  Immigrant Density of Each Neighbourhood "
GUI_BUTTON_4 = "EXIT"
GUI_BUTTON_5 = "CONTINUE"

OPTION_1 = "1"  
OPTION_2 = "2" 
OPTION_3 = "3" 

DISABLED = "disabled"
ACTIVE = "!disabled"


def data_viewer(names, pop_2006_lst, pop_2016_lst, immi_pop_2006_lst,
                immi_pop_2016_lst, immi_density_2006_lst,
                immi_density_2016_lst, pop_growth_lst, immi_growth_lst,
                immi_density_growth_lst):
    '''
    Functions: data_viewer
    Purpose: this is the GUI for the program. 
    Param:   - names; the list of neighbhourhood names
             - pop_2006_lst; list of 2006 population
             - pop_2016_lst; list of 2016 population
             - immi_pop_2006_lst: list of 2006 immigrant population
             - immi_pop_2016_lst: list of 2016 immigrant population
             - immi_density_2006_lst: list of 2006 immigrant density 
             - immi_density_2016_lst: list of 2016 immigrant density
             - pop_growth_lst: list of population change %
             - immi_growth_lst: list of immigrant population change %
             - immi_density_growth_lst: list of immigrant density change %
    Return:  none
    '''

    def show_selected_graph(graph_option):
        '''
        this function takes a graph option selected by the user and 
        run create_graph function to generate the selected bar chart
        '''
        create_graph(graph_option, names, pop_2006_lst, pop_2016_lst, 
                    immi_pop_2006_lst, immi_pop_2016_lst, 
                    immi_density_2006_lst, immi_density_2016_lst, 
                    pop_growth_lst, immi_growth_lst, immi_density_growth_lst)

    def disable(btn):
        '''
        this function disables the pressed button
        '''
        btn.config(state = DISABLED)
    
    def activate_button():
        '''
        this function makes all three buttons active
        '''
        for btn in [button_1, button_2, button_3]:
            btn.config(state = ACTIVE)

    root = Tk()
    root.title(TITLE)
    root.minsize(WIDTH, HEIGHT)

    frame1 = Frame(root)
    frame1.place(relheight=FULL_WINDOW, relwidth=FULL_WINDOW)
    frame2 = Frame(root)
    frame2.place(relheight=FULL_WINDOW, relwidth=FULL_WINDOW)


    label_0 = ttk.Label(frame1, text=GUI_LABEL_0, justify=CENTER,
                        wraplength = LABEL_LENGTH)
    label_0.place(relx=X_POSITION, rely=Y_LABEL_0, anchor=CENTER)

    label_1 = ttk.Label(frame1, text=GUI_LABEL_1)
    label_1.place(relx=X_POSITION, rely=Y_LABEL_1, anchor=CENTER)

    button_0 = ttk.Button(frame1, text=GUI_BUTTON_O, 
                          command=lambda:frame2.tkraise())
    button_0.place(relx=X_POSITION, rely=Y_BUTTON_0, anchor=CENTER)


    label_2 = ttk.Label(frame2, text=GUI_LABEL_2)
    label_2.place(relx=X_POSITION, rely=Y_LABEL_2, anchor=CENTER)

    button_1 = ttk.Button(frame2, text=GUI_BUTTON_1, 
                          command=lambda:[show_selected_graph(OPTION_1), 
                                          disable(button_1)])
    button_1.place(relx=X_POSITION, rely=Y_BUTTON_1, anchor=CENTER)

    button_2 = ttk.Button(frame2, text=GUI_BUTTON_2, 
                          command=lambda:[show_selected_graph(OPTION_2), 
                                          disable(button_2)])
    button_2.place(relx=X_POSITION, rely=Y_BUTTON_2, anchor=CENTER)

    button_3 = ttk.Button(frame2, text=GUI_BUTTON_3, 
                          command=lambda:[show_selected_graph(OPTION_3), 
                                          disable(button_3)])
    button_3.place(relx=X_POSITION, rely=Y_BUTTON_3, anchor=CENTER)

    label_3 = ttk.Label(frame2, text=GUI_LABEL_3)
    label_3.place(relx=X_POSITION, rely=Y_LABEL_3, anchor=CENTER)

    button_4 = ttk.Button(frame2, text=GUI_BUTTON_4, command=exit)
    button_4.place(relx=X_POSITION, rely=Y_BUTTON_4, anchor=CENTER)

    button_5 = ttk.Button(frame2, text=GUI_BUTTON_5, command=activate_button)
    button_5.place(relx=X_POSITION, rely=Y_BUTTON_5, anchor=CENTER)
    
    frame1.tkraise()

    root.mainloop()
