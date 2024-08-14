import itertools
import tkinter as tk


def new_words():
    a = []
    f_hand = open("russian_nouns.txt", "r", encoding="utf-8")
    for line in f_hand:
        line = line.rstrip()
        a.append(line)
    rdict = set(a)
    words = []
    word = word_entry.get().lower()
    length = int(length_entry.get())
    for i in itertools.permutations(word, length):
        x = "".join(i)
        words.append(x)
    variant = set(words)
    answer = ", ".join(rdict.intersection(variant))
    result_entry.delete(1.0, "end")
    if answer == "":
        result_entry.insert(1.0, "Нет вариантов")
    else:
        result_entry.insert(1.0, answer)


window = tk.Tk()
window.title("Поиск слов")
window.geometry("500x450")
window.resizable(width=False, height=False)
window["bg"] = "grey60"
button_result = tk.Button(window, text="Получить результат", bg="red", command=new_words)
button_result.place(x=50, y=400)
word_entry = tk.Entry(window, width=30)
word_entry.place(x=50, y=50)
length_entry = tk.Entry(window, width=11)
length_entry.place(x=380, y=50)
result_entry = tk.Text(window, width=50, height=7, font="Times 12", bg="pink", fg="black", wrap="word")
result_entry.place(x=50, y=250)
word_in = tk.Label(window, text="Введите исходное слово")
word_in.place(x=50, y=25)
number_in = tk.Label(window, text="Длина слов")
number_in.place(x=380, y=25)
word_out = tk.Label(window, text="Получились такие слова:")
word_out.place(x=50, y=220)
window.mainloop()
