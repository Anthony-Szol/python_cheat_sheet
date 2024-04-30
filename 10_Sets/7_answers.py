# Follow the instructions of Hogwarts enrollment

dark_arts = {"Harry", "Ron", "Neville", "Ginny"}
potions = {"Dean", "Ginny", "Draco", "Hermione"}

# Nellive wants to enroll in potions
potions.add("Nellive")

# Ginny wants to drop potions
potions.remove("Ginny")

# Cedric wants to enroll in dark arts
dark_arts.add("Cedric")

# Are there any students in both classes? There should not be. 
dark_arts.intersection(potions)