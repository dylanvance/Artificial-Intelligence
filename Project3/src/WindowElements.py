import tkinter as tk
from tkinter.filedialog import askopenfilename

def addAttributeElements(window, attribute_list):
    '''
    User inputs for Attribuites
    '''

    # Create a attribute input
    attribute_label = tk.Label(window, text="Enter the attribute:")
    attribute_label.grid(row=0, column=0, padx=10, pady=5)

    attribute_input = tk.Entry(window)
    attribute_input.grid(row=1, column=0, padx=10, pady=5)

    # Create a first value input
    value_1_label = tk.Label(window, text="Enter the first value:")
    value_1_label.grid(row=0, column=1, padx=10, pady=5)

    value_1_input = tk.Entry(window)
    value_1_input.grid(row=1, column=1, padx=10, pady=5)

    # Create a second value input
    value_2_label = tk.Label(window, text="Enter the second value:")
    value_2_label.grid(row=0, column=2, padx=10, pady=5)

    value_2_input = tk.Entry(window)
    value_2_input.grid(row=1, column=2, padx=10, pady=5)

    '''
    Attribuites list
    '''

    # Create a Listbox widget
    listbox = tk.Listbox(window, width=50)
    listbox.grid(row=0, column=3, rowspan=2, pady=5)

    # Creating a Scrollbar and attaching it to root window
    scrollbar = tk.Scrollbar(window)
    scrollbar.grid(row=0, column=4, rowspan=2, pady=5, sticky='ns')
    scrollbar.config(command=listbox.yview)
    listbox.config(width=0, height=4, yscrollcommand=scrollbar.set)

    # Define a function to clear all the items in the Listbox widget
    def clear_list():
        listbox.delete(0, tk.END)
        attribute_list.clear()

    # Create a Clear List button
    clear_button = tk.Button(window, text="Clear List", command=clear_list)
    clear_button.grid(row=2, column=3, padx=10, pady=5)




    '''
    Input handler buttons
    '''

    # Define a function to get the input when the button is clicked
    def get_input():
        attribute = attribute_input.get()
        val_1 = value_1_input.get()
        val_2 = value_2_input.get()

        attribute_list.append((attribute, val_1, val_2))
        listbox.insert(tk.END, f"{attribute}: ( {val_1}, {val_2} )")
        clear_all_inputs()

    # Create a button to submit the input and position it using grid
    submit_button = tk.Button(window, text="Add", command=get_input)
    submit_button.grid(row=2, column=0, padx=10, pady=5)

    def clear_all_inputs():
        attribute_input.delete(0, tk.END)
        value_1_input.delete(0, tk.END)
        value_2_input.delete(0, tk.END)

    # Create a button to clear the input and position it using grid
    clear_button = tk.Button(window, text="Clear", command=clear_all_inputs)
    clear_button.grid(row=2, column=2, padx=10, pady=5)

def addConstraintElements(window, constraint_list):
    '''
    User inputs for constraints
    '''

    # Create a attribute input
    constraint_label = tk.Label(window, text="Enter the constraint:")
    constraint_label.grid(row=3, column=0, columnspan=3, padx=10, pady=5)

    constraint_input = tk.Entry(window)
    constraint_input.grid(row=4, column=0, columnspan=3, padx=10, pady=5)

    '''
    Attribuites list
    '''

    # Create a Listbox widget
    listbox = tk.Listbox(window, width=50)
    listbox.grid(row=3, column=3, rowspan=2, pady=5)

    # Creating a Scrollbar and attaching it to root window
    scrollbar = tk.Scrollbar(window)
    scrollbar.grid(row=3, column=4, rowspan=2, pady=5, sticky='ns')
    scrollbar.config(command=listbox.yview)
    listbox.config(width=0, height=4, yscrollcommand=scrollbar.set)

    # Define a function to clear all the items in the Listbox widget
    def clear_list():
        listbox.delete(0, tk.END)
        constraint_list.clear()

    # Create a Clear List button
    clear_button = tk.Button(window, text="Clear List", command=clear_list)
    clear_button.grid(row=5, column=3, padx=10, pady=5)

    '''
    Input handler buttons
    '''

    # Define a function to get the input when the button is clicked
    def get_input():
        constraint = constraint_input.get()

        constraint_list.append(constraint)
        listbox.insert(tk.END, constraint)
        clear_all_inputs()

    # Create a button to submit the input and position it using grid
    submit_button = tk.Button(window, text="Add", command=get_input)
    submit_button.grid(row=5, column=0, padx=10, pady=5)

    def clear_all_inputs():
        constraint_input.delete(0, tk.END)

    # Create a button to clear the input and position it using grid
    clear_button = tk.Button(window, text="Clear", command=clear_all_inputs)
    clear_button.grid(row=5, column=2, padx=10, pady=5)

