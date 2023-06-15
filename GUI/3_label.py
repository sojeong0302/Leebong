#글자만 보여준다!!

from tkinter import * #tkinter을 쓰기 위함

root =Tk()
root.title("Nado GUI") #프로그래밍 제목 설정
root.geometry("640x480")

label1=Label(root, text="안녕하세요")
label1.pack()

photo=PhotoImage(file="GUI/img.png")
label2=Label(root, image=photo)
label2.pack()

#글자가 바뀜
def change():
    label1.config(text="또 만나요")
    
    global photo2
    photo2=PhotoImage(file="GUI/img2.png")
    label2.config(image=photo2)

btn=Button(root, text="클릭", command=change)


btn.pack()
root.mainloop()