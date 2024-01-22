# America's States in the order they joined the Union
usa_states = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

print("Type a number to see the American state, and it must be in the order it joined the Union!")
while True:
    n = int(input("Please enter the number corresponding to the American state you'd like to see:"))
    if 1 <= n <= 50:
        print(f"The state you requested state is: {usa_states[n-1]}.")
        break
    else:
        print(f"Invalid input. Please, enter a number between 1 and 50!")
