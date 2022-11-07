from tkinter import END, Tk, Button, Entry

# Configuración ventana principal
root = Tk()
root.title("Calculadora POO")
root.resizable(0,0)
root.geometry("295x250")

# Configuración pantalla de salida 
pantalla  =  Entry(root, width = 40, bg = "black", fg = "white", borderwidth = 0, font = ("arial", 18, "bold"))
pantalla.grid(row = 0, column = 0, columnspan = 80, padx = 1, pady = 1)

# Configuración botones
boton_1 = Button(root, text = "1", width = 9, height = 3, bg = "white", fg = "red", borderwidth = 0, cursor = "hand2", command = lambda: escribir(1)).grid(row = 1, column = 0, padx = 1, pady = 1 )
boton_2 = Button(root, text = "2", width = 9, height = 3, bg = "white", fg = "red", borderwidth = 0, cursor = "hand2", command = lambda: escribir(2)).grid(row = 1, column = 1, padx = 1, pady = 1 )
boton_3 = Button(root, text = "3", width = 9, height = 3, bg = "white", fg = "red", borderwidth = 0, cursor = "hand2", command = lambda: escribir(3)).grid(row = 1, column = 2, padx = 1, pady = 1 )
boton_4 = Button(root, text = "4", width = 9, height = 3, bg = "white", fg = "red", borderwidth = 0, cursor = "hand2", command = lambda: escribir(4)).grid(row = 2, column = 0, padx = 1, pady = 1 )
boton_5 = Button(root, text = "5", width = 9, height = 3, bg = "white", fg = "red", borderwidth = 0, cursor = "hand2", command = lambda: escribir(5)).grid(row = 2, column = 1, padx = 1, pady = 1 )
boton_6 = Button(root, text = "6", width = 9, height = 3, bg = "white", fg = "red", borderwidth = 0, cursor = "hand2", command = lambda: escribir(6)).grid(row = 2, column = 2, padx = 1, pady = 1 )
boton_7 = Button(root, text = "7", width = 9, height = 3, bg = "white", fg = "red", borderwidth = 0, cursor = "hand2", command = lambda: escribir(7)).grid(row = 3, column = 0, padx = 1, pady = 1 )
boton_8 = Button(root, text = "8", width = 9, height = 3, bg = "white", fg = "red", borderwidth = 0, cursor = "hand2", command = lambda: escribir(8)).grid(row = 3, column = 1, padx = 1, pady = 1 )
boton_9 = Button(root, text = "9", width = 9, height = 3, bg = "white", fg = "red", borderwidth = 0, cursor = "hand2", command = lambda: escribir(9)).grid(row = 3, column = 2, padx = 1, pady = 1 )
boton_igual = Button(root, text = " = ", width = 20, height = 3, bg = "red", fg = "white", borderwidth = 0, cursor = " hand2", command = lambda: computar()).grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1)
boton_punt  = Button(root, text = ".", width = 9, height = 3, bg = "spring green", fg = "black",borderwidth = 0, cursor = "hand2", command = lambda: escribir(".")).grid(row = 4, column = 2, padx = 1, pady = 1)
boton_mas = Button(root, text = "+", width = 9, height = 3, bg = "deep sky blue", fg = "black", borderwidth = 0, cursor = "hand2", command = lambda: escribir("+")).grid(row = 1, column = 3, padx = 1, pady = 1)
boton_menos = Button(root, text = "-", width = 9, height = 3, bg = "deep sky blue", fg = "black", borderwidth = 0, cursor = "hand2", command = lambda: escribir("-")).grid(row = 2, column = 3, padx = 1, pady = 1)
boton_multiplicacion = Button(root, text = "*",  width = 9, height = 3, bg = "deep sky blue", fg = "black", borderwidth = 0, cursor = "hand2", command = lambda: escribir("*")).grid(row = 3, column = 3, padx = 1, pady = 1)
boton_division = Button(root, text = "/", width = 9, height = 3, bg = "deep sky blue", fg = "black", borderwidth = 0, cursor = "hand2", command = lambda: escribir("/")).grid(row = 4, column = 3, padx = 1, pady = 1)

# Configuración de entrada por pantalla

def escribir(int):
    pantalla.insert(END,int)

def computar():
    resultado = eval(pantalla.get())
    pantalla.delete(0,END)
    pantalla.insert(END,resultado)


root.mainloop()