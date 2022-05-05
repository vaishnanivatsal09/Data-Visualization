import pandas as pd
import plotly.express as px
from tkinter import *

win= Tk()
win.geometry("750x250")

df = pd.read_csv('covid.csv')
values = df['Deaths']
names = df['Country'].tolist()

fig = px.pie(df, values=values, names=names, title="Covid analysis")
fig.write_image("images/fig1.png")

import matplotlib.pyplot as plt

def graph():
    plt.pie(values,labels = names,autopct = '%.2f%%',shadow=True)
    plt.title('Covid Analytics', fontsize = 20)
    plt.show()
    plt.write_image("images/fig1.png")

Button(win, text= "Show Graph", command= graph).pack(pady=20)
win.mainloop()