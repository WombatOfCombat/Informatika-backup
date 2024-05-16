import tkinter as tk
from tkinter import messagebox
import random

class Gift:
    def __init__(self, weight):
        self.weight = weight

def generate_gifts():
    weights = list(range(1, 8))
    random.shuffle(weights)
    return [Gift(weight) for weight in weights]

class GiftSortingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Gift Sorting Game")

        self.gifts = generate_gifts()
        self.clicked_gifts = []

        self.create_widgets()

    def create_widgets(self):
        self.gift_labels = []
        for i, gift in enumerate(self.gifts):
            gift_label = tk.Label(self.master, text="?", width=3, font=("Helvetica", 16))
            gift_label.grid(row=0, column=i, padx=5)
            gift_label.bind("<Button-1>", lambda event, index=i: self.handle_gift_click(index))
            self.gift_labels.append(gift_label)

        self.sort_button = tk.Button(self.master, text="Sort Gifts", command=self.sort_gifts)
        self.sort_button.grid(row=1, columnspan=len(self.gifts), pady=10)

    def handle_gift_click(self, index):
        clicked_gift = self.gifts[index]
        self.reveal_weight(clicked_gift)
        self.clicked_gifts.append(clicked_gift)
        self.gift_labels[index].unbind("<Button-1>")
        if len(self.clicked_gifts) == len(self.gifts):
            self.sort_button.config(state=tk.NORMAL)

    def reveal_weight(self, gift):
        for gift_label in self.gift_labels:
            if gift_label["text"] == "?":
                gift_label.config(text=str(gift.weight))
                break

    def sort_gifts(self):
        self.clicked_gifts.sort(key=lambda x: x.weight)
        for i, gift in enumerate(self.clicked_gifts):
            self.gift_labels[i].config(text="?")
            self.gift_labels[i].grid(row=2, column=i, padx=5)
        self.check_sorting()

    def check_sorting(self):
        sorted_weights = [gift.weight for gift in self.clicked_gifts]
        if sorted_weights == list(range(1, 8)):
            messagebox.showinfo("Congratulations", "Gifts are sorted correctly!")
        else:
            messagebox.showerror("Oops", "Gifts are not sorted correctly. Try again.")

if __name__ == "__main__":
    root = tk.Tk()
    game = GiftSortingGame(root)
    root.mainloop()