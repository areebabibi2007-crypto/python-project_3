# 🔐 Random Password Generator

## 👩‍💻 Author

*Student Name:* Areeba Bibi  
*Course:* Python Programming  
*Project:* Project 3 – Random Password Generator  
*Batch:* 2026  

---

# 📌 Project Overview

The *Random Password Generator* is a Python-based application that generates secure and random passwords. The user enters the desired password length, and the application creates a strong password using uppercase letters, lowercase letters, numbers, and special characters.

This project is developed to practice Python modules, string manipulation, input validation, and modular programming.

---

# 🎯 Objectives

- Learn how to use Python built-in modules.
- Understand random password generation.
- Practice string manipulation.
- Validate user input.
- Create a modular Python project.
- Improve problem-solving skills.

---

# ✨ Features

- User-friendly interface.
- Accepts password length from the user.
- Validates user input.
- Generates secure random passwords.
- Uses uppercase letters (A-Z).
- Uses lowercase letters (a-z).
- Uses digits (0-9).
- Uses special characters (!@#$%^&*).
- Handles invalid input using exception handling.
- Modular project structure.

---

# 🛠️ Technologies Used

- Python 3.x
- random module
- string module

---

# 📂 Project Structure


Random_Password_Generator/
│
├── assets/
│
├── src/
│   ├── __init__.py
│   ├── password_generator.py
│   └── validator.py
│
├── main.py
├── README.md
├── requirements.txt
├── LICENSE
└── .gitignore


---

# 📄 File Description

### main.py
The main file that starts the application and manages user interaction.

### password_generator.py
Contains the logic for generating secure random passwords.

### validator.py
Validates the password length entered by the user.

### README.md
Contains the complete project documentation.

### requirements.txt
Lists all required dependencies.

### LICENSE
Contains the MIT License information.

### .gitignore
Ignores unnecessary Python cache files and IDE configuration files.

---

# ▶️ How to Run

1. Open the project folder.
2. Open Terminal or Command Prompt.
3. Navigate to the project directory.
4. Run the following command:

bash
python main.py


---

# 💻 Sample Output 1 (Valid Input)


==================================================
          RANDOM PASSWORD GENERATOR
==================================================

Enter Password Length (6-50): 12

--------------------------------------------------
Generated Password
--------------------------------------------------
K@8mP#2xL!9Q
--------------------------------------------------

Thank you for using Random Password Generator!


---

# 💻 Sample Output 2 (Another Valid Input)


==================================================
          RANDOM PASSWORD GENERATOR
==================================================

Enter Password Length (6-50): 16

--------------------------------------------------
Generated Password
--------------------------------------------------
Y$7qN@2Lp#8Xv!4M
--------------------------------------------------

Thank you for using Random Password Generator!


---

# ❌ Sample Output (Password Too Short)


==================================================
          RANDOM PASSWORD GENERATOR
==================================================

Enter Password Length (6-50): 4

Error: Password length must be at least 6.

Enter Password Length (6-50):


---

# ❌ Sample Output (Password Too Long)


==================================================
          RANDOM PASSWORD GENERATOR
==================================================

Enter Password Length (6-50): 70

Error: Password length cannot exceed 50.

Enter Password Length (6-50):


---

# ❌ Sample Output (Invalid Input)


==================================================
          RANDOM PASSWORD GENERATOR
==================================================

Enter Password Length (6-50): abc

Please enter a valid number.

Enter Password Length (6-50):


---

# 📚 Modules Used

- random
- string

---

# 🚀 Future Improvements

- Add a password strength meter.
- Allow users to choose whether to include special characters.
- Allow users to include or exclude numbers.
- Save generated passwords to a text file.
- Add a graphical user interface (GUI) using Tkinter.
- Add a copy-to-clipboard feature.

---

# 📖 Learning Outcomes

After completing this project, you will be able to:

- Import and use Python modules.
- Generate random data.
- Perform string manipulation.
- Validate user input.
- Use loops and functions effectively.
- Organize code into multiple modules.
- Build a professional Python project.

---

# 📜 License

This project is licensed under the MIT License.

---

# 🙏 Acknowledgement

This project was developed as part of the *Python Programming Industrial Training (Project 3)* to enhance programming skills, understand Python modules, and practice real-world project development.

---

## ⭐ Thank You

*Created by:* *Areeba Bibi*

*Project:* Random Password Generator

*Language:* Python 3

*Batch:* 2026