def addPenaltyLogicElements(window, pentalty_logic_list):
    '''
    User inputs for penalty logics
    '''

    # Create a attribute input
    logic_label = tk.Label(window, text="Enter the penalty logic:")
    logic_label.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

    logic_input = tk.Entry(window)
    logic_input.grid(row=7, column=0, columnspan=2, padx=10, pady=5)

    # Create a attribute input
    value_label = tk.Label(window, text="Enter the penalty value:")
    value_label.grid(row=6, column=2, padx=10, pady=5)

    value_input = tk.Entry(window)
    value_input.grid(row=7, column=2, padx=10, pady=5)

    '''
    Attribuites list
    '''

    # Create a Listbox widget
    listbox = tk.Listbox(window, width=50)
    listbox.grid(row=6, column=3, rowspan=2, pady=5)

    # Creating a Scrollbar and attaching it to root window
    scrollbar = tk.Scrollbar(window)
    scrollbar.grid(row=6, column=4, rowspan=2, pady=5, sticky='ns')
    scrollbar.config(command=listbox.yview)
    listbox.config(width=0, height=4, yscrollcommand=scrollbar.set)

    # Define a function to clear all the items in the Listbox widget
    def clear_list():
        listbox.delete(0, tk.END)
        pentalty_logic_list.clear()

    # Create a Clear List button
    clear_button = tk.Button(window, text="Clear List", command=clear_list)
    clear_button.grid(row=8, column=3, padx=10, pady=5)

    '''
    Input handler buttons
    '''

    # Define a function to get the input when the button is clicked
    def get_input():
        value = value_input.get()
        logic = logic_input.get()

        pentalty_logic_list.append((logic, value))
        listbox.insert(tk.END, f"{logic}: {value}")
        clear_all_inputs()

    # Create a button to submit the input and position it using grid
    submit_button = tk.Button(window, text="Add", command=get_input)
    submit_button.grid(row=8, column=0, padx=10, pady=5)

    def clear_all_inputs():
        logic_input.delete(0, tk.END)
        value_input.delete(0, tk.END)

    # Create a button to clear the input and position it using grid
    clear_button = tk.Button(window, text="Clear", command=clear_all_inputs)
    clear_button.grid(row=8, column=2, padx=10, pady=5)

