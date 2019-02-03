import tkinter as tk

root = tk.Tk()
root.title("コイン")
root.geometry("340x540")
C = tk.Canvas(root, bg="white", height=340, width=340)
C.create_line(10, 10, 10, 330, 330, 330, 330, 10, 10, 10) #外に10px残し四角形を描画
C.create_line(170, 10, 170, 330)#縦線の描画
C.create_line(10, 170, 330, 170)#横線の描画
C.create_line(90, 10, 90, 330)#さらに縦線その1
C.create_line(250, 10, 250, 330)#さらに縦線その2
C.create_line(10, 90, 330, 90)#さらに横線その1
C.create_line(10, 250, 330, 250)#さらに横線その2

C.pack()

icon0 = tk.PhotoImage(file='player0.png')
icon1 = tk.PhotoImage(file='player1.png')
C.create_image(290, 290, image=icon0)
C.create_image(50, 50, image=icon1)

root.mainloop()