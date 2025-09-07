from kivy.app import App
from kivy.uix.actionbar import ActionBar, ActionButton, ActionView, ActionPrevious, ActionGroup, ActionCheck
from kivy.uix.boxlayout import BoxLayout


class MyApp(App):
    def build(self):
        main_layout = ActionBar(pos = (0, 675))
        actionview = ActionView()
        main_layout.add_widget(actionview)

        actionview.add_widget(ActionPrevious())
        actionview.add_widget(ActionButton(text = '', icon = 'zvuk.png'))

        group = ActionGroup(text='Group', dropdown_width=100)
        for i in range(10):
            group.add_widget(ActionButton(text=str(i)))
        actionview.add_widget(group)

        check = ActionCheck(size_hint = (0.1, 1))
        actionview.add_widget(check)

        return main_layout



if __name__ == '__main__':
    MyApp().run()