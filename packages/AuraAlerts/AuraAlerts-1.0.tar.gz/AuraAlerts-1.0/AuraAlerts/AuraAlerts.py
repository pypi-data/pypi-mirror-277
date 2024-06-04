import PIL.Image
import PIL.ImageTk
import customtkinter as ctk
import os


class Aa:
    """
    This is source code of  [AuraAlerts.py]

        enjoy :)
    """
    __errors = [
        "Error 0: Content Is NULL",
        "Error 1: Img Is Not Found"
    ]
    __imgsPath = [
        r'imgs/close.png',
        r'imgs/check.png',
        r'imgs/info.png',
        r'imgs/warn.png',
        r"imgs/icon.png",
        r"imgs/custom.png",
    ]

    def __init__(self):
        pass

    def __fileFinder(self, path: str = None):
        if not path:
            print('Enter File Path')
            return None
        File = os.path.abspath(__file__)
        Dir = os.path.dirname(File)
        FilePath = os.path.join(Dir, path)
        return FilePath

    def __initialize_app(self, title, content, theme):
        app = ctk.CTk()
        app.resizable(False, False)
        ctk.set_appearance_mode(theme)
        
        if content is None:
            print(f"{Aa.__errors[0]}")
            return None
        
        app.title(title if title else 'Beauty Alerts!!')
        height = len(content) + 10
        width = len(content) + 10
        app._max_height = height
        app._max_width = width
        
        iconPath = self.__fileFinder(self.__imgsPath[4])
        if iconPath and os.path.exists(iconPath):
            image = PIL.Image.open(iconPath)
            photo = PIL.ImageTk.PhotoImage(image)
            app.wm_iconbitmap(iconPath)
            app.iconphoto(False, photo)
        
        return app

    
    def __create_alert_window(self, title, content, buttonText, theme, imgPath, buttonColor, buttonHoverColor,imgSize=(33,33)):
        app = self.__initialize_app(title, content, theme)
        if app is None:
            return
        
        if imgPath and os.path.exists(imgPath):
            img = PIL.Image.open(imgPath)
            ico = ctk.CTkImage(light_image=img, dark_image=img, size=imgSize)
            ctk.CTkLabel(app, text='', image=ico).pack(pady=10)
        else:
            print(Aa.__errors[1])

        ctk.CTkLabel(app, text=content).pack(padx=20, pady=0)
        bottomFrame = ctk.CTkFrame(app, bg_color='#333', fg_color='#333')
        bottomFrame.pack(fill='both', anchor='center')
        ctk.CTkButton(bottomFrame, text=buttonText, fg_color=buttonColor, hover_color=buttonHoverColor, width=25,
                    corner_radius=4, text_color='#222', command=lambda: app.destroy()).pack(anchor='e', pady=7, padx=15)
        app.mainloop()

    def error(self, title=None, content=None, buttonText='close', theme='light'):
        imgPath = self.__fileFinder(self.__imgsPath[0])
        self.__create_alert_window(title, content, buttonText, theme, imgPath, "#ff8080", "#df7272")

    def success(self, title=None, content=None, buttonText='close', theme='light'):
        imgPath = self.__fileFinder(self.__imgsPath[1])
        self.__create_alert_window(title, content, buttonText, theme, imgPath, "#42ff68", "#12dd79")

    def info(self, title=None, content=None, buttonText='close', theme='light'):
        imgPath = self.__fileFinder(self.__imgsPath[2])
        self.__create_alert_window(title, content, buttonText, theme, imgPath, "#80b3ff", "#5c9dff")

    def warn(self, title=None, content=None, buttonText='close', theme='light'):
        imgPath = self.__fileFinder(self.__imgsPath[3])
        self.__create_alert_window(title, content, buttonText, theme, imgPath, "#ffe680", "#ffdd57")

    def custom(self, title=None, content=None, buttonText='close', buttonColor='#e08aff', buttonHoverColor='#d561ff', imagePath=None, imgSize=(33, 33), theme='light'):
        imgPath = imagePath if imagePath else self.__fileFinder(self.__imgsPath[5])
        self.__create_alert_window(title, content, buttonText, buttonColor, buttonHoverColor, theme, imgPath, imgSize)

