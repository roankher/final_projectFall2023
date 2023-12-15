import tkinter as tk

def on_stats_button_click():
    label.config(text="Stats!", font=border_font, bg="White")
    projections_button.place(x=150, y=100)
    stats_button.place_forget()
    create_fantasy_boxes()  # Create fantasy boxes
    label.after(3000, reset_label_text2)
    show_search_bar()

def reset_label_text2():
    label.config(text="Welcome to Team Statistics", bg="white")

def on_projections_button_click():
    label.config(text="Projections", font=border_font, bg="white")
    stats_button.place(x=50, y=100)
    projections_button.place_forget()
    create_projection_boxes()  # Create projection boxes
    label.after(3000, reset_label_text)
    show_search_bar()

def reset_label_text():
    label.config(text="Welcome to Projections!", bg="white")

def show_search_bar():
    search_entry.place(x=800, y=50)
    search_entry.delete(0, tk.END)  # Clear the search entry
    clear_button.place_forget()  # Hide the clear button
teams = []
def handle_search_entry(event):
    search_text = search_entry.get()
    names = search_text.split(",")
    if len(names) == 2:
        team1_name, team2_name = names[0].strip(), names[1].strip()
        team_names_label.config(text=f"{team1_name} vs {team2_name}")
        clear_button.place(x=800, y=100)  # Show the clear button
        for i in teams:
            if i['Team'] == team1_name:
                update_values_in_window(i, row=2)
            elif i['Team'] == team2_name:
                update_values_in_window(i, row=3)

def update_values_in_window(team_data, row):
    for idx, key in enumerate(['PPG/F', 'Pass TD/F', 'Rush TD/F', 'FGM/F',
                               'PPG/A', 'Pass TD/A', 'Rush TD/A', 'FGM/A']):
        boxes[row][idx].config(text=f"{key}: {team_data[key]}")

def clear_values():
    for box_row in boxes:
        for box in box_row:
            box.config(text="")

def create_fantasy_boxes():
    destroy_all_boxes()  # Clear all boxes
    box_texts = ["Points", "Passing", "Rushing", "FG", "Points Allowed", "Pass TD Allowed", "Rush TD Allowed", "Field Goals"]
    for i, text in enumerate(box_texts):
        box = tk.Label(window, text=text, font=button_font, bg="light gray", width=15, height=2)
        box.place(x=50, y=200 + i * 50)
        boxes.append(box)

def create_projection_boxes():
    destroy_all_boxes()  # Clear all boxes
    projectionsbox_texts = ["PredictedPoints", "PredictedPassing", "PredictedRushing", "PredictedFG", "PredictedPoints Allowed", "PredictedPass TD Allowed", "PredictedRush TD Allowed", "PredictedField Goals"]
    for i, text in enumerate(projectionsbox_texts):
        projectionsbox = tk.Label(window, text=text, font=button_font, bg="light gray", width=25, height=2)
        projectionsbox.place(x=50, y=200 + i * 50)
        boxes.append(projectionsbox)

def destroy_all_boxes():
    for box in boxes:
        box.destroy()
    boxes.clear()

window = tk.Tk()
window.title("My Python Window")
window.geometry("1000x800")
window.configure(bg="white")

button_font = ("Times New Roman", 12, "bold")
border_font = ("Times New Roman", 24, "bold")

stats_button = tk.Button(window, text="Stats", command=on_stats_button_click, font=button_font, width=10, height=3, bg="light blue")
stats_button.place(x=50, y=100)

projections_button = tk.Button(window, text="Projections", command=on_projections_button_click, font=button_font, width=10, height=3, bg="light green")
projections_button.place(x=150, y=100)

label = tk.Label(window, text="Welcome to our website", bg="light blue")
label.pack()

search_entry = tk.Entry(window, width=20, font=button_font)
search_entry.bind("<Return>", handle_search_entry)  # Bind the Enter key event

clear_button = tk.Button(window, text="Clear", command=clear_values, font=button_font, width=10, height=3, bg="light coral")

team_names_label = tk.Label(window, text="", font=("Arial", 14))
team_names_label.pack()

