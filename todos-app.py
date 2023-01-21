from beeware import Toga
from toga.style.pack import Pack

class TodoApp(Toga.App):

    def startup(self):
        self.main_window = Toga.MainWindow(self.name)

        self.todo_list = Toga.Table(['Task', 'Completed'], on_select=self.select_todo)

        add_button = Toga.Button('Add', on_press=self.add_todo)

        self.main_window.content = Toga.Box(
            children=[self.todo_list, add_button],
            style=Pack(direction=Toga.ROW, alignment=Toga.BOTTOM)
        )

        self.main_window.show()

    def add_todo(self, widget):
        new_todo = Toga.TextInput()
        add_button = Toga.Button('Confirm', on_press=self.confirm_add)
        self.main_window.content = Toga.Box(
            children=[new_todo, add_button],
            style=Pack(direction=Toga.ROW, alignment=Toga.BOTTOM)
        )

    def confirm_add(self, widget):
        task = self.main_window.content.children[0].value
        self.todo_list.data.append([task, False])
        self.main_window.content = Toga.Box(
            children=[self.todo_list, Toga.Button('Add', on_press=self.add_todo)],
            style=Pack(direction=Toga.ROW, alignment=Toga.BOTTOM)
        )

    def select_todo(self, widget, row):
        task, completed = self.todo_list.data[row]
        self.todo_list.data[row] = [task, not completed]

if __name__ == '__main__':
    app = TodoApp('Todo List', 'org.beeware.todo')
    app.main_loop()
