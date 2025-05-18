import tkinter as tk
import pygame
# estilos.Aplica_estilos.arg(prop)

class Aplica_estilos:
    pygame.mixer.init()
    def __init__(self):
        pass
    
    

    # NoSerif - Garamond, Lucida Console 
    # Serif - Palatino Linotype
    #474448, #2d232e, #e0ddcf, #ec4e20, #2081c3
        
    
    @staticmethod    
    def janela(jnl):
        jnl.geometry("570x500+400+100")
        jnl.config(
        )
        
        
    @staticmethod    
    def lbBlock(labelB):
        labelB.config(
            bg="#2d232e",
            pady=10,
            padx=10,
            borderwidth=5, 
            relief="raised",
            
        )
        labelB.pack_configure(
            fill="both",
            expand=True,
        )
        
    @staticmethod    
    def frBlock(frameB):
        frameB.config(
            bg="#474448",
            pady=10,
            borderwidth=5, 
            relief="raised",
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
            borderwidth=5, 
            relief="raised",
        )
        buttonB.pack_configure(
            fill="both",
            expand=True,
        )
        
    @staticmethod    
    def divTempo(div):
        div.config(
            bg="#474448",
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
            font=( "Lucida Console", 14, "bold"), 
            bg="#2d232e", 
            foreground="#e0ddcf",
            borderwidth=3, 
            relief="ridge",
            pady= 7,
            padx= 7,
        )
        titulo.pack_configure(
            anchor="nw"
        )
        
    @staticmethod
    def processando(titulo):
        titulo.config(
            font=( "Lucida Console", 14, "bold"), 
            bg="#2d232e", 
            foreground="#e0ddcf",
            borderwidth=3, 
            relief="ridge",
            pady= 7,
            padx= 7,
        )
        titulo.pack_configure(
            anchor="sw",
            side="bottom",
            padx=20
        )
        
    @staticmethod    
    def label2(titulo):
        titulo.config(
            font=( "Garamond", 12, "bold"), 
            bg="#474448", 
            foreground="#e0ddcf", 
            borderwidth=3, 
            relief="ridge",
            pady= 7,
            padx= 7,
        )
        titulo.pack_configure(
            anchor="w",
            pady= 5,
        )
    @staticmethod 
    def div_left_right(div_left, div_right):
        div_left.config(
            bg="#474448",
            borderwidth=5, 
            relief="raised",
        )
        
        div_left.pack(
            side="left",
            anchor="n",
            fill="both",
            expand=True
        )
        
        div_right.config(
            bg="#474448",
            borderwidth=5, 
            relief="raised",
            
        )
        
        div_right.pack(
            side="right",
            anchor="n",
            fill="both",
            expand=True
        )
    #474448, #2d232e, #e0ddcf, #ec4e20, #2081c3    
    @staticmethod
    def widgets_progs_manager(titulo_add, label_nome, entry, btn_caminho, btn_add, btn_exc, info):
        # titulo_add_prog, label_info_nome, entry_nome, btn_caminho, btn_add_progs, btn_exc_progs, info
        titulo_add.config(
            font=( "Lucida Console", 12, "bold"), 
            bg="#474448", 
            foreground="#e0ddcf",
            borderwidth=3, 
            relief="ridge",
            pady= 7,
            padx= 7,
        )
        
        titulo_add.pack(
            
        )
        
        label_nome.config(
            font=( "Lucida Console", 10, "bold"), 
            bg="#474448", 
            foreground="#e0ddcf",
            borderwidth=3, 
            relief="ridge",
            pady= 7,
            padx= 7,
        )
        
        label_nome.pack(
            side="left"
        )
        
        entry.config(
            font=( "Lucida Console", 10),
            bg="#e0ddcf", 
            foreground="#2d232e",
        )
        
        entry.pack(
            side="left",
            pady=15,
            ipady=5,
        )
        
        btn_caminho.config(
            font=( "Lucida Console", 10), 
            borderwidth=5,
            bg="#e0ddcf",
            foreground="#2d232e",
        )
        
        btn_caminho.pack(
            side="left" 
        )
        
        btn_add.config(
            font=( "Lucida Console", 10), 
            borderwidth=5,
            bg="#e0ddcf",
            foreground="#2d232e",
        )
        
        btn_add.pack(
            anchor="w",
        )
        
        btn_exc.config(
            font=( "Lucida Console", 10, "bold"), 
            borderwidth=5,
            bg="#e0ddcf",
            fg="red",
        )
        
        btn_exc.pack(
            pady=10,
        )
        
        info.config(
            font=( "Garamond", 10, "bold"), 
            bg="#474448", 
            foreground="#e0ddcf",
        )
        
        info.pack(
            
        )
        
    
    @staticmethod
    def div_top_bottom(div_top, div_bottom, div_exc):
        div_top.config(
            bg="#474448",
        )
        
        div_top.pack(
            side="top",
            ipady=10,
            padx=5
        )
        
        div_bottom.config(
            bg="#474448"
        )
        div_bottom.pack(
           
        )
        
        div_exc.config(
            bg="#474448",
            borderwidth=5,
            relief="ridge"
        )
        
        div_exc.pack(
            side="bottom"
        )        
        
    @staticmethod    
    def button(btn, btn2, btn3):
        click_sound = pygame.mixer.Sound("click.wav")
        s3_sound = pygame.mixer.Sound("s3.wav")
        btn.config(
            font=( "Lucida Console", 12), 
            borderwidth=5,
            bg="#e0ddcf",
            fg="#2d232e",
    )
        btn.pack_configure(
            side="left",
            anchor="sw"
        )
        btn2.config(
            font=( "Lucida Console", 12), 
            borderwidth=5,
            bg="#e0ddcf",
            fg="#2d232e",
    )
        btn2.pack_configure(
            side="right",
            padx=3,
            anchor="sw"
        )
        btn3.config(
            font=( "Lucida Console", 12), 
            borderwidth=5,
            bg="#e0ddcf",
            fg="#2d232e",
    )
        btn3.pack_configure(
            side="right",
            padx=3,
            anchor="sw"
        )
        btn.bind("<Button-1>", lambda _: click_sound.play())
        btn2.bind("<Button-1>", lambda _: s3_sound.play())
        
        
        
    @staticmethod    
    def btns(btn):
        s1_sound = pygame.mixer.Sound("s1.wav")
        btn.config(
            font=( "Lucida Console", 12), 
            borderwidth=5,
            #bg="#e0ddcf",
    )
        btn.pack_configure(
            pady=2,
            anchor="w"
        )
        btn.bind("<Button-1>", lambda _: s1_sound.play())
    
    @staticmethod    
    def chkbutton(chkBtn):
        s2_sound = pygame.mixer.Sound("s2.wav")
        chkBtn.config(
            font=( "Garamond", 12, "bold"), 
            foreground="#e0ddcf",
            bg="#ec4e20",
            borderwidth=5,
            relief="groove",
            pady= 2,
            padx= 2,
            cursor="hand2",
            indicator=0,
            selectcolor="#2081c3", 
            activebackground="#ec4e20",
            activeforeground="#e0ddcf",
        )
        chkBtn.pack_configure(
            anchor="w",
            padx= 10,
            pady=2,
        )
        chkBtn.bind("<Button-1>", lambda _: s2_sound.play())
    
    @staticmethod    
    def rdbutton(rdBtn, rdBtn2):
        s2_sound = pygame.mixer.Sound("s2.wav")
        rdBtn.config(
            foreground="#e0ddcf",
            bg="#ec4e20",
            font=( "Garamond", 12, "bold"), 
            borderwidth=5,
            relief="sunken",
            pady= 2,
            padx= 2,
            cursor="hand2",
            indicator=0,
            selectcolor="#2081c3", 
            activebackground="#ec4e20",
            activeforeground="#e0ddcf",
        )
        rdBtn.pack_configure(
            side="left",
            padx= 10,
            anchor="nw"
        )
        rdBtn.bind("<Button-1>", lambda _: s2_sound.play())
        
        rdBtn2.config(
            foreground="#e0ddcf",
            bg="#ec4e20",
            font=( "Garamond", 12, "bold"), 
            borderwidth=5,
            relief="sunken",
            pady= 2,
            padx= 2,
            cursor="hand2",
            indicator=0,
            selectcolor="#2081c3",
            activebackground="#ec4e20",
            activeforeground="#e0ddcf",
        )
        rdBtn2.pack_configure(
            side="left",
            anchor="nw"
        )
        rdBtn2.bind("<Button-1>", lambda _: s2_sound.play())
        