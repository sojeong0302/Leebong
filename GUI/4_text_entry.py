from tkinter import * #tkinter을 쓰기 위함

root =Tk()
root.title("Nado GUI") #프로그래밍 제목 설정
root.geometry("640x480") #크기 설정

txt=Text(root, width=30, height=5)
txt.pack()

#엔터 입력 가능
txt.insert(END, "글자를 입력하세요")#사람들에게 이 텍스트가 뭘하는지 알려주기 위함

#엔터 입력 불가
e=Entry(root, width=30)
e.pack()
e.insert(0, "한 줄만 입력해요")

def btncmd():
    print(txt.get("1.0",END))#1: 첫번째 라인, 0 : 0번째 column 위치
    print(e.get())

    #내용 삭제
    txt.delete("1.0", END)
    e.delete(0,END)

btn=Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()