import tkinter as tk
from tkinter import messagebox, filedialog
import re

# Function to generate the readme.md content
def generate_readme():
    links = []
    
    for i in range(1, 11):
        title = globals()[f"title_entry_{i}"].get()
        link = globals()[f"link_entry_{i}"].get()
        category = category_entry.get()
        
        if title and link:
            links.append({"title": title, "link": link, "category": category})
    
    readme_content = ""
    current_category = None
    for link in links:
        if link['category'] != current_category:
            readme_content += f"\n## {link['category']}\n"
            current_category = link['category']
        
        readme_content += f"- [{link['title']}]({link['link']})\n"
    
    readme_textbox.delete("1.0", tk.END)
    readme_textbox.insert(tk.END, readme_content)
    
    update_info_bar(len(links))

# Function to update the information bar
def update_info_bar(num_links):
    info_bar.config(text=f"Links: {num_links}")

# Function to load a readme.md file
def load_readme():
    file_path = filedialog.askopenfilename(filetypes=[("Markdown Files", "*.md")])
    
    if file_path:
        with open(file_path, "r") as file:
            content = file.read()
        
        readme_textbox.delete("1.0", tk.END)
        readme_textbox.insert(tk.END, content)

# Function to reset all input fields
def reset_fields():
    for i in range(1, 11):
        globals()[f"title_entry_{i}"].delete(0, tk.END)
        globals()[f"link_entry_{i}"].delete(0, tk.END)
    category_entry.delete(0, tk.END)
    readme_textbox.delete("1.0", tk.END)
    update_info_bar(0)

# Create the main window
window = tk.Tk()
window.title("Readme.md Generator")

# Create the input section
input_frame = tk.Frame(window)
input_frame.pack(pady=10)

category_label = tk.Label(input_frame, text="Category:")
category_label.grid(row=0, column=0, sticky="w")

category_entry = tk.Entry(input_frame)
category_entry.grid(row=0, column=1, padx=10)

for i in range(1, 11):
    title_label = tk.Label(input_frame, text=f"Title {i}:")
    title_label.grid(row=i, column=0, sticky="w")

    globals()[f"title_entry_{i}"] = tk.Entry(input_frame)
    globals()[f"title_entry_{i}"].grid(row=i, column=1, padx=10)

    link_label = tk.Label(input_frame, text=f"Link {i}:")
    link_label.grid(row=i, column=2, sticky="w")

    globals()[f"link_entry_{i}"] = tk.Entry(input_frame)
    globals()[f"link_entry_{i}"].grid(row=i, column=3, padx=10)

# Create the button section
button_frame = tk.Frame(window)
button_frame.pack(pady=10)

generate_button = tk.Button(button_frame, text="Generate Readme", command=generate_readme)
generate_button.grid(row=0, column=0, padx=10)

load_button = tk.Button(button_frame, text="Load Readme", command=load_readme)
load_button.grid(row=0, column=1, padx=10)

reset_button = tk.Button(button_frame, text="Reset", command=reset_fields)
reset_button.grid(row=0, column=2, padx=10)

# Create the output section
output_frame = tk.Frame(window)
output_frame.pack(pady=10)

info_bar = tk.Label(output_frame, text="Links: 0")
info_bar.pack()

readme_label = tk.Label(output_frame, text="Generated Readme:")
readme_label.pack()

readme_textbox = tk.Text(output_frame, width=80, height=20)
readme_textbox.pack(padx=10, pady=5)

window.mainloop()
