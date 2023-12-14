#STEP ONE: prompt user for input on an ingredient that they like

#importing packages
import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd 

# Create the main application window
root = tk.Tk()
root.title("Choose An Ingredient You Like")
root.geometry("400x300")

# Create a StringVar to hold the selected option
selected_option = tk.StringVar()

# Add a label
label = tk.Label(root, text="Select an ingredient you like:")
label.pack(pady=10)

# Create the dropdown menu
dropdown = tk.OptionMenu(root, selected_option, "vanilla extract", 
	"granulated sugar", "ground cinnamon", "freshly ground pepper", 
	"sour cream", "canola oil", "lemon juice", "baking soda", "chicken stock",
	"whole milk", "fresh parsley", "ground cumin", "chicken broth", 
	"pure vanilla extract", "light brown sugar")
dropdown.pack()

# Run the main event loop
#root.mainloop()

#yay! that is step one.

#STEP TWO: Create an exit button

show_button = tk.Button(root, text="Submit", 
	command=root.destroy)
show_button.pack()
root.mainloop()


#STEP THREE: read in apriori rules involving those ingredients


df = pd.read_csv(r'C:\Users\arthu\OneDrive\letsgo.csv')

#df = pd.DataFrame(data, columns=['ingredient1', 'ingredient2', 'ingredient3'])


#STEP FOUR: show apriori rules for user input 


user_input1 = selected_option.get()
    
value1 = user_input1



print(df[df['FirstIngredient'] == value1])

