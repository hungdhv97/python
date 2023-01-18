import threading
import mouse
import keyboard


def monitorMouseKeyboardEvents():
    # These are the list where all the events will be stored
    mouse_events = []
    keyboard_events = []

    # Start recording
    mouse.hook(mouse_events.append)  # starting the mouse recording
    # keyboard.hook(lambda _: keyboard_events.append(_))
    keyboard.start_recording()

    keyboard.wait("esc")  # Waiting for 'Esc' button to be pressed

    # Stopping recording
    mouse.unhook(mouse_events.append)
    # keyboard.unhook(keyboard_events.append)
    keyboard_events = keyboard.stop_recording()

    return mouse_events, keyboard_events


def playMouseMouseKeyboardEvents(mouse_events, keyboard_events):
    '''
    Playing the recorded events at the same time
    '''
    k_thread = threading.Thread(target=lambda: keyboard.play(keyboard_events))
    k_thread.start()

    # Mouse threadings:
    m_thread = threading.Thread(target=lambda: mouse.play(mouse_events))
    m_thread.start()

    # waiting for both threadings to be completed
    k_thread.join()
    m_thread.join()


if __name__ == "__main__":
    mouse_events, keyboard_events = monitorMouseKeyboardEvents()
    playMouseMouseKeyboardEvents(mouse_events, keyboard_events)