# Create labels for displaying values
boxes = []
for i in range(4):
    row = []
    for j in range(8):
        box = tk.Label(window, text="", font=button_font, bg="light gray", width=25, height=2)
        box.grid(row=i + 2, column=j, padx=10, pady=5, sticky="w")
        row.append(box)
    boxes.append(row)



arizona = {
    'Team': 'Arizona',
    'PPG/F': 17.2,
    'Pass TD/F': 0.8,
    'Rush TD/F': 0.9,
    'FGM/F': 1.6,
    'PPG/A': 26.8,
    'Pass TD/A': 1.8,
    'Rush TD/A': 1.3,
    'FGM/A': 1.6
}

atlanta = {
    'Team': 'Atlanta',
    'PPG/F': 19.4,
    'Pass TD/F': 0.9,
    'Rush TD/F': 0.9,
    'FGM/F': 2.0,
    'PPG/A': 21.1,
    'Pass TD/A': 1.5,
    'Rush TD/A': 0.4,
    'FGM/A': 2.4
}

baltimore = {
    'Team': 'Baltimore',
    'PPG/F': 27.0,
    'Pass TD/F': 1.2,
    'Rush TD/F': 1.8,
    'FGM/F': 1.8,
    'PPG/A': 15.6,
    'Pass TD/A': 0.8,
    'Rush TD/A': 0.3,
    'FGM/A': 2.1
}

buffalo = {
    'Team': 'Buffalo',
    'PPG/F': 27.3,
    'Pass TD/F': 2.0,
    'Rush TD/F': 1.2,
    'FGM/F': 1.5,
    'PPG/A': 18.9,
    'Pass TD/A': 1.3,
    'Rush TD/A': 0.7,
    'FGM/A': 1.6
}

carolina = {
    'Team': 'Carolina',
    'PPG/F': 15.7,
    'Pass TD/F': 1.0,
    'Rush TD/F': 0.3,
    'FGM/F': 1.6,
    'PPG/A': 26.5,
    'Pass TD/A': 1.2,
    'Rush TD/A': 1.6,
    'FGM/A': 1.5
}

chicago = {
    'Team': 'Chicago',
    'PPG/F': 20.2,
    'Pass TD/F': 1.3,
    'Rush TD/F': 0.8,
    'FGM/F': 1.9,
    'PPG/A': 24.7,
    'Pass TD/A': 1.9,
    'Rush TD/A': 0.5,
    'FGM/A': 1.6
}

cincinnati = {
    'Team': 'Cincinnati',
    'PPG/F': 19.3,
    'Pass TD/F': 1.5,
    'Rush TD/F': 0.4,
    'FGM/F': 1.5,
    'PPG/A': 22.0,
    'Pass TD/A': 1.2,
    'Rush TD/A': 1.1,
    'FGM/A': 2.0
}

cleveland = {
    'Team': 'Cleveland',
    'PPG/F': 21.7,
    'Pass TD/F': 0.8,
    'Rush TD/F': 1.0,
    'FGM/F': 2.5,
    'PPG/A': 19.0,
    'Pass TD/A': 0.9,
    'Rush TD/A': 1.1,
    'FGM/A': 1.0
}

dallas = {
    'Team': 'Dallas',
    'PPG/F': 31.5,
    'Pass TD/F': 2.1,
    'Rush TD/F': 0.9,
    'FGM/F': 2.0,
    'PPG/A': 16.8,
    'Pass TD/A': 1.3,
    'Rush TD/A': 0.7,
    'FGM/A': 1.0
}

denver = {
    'Team': 'Denver',
    'PPG/F': 22.4,
    'Pass TD/F': 1.8,
    'Rush TD/F': 0.3,
    'FGM/F': 2.2,
    'PPG/A': 25.5,
    'Pass TD/A': 1.7,
    'Rush TD/A': 1.0,
    'FGM/A': 1.8
}

detroit = {
    'Team': 'Detroit',
    'PPG/F': 26.7,
    'Pass TD/F': 1.6,
    'Rush TD/F': 1.5,
    'FGM/F': 1.2,
    'PPG/A': 23.5,
    'Pass TD/A': 1.7,
    'Rush TD/A': 0.7,
    'FGM/A': 1.5
}

