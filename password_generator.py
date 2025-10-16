import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import random
import itertools

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Password Generator")
        self.root.geometry("750x800")
        self.root.configure(bg='#2C3E50')
        self.root.resizable(True, True)
        
        # Style configuration
        self.style = ttk.Style()
        self.style.configure('TFrame', background='#2C3E50')
        self.style.configure('TLabel', background='#2C3E50', foreground='white', font=('Arial', 10))
        self.style.configure('TButton', font=('Arial', 10, 'bold'))
        self.style.configure('Header.TLabel', font=('Arial', 18, 'bold'), foreground='#3498DB')
        self.style.configure('Custom.TButton', background='#3498DB', foreground='white')
        
        self.data = {}
        self.create_widgets()
    
    def create_widgets(self):
        # Header
        header_frame = ttk.Frame(self.root)
        header_frame.pack(fill=tk.X, padx=20, pady=15)
        
        title_label = ttk.Label(header_frame, text="🔐 Advanced Password Generator", style='Header.TLabel')
        title_label.pack()
        
        subtitle_label = ttk.Label(header_frame, text="Create thousands of passwords based on your personal information, by nactch", 
                                  font=('Arial', 11), foreground='#BDC3C7')
        subtitle_label.pack(pady=5)
        
        # Main container
        main_container = ttk.Frame(self.root)
        main_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        # Left frame for inputs
        left_frame = ttk.Frame(main_container)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))
        
        # Right frame for results
        right_frame = ttk.Frame(main_container)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(10, 0))
        
        # Input fields
        input_fields = [
            ("First Name", "first_name"),
            ("Last Name", "last_name"),
            ("Birth Day", "birth_day"),
            ("Birth Month", "birth_month"), 
            ("Birth Year", "birth_year"),
            ("Favorite Number", "fav_number"),
            ("Favorite Animal", "fav_animal"),
            ("Favorite Color", "fav_color"),
            ("Favorite Food", "fav_food"),
            ("City", "city"),
            ("Country", "country"),
            ("Hobby", "hobby"),
            ("Favorite Sport", "fav_sport"),
            ("Favorite Movie", "fav_movie"),
            ("Favorite Music", "fav_music"),
            ("Pet Name", "pet_name"),
            ("Favorite Car", "fav_car"),
            ("Favorite Book", "fav_book"),
            ("Nickname", "nickname"),
            ("Childhood Hero", "childhood_hero"),
        ]
        
        self.entries = {}
        for i, (label_text, field_name) in enumerate(input_fields):
            frame = ttk.Frame(left_frame)
            frame.pack(fill=tk.X, pady=3)
            
            label = ttk.Label(frame, text=label_text, width=15, anchor="w")
            label.pack(side=tk.LEFT, padx=(0, 5))
            
            entry = ttk.Entry(frame, font=('Arial', 10))
            entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
            
            self.entries[field_name] = entry
        
        # Options frame
        options_frame = ttk.LabelFrame(left_frame, text="Generation Options", padding=10)
        options_frame.pack(fill=tk.X, pady=15)
        
        # Number of passwords
        ttk.Label(options_frame, text="Number of passwords:").grid(row=0, column=0, sticky="w", pady=5)
        self.num_passwords = tk.StringVar(value="500")
        ttk.Entry(options_frame, textvariable=self.num_passwords, width=10).grid(row=0, column=1, sticky="w", padx=5, pady=5)
        
        # Max password length
        ttk.Label(options_frame, text="Max password length:").grid(row=0, column=2, sticky="w", padx=20, pady=5)
        self.max_length = tk.StringVar(value="20")
        ttk.Entry(options_frame, textvariable=self.max_length, width=10).grid(row=0, column=3, sticky="w", padx=5, pady=5)
        
        # Complexity options
        ttk.Label(options_frame, text="Add special chars:").grid(row=1, column=0, sticky="w", pady=5)
        self.add_special = tk.BooleanVar(value=True)
        ttk.Checkbutton(options_frame, variable=self.add_special).grid(row=1, column=1, sticky="w", pady=5)
        
        ttk.Label(options_frame, text="Add numbers:").grid(row=1, column=2, sticky="w", padx=20, pady=5)
        self.add_numbers = tk.BooleanVar(value=True)
        ttk.Checkbutton(options_frame, variable=self.add_numbers).grid(row=1, column=3, sticky="w", pady=5)
        
        # Control buttons
        button_frame = ttk.Frame(left_frame)
        button_frame.pack(fill=tk.X, pady=10)
        
        ttk.Button(button_frame, text="✨ Generate Passwords", 
                  command=self.generate_passwords, style='Custom.TButton').pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="💾 Save to File", 
                  command=self.save_to_file).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="🗑️ Clear All", 
                  command=self.clear_fields).pack(side=tk.LEFT, padx=5)
        
        # Progress bar
        self.progress = ttk.Progressbar(left_frame, orient=tk.HORIZONTAL, mode='indeterminate')
        self.progress.pack(fill=tk.X, pady=5)
        
        # Status label
        self.status_label = ttk.Label(left_frame, text="Ready to generate passwords", foreground="#27AE60")
        self.status_label.pack()
        
        # Results area
        results_frame = ttk.LabelFrame(right_frame, text="Generated Passwords", padding=10)
        results_frame.pack(fill=tk.BOTH, expand=True)
        
        # Scrollbar for text area
        text_scrollbar = ttk.Scrollbar(results_frame)
        text_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.password_text = tk.Text(
            results_frame, 
            height=30, 
            yscrollcommand=text_scrollbar.set,
            font=('Consolas', 10),
            bg='#1C2833',
            fg='#EAECEE',
            insertbackground='white'
        )
        self.password_text.pack(fill=tk.BOTH, expand=True)
        text_scrollbar.config(command=self.password_text.yview)
        
        # Counter label
        self.counter_label = ttk.Label(right_frame, text="Passwords generated: 0")
        self.counter_label.pack(pady=5)
    
    def get_data(self):
        """Collect data from input fields"""
        data = {}
        for field, entry in self.entries.items():
            value = entry.get().strip()
            if value:
                data[field] = value
        return data
    
    def generate_combinations(self, data):
        """Generate password combinations from the data"""
        combinations = []
        
        # Extract basic values
        first_name = data.get('first_name', '')
        last_name = data.get('last_name', '')
        birth_day = data.get('birth_day', '')
        birth_month = data.get('birth_month', '')
        birth_year = data.get('birth_year', '')
        fav_number = data.get('fav_number', '')
        fav_animal = data.get('fav_animal', '')
        
        # Other values
        other_values = [v for k, v in data.items() if k not in 
                       ['first_name', 'last_name', 'birth_day', 'birth_month', 'birth_year']]
        
        # Name + Year combinations
        if first_name and birth_year:
            combinations.extend([
                f"{first_name}{birth_year}",
                f"{birth_year}{first_name}",
                f"{first_name}.{birth_year}",
                f"{first_name}_{birth_year}",
                f"{first_name}-{birth_year}",
                f"{birth_year}.{first_name}",
                f"{birth_year}_{first_name}",
                f"{birth_year}-{first_name}",
            ])
        
        # Name + Month combinations
        if first_name and birth_month:
            combinations.extend([
                f"{first_name}{birth_month}",
                f"{birth_month}{first_name}",
                f"{first_name}.{birth_month}",
                f"{first_name}_{birth_month}",
            ])
        
        # Name + Day combinations
        if first_name and birth_day:
            combinations.extend([
                f"{first_name}{birth_day}",
                f"{birth_day}{first_name}",
                f"{first_name}.{birth_day}",
                f"{first_name}_{birth_day}",
            ])
        
        # Name + Favorite Number
        if first_name and fav_number:
            combinations.extend([
                f"{first_name}{fav_number}",
                f"{fav_number}{first_name}",
                f"{first_name}.{fav_number}",
                f"{first_name}_{fav_number}",
            ])
        
        # Name + Animal combinations
        if first_name and fav_animal:
            combinations.extend([
                f"{first_name}{fav_animal}",
                f"{fav_animal}{first_name}",
                f"{first_name}.{fav_animal}",
                f"{first_name}_{fav_animal}",
            ])
        
        # Full name combinations
        if first_name and last_name:
            combinations.extend([
                f"{first_name}{last_name}",
                f"{last_name}{first_name}",
                f"{first_name}.{last_name}",
                f"{first_name}_{last_name}",
                f"{first_name[0]}{last_name}",
                f"{last_name}{first_name[0]}",
                f"{first_name[0]}.{last_name}",
                f"{first_name[0]}_{last_name}",
            ])
        
        # Date combinations
        if birth_day and birth_month and birth_year:
            combinations.extend([
                f"{birth_day}{birth_month}{birth_year}",
                f"{birth_year}{birth_month}{birth_day}",
                f"{birth_day}.{birth_month}.{birth_year}",
                f"{birth_day}_{birth_month}_{birth_year}",
                f"{birth_month}{birth_day}{birth_year}",
            ])
        
        # Random combinations with other values
        all_values = [v for v in data.values() if v]
        if len(all_values) >= 2:
            for _ in range(min(100, len(all_values) * 10)):
                num_values = random.randint(2, min(4, len(all_values)))
                selected = random.sample(all_values, num_values)
                
                separators = ['', '.', '_', '-', '']
                separator = random.choice(separators)
                
                random.shuffle(selected)
                combination = separator.join(selected)
                
                # Add variations
                variations = [
                    combination,
                    combination.lower(),
                    combination.upper(),
                    combination.capitalize(),
                ]
                
                # Add leet speak variations occasionally
                if random.random() < 0.3:
                    leet = (combination
                           .replace('a', '@')
                           .replace('i', '!')
                           .replace('s', '$')
                           .replace('e', '3')
                           .replace('o', '0'))
                    variations.append(leet)
                
                combinations.extend(variations[:2])
        
        return list(set(combinations))
    
    def add_complexity(self, password):
        """Add special characters and numbers to passwords"""
        special_chars = ['!', '@', '#', '$', '%', '&', '*']
        numbers = '0123456789'
        
        modified = password
        
        # Add numbers if enabled
        if self.add_numbers.get() and random.random() < 0.4:
            if random.random() < 0.5:
                modified = modified + ''.join(random.choices(numbers, k=random.randint(1, 3)))
            else:
                modified = ''.join(random.choices(numbers, k=random.randint(1, 2))) + modified
        
        # Add special characters if enabled
        if self.add_special.get() and random.random() < 0.3:
            if random.random() < 0.5:
                modified = modified + random.choice(special_chars)
            else:
                modified = random.choice(special_chars) + modified
        
        return modified
    
    def generate_passwords(self):
        """Generate and display passwords"""
        data = self.get_data()
        
        if not data:
            messagebox.showwarning("Input Required", "Please enter some information first")
            return
        
        try:
            num_passwords = int(self.num_passwords.get())
            max_length = int(self.max_length.get())
            
            if num_passwords <= 0 or max_length <= 0:
                raise ValueError("Values must be positive")
                
        except ValueError as e:
            messagebox.showerror("Invalid Input", "Please enter valid positive numbers for count and length")
            return
        
        # Start progress bar
        self.progress.start()
        self.status_label.config(text="Generating passwords...", foreground="#F39C12")
        self.root.update()
        
        # Generate base combinations
        all_passwords = []
        base_combinations = self.generate_combinations(data)
        
        # Generate additional passwords
        while len(all_passwords) < num_passwords and base_combinations:
            sample_size = min(200, len(base_combinations))
            sample = random.sample(base_combinations, sample_size)
            
            for combo in sample:
                if len(all_passwords) >= num_passwords:
                    break
                
                # Apply complexity modifications
                modified = self.add_complexity(combo)
                
                # Trim to max length
                if len(modified) > max_length:
                    modified = modified[:max_length]
                
                all_passwords.append(modified)
        
        # Remove duplicates and take required number
        unique_passwords = list(set(all_passwords))
        final_passwords = unique_passwords[:num_passwords]
        
        # Stop progress bar
        self.progress.stop()
        
        # Display results
        self.password_text.delete(1.0, tk.END)
        for password in final_passwords:
            self.password_text.insert(tk.END, f"{password}\n")
        
        # Update counter and status
        self.counter_label.config(text=f"Passwords generated: {len(final_passwords)}")
        self.status_label.config(text=f"Successfully generated {len(final_passwords)} passwords!", foreground="#27AE60")
        
        messagebox.showinfo("Success", f"Generated {len(final_passwords)} unique passwords!")
    
    def save_to_file(self):
        """Save passwords to file"""
        passwords = self.password_text.get(1.0, tk.END).strip()
        if not passwords:
            messagebox.showwarning("No Passwords", "No passwords to save. Please generate passwords first.")
            return
        
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
            title="Save Passwords As"
        )
        
        if file_path:
            try:
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(passwords)
                messagebox.showinfo("Success", f"Passwords saved to:\n{file_path}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save file:\n{str(e)}")
    
    def clear_fields(self):
        """Clear all input fields and results"""
        for entry in self.entries.values():
            entry.delete(0, tk.END)
        self.password_text.delete(1.0, tk.END)
        self.counter_label.config(text="Passwords generated: 0")
        self.status_label.config(text="Ready to generate passwords", foreground="#27AE60")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()