def addPossbilisticLogicElements(window, possbilistic_logic_list):
    '''
    User inputs for penalty logics
    '''

    # Create a attribute input
    logic_label = tk.Label(window, text="Enter the possbilistic logic:")
    logic_label.grid(row=9, column=0, columnspan=2, padx=10, pady=5)

    logic_input = tk.Entry(window)
    logic_input.grid(row=10, column=0, columnspan=2, padx=10, pady=5)

    # Create a attribute input
    value_label = tk.Label(window, text="Enter the possbilistic value:")
    value_label.grid(row=9, column=2, padx=10, pady=5)

    value_input = tk.Entry(window)
    value_input.grid(row=10, column=2, padx=10, pady=5)

    '''
    Attribuites list
    '''

    # Create a Listbox widget
    listbox = tk.Listbox(window, width=50)
    listbox.grid(row=9, column=3, rowspan=2, pady=5)

    # Creating a Scrollbar and attaching it to root window
    scrollbar = tk.Scrollbar(window)
    scrollbar.grid(row=9, column=4, rowspan=2, pady=5, sticky='ns')
    scrollbar.config(command=listbox.yview)
    listbox.config(width=0, height=4, yscrollcommand=scrollbar.set)

    # Define a function to clear all the items in the Listbox widget
    def clear_list():
        listbox.delete(0, tk.END)
        possbilistic_logic_list.clear()

    # Create a Clear List button
    clear_button = tk.Button(window, text="Clear List", command=clear_list)
    clear_button.grid(row=11, column=3, padx=10, pady=5)

    '''
    Input handler buttons
    '''

    # Define a function to get the input when the button is clicked
    def get_input():
        value = value_input.get()
        logic = logic_input.get()

        possbilistic_logic_list.append((logic, value))
        listbox.insert(tk.END, f"{logic}: {value}")
        clear_all_inputs()

    # Create a button to submit the input and position it using grid
    submit_button = tk.Button(window, text="Add", command=get_input)
    submit_button.grid(row=11, column=0, padx=10, pady=5)

    def clear_all_inputs():
        logic_input.delete(0, tk.END)
        value_input.delete(0, tk.END)

    # Create a button to clear the input and position it using grid
    clear_button = tk.Button(window, text="Clear", command=clear_all_inputs)
    clear_button.grid(row=11, column=2, padx=10, pady=5)

def addQualitativeChoiceLogicElements(window, qualitative_choice_logic_list):
    '''
    User inputs for qualitative choice logic
    '''

    # Create a attribute input
    label = tk.Label(window, text="Enter the qualitative choice logic:")
    label.grid(row=12, column=0, columnspan=3, padx=10, pady=5)

    value_input = tk.Entry(window)
    value_input.grid(row=13, column=0, columnspan=3, padx=10, pady=5)

    '''
    Attribuites list
    '''

    # Create a Listbox widget
    listbox = tk.Listbox(window, width=50)
    listbox.grid(row=12, column=3, rowspan=2, pady=5)

    # Creating a Scrollbar and attaching it to root window
    scrollbar = tk.Scrollbar(window)
    scrollbar.grid(row=12, column=4, rowspan=2, pady=5, sticky='ns')
    scrollbar.config(command=listbox.yview)
    listbox.config(width=0, height=4, yscrollcommand=scrollbar.set)

    # Define a function to clear all the items in the Listbox widget
    def clear_list():
        listbox.delete(0, tk.END)
        qualitative_choice_logic_list.clear()

    # Create a Clear List button
    clear_button = tk.Button(window, text="Clear List", command=clear_list)
    clear_button.grid(row=14, column=3, padx=10, pady=5)

    '''
    Input handler buttons
    '''

    # Define a function to get the input when the button is clicked
    def get_input():
        constraint = value_input.get()

        qualitative_choice_logic_list.append(constraint)
        listbox.insert(tk.END, constraint)
        clear_all_inputs()

    # Create a button to submit the input and position it using grid
    submit_button = tk.Button(window, text="Add", command=get_input)
    submit_button.grid(row=14, column=0, padx=10, pady=5)

    def clear_all_inputs():
        value_input.delete(0, tk.END)

    # Create a button to clear the input and position it using grid
    clear_button = tk.Button(window, text="Clear", command=clear_all_inputs)
    clear_button.grid(row=14, column=2, padx=10, pady=5)



