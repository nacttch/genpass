# 🔐 Advanced Password Generator

A powerful and user-friendly Python application that generates thousands of personalized passwords based on your personal information. Created by **nactch**.
## 🖼️ Screenshot



## 🌟 Features

- **Massive Password Generation**: Create hundreds or thousands of unique password combinations
- **Personalized Passwords**: Generate passwords based on your personal information (name, birthdate, favorites, etc.)
- **Smart Combinations**: Automatically combines different pieces of information in various formats
- **Customizable Options**: 
  - Set the number of passwords to generate
  - Control maximum password length
  - Add special characters and numbers
- **Beautiful Dark Theme**: Modern, eye-friendly interface
- **Export Functionality**: Save generated passwords to a text file
- **Real-time Progress**: Visual progress indicator during generation
- **Password Counter**: Track how many passwords were generated

## 🚀 Quick Start

### Prerequisites

- Python 3.6 or higher
- tkinter (usually comes with Python)

### Installation

1. **Download the script**:
   ```bash
   # Save the Python code as 'password_generator.py'
   ```

2. **Run the application**:
   ```bash
   python password_generator.py
   ```

### No Additional Dependencies Required!

This tool uses only Python's built-in libraries:
- `tkinter` for the GUI
- `random` for password generation
- `itertools` for combinations

## 📋 How to Use

### Step 1: Enter Your Information
Fill in any combination of these fields:
- **Personal Details**: First name, last name, birth date (day, month, year)
- **Favorites**: Number, animal, color, food, sport, movie, music, car, book
- **Other**: City, country, hobby, pet name, nickname, childhood hero

### Step 2: Configure Options
- **Number of passwords**: How many passwords to generate (default: 500)
- **Max password length**: Maximum characters per password (default: 20)
- **Add special characters**: Include !, @, #, $, etc.
- **Add numbers**: Append random numbers to passwords

### Step 3: Generate Passwords
Click the **"✨ Generate Passwords"** button to create your personalized password list.

### Step 4: Save Results
Use **"💾 Save to File"** to export your passwords to a text file.

## 🎯 What Information to Provide

### Essential Fields (Highly Recommended):
- First Name
- Last Name  
- Birth Year
- Favorite Number

### Additional Fields (More Data = Better Passwords):
- Birth Month & Day
- Favorite Animal, Color, Food
- City, Country
- Hobbies and Interests
- Pet Name
- Nickname

## 🔧 How It Works

The generator creates passwords by:

1. **Combining your information** in different patterns:
   - `name + year` → `john2023`
   - `year + name` → `2023john`
   - `name.lastname` → `john.doe`
   - `name_year` → `john_2023`

2. **Adding variations**:
   - Upper/lower case combinations
   - Special character substitutions (leet speak)
   - Random number additions
   - Special character prefixes/suffixes

3. **Ensuring uniqueness** by removing duplicates

## 💡 Example Output

Based on input: `John`, `Doe`, `1990`, `15`

The generator creates passwords like:
```
john1990
1990john
john.1990
john_1990
johndoe
doejohn
john15
15john
John1990
JOHN1990
j0hn1990
john1990!
1990john15
```

## ⚠️ Important Security Notes

### 🔒 For Educational & Personal Use
- This tool is designed for **educational purposes** and **personal use**
- **Do not use** generated passwords for important accounts (email, banking, etc.)
- The passwords are based on personal information that might be guessable

### 🛡️ Password Security Best Practices
- Use a **password manager** for important accounts
- Enable **two-factor authentication** whenever possible
- Use **unique passwords** for different services
- Consider using **passphrases** instead of complex passwords

## 🐛 Troubleshooting

### Common Issues:

1. **Application won't start**
   - Ensure you have Python installed
   - Check that tkinter is available (it's included in most Python installations)

2. **No passwords generated**
   - Make sure you've entered at least one piece of information
   - Check that the number of passwords is greater than 0

3. **Passwords too similar**
   - Provide more diverse information in the input fields
   - Enable "Add special characters" and "Add numbers" options

## 📁 File Structure

```
password_generator/
├── password_generator.py  # Main application file
├── generated_passwords.txt # Example output file (created after save)
└── README.md              # This documentation
```

## 🎨 Customization

You can easily modify the script to:

- Add new input fields (edit the `input_fields` list)
- Change the color scheme (modify the color codes)
- Add new password generation patterns (update `generate_combinations` method)
- Adjust complexity options (modify `add_complexity` method)

## 🤝 Contributing

Feel free to:
- Report bugs and issues
- Suggest new features
- Submit pull requests
- Share your modifications

## 📄 License

This project is open source and available under the MIT License.

## 👨‍💻 About the Developer

**nactch** - Passionate about creating useful tools that make digital life easier and more secure.

---

### 💬 Need Help?

If you have any questions or run into issues:
1. Check this README first
2. Ensure you're using a supported Python version
3. Verify all input fields are correctly filled

**Happy Password Generating! 🎉**
