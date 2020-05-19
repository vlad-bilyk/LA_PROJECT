import threading
from tkinter import *
from tkinter.ttk import Progressbar

from interface.commands import *


window = Tk()
window.geometry('1280x720')
window.title("Welcome to LikeGeeks app")


radio_var = IntVar()
radio_var.set(10)
radio_buttons = []
chosen_songs = []
radio_text = []

check_vars = []
check_buttons = []
chosen_bands = []

curr_band_songs = []
curr_band_index = 0

reroll_songs_btn = None


def submit_check():
    boxes_status = [i.get() for i in check_vars]  # true or false list

    for box, text in zip(boxes_status, check_text):
        if box:
            chosen_bands.append(text)


def submit_radio():
    global radio_text, curr_band_songs, curr_band_index, lbl

    if radio_var.get() < 10 and len(chosen_songs) < len(chosen_bands):
        chosen_songs.append(radio_text[int(radio_var.get())])

    print(chosen_songs)

    if len(chosen_songs) < len(chosen_bands):

        destroy_radio_buttons()
        lbl.destroy()

        curr_band_songs = get_band_songs(chosen_bands[curr_band_index + 1])
        curr_band_index += 1

        radio_text = get_next_songs(curr_band_songs)
        create_radio_buttons(radio_text)
        lbl = Label(window, text="Choose one song of {}".format(chosen_bands[curr_band_index]))
        lbl.grid(column=2, row=1)
    else:
        show_results()


def show_results():

    def work():
        submit_btn.destroy()
        reroll_songs_btn.destroy()
        destroy_radio_buttons()
        lbl.destroy()

        progress_var = DoubleVar()
        progress = Progressbar(window, variable=progress_var, orient=HORIZONTAL,
                               length=100, mode='determinate')
        progress.grid(column=10, row=15)

        time.sleep(5)

        # window.update_idletasks()

        model = load_model('../data/first.model')

        lyrics = []

        for b, s in zip(chosen_bands, chosen_songs):
            print(b, s)
            artist = df[df.band == b]
            song = artist[df.name == s]
            lyr = song.lyrics.item().split(';')
            lyrics.append(song2matrix(most_freq_words(lyr), model))

        final_matrix = []

        for mat in lyrics:
            final_matrix = add_matices(final_matrix, mat)

        songs_recommended = ""
        for i in get_recommendations(final_matrix, model, pvar=progress_var, window=window):
            songs_recommended += get_band(i) + " - " + get_name(i) + "\n"

        t1 = 'Based on your taste:'
        for b, s in zip(chosen_bands, chosen_songs):
            t1 += "\n{} - {}".format(b, s)

        final_lbl = Label(window, text=t1)
        final_lbl.grid(column=4, row=4)

        t2 = "Recommended songs are:\n" + songs_recommended

        final_lbl = Label(window, text=t2)
        final_lbl.grid(column=4, row=10)

        progress.stop()
        done_lbl = Label(window, text="Done! 100%")
        done_lbl.grid(column=11, row=17)

        print("Done!")

    t = threading.Thread(target=work)
    t.start()


def reroll_songs():
    global radio_text

    destroy_radio_buttons()

    if len(curr_band_songs) >= 6:
        radio_text = get_next_songs(curr_band_songs)
    elif len(curr_band_songs) == 0:
        submit_radio()
        return
    else:
        radio_text = curr_band_songs

    create_radio_buttons(radio_text)


def reroll_bands():
    global check_text
    destroy_check_buttons()
    check_text = get_next_bands()
    create_check_buttons(check_text)


def go_to_songs():
    global curr_band_songs, radio_text, submit_btn, reroll_songs_btn

    destroy_all_buttons_check()

    curr_band_songs = get_band_songs(chosen_bands[curr_band_index])
    radio_text = get_next_songs(curr_band_songs)

    create_radio_buttons(radio_text)

    lbl = Label(window, text="Choose one song of {}".format(chosen_bands[curr_band_index]))
    lbl.grid(column=2, row=1)

    submit_btn = Button(window, text="Submit", command=submit_radio)
    submit_btn.grid(column=30, row=20)

    reroll_songs_btn = Button(window, text="Rerrol songs", command=reroll_songs)
    reroll_songs_btn.grid(column=40, row=30)

    # reroll_songs_btn = Button(window, text="Rerrol songs", command=reroll_songs)


    # next_band_btn = Button(window, text="Next band", command=next_band)
    # next_band_btn.grid(column=70, row=15)

    # reroll songs for current band


def destroy_all_buttons_check():
    if len(check_buttons) > 0:
        destroy_check_buttons()

    submit_btn.destroy()
    reroll_btn.destroy()
    go_to_songs_btn.destroy()
    lbl.destroy()


def destroy_check_buttons():
    global check_buttons, check_text, check_vars

    for i in check_buttons:
        i.destroy()

    check_buttons = []
    check_text = []
    check_vars = []


def destroy_radio_buttons():
    global radio_buttons, radio_text, radio_var

    for i in radio_buttons:
        i.destroy()

    radio_buttons = []
    radio_text = []
    radio_var = IntVar()


def create_radio_buttons(text_lst):
    col = 10
    value = 0
    for i in range(len(text_lst)):

        rb = Radiobutton(window, text=text_lst[i], variable=radio_var, value=value)
        rb.grid(column=col, row=10)
        radio_buttons.append(rb)

        col += 5
        value += 1


def create_check_buttons(text_lst):
    col = 1
    for i in range(len(text_lst)):
        var = BooleanVar()
        var.set(False)
        check_vars.append(var)

        c = Checkbutton(window, text=text_lst[i], variable=var, onvalue=True, offvalue=False)
        c.grid(column=col, row=2)
        check_buttons.append(c)

        col += 1


check_text = get_next_bands()
create_check_buttons(check_text)

lbl = Label(window, text="Choose bands/artist that you listent to:")
lbl.grid(column=2, row=1)

submit_btn = Button(window, text="Submit", command=submit_check)
submit_btn.grid(column=3, row=3)


reroll_btn = Button(window, text='Reroll bands', command=reroll_bands)
reroll_btn.grid(column=10, row=10)

go_to_songs_btn = Button(window, text='Choose songs', command=go_to_songs)
go_to_songs_btn.grid(column=10, row=15)


window.mainloop()