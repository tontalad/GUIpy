import flet
from flet import ( FloatingActionButton, Page, TextField, icons,Text,AppBar,Icon,
IconButton,Page,colors,ListView,Dropdown,dropdown,Container,Row,alignment,border_radius
,AlertDialog,Checkbox)


def main (page:Page):


    #Variable
    show_dlg = page.dialog = AlertDialog(title=Text("No Todo List"))
    todolist = ListView()
    read_txt = Column()
    new_task=TextField(hint_text='Enter Your To Do List',autofocus=True,width=800)



    #delete 

    #Show content
    def show_text(content_):  
        return Row([Container(
            content=Text(value=content_,size=25,color=colors.BROWN),
            width=500,
            height=450,
            bgcolor=colors.PINK_50,
            alignment=alignment.center,
            border_radius=border_radius.all(5)        
        )],alignment='center')
   

    #Write to filet text 
    def keep_txt(write):
        with open('test_file.txt','a+') as text:
            text.write(f'{write}\n')
            print(write)


    #Read file text
    def read_file():
        with open('test_file.txt','r') as file_read:
            for i in file_read:            
                i = i.replace("\n", "")
                if i !='':
                    read_txt.controls.append(Checkbox(label=f"{i}"))

        return read_txt


    #Realtime
    def real_text(text):
        read_txt.controls.append(Checkbox(label=f"{text}"))


    #Click Button
    def addclick(button):
        #Chaeck empty
        if new_task.value == "":
            print("todo is empty")
            page.dialog = show_dlg
            show_dlg.open = True
        else:
            keep_txt(new_task.value)
            real_text(new_task.value)
            new_task.value = str()       
        page.update()


    #Dropdown Changed
    a=read_file()
    def dropdown_changed(e):
        #Todolist
        if knowledge.value=="Todolist":
            page.clean()
            page.add(Row([new_task,knowledge]),FloatingActionButton(icon=icons.ADD,on_click=addclick))
            page.add(a)
        #Content
        else:
            count2 =0
            for x in d:
                if knowledge.value==(f'{count2+1}){x["หัวข้อ"]}'):
                    page.clean()
                    page.add(Row([new_task,knowledge]),FloatingActionButton(icon=icons.ADD,on_click=addclick))
                    page.add(show_text(x["บทความ"]))
                count2 +=1


    #Show Dropdown list Todolist
    knowledge=Dropdown(on_change = dropdown_changed,
        label="List & Poem",
        hint_text="",
        width=430,
        options=[
            dropdown.Option("Todolist")
        ],
        autofocus=True,
        )



    #Show list Dropdown Content
    with open("working.txt","r",encoding="utf-8") as read_knowledge:
        a1 = read_knowledge.readlines()
        d = []
        know_dict = {}
        counts=0
        for i in a1:
            i=i.replace("\n","")
            Subject,Content = i.split(", ")
            know_dict = {"หัวข้อ":(Subject),"บทความ":(Content)}
            d.append(know_dict)
            counts+=1
            knowledge.options.append(dropdown.Option(f'{counts}){Subject}'))
        

    
    #Show page
    page.add(Row([new_task,knowledge]),read_file(),FloatingActionButton(icon=icons.ADD,on_click=addclick))
    

    #Show Appbar
    page.appbar = AppBar(
        leading=Icon(icons.TIMELAPSE_ROUNDED),
        leading_width=30,
        title=Text('TO DO LIST'),
        center_title= False,
        elevation=1,
        bgcolor=colors.PINK_100,
       )

   
    page.update()
#Run app
flet.app(target=main)