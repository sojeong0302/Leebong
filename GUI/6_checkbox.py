#여러줄에 거쳐서 어떠한 목록을 관리함

from tkinter import * #tkinter을 쓰기 위함

root =Tk()
root.title("Nado GUI") #프로그래밍 제목 설정
root.geometry("640x480") #크기 설정

chkvar=IntVar() #chkvar에 int 형으로 값을 저장한다
chkbox=Checkbutton(root, text="오늘 하루 보지 않기", variable=chkvar)
# chkbox.select()#자동 선택 처리
# chkbox.deselect() #선택 해제 처리
chkbox.pack()

def btncmd():
    print(chkvar.get()) # 0 : 체크 해제, 1 : 체크
    
btn=Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()