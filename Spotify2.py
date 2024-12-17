# подключаем среду для работы графического интерфейса
import tkinter.messagebox
from tkinter import *
from tkinter import ttk
# подключаем среду для работы с операционной системой
import os
# подключаем среду для работы с музыкой(в нашем случае)
import pygame

pygame.init() # разворачиваем среду для музыки

# получаем порядковый номер текущего элемента
def getVar():
    # ПОДРОБНЕЕ
    # Все плейлисты образуют между собой 1 большой список. Как и в реальной жизни, каждый элемент имеет свой порядковый номер.
    # Пример: Есть у нас список плейлистов [кишлак, пошлая молли, афпс, rozzy], в нашем случае если мы выберем кишлака, то функция вернет 0, то есть у этого плейлиста порядковый номер 0. Значит пошлая молли это 1, афпс это 2 и так далее.
    # Эта функция с помощью return вернет порядковый номер(число) нашего ВЫБРАННОГО плейлиста
    return var.get()

# самое сложное
# это функция для воспроизведения плейлиста
def music_list():
    # показываем что переменные height и width глобальные
    global width, height
    # функция стоп для включения и выключения проигрыша песни
    def stop():
        if len(os.listdir(os.getcwd() + '/playlists/' + os.listdir(os.getcwd() + '/playlists/')[getVar()])) > 0: # проверка на наличие хотябы 1 песни
            if playBtn['text'] == 'Play': # если у нас песня не идет, плейлист не запущен
                playBtn['text'] = 'Stop' # меняем текст на кнопке с Play на Stop
                playM() # проигрываем плейлист (подробнее ниже)
            # иначе если плейлист идет и мы хотим его остановить
            else:
                playBtn['text'] = 'Play' # меняем Stop на Play
                pygame.mixer.music.stop() # останавливаем плейлист
        else:
            # а теперь логика, смотри если у нас есть папка(плейлист) и она пустая, то мы не сможем его воспроизвести, верно?
            # ну так вот, тут если такое произошло, то наша программа не крашнется, а просто скажет, что плейлист пустой и его нужно заполнить
            tkinter.messagebox.showerror(title='Error PlayList', message='Пустой плейлист')
            window.destroy() # закрываем окно

    def playM():
        # os.getcwd() получаем текущую папку проекта
        # добавляем нашу папку playlists со всеми плейлистами
        #       - os.listdir(os.getcwd() + '/playlists/')[getVar()]
        #       - os.listdir - список всех песен в папке по опр пути (os.getcwd() + '/playlists/')
        #       - по итогу ма получим список всех плейлистов, мы добавили [getVar()], то есть указали конкретный плейлист, который мы хотим прослушать

        directory = os.getcwd() + '/playlists/' + os.listdir(os.getcwd() + '/playlists/')[getVar()]

        # создаем отвельный список со всеми песнями из выбранного плейлиста(для удобства)
        mp3_files = [f for f in os.listdir(directory)]

        # перебираем все песни из плейлиста
        for mp3_file in mp3_files:

            file_path = os.path.join(directory, mp3_file) # генерируем конечный путь к песне на твоем пк
            pygame.mixer.music.load(file_path) # загружаем в проигрыватель песню по нашему пути
            pygame.mixer.music.play(0) # воспроизводим каждую песню 1 раз


    window = Tk() # создаем окно
    window.title('Play')  # даем имя

    playBtn = Button(window, text='Play', command=stop, height=height, width=width) # делаем кнопку и добавляем на нее текст Play
    playBtn.pack() # подключаем ее к окну

# создаем новый плейлист
def playlist_new():
    # показываем что переменные height и width глобальные
    global height, width

    def savedir():
        # подфункция для создания плейлиста и нашей корневой папке.
        try:
            playlist_name = entry.get()
            os.mkdir(os.getcwd() + '/playlists/' + playlist_name) # создаем папку по указанному пути
        except:
            # а теперь логика, смотри если у нас уже есть папка(плейлист) с таким же именем, то мы не спожем его создать, верно?
            # ну так вот, тут если такое произошло, то наша программа не крашнется, а просто скажет, что такое название уже есть и нужно его поменять
            tkinter.messagebox.showerror(title='error name', message='Введите другое имя')

    create_playlist = Tk() # создаем отдельно окно
    create_playlist.title('создание плейлиста') # даем ему название

    label = ttk.Label(create_playlist, text="введи название плейлиста") # это поле для текста. Вот тут подробнее: https://metanit.com/python/tkinter/2.7.php
    label.pack() # подключаем поле к нашему окну

    entry = ttk.Entry(create_playlist) # это поле для ввода текста. Вот тут подробнее: https://metanit.com/python/tkinter/2.7.php
    entry.pack(anchor=NW, padx=6, pady=6) # так же подключаем

    btn = Button(create_playlist,text='save', command=savedir, height=height, width=width) # это кнопка! Вот тут подробнее: https://metanit.com/python/tkinter/2.7.php
    btn.pack() # это подключение!

# это просто заглушка, она ничего не делает, в ней нету функционала, она максимум выводит ошибку, что данный момент эта часть кода не активна (в 78 строке)
def setting_playlist():
    """TODO: create edit name playlist, delete playlist"""

    setting_playlist = Tk()
    setting_playlist.title('edit')

    tkinter.messagebox.showerror(title='time error', message='не работает')
    setting_playlist.destroy()

# создаем папку playlists в папке проекта
try:
    os.mkdir(os.getcwd() + '/playlists')
except:
    pass

# я устал писать комменты :((((

root = Tk() # создаем окно
root.title("Spotify") # даем имя
var = IntVar() # получаем индекс выбранного плейлиста

# длина и ширина кнопок
width = 10
height = 2

# добавляем каждый плейлист на нашем окне
try:
    a = 0 # id первого плейлиста
    # перебираем все плейлисты в папке playlists
    for i in os.listdir(os.getcwd() + '/playlists'):
        # добавляем радио-кнопку
        python_btn = ttk.Radiobutton(text=i, variable=var, value=a, command=getVar)
        a += 1 # изменяем id
        python_btn.pack(padx=6, pady=6, anchor=NW) # рисуем на окно
except:
    # если ошибка, то просто игнорим ее (чел ты в муте.......)
    pass

# создаем кнопка для создания плейлиста, настройки плейлиста(та которая не работает пока что) и проигрыванию выбранного плейлиста
btn1 = Button(text='create playlist', command=playlist_new, height=height, width=width)
btn1.pack()
btn2 = Button(text='edit playlist', command=setting_playlist, height=height, width=width)
btn2.pack()
btn2 = Button(text='play playlist', command=music_list, height=height, width=width)
btn2.pack()

root.mainloop() # запускаем наш код, УРААААААААААААААА !!!111!!!!!1!!11!1111!1!!!!!1!!!!
