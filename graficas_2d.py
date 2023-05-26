from tkinter import*

BASE = 460
ALTURA = 220

Ventana_principal = Tk ()
Ventana_principal.title("Graficas 2D")
Ventana_principal.resizable(False,False)
Ventana_principal.geometry("500x500")
Ventana_principal.config(bg="White")

frame_graficacion= Frame(Ventana_principal)
frame_graficacion.config(bg="green", width=480, height=240)
frame_graficacion.place(x=10, y=10)

c = Canvas(frame_graficacion, width=BASE, height=ALTURA)
c.config(bg="black")
c.place(x=10, y=10)

#line_1 = c.create_line(BASE/2, ALTURA/2, BASE,ALTURA, fill="green", width=2)
#line_2 = c.create_line(BASE/2, ALTURA/2, BASE,0, fill="yellow", width=2)line_3 = c.create_line(0,0,BASE/2, ALTURA/2, fill="green", width=2)
#line_6 = c.create_line(BASE/2, ALTURA/2, 0,ALTURA, fill="yellow", width=2)



#Text_1 = c.create_text(BASE/4, ALTURA/2, anchor="center", text="Sistemas", font=("Arial", 25,"bold"),fill="blue", activefill="yellow")
#Text_2 = c.create_text(3*BASE/4, ALTURA/2, anchor="center", text="Colegio", font=("Arial", 25,"bold"),fill="blue",activefill="yellow")
#Text_3 = c.create_text(BASE/2, 3*ALTURA/4, anchor="center", text="Guanenta", font=("Arial", 25,"bold"),fill="blue", activefill="yellow")
#Text_4 = c.create_text(BASE/2, ALTURA/4, anchor="center", text="Especialidad", font=("Arial", 25,"bold"),fill="blue",activefill="yellow")


#rect_1 = c.create_rectangle(BASE/2, ALTURA/2, BASE,ALTURA,fill="pink", outline="blue")
#rect_2 = c.create_rectangle(0,0,BASE/2,ALTURA/2, fill="orange", outline="white")
#rect_3 = c.create_rectangle(BASE/2, ALTURA/2, BASE,0, fill="red", outline="blue")
#rect_3 = c.create_rectangle(BASE/2, ALTURA/2, 3*BASE/2,0, fill="yellow", outline="blue")
#rect_1 = c.create_rectangle(BASE/2, ALTURA/2, BASE,ALTURA/2, fill="purple", outline="blue")
#rect_2 = c.create_rectangle(BASE/2, ALTURA/2, BASE,ALTURA, fill="white", outline="blue")
#rect_2 = c.create_rectangle(BASE/2, ALTURA/2, BASE/4,ALTURA/2, fill="black", outline="blue")


#circ_1 = c.create_oval(BASE/2,0,BASE,ALTURA/2, fill="blue")
#circ_2 = c.create_oval(0,ALTURA/2,BASE/4,ALTURA, fill="yellow")
#circ_3 = c.create_oval(BASE/4,ALTURA/2,BASE/2,ALTURA, fill="red")

#polig_1 = c.create_polygon(3*BASE/4,ALTURA/2,BASE,ALTURA,BASE/2,ALTURA, fill="red")
#polig_2 = c.create_polygon(BASE/4,0,BASE/2,ALTURA/4,0,ALTURA/4, fill="red")

#cruz = c.create_polygon(BASE/2-25,ALTURA/2-75,BASE/2+25,ALTURA/2-75,BASE/2+25,ALTURA/2-25, BASE/2+75,ALTURA/2-25, BASE/2+75,ALTURA/2+25, BASE/2+25, ALTURA/2+25, BASE/2+25, ALTURA/2+75, BASE/2-25, ALTURA/2+75, BASE/2-25, ALTURA/2+25, BASE/2-75, ALTURA/2+25, BASE/2-75, ALTURA/2-25, BASE/2-25, ALTURA/2-25, fill="white")

#linea_1 = c.create_polygon(BASE/3,0,2*BASE/3,0,2*BASE/3,ALTURA/4,2*BASE,ALTURA/4,BASE,2*ALTURA/2.6,2*BASE/3,2*ALTURA/2.6,2*BASE/3,ALTURA,BASE/3,ALTURA,BASE/3,2*ALTURA/2.6,0,2*ALTURA/2.6,0,ALTURA/4,BASE/3,ALTURA/4, fill="red")


#polig_1 = c.create_polygon(BASE/3,0,2*BASE/3,0,2*BASE/3,ALTURA/4,2*BASE,ALTURA/4,BASE,2*ALTURA/2.6,2*BASE/3,2*ALTURA/2.6,2*BASE/3,ALTURA,BASE/3,ALTURA,BASE/3,2*ALTURA/2.6,0,2*ALTURA/2.6,0,ALTURA/4,BASE/3,ALTURA/4, fill="red")

base_1 = c.create_rectangle(0+100, ALTURA/2+80, BASE-100, ALTURA/2+100, fill="blue4", outline="black")
base_2 = c.create_polygon(0+200, ALTURA/2+80, 0+235, ALTURA/2+5, 0+270, ALTURA/2+80,fill="blue", outline="black")

arco_1 = c.create_arc(BASE/2-120, ALTURA/2-50, BASE-100, ALTURA/2+60, start=60, extent=60, fill="purple", outline="black")
arco_2 = c.create_arc(BASE/2-120, ALTURA/2-50, BASE-100, ALTURA/2+60, start=180, extent=60, fill="purple", outline="black")
arco_3 = c.create_arc(BASE/2-120, ALTURA/2-50, BASE-100, ALTURA/2+60, start=300, extent=60,fill="purple", outline="black")

frame_controles= Frame(Ventana_principal)
frame_controles.config(bg="green", width=480, height=230)
frame_controles.place(x=10, y=260)

Ventana_principal.mainloop()