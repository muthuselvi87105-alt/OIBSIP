
# 🔐 Random Password Generator

## 📌 Project Description

The Random Password Generator is a Python application that generates strong and secure random passwords based on the length entered by the user. It uses letters, numbers, and special characters to create secure passwords.

---

## 🚀 Features

- User enters the password length
- Generates a random password
- Uses uppercase letters
- Uses lowercase letters
- Uses numbers
- Uses special characters
- Handles invalid input
- Prevents zero or negative password lengths

---

## 🛠️ Technologies Used

- Python
- random module
- string module

---

## 📂 Project Structure

```
Random_Password_Generator/
│── password_generator.py
│── README.md
│── screenshots/
```

---

## ▶️ Run the Project

```bash
python password_generator.py
```

---

## 📸 Sample Output

```
Enter password length: 10

Generated Password:
aB8@kP1#xQ
```

---

## 📚 Python Modules Used

- random
- string

---

## 📝 How It Works

1. The user enters the desired password length.
2. The program combines:
   - Uppercase letters
   - Lowercase letters
   - Digits
   - Special characters
3. It randomly selects characters using `random.choice()`.
4. The generated password is displayed.

---

## ⚠️ Error Handling

- Displays a message if the user enters text instead of a number.
- Displays a message if the password length is zero or negative.

Example:

```
Enter password length: abc

Please enter numbers only.
```

```
Enter password length: -5

Password length must be greater than 0.
```

---

## 📷 Screenshots

Add screenshots of:

- Successful password generation
- Invalid input (letters)
- Negative input
- Different password lengths

---

## 🔮 Future Improvements

- Copy password to clipboard
- Password strength indicator
- Option to exclude special characters
- Save generated passwords to a file
- GUI version using Tkinter

---

## 👩‍💻 Author

**Muthuselvi**

Python Developer | Full Stack Python Learner

---

## ⭐ Internship Project

This project was developed as part of the **Oasis Infobyte Python Programming Internship**
