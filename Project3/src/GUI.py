import tkinter as tk
import WindowElements as we

class GUI:

    def __init__(self, attribute_list, constraint_list, pentalty_logic_list, possbilistic_logic_list, qualitative_choice_logic_list, file_name_list, SubmitFieldsCallBack, SubmitFileCallBack, gui_results_list):
        '''
        Super variables
        '''
        WINDOW_WIDTH_PX = "1100"
        WINDOW_HEIGHT_PX = "800"

        '''
        Setup Variables
        '''
        self.attribute_list = attribute_list  # Looks like: [ (Attr1, val1, val2), (Attr2, val1, val2), (Attr3, val1, val2) ]
        self.constraint_list = constraint_list  # Looks like: [ const1, const2 ]
        self.pentalty_logic_list = pentalty_logic_list  # Looks like: [ (logic1, value1), (logic2, value2) ]
        self.possbilistic_logic_list = possbilistic_logic_list  # Looks like: [ (logic1, value1), (logic2, value2) ]
        self.qualitative_choice_logic_list = qualitative_choice_logic_list  # Looks like: [ logic1, logic1 ]

        # The order of the list from 0 to 4 is as follows:
        # Attributes, constraint, pentalty, possbilistic, qualitative
        self.file_name_list = file_name_list # Looks like: [ "C:/Users/Alex/Desktop/Attributes.txt", "C:/Users/Alex/Desktop/Constraint.txt", ... ]

        '''
        Window setup
        '''
        window = tk.Tk() # Create a new window
        window.title("AI Project 3") # Set the title of the window
        window.geometry( WINDOW_WIDTH_PX + "x" + WINDOW_HEIGHT_PX ) # Set the size of the window

        '''
        Window Elements
        '''
        we.addAttributeElements(window, attribute_list)
        we.addConstraintElements(window, constraint_list)
        we.addPenaltyLogicElements(window, pentalty_logic_list)
        we.addPossbilisticLogicElements(window, possbilistic_logic_list)
        we.addQualitativeChoiceLogicElements(window, qualitative_choice_logic_list)
        result_modification_functions = we.addResultsElements(window)
        we.addFileInputElements(window, file_name_list)

        def SubmitFields():
            SubmitFieldsCallBack()

            #Clear all existing elements
            for i in range(len(result_modification_functions)):
                result_modification_functions[i][1]()

            for feaseableElement in gui_results_list[0]:
                result_modification_functions[0][0](feaseableElement)

            for penaltyOptimal in gui_results_list[1]:
                result_modification_functions[1][0](penaltyOptimal)

            for possibililisticOptimal in gui_results_list[2]:
                result_modification_functions[2][0](possibililisticOptimal)

            for choiceOptimal in gui_results_list[3]:
                result_modification_functions[3][0](choiceOptimal)

        def SubmitFiles():
            SubmitFileCallBack()

            #Clear all existing elements
            for i in range(len(result_modification_functions)):
                result_modification_functions[i][1]()

            for feaseableElement in gui_results_list[0]:
                result_modification_functions[0][0](feaseableElement)

            for penaltyOptimal in gui_results_list[1]:
                result_modification_functions[1][0](penaltyOptimal)

            for possibililisticOptimal in gui_results_list[2]:
                result_modification_functions[2][0](possibililisticOptimal)

            """
            for choiceOptimal in gui_results_list[3]:
                result_modification_functions[3][0](choiceOptimal)
            """

        we.addSubmitElement(window, SubmitFields, SubmitFiles)

        '''
        Main loop runner
        '''
        # Run the main event loop
        window.mainloop()


if __name__ == "__main__":
    attribute_list = []
    constraint_list = []
    penalty_logic_list = []
    possbilistic_logic_list = []
    qualitative_choice_logic_list = []
    file_name_list = ["" for i in range(5)]
    def SubmitFields():
        print("User Submitted Fields")
    def SubmitFiles():
        print("User Submitted Files")


    gui = GUI(attribute_list, constraint_list, penalty_logic_list, possbilistic_logic_list, qualitative_choice_logic_list, file_name_list, SubmitFields, SubmitFiles, [])