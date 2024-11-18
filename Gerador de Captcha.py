import tkinter as tk
from tkinter import messagebox
import random
import string
from PIL import Image, ImageDraw, ImageFont, ImageTk


class CaptchaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerador de CAPTCHA")
        self.root.geometry("400x300")
        self.root.configure(bg="#f0f8ff")
        
        # Frame para o CAPTCHA
        self.captcha_frame = tk.Frame(self.root, bg="#f0f8ff")
        self.captcha_frame.pack(pady=20)
        
        # Canvas para exibir o CAPTCHA
        self.captcha_canvas = tk.Canvas(self.captcha_frame, width=200, height=80, bg="#ffffff", highlightthickness=0)
        self.captcha_canvas.pack()
        
        # Entrada de texto
        self.captcha_entry = tk.Entry(self.root, font=("Arial", 14), justify="center")
        self.captcha_entry.pack(pady=10)
        
        # Botão para verificar o CAPTCHA
        self.verify_button = tk.Button(self.root, text="Verificar", command=self.verify_captcha, bg="#32CD32", fg="#ffffff", font=("Arial", 12))
        self.verify_button.pack(pady=5)
        
        # Botão para gerar novo CAPTCHA
        self.new_captcha_button = tk.Button(self.root, text="Novo CAPTCHA", command=self.generate_captcha, bg="#1E90FF", fg="#ffffff", font=("Arial", 12))
        self.new_captcha_button.pack(pady=5)
        
        # Gerar o primeiro CAPTCHA
        self.captcha_text = ""
        self.generate_captcha()

    def generate_captcha(self):
        """Gera um novo CAPTCHA."""
        # Limpar entrada de texto
        self.captcha_entry.delete(0, tk.END)
        
        # Gerar texto randômico
        self.captcha_text = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        
        # Criar imagem CAPTCHA
        image = Image.new("RGB", (200, 80), color=(255, 255, 255))
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype("arial.ttf", 36)
        
        # Desenhar o texto com ruído
        for i in range(len(self.captcha_text)):
            draw.text((10 + i * 30, random.randint(5, 15)), self.captcha_text[i], font=font, fill=self.random_color())
        for _ in range(30):  # Adicionar linhas de ruído
            x1, y1 = random.randint(0, 200), random.randint(0, 80)
            x2, y2 = random.randint(0, 200), random.randint(0, 80)
            draw.line((x1, y1, x2, y2), fill=self.random_color(), width=1)
        
        # Exibir imagem no canvas
        self.captcha_image = ImageTk.PhotoImage(image)
        self.captcha_canvas.create_image(0, 0, anchor="nw", image=self.captcha_image)

    def random_color(self):
        """Gera uma cor aleatória."""
        return tuple(random.randint(0, 255) for _ in range(3))

    def verify_captcha(self):
        """Verifica se o texto digitado corresponde ao CAPTCHA."""
        user_input = self.captcha_entry.get().strip().upper()
        if user_input == self.captcha_text:
            messagebox.showinfo("Resultado", "Você acertou o CAPTCHA!")
        else:
            messagebox.showerror("Resultado", "Você errou o CAPTCHA. Tente novamente!")
        

# Criar a janela principal
if __name__ == "__main__":
    root = tk.Tk()
    app = CaptchaApp(root)
    root.mainloop()