def addFileInputElements(window, fileNames):
    '''
    File input
    '''
    def AttributeUploadAction(event=None):
        fileNames[0] = askopenfilename()
        if(len(fileNames[0]) > 30):
            shortName = "..." + fileNames[0][-30:]
            attribute_filename_label.config(text = shortName)
        else:
            attribute_filename_label.config(text = fileNames[0])

    attribute_file_button = tk.Button(window, text="Upload Attributes File", command=AttributeUploadAction)
    attribute_file_button.config(font='sans 10 bold')
    attribute_file_button.grid(row=15, column=0, padx=10, pady=0)

    attribute_filename_label = tk.Label(window, text=fileNames[0])
    attribute_filename_label.grid(row=16, column=0, padx=10, pady=0)

    def ConstraintUploadAction(event=None):
        fileNames[1] = askopenfilename()
        if(len(fileNames[1]) > 30):
            shortName = "..." + fileNames[1][-30:]
            constraint_filename_label.config(text = shortName)
        else:
            constraint_filename_label.config(text = fileNames[1])

    constraint_file_button = tk.Button(window, text="Upload Constraint File", command=ConstraintUploadAction)
    constraint_file_button.config(font='sans 10 bold')
    constraint_file_button.grid(row=15, column=2, padx=10, pady=0)

    constraint_filename_label = tk.Label(window, text=fileNames[1])
    constraint_filename_label.grid(row=16, column=2, padx=10, pady=0)      

    def PenaltyUploadAction(event=None):
        fileNames[2] = askopenfilename()
        if(len(fileNames[2]) > 30):
            shortName = "..." + fileNames[2][-30:]
            penalty_filename_label.config(text = shortName)
        else:
            penalty_filename_label.config(text = fileNames[2])

    penalty_file_button = tk.Button(window, text="Upload Penalty Logic File", command=PenaltyUploadAction)
    penalty_file_button.config(font='sans 10 bold')
    penalty_file_button.grid(row=17, column=0, padx=10, pady=0)

    penalty_filename_label = tk.Label(window, text=fileNames[2])
    penalty_filename_label.grid(row=18, column=0, padx=10, pady=0)  

    def PossbilisticUploadAction(event=None):
        fileNames[3] = askopenfilename()
        if(len(fileNames[3]) > 30):
            shortName = "..." + fileNames[3][-30:]
            possbilistic_filename_label.config(text = shortName)
        else:
            possbilistic_filename_label.config(text = fileNames[3])

    possbilistic_file_button = tk.Button(window, text="Upload Possbilistic Logic File", command=PossbilisticUploadAction)
    possbilistic_file_button.config(font='sans 10 bold')
    possbilistic_file_button.grid(row=17, column=1, padx=10, pady=0)

    possbilistic_filename_label = tk.Label(window, text=fileNames[3])
    possbilistic_filename_label.grid(row=18, column=1, padx=10, pady=0)   

    def QualitativeUploadAction(event=None):
        fileNames[4] = askopenfilename()
        if(len(fileNames[4]) > 30):
            shortName = "..." + fileNames[4][-30:]
            qualitative_filename_label.config(text = shortName)
        else:
            qualitative_filename_label.config(text = fileNames[4])

    qualitative_file_button = tk.Button(window, text="Upload Qualitative Logic File", command=QualitativeUploadAction)
    qualitative_file_button.config(font='sans 10 bold')
    qualitative_file_button.grid(row=17, column=2, padx=10, pady=0)

    qualitative_filename_label = tk.Label(window, text=fileNames[4])
    qualitative_filename_label.grid(row=18, column=2, padx=10, pady=0)   

def addSubmitElement(window, SubmitFieldsCallBack, SubmitFileCallback):
    '''
    Submit
    '''
    attribute_file_button = tk.Button(window, text="Submit Fields", command=SubmitFieldsCallBack)
    attribute_file_button.config(bg='#8888ff')
    attribute_file_button.grid(row=19, column=0, padx=10, pady=10)

    constraint_file_button = tk.Button(window, text="Submit Files", command=SubmitFileCallback)
    constraint_file_button.config(bg='#8888ff')
    constraint_file_button.grid(row=19, column=2, padx=10, pady=10)


