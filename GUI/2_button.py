from tkinter import * #tkinter을 쓰기 위함

root =Tk()
root.title("Nado GUI") #프로그래밍 제목 설정

btn1=Button(root, text="버튼1")
btn1.pack() #이거까지 적어야 버튼이 생성 완료

btn2=Button(root, padx=5, pady=10,text="버튼2") 
btn2.pack()

btn3=Button(root, padx=10, pady=5,text="버튼3")
btn3.pack()

btn4=Button(root, width=10, height=3, text="버튼4") #버튼 크기 자체를 설정
btn4.pack()

btn5=Button(root, fg="red", bg="yellow", text="버튼5")
btn5.pack()

photo =PhotoImage(file="GUI/img.png")
btn6=Button(root, image=photo)
btn6.pack()

def btncmd():
    print("버튼이 클릭되었어요")

btn7=Button(root, text="동작하는 버튼", command=btncmd)
btn7.pack()

root.mainloop()