green_bay = {
    'Team': 'Green Bay',
    'PPG/F': 21.0,
    'Pass TD/F': 1.7,
    'Rush TD/F': 0.5,
    'FGM/F': 1.4,
    'PPG/A': 20.4,
    'Pass TD/A': 1.1,
    'Rush TD/A': 0.9,
    'FGM/A': 1.9
}

houston = {
    'Team': 'Houston',
    'PPG/F': 23.5,
    'Pass TD/F': 1.8,
    'Rush TD/F': 0.6,
    'FGM/F': 2.0,
    'PPG/A': 21.1,
    'Pass TD/A': 1.0,
    'Rush TD/A': 1.2,
    'FGM/A': 1.9
}

indianapolis = {
    'Team': 'Indianapolis',
    'PPG/F': 24.5,
    'Pass TD/F': 1.0,
    'Rush TD/F': 1.5,
    'FGM/F': 1.7,
    'PPG/A': 24.4,
    'Pass TD/A': 1.1,
    'Rush TD/A': 1.4,
    'FGM/A': 2.2
}

jacksonville = {
    'Team': 'Jacksonville',
    'PPG/F': 23.1,
    'Pass TD/F': 1.1,
    'Rush TD/F': 1.1,
    'FGM/F': 2.1,
    'PPG/A': 20.5,
    'Pass TD/A': 1.6,
    'Rush TD/A': 0.6,
    'FGM/A': 1.1
}

kansas_city = {
    'Team': 'Kansas City',
    'PPG/F': 23.3,
    'Pass TD/F': 1.9,
    'Rush TD/F': 0.5,
    'FGM/F': 1.8,
    'PPG/A': 16.5,
    'Pass TD/A': 1.2,
    'Rush TD/A': 0.6,
    'FGM/A': 0.9
}

la_chargers = {
    'Team': 'LA Chargers',
    'PPG/F': 24.5,
    'Pass TD/F': 1.9,
    'Rush TD/F': 0.8,
    'FGM/F': 1.5,
    'PPG/A': 23.5,
    'Pass TD/A': 1.5,
    'Rush TD/A': 1.2,
    'FGM/A': 1.5
}

la_rams = {
    'Team': 'LA Rams',
    'PPG/F': 21.1,
    'Pass TD/F': 1.2,
    'Rush TD/F': 1.0,
    'FGM/F': 2.0,
    'PPG/A': 21.3,
    'Pass TD/A': 1.0,
    'Rush TD/A': 1.0,
    'FGM/A': 2.1
}

las_vegas = {
    'Team': 'Las Vegas',
    'PPG/F': 16.8,
    'Pass TD/F': 0.9,
    'Rush TD/F': 0.7,
    'FGM/F': 1.7,
    'PPG/A': 21.3,
    'Pass TD/A': 1.3,
    'Rush TD/A': 1.0,
    'FGM/A': 1.8
}

miami = {
    'Team': 'Miami',
    'PPG/F': 30.8,
    'Pass TD/F': 2.1,
    'Rush TD/F': 1.7,
    'FGM/F': 1.0,
    'PPG/A': 22.8,
    'Pass TD/A': 1.5,
    'Rush TD/A': 0.8,
    'FGM/A': 1.3
}

minnesota = {
    'Team': 'Minnesota',
    'PPG/F': 21.9,
    'Pass TD/F': 1.9,
    'Rush TD/F': 0.4,
    'FGM/F': 1.5,
    'PPG/A': 20.2,
    'Pass TD/A': 1.3,
    'Rush TD/A': 0.6,
    'FGM/A': 2.2
}

new_england = {
    'Team': 'New England',
    'PPG/F': 13.5,
    'Pass TD/F': 0.9,
    'Rush TD/F': 0.5,
    'FGM/F': 1.1,
    'PPG/A': 22.5,
    'Pass TD/A': 1.2,
    'Rush TD/A': 0.8,
    'FGM/A': 1.9
}

new_orleans = {
    'Team': 'New Orleans',
    'PPG/F': 20.8,
    'Pass TD/F': 1.2,
    'Rush TD/F': 0.6,
    'FGM/F': 2.2,
    'PPG/A': 20.2,
    'Pass TD/A': 1.3,
    'Rush TD/A': 0.6,
    'FGM/A': 1.8
}

