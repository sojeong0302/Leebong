#여러줄에 거쳐서 어떠한 목록을 관리함

from tkinter import * #tkinter을 쓰기 위함

root =Tk()
root.title("Nado GUI") #프로그래밍 제목 설정
root.geometry("640x480") #크기 설정

listbox=Listbox(root, selectmode="extended", height=0)
listbox.insert(0, "딸기")
listbox.insert(1, "사과")
listbox.insert(2, "수박")
listbox.insert(END, "파파야")
listbox.pack()



def btncmd():
    #맨 뒤에 항목을 삭제
    listbox.delete(END)

    #항목 확인 (시작 idx, 끝 idx)
    #print("1번째부터 3번째까지의 항목 : ", listbox.get(0,2))

    #선택된 항목 확인(위치로 반환(ex)(1,2,3))
    print("선택된 항목 : ", listbox.curselection() )
btn=Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()