import tkinter as tk

class GUI:

    def __init__(self, predict):
        '''
        Super variables
        '''
        WINDOW_WIDTH_PX = "500"
        WINDOW_HEIGHT_PX = "200"

        '''
        Window setup
        '''
        window = tk.Tk() # Create a new window
        window.title("AI Project 4") # Set the title of the window
        window.geometry( WINDOW_WIDTH_PX + "x" + WINDOW_HEIGHT_PX ) # Set the size of the window

        '''
        Window Elements
        '''
        # Create a review input
        review_label = tk.Label(window, text="Enter the review:")
        review_label.grid(row=0, column=0, columnspan=2, padx=10, pady=5)

        review_input = tk.Entry(window)
        review_input.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

        '''
        Results
        '''
        review_label = tk.Label(window, text="Prediction Here")
        review_label.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

        '''
        Input handler buttons
        '''
        # Define a function to get the input when the button is clicked
        def get_input():
            review = review_input.get()
            review_label.config(text = "Predicting..")

            prediction = predict([review])

            review_label.config(text = prediction)

        # Create a button to submit the input and position it using grid
        submit_button = tk.Button(window, text="Submit", command=get_input)
        submit_button.grid(row=2, column=0, padx=10, pady=5)

        def clear_all_inputs():
            review_input.delete(0, tk.END)

        # Create a button to clear the input and position it using grid
        clear_button = tk.Button(window, text="Clear", command=clear_all_inputs)
        clear_button.grid(row=2, column=1, padx=10, pady=5)

        '''
        Main loop runner
        '''
        # Run the main event loop
        window.mainloop()


if __name__ == "__main__":
    gui = GUI()