def addResultsElements(window):
    '''
    Possibile Sets
    '''   
    # Add Listbox label
    feasible_objects_label = tk.Label(window, text="Feasible objects results")
    feasible_objects_label.config(font='sans 11 bold')
    feasible_objects_label.grid(row=0, column=5, padx=10, pady=5)

    # Create a Listbox widget
    feasible_objects_listbox = tk.Listbox(window, width=50)
    feasible_objects_listbox.grid(row=1, column=5, rowspan=5, padx=10, pady=5)

    # Creating a Scrollbar and attaching it to root window
    feasible_objects_scrollbar = tk.Scrollbar(window)
    feasible_objects_scrollbar.grid(row=1, column=6, rowspan=5, pady=5, sticky='ns')
    feasible_objects_scrollbar.config(command=feasible_objects_listbox.yview)
    feasible_objects_listbox.config(width=0, height=10, yscrollcommand=feasible_objects_scrollbar.set)

    '''
    Optimal penalty
    '''   
    # Add Listbox label
    penalty_objects_label = tk.Label(window, text="Optimal penalty objects results")
    penalty_objects_label.config(font='sans 11 bold')
    penalty_objects_label.grid(row=6, column=5, padx=10, pady=5)

    # Create a Listbox widget
    penalty_objects_listbox = tk.Listbox(window, width=50)
    penalty_objects_listbox.grid(row=7, column=5, rowspan=2, padx=10, pady=5)

    # Creating a Scrollbar and attaching it to root window
    penalty_objects_scrollbar = tk.Scrollbar(window)
    penalty_objects_scrollbar.grid(row=7, column=6, rowspan=2, pady=5, sticky='ns')
    penalty_objects_scrollbar.config(command=penalty_objects_listbox.yview)
    penalty_objects_listbox.config(width=0, height=4, yscrollcommand=penalty_objects_scrollbar.set)

    '''
    Optimal possbilistic
    '''   
    # Add Listbox label
    possbilistic_objects_label = tk.Label(window, text="Optimal possbilistic results")
    possbilistic_objects_label.config(font='sans 11 bold')
    possbilistic_objects_label.grid(row=9, column=5, padx=10, pady=5)

    # Create a Listbox widget
    possbilistic_objects_listbox = tk.Listbox(window, width=50)
    possbilistic_objects_listbox.grid(row=10, column=5, rowspan=2, padx=10, pady=5)

    # Creating a Scrollbar and attaching it to root window
    possbilistic_objects_scrollbar = tk.Scrollbar(window)
    possbilistic_objects_scrollbar.grid(row=10, column=6, rowspan=2, pady=5, sticky='ns')
    possbilistic_objects_scrollbar.config(command=possbilistic_objects_listbox.yview)
    possbilistic_objects_listbox.config(width=0, height=4, yscrollcommand=possbilistic_objects_scrollbar.set)

    '''
    Optimal qualitative choice
    '''   
    # Add Listbox label
    qualitative_choice_objects_label = tk.Label(window, text="Optimal qualitative choice results")
    qualitative_choice_objects_label.config(font='sans 11 bold')
    qualitative_choice_objects_label.grid(row=12, column=5, padx=10, pady=5)

    # Create a Listbox widget
    qualitative_choice_objects_listbox = tk.Listbox(window, width=50)
    qualitative_choice_objects_listbox.grid(row=13, column=5, rowspan=2, padx=10, pady=5)

    # Creating a Scrollbar and attaching it to root window
    qualitative_choice_objects_scrollbar = tk.Scrollbar(window)
    qualitative_choice_objects_scrollbar.grid(row=13, column=6, rowspan=2, pady=5, sticky='ns')
    qualitative_choice_objects_scrollbar.config(command=qualitative_choice_objects_listbox.yview)
    qualitative_choice_objects_listbox.config(width=0, height=4, yscrollcommand=qualitative_choice_objects_scrollbar.set)    


    def clear_list(listbox):

        def clear():
            listbox.delete(0, tk.END)

        return clear

    def add_to_list(listbox):
        
        def add(value):
            listbox.insert(tk.END, value)

        return add


    elements = [feasible_objects_listbox, penalty_objects_listbox, possbilistic_objects_listbox, qualitative_choice_objects_listbox]

    modification_functions = []

    for element in elements:
        modification_functions.append((add_to_list(element), clear_list(element)))

    return modification_functions