ny_giants = {
    'Team': 'NY Giants',
    'PPG/F': 13.3,
    'Pass TD/F': 0.9,
    'Rush TD/F': 0.3,
    'FGM/F': 1.2,
    'PPG/A': 24.3,
    'Pass TD/A': 1.2,
    'Rush TD/A': 1.5,
    'FGM/A': 1.3
}

ny_jets = {
    'Team': 'NY Jets',
    'PPG/F': 14.8,
    'Pass TD/F': 0.6,
    'Rush TD/F': 0.3,
    'FGM/F': 2.1,
    'PPG/A': 21.6,
    'Pass TD/A': 1.2,
    'Rush TD/A': 0.6,
    'FGM/A': 2.5
}

philadelphia = {
    'Team': 'Philadelphia',
    'PPG/F': 28.2,
    'Pass TD/F': 1.6,
    'Rush TD/F': 1.5,
    'FGM/F': 1.7,
    'PPG/A': 22.4,
    'Pass TD/A': 2.1,
    'Rush TD/A': 0.5,
    'FGM/A': 1.1
}

pittsburgh = {
    'Team': 'Pittsburgh',
    'PPG/F': 16.5,
    'Pass TD/F': 0.6,
    'Rush TD/F': 0.7,
    'FGM/F': 1.9,
    'PPG/A': 18.6,
    'Pass TD/A': 1.2,
    'Rush TD/A': 0.5,
    'FGM/A': 2.1
}

san_francisco = {
    'Team': 'San Francisco',
    'PPG/F': 28.2,
    'Pass TD/F': 1.7,
    'Rush TD/F': 1.6,
    'FGM/F': 1.5,
    'PPG/A': 15.5,
    'Pass TD/A': 1.0,
    'Rush TD/A': 0.5,
    'FGM/A': 1.6
}

seattle = {
    'Team': 'Seattle',
    'PPG/F': 20.8,
    'Pass TD/F': 1.1,
    'Rush TD/F': 0.6,
    'FGM/F': 2.3,
    'PPG/A': 22.6,
    'Pass TD/A': 1.3,
    'Rush TD/A': 1.3,
    'FGM/A': 1.6
}

tampa_bay = {
    'Team': 'Tampa Bay',
    'PPG/F': 19.3,
    'Pass TD/F': 1.5,
    'Rush TD/F': 0.4,
    'FGM/F': 1.7,
    'PPG/A': 20.6,
    'Pass TD/A': 1.5,
    'Rush TD/A': 0.6,
    'FGM/A': 2.0
}

tennessee = {
    'Team': 'Tennessee',
    'PPG/F': 16.8,
    'Pass TD/F': 0.8,
    'Rush TD/F': 0.7,
    'FGM/F': 2.0,
    'PPG/A': 20.4,
    'Pass TD/A': 1.1,
    'Rush TD/A': 0.7,
    'FGM/A': 2.5
}

washington = {
    'Team': 'Washington',
    'PPG/F': 20.5,
    'Pass TD/F': 1.5,
    'Rush TD/F': 0.8,
    'FGM/F': 1.4,
    'PPG/A': 29.2,
    'Pass TD/A': 2.3,
    'Rush TD/A': 0.6,
    'FGM/A': 2.2
}




teams.append(arizona)
teams.append(atlanta)
teams.append(baltimore)
teams.append(buffalo)
teams.append(carolina)
teams.append(chicago)
teams.append(cincinnati)
teams.append(cleveland)
teams.append(dallas)
teams.append(denver)
teams.append(detroit)
teams.append(green_bay)
teams.append(houston)
teams.append(indianapolis)
teams.append(jacksonville)
teams.append(kansas_city)
teams.append(la_chargers)
teams.append(la_rams)
teams.append(las_vegas)
teams.append(miami)
teams.append(minnesota)
teams.append(new_england)
teams.append(new_orleans)
teams.append(ny_giants)
teams.append(ny_jets)
teams.append(philadelphia)
teams.append(pittsburgh)
teams.append(san_francisco)
teams.append(seattle)
teams.append(tampa_bay)
teams.append(tennessee)
teams.append(washington)



window.mainloop()
