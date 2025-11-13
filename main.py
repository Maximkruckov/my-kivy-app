from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle, Line
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.textinput import TextInput
from kivy.uix.togglebutton import ToggleButton
from kivy.clock import Clock
from kivy.uix.scrollview import ScrollView

Window.size = (370, 680)

class ImageButton(ButtonBehavior, Image):
    pass

class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.setup_ui()
    
    def setup_ui(self):
        Window.clearcolor = (1, 1, 1, 1)
        
        layout = FloatLayout()
        
        self.label = Label(
            text='Меню', 
            font_size='40', 
            color='black', 
            bold=True,
            size=(200, 60),
            pos_hint={'center_x': 0.5, 'center_y': 0.95} 
        )

        self.evryday = Button(
            text='Ежедневные дела', 
            color='black', 
            size_hint=(None, None),
            font_size='30',
            size=(300, 60),
            background_normal='',
            pos_hint={'center_x': 0.5, 'center_y': 0.8},
            on_press=self.go_to_evryday
        )
        
        self.segodna = Button(
            text='Сегодняшние дела', 
            color='black', 
            size_hint=(None, None),
            font_size='30',
            size=(300, 60),
            background_normal='',
            pos_hint={'center_x': 0.5, 'center_y': 0.7},
            on_press=self.go_to_segodna
        )
        
        self.spisky = Button(
            text='Списки', 
            color='black', 
            size_hint=(None, None),
            font_size='30',
            size=(300, 60),
            background_normal='',
            pos_hint={'center_x': 0.5, 'center_y': 0.6},
            on_press=self.go_to_spisky
        )
        
        layout.add_widget(self.label)      
        layout.add_widget(self.evryday)
        layout.add_widget(self.segodna)
        layout.add_widget(self.spisky)
        
        self.add_widget(layout)
    
    def go_to_evryday(self, instance):
        self.manager.current = 'evryday'
    
    def go_to_segodna(self, instance):
        self.manager.current = 'segodna'
    
    def go_to_spisky(self, instance):
        self.manager.current = 'spisky'

class SegodnaScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.setup_ui()
        self.cordin, self.cordin2 = 0.88, 0.879
    
    def setup_ui(self):
        layout = FloatLayout()

        label = Label(
            text='Сегодняшние дела', 
            font_size='32', 
            color=[0, 0, 0, 0.4],
            size=(200, 60),
            pos_hint={'center_x': 0.325, 'center_y': 0.05} 
        )
        
        back_button = ImageButton(
            source='home.png',
            color=[0, 0, 0, 0.4],
            size_hint=(None, None),
            size=(40, 40),
            pos_hint={'center_x': 0.85, 'center_y': 0.05},
            allow_stretch=True,
            keep_ratio=True,
            on_press=self.go_back
        )

        add_sps = Button(
            text='+',
            color=[0, 0, 0, 0.4],
            background_normal='',
            size_hint=(None, None),
            font_size='50',
            size=(60, 60),
            pos_hint={'center_x': 0.7, 'center_y': 0.05},
            on_press=self.add_spisok
        )
        
        layout.add_widget(label)
        layout.add_widget(back_button)
        layout.add_widget(add_sps)
        self.add_widget(layout)
    
    def add_spisok(self, instance):
        # Создаем виджеты при нажатии на кнопку "+"
        layout = self.children[0]  # Получаем текущий layout
        
        # Пример списка
        primer = TextInput(
            text='Name', 
            font_size=25,
            foreground_color=(0, 0, 0, 1),
            background_color=(0, 0, 0, 0),
            size_hint=(None, None),
            size=(200, 60),
            pos_hint={'center_x': 0.31, 'center_y': 0.95} 
        )

        primtr_add_sps = Button(
            text='+',
            color=[0.4, 0.4, 0.4, 0.4],
            background_normal='',
            bold=True, 
            size_hint=(None, None),
            font_size='40',
            size=(60, 60),
            pos_hint={'center_x': 0.85, 'center_y': 0.955},
            on_press=self.add_item 
        )
        
        # Добавляем виджеты в layout
        layout.add_widget(primer)
        layout.add_widget(primtr_add_sps)
        
        # Вызываем обновление внешнего вида для начальной отрисовки
        
    
    def add_item(self, instance,):
        layout = self.children[0]

        name_input = TextInput(
            text='name',
            background_color=(0, 0, 0, 0),
            size_hint=(None, None),
            size=(300, 40),
            font_size='23',
            pos_hint={'center_x': 0.43, 'center_y': self.cordin},
            foreground_color=(0.5, 0.5, 0.5, 1)
        )

        toggle_square = ToggleButton(
            text='',
            size_hint=(None, None),
            size=(20, 20),
            background_normal='',
            background_down='',
            background_color=(0, 0, 0, 0),
            pos_hint={'center_x': 0.85, 'center_y': self.cordin2}
        )

        self.cordin -= 0.053
        self.cordin2 -= 0.053

        def update_appearance(instance, value):
            instance.canvas.before.clear()
            with instance.canvas.before:
                if instance.state == 'down':  # ВКЛ - белый фон с обводкой
                    Color(0.3, 0.3, 0.3, 1)  # Темно-серый фон
                    Rectangle(pos=instance.pos, size=instance.size)
                    name_input.foreground_color = (0.5, 0.5, 0.5, 1)
                    print('Вкл')
                else:  # ВЫКЛ - темно-серый фон
                    Color(1, 1, 1, 1)  # Белый фон
                    Rectangle(pos=instance.pos, size=instance.size)
                    Color(0.3, 0.3, 0.3, 1)  # Темно-серая обводка
                    Line(rectangle=(instance.pos[0], instance.pos[1], instance.width, instance.height), width=1.5)
                    name_input.foreground_color = (0, 0, 0, 1)
                    print('Выкл')

        toggle_square.bind(state=update_appearance)

        toggle_square.bind(pos=update_appearance, size=update_appearance)

        layout.add_widget(name_input)
        layout.add_widget(toggle_square)

        Clock.schedule_once(lambda dt: update_appearance(toggle_square, toggle_square.state))
        print("Добавление нового элемента списка")
    
    def go_back(self, instance):
        self.manager.current = 'menu'

class EvrydayScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.setup_ui()
        self.cordin, self.cordin2, self.cordin3, self.cordin4 = 0.8, 0.799, 0.76, 0.757
    
    def setup_ui(self):
        layout = FloatLayout()
        scroll_view = ScrollView()

        label = Label(
            text='Ежедневные дела', 
            font_size='32', 
            color=[0, 0, 0, 0.4],
            size=(200, 60),
            pos_hint={'center_x': 0.32, 'center_y': 0.05} 
        )
        
        back_button = ImageButton(
            source='home.png',
            color=[0, 0, 0, 0.4],
            size_hint=(None, None),
            size=(40, 40),
            pos_hint={'center_x': 0.85, 'center_y': 0.05},
            allow_stretch=True,
            keep_ratio=True,
            on_press=self.go_back
        )

        add_sps = Button(
            text='+',
            color=[0, 0, 0, 0.4],
            background_normal='',
            size_hint=(None, None),
            font_size='50',
            size=(60, 60),
            pos_hint={'center_x': 0.7, 'center_y': 0.05},
            on_press=self.add_spisok
        )
        
        layout.add_widget(label)
        layout.add_widget(back_button)
        layout.add_widget(add_sps)
        self.add_widget(layout)
    
    def add_spisok(self, instance):
        # Создаем виджеты при нажатии на кнопку "+"
        layout = self.children[0]  # Получаем текущий layout
        
        
        # Пример списка
        primer = TextInput(
            text='Name', 
            font_size=25,
            foreground_color=(0, 0, 0, 1),
            background_color=(0, 0, 0, 0),
            size_hint=(None, None),
            size=(200, 60),
            pos_hint={'center_x': 0.31, 'center_y': 0.95} 
        )

        name = Label(
            text='Название', 
            font_size='20', 
            color=[0.5, 0.5, 0.5, 0.5], 
            size=(200, 60),
            pos_hint={'center_x': 0.22, 'center_y': 0.87} 
        )

        kol_vo = Label(
            text='Кол-во', 
            font_size='20', 
            color=[0.5, 0.5, 0.5, 0.5], 
            size=(200, 60),
            pos_hint={'center_x': 0.65, 'center_y': 0.87} 
        )

        primtr_add_sps = Button(
            text='+',
            color=[0.4, 0.4, 0.4, 0.4],
            background_normal='',
            bold=True, 
            size_hint=(None, None),
            font_size='40',
            size=(60, 60),
            pos_hint={'center_x': 0.85, 'center_y': 0.95},
            on_press=self.add_item 
        )
        
        # Добавляем виджеты в layout
        layout.add_widget(primer)
        layout.add_widget(primtr_add_sps)
        layout.add_widget(name)
        layout.add_widget(kol_vo)
        
        # Вызываем обновление внешнего вида для начальной отрисовки
        
    
    def add_item(self, instance,):
        layout = self.children[0]

        name_input = TextInput(
            text='name',
            background_color=(0, 0, 0, 0),
            size_hint=(None, None),
            size=(300, 40),
            font_size='23',
            pos_hint={'center_x': 0.43, 'center_y': self.cordin},
            foreground_color=(0.5, 0.5, 0.5, 1)
        )

        schet = Label(
            text='Счет:', 
            font_size='18', 
            color=[0.5, 0.5, 0.5, 0.5], 
            size=(200, 60),
            bold=True,
            pos_hint={'center_x': 0.165, 'center_y': self.cordin3}
        )

        schet_input = TextInput(
            text='-',
            background_color=(0, 0, 0, 0),
            size_hint=(None, None),
            size=(300, 40),
            font_size='19',
            pos_hint={'center_x': 0.55, 'center_y': self.cordin4},
            foreground_color=(0, 0, 0, 1)
        )
        
        kol_vo_input = TextInput(
            text='name',
            background_color=(0, 0, 0, 0), 
            size_hint=(None, None),
            size=(300, 40),
            font_size='23',
            pos_hint={'center_x': 0.9, 'center_y': self.cordin},
            foreground_color=(0.5, 0.5, 0.5, 1)
        )

        toggle_square = ToggleButton(
            text='',
            size_hint=(None, None),
            size=(20, 20),
            background_normal='',
            background_down='',
            background_color=(0, 0, 0, 0),
            pos_hint={'center_x': 0.85, 'center_y': self.cordin2}
        )

        self.cordin -= 0.08
        self.cordin2 -= 0.08
        self.cordin3 -= 0.08
        self.cordin4 -= 0.08

        def update_appearance(instance, value):
            instance.canvas.before.clear()
            with instance.canvas.before:
                if instance.state == 'down':  # ВКЛ - белый фон с обводкой
                    Color(0.3, 0.3, 0.3, 1)  # Темно-серый фон
                    Rectangle(pos=instance.pos, size=instance.size)
                    name_input.foreground_color = (0.5, 0.5, 0.5, 1)
                    kol_vo_input.foreground_color = (0.5, 0.5, 0.5, 1)
                    schet_input.foreground_color = (0.5, 0.5, 0.5, 1)
                    print('Вкл')
                else:  # ВЫКЛ - темно-серый фон
                    Color(1, 1, 1, 1)  # Белый фон
                    Rectangle(pos=instance.pos, size=instance.size)
                    Color(0.3, 0.3, 0.3, 1)  # Темно-серая обводка
                    Line(rectangle=(instance.pos[0], instance.pos[1], instance.width, instance.height), width=1.5)
                    name_input.foreground_color = (0, 0, 0, 1)
                    kol_vo_input.foreground_color = (0, 0, 0, 1)
                    schet_input.foreground_color = (0, 0, 0, 1)
                    print('Выкл')

        toggle_square.bind(state=update_appearance)

        toggle_square.bind(pos=update_appearance, size=update_appearance)

        layout.add_widget(name_input)
        layout.add_widget(kol_vo_input)
        layout.add_widget(toggle_square)
        layout.add_widget(schet)
        layout.add_widget(schet_input)

        Clock.schedule_once(lambda dt: update_appearance(toggle_square, toggle_square.state))
        print("Добавление нового элемента списка")
    
    def go_back(self, instance):
        self.manager.current = 'menu'

class SpiskyScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.setup_ui()
        self.cordin, self.cordin2 = 0.8, 0.799
    
    def setup_ui(self):
        layout = FloatLayout()

        label = Label(
            text='Списки', 
            font_size='40', 
            color=[0, 0, 0, 0.4],
            size=(200, 60),
            pos_hint={'center_x': 0.25, 'center_y': 0.05} 
        )
        
        back_button = ImageButton(
            source='home.png',
            color=[0, 0, 0, 0.4],
            size_hint=(None, None),
            size=(40, 40),
            pos_hint={'center_x': 0.85, 'center_y': 0.05},
            allow_stretch=True,
            keep_ratio=True,
            on_press=self.go_back
        )

        add_sps = Button(
            text='+',
            color=[0, 0, 0, 0.4],
            background_normal='',
            size_hint=(None, None),
            font_size='50',
            size=(60, 60),
            pos_hint={'center_x': 0.7, 'center_y': 0.05},
            on_press=self.add_spisok
        )
        
        layout.add_widget(label)
        layout.add_widget(back_button)
        layout.add_widget(add_sps)
        self.add_widget(layout)
    
    def add_spisok(self, instance):
        # Создаем виджеты при нажатии на кнопку "+"
        layout = self.children[0]  # Получаем текущий layout
        
        # Пример списка
        primer = TextInput(
            text='Name', 
            font_size=25,
            foreground_color=(0, 0, 0, 1),
            background_color=(0, 0, 0, 0),
            size_hint=(None, None),
            size=(200, 60),
            pos_hint={'center_x': 0.31, 'center_y': 0.95} 
        )

        name = Label(
            text='Название', 
            font_size='20', 
            color=[0.5, 0.5, 0.5, 0.5], 
            size=(200, 60),
            pos_hint={'center_x': 0.22, 'center_y': 0.87} 
        )

        kol_vo = Label(
            text='Кол-во', 
            font_size='20', 
            color=[0.5, 0.5, 0.5, 0.5], 
            size=(200, 60),
            pos_hint={'center_x': 0.65, 'center_y': 0.87} 
        )

        primtr_add_sps = Button(
            text='+',
            color=[0.4, 0.4, 0.4, 0.4],
            background_normal='',
            bold=True, 
            size_hint=(None, None),
            font_size='40',
            size=(60, 60),
            pos_hint={'center_x': 0.85, 'center_y': 0.95},
            on_press=self.add_item 
        )
        
        # Добавляем виджеты в layout
        layout.add_widget(primer)
        layout.add_widget(primtr_add_sps)
        layout.add_widget(name)
        layout.add_widget(kol_vo)
        
        # Вызываем обновление внешнего вида для начальной отрисовки
        
    
    def add_item(self, instance,):
        layout = self.children[0]

        name_input = TextInput(
            text='name',
            background_color=(0, 0, 0, 0),
            size_hint=(None, None),
            size=(300, 40),
            font_size='23',
            pos_hint={'center_x': 0.43, 'center_y': self.cordin},
            foreground_color=(0.5, 0.5, 0.5, 1)
        )
        
        kol_vo_input = TextInput(
            text='name',
            background_color=(0, 0, 0, 0), 
            size_hint=(None, None),
            size=(300, 40),
            font_size='23',
            pos_hint={'center_x': 0.9, 'center_y': self.cordin},
            foreground_color=(0.5, 0.5, 0.5, 1)
        )

        toggle_square = ToggleButton(
            text='',
            size_hint=(None, None),
            size=(20, 20),
            background_normal='',
            background_down='',
            background_color=(0, 0, 0, 0),
            pos_hint={'center_x': 0.85, 'center_y': self.cordin2}
        )

        self.cordin -= 0.053
        self.cordin2 -= 0.053

        def update_appearance(instance, value):
            instance.canvas.before.clear()
            with instance.canvas.before:
                if instance.state == 'down':  # ВКЛ - белый фон с обводкой
                    Color(0.3, 0.3, 0.3, 1)  # Темно-серый фон
                    Rectangle(pos=instance.pos, size=instance.size)
                    name_input.foreground_color = (0.5, 0.5, 0.5, 1)
                    kol_vo_input.foreground_color = (0.5, 0.5, 0.5, 1)
                    print('Вкл')
                else:  # ВЫКЛ - темно-серый фон
                    Color(1, 1, 1, 1)  # Белый фон
                    Rectangle(pos=instance.pos, size=instance.size)
                    Color(0.3, 0.3, 0.3, 1)  # Темно-серая обводка
                    Line(rectangle=(instance.pos[0], instance.pos[1], instance.width, instance.height), width=1.5)
                    name_input.foreground_color = (0, 0, 0, 1)
                    kol_vo_input.foreground_color = (0, 0, 0, 1)
                    print('Выкл')

        toggle_square.bind(state=update_appearance)

        toggle_square.bind(pos=update_appearance, size=update_appearance)

        layout.add_widget(name_input)
        layout.add_widget(kol_vo_input)
        layout.add_widget(toggle_square)

        Clock.schedule_once(lambda dt: update_appearance(toggle_square, toggle_square.state))
        print("Добавление нового элемента списка")
    
    def go_back(self, instance):
        self.manager.current = 'menu'

class Application(App):
    def build(self):
        # Создаем менеджер экранов БЕЗ анимации
        sm = ScreenManager(transition=NoTransition())
        
        # Добавляем экраны
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(EvrydayScreen(name='evryday'))
        sm.add_widget(SegodnaScreen(name='segodna'))
        sm.add_widget(SpiskyScreen(name='spisky'))
        
        return sm

if __name__ == "__main__":
    Application().run()