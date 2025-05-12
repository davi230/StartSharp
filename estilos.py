import tkinter as tk

# estilos.Aplica_estilos.arg(prop)

class Aplica_estilos:
    def __init__(self):
        pass
    
    # NoSerif - Garamond, Lucida Console 
    # Serif - Palatino Linotype
    #474448, #2d232e, #e0ddcf, #ec4e20, #2081c3

    
    @staticmethod    
    def janela(jnl):
        #jnl.geometry("370x200+400+300")
        jnl.config(
            
        )
        
        
    @staticmethod    
    def lbBlock(labelB):
        labelB.config(
            bg="#474448",
            pady=10,
            padx=10,
            borderwidth=2, 
            relief="groove",
            
        )
        labelB.pack_configure(
            fill="both",
            expand=True,
        )
        
    @staticmethod    
    def frBlock(frameB):
        frameB.config(
            bg="#e0ddcf",
            pady=10,
            heigh=3,
            borderwidth=2, 
            relief="groove",
        )
        frameB.pack_configure(
            fill="both",
            expand=True,
        )
        
        
    @staticmethod    
    def btnBlock(buttonB):
        buttonB.config(
            bg="#2d232e",
            pady=10,
            padx=10,
            borderwidth=2, 
            relief="groove",
        )
        buttonB.pack_configure(
            fill="both",
            expand=True,
        )
        
    @staticmethod    
    def divTempo(div):
        div.config(
            bg="#e0ddcf",
            pady=10,
            padx=10,
        )
        div.pack_configure(
            fill="both",
            expand=True,
            side="bottom"
        )
        
    @staticmethod    
    def label(titulo):
        titulo.config(
            font=( "Garamond", 14, "bold"), 
            bg="#474448", 
            foreground="#e0ddcf", 
            borderwidth=5, 
            relief="groove",
            pady= 10,
            padx= 10,
        )
        titulo.pack_configure(
            anchor="nw"
        )
        
    @staticmethod    
    def label2(titulo):
        titulo.config(
            font=( "Garamond", 14, "bold"), 
            bg="#e0ddcf", 
            foreground="#474448", 
            borderwidth=5, 
            relief="groove",
            pady= 5,
            padx= 5,
        )
        titulo.pack_configure(
            anchor="w",
            pady= 5,
        )
        
    @staticmethod    
    def button(btn, btn2, btn3):
        btn.config(
            font=( "Lucida Console", 12), 
            borderwidth=5,
    )
        btn.pack_configure(
            side="left",
            anchor="sw"
        )
        btn2.config(
            font=( "Lucida Console", 12), 
            borderwidth=5,
    )
        btn2.pack_configure(
            side="left",
            padx=3,
            anchor="sw"
        )
        btn3.config(
            font=( "Lucida Console", 12), 
            borderwidth=5,
    )
        btn3.pack_configure(
            side="left",
            padx=3,
            anchor="sw"
        )
        
    @staticmethod    
    def btns(btn):
        btn.config(
            font=( "Lucida Console", 12), 
            borderwidth=5,
            bg="#e0ddcf",
    )
        btn.pack_configure(
            pady=2,
            anchor="w"
        )
    
    @staticmethod    
    def chkbutton(chkBtn):
        chkBtn.config(
            font=( "Lucida Console", 12), 
            bg="#e0ddcf",
            borderwidth=5,
            relief="groove",
            pady= 2,
            padx= 2,
            activebackground="#2081c3",
            cursor="hand2",
            indicator=0
        )
        chkBtn.pack_configure(
            anchor="w",
            padx= 10,
            pady=2,
        )
    
    @staticmethod    
    def rdbutton(rdBtn, rdBtn2):
        rdBtn.config(
            
            bg="#e0ddcf",
            font=( "Lucida Console", 12), 
            borderwidth=5,
            relief="groove",
            pady= 2,
            padx= 2,
            cursor="hand2",
            indicator=0
        )
        rdBtn.pack_configure(
            side="left",
            padx= 10,
            anchor="nw"
        )
        rdBtn2.config(
            bg="#e0ddcf",
            font=( "Lucida Console", 12), 
            borderwidth=5,
            relief="groove",
            pady= 2,
            padx= 2,
            cursor="hand2",
            indicator=0
        )
        rdBtn2.pack_configure(
            side="left",
            anchor="nw"
        )
        