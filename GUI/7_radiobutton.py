#여러줄에 거쳐서 어떠한 목록을 관리함

from tkinter import * #tkinter을 쓰기 위함

root =Tk()
root.title("Nado GUI") #프로그래밍 제목 설정
root.geometry("640x480") #크기 설정

Label(root, text="메뉴를 선택하세요").pack()

burger_var=IntVar() # 여기에 int 형으로 값을 저장한다
btn_burger1 = Radiobutton(root, text="햄버거", value=1, variable=burger_var)
btn_burger2 = Radiobutton(root, text="치즈버거", value=2, variable=burger_var)
btn_burger3 = Radiobutton(root, text="치킨버거", value=3, variable=burger_var)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

def btncmd():
    pass
    
btn=Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()