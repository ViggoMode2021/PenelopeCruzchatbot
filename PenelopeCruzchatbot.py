from tkinter import *
root = Tk()
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import pyttsx3

plist = [      'Hola',
               'Hola me llamo Penélope Cruz. Mucho gusto.',
               '¿Cómo estás?',
               'Estoy bien, gracias. ¿Y tú?',
               '¿Cómo eres?',
               'Yo soy alta, bronceada, talentosa, y sociable.',
               '¿Cómo son tus primos?',
               'Mis primos son trabajadores, inteligentes, rubios, y delgados.',
               '¿Cómo son tú y tu hermana?.',
               'Mi hermana y yo tenemos pelo largo y somos jóvenes y artísticas.',
               '¿Qué te gusta hacer?',
               'Me gusta cantar, correr, y bailar.',
               '¿Cuál es la fecha de tu cumpleaños?',
               'Mi cumpleaños es el veintiocho de abril.',
               '¿Cuántos años tienes?',
               'Yo tengo cuarenta y siete años.',
               '¿Cuál es tu color favorito?',
               'Mi color favorito es rojo.',
               '¿De dónde eres?',
               'Yo soy de Alcobendas, España.',
               '¿Qué comes en el desayuno?',
               'Yo como huevos, pan tostado, tocino, y fresas.',
               '¿Qué bebes en el desayuno?',
               'Yo bebo jugo de naranja y café.'
         ]

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)

bot = ChatBot('El robot de Penélope Cruz')
read_only=True
trainer = ListTrainer(bot)

trainer.train(plist)

def bot_reply():
    question= question_field.get()
    answer=bot.get_response(question)
    text_area.insert(END, "Tú: " + question+'\n\n')
    text_area.insert(END, "Penélope Cruz: " + str(answer) + '\n\n')
    pyttsx3.speak(answer)
    question_field.delete(0, END)

root.geometry('500x570')
root.title('El robot de Penelope Cruz')
root.config(bg="orange")

logo_pic = PhotoImage(file="Penelope Cruz.png")
logo_pic_label= Label(root,image=logo_pic, bg="orange")
logo_pic_label.pack()

center_frame = Frame(root)
center_frame.pack()

scroll_bar=Scrollbar(center_frame)
scroll_bar.pack(side=RIGHT)

text_area=Text(center_frame, font=('times new roman', 20, 'bold'), height=10, yscrollcommand=scroll_bar.set
               , wrap='word')

text_area.pack(side=LEFT)
scroll_bar.config(command=text_area.yview)

question_field = Entry(root, font=('verdana', 20, 'bold'))
question_field.pack(pady=15, fill=X)

ask_pic = PhotoImage(file="Enviar.png")

ask_button = Button(root, image= ask_pic, command=bot_reply)
ask_button.pack()

root.mainloop()
