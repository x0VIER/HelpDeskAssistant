import tkinter as tk
from tkinter import simpledialog, scrolledtext, messagebox
import psutil
import platform
import openai

# Pop-up window for API key
root = tk.Tk()
root.withdraw()
api_key = simpledialog.askstring("API Key", "Enter your OpenAI API key:", show="*")
if not api_key:
    messagebox.showerror("Error", "No API key entered. Exiting.")
    root.quit()
    exit()
openai.api_key = api_key

# Gather system info
sys_info = {
    "os": platform.system(),
    "os_version": platform.version(),
    "cpu": platform.processor(),
    "ram_gb": round(psutil.virtual_memory().total / (1024 ** 3), 2)
}

# Pop-up window for user question
user_question = simpledialog.askstring("Help Desk", "Describe your problem:")
if not user_question:
    messagebox.showerror("Error", "No question entered. Exiting.")
    root.quit()
    exit()

prompt = (
    f"You are an IT Help Desk assistant. A user needs help.\n"
    f"User system info: {sys_info}\n"
    f"User question: {user_question}\n"
    "Give clear, step-by-step instructions even for non-technical users. Use simple language."
)

# Call OpenAI
try:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    answer = response.choices[0].message.content
except Exception as e:
    answer = f"Error: {str(e)}"

# Show response in scrollable pop-up
result_window = tk.Tk()
result_window.title("Help Desk Assistant")
text_area = scrolledtext.ScrolledText(result_window, wrap=tk.WORD, width=80, height=20)
text_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
text_area.insert(tk.END, answer)
text_area.config(state="disabled")
result_window.mainloop()
