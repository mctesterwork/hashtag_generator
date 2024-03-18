import customtkinter
import chat_settings as chat_settings

numOfHashtags = "10"
topic = "software"
customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()
app.title('AI Hashtag Generator')
app.geometry("400x400")

def button_function():
    inHashtags = inputHashtags.get()
    if not validateHashtagInput(inHashtags):
        labelHashtags.configure(bg_color='#ff0000')
    elif len(inputTopic.get()) < 1:
        labelTopic.configure(bg_color="#ff0000")
    else:
        numOfHashtags = inHashtags
        topic = inputTopic.get()
        labelTopic.configure(bg_color='transparent')
        labelHashtags.configure(bg_color='transparent')
        response = chat_settings.getHashtags(numOfHashtags, topic)
        textBoxResponse.configure(state='normal')
        textBoxResponse.insert("0.0", response)
        print(response)

# Component definitions
labelHashtags = customtkinter.CTkLabel(master=app, text='Número de hashtags:')
labelTopic = customtkinter.CTkLabel(master=app, text='Categoría:')
inputHashtags = customtkinter.CTkEntry(master=app, placeholder_text=numOfHashtags)
inputTopic = customtkinter.CTkEntry(master=app, placeholder_text=topic)
textBoxResponse = customtkinter.CTkTextbox(master=app, width=300, height=100, state="disabled")
textBoxResponse.grid(row=0, column=0)

# Component placement
labelHashtags.place(relx=0.2, rely=0.2, anchor=customtkinter.CENTER)
labelTopic.place(relx=0.2, rely=0.4, anchor=customtkinter.CENTER)
inputHashtags.place(relx=0.6, rely=0.2, anchor=customtkinter.CENTER)
inputTopic.place(relx=0.6, rely=0.4, anchor=customtkinter.CENTER)
textBoxResponse.place(relx=0.5, rely=0.7, anchor=customtkinter.CENTER)

# Use CTkButton instead of tkinter Button
button = customtkinter.CTkButton(master=app, text="Enviar", command=button_function)
button.place(relx=0.5, rely=0.9, anchor=customtkinter.CENTER)

def validateHashtagInput(input):
    if len(input) < 1 or not str.isdigit(input):
        return False
    return True

app.mainloop()


