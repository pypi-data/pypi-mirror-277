import ctypes
import ctypes.wintypes
from ctypes import *
import os

dll_path = os.path.join(os.path.dirname(__file__), 'PyGUIBuilder.dll')

mygui_dll = ctypes.CDLL(dll_path)

HWND = c_int

class Window_t(Structure):
    _fields_ = [("hwnd", c_void_p),
                ("hInstance", c_void_p),
                ("width", c_int),
                ("height", c_int)]

mygui_dll.createWindow_dll.argtypes = [c_char_p, c_char_p, c_int, c_int]
mygui_dll.createWindow_dll.restype = Window_t

mygui_dll.createLabel_dll.argtypes = [Window_t, c_char_p, c_int, c_int]
mygui_dll.createLabel_dll.restype = c_void_p

mygui_dll.createButton_dll.argtypes = [Window_t, c_char_p, CFUNCTYPE(None), c_int, c_int]
mygui_dll.createButton_dll.restype = c_void_p

mygui_dll.createEntry_dll.argtypes = [Window_t, c_char_p, c_int, c_int]
mygui_dll.createEntry_dll.restype = c_void_p

mygui_dll.clearText_dll.argtypes = [HWND]
mygui_dll.clearText_dll.restype = None

mygui_dll.getText_dll.argtypes = [HWND]
mygui_dll.getText_dll.restype = c_char_p

mygui_dll.setText_dll.argtypes = [HWND, c_char_p]
mygui_dll.setText_dll.restype = None

def createWindow(title, icon, width, height):
    return mygui_dll.createWindow_dll(title.encode('utf-8'), icon.encode('utf-8'), width, height)

def createLabel(window, text, row, column):
    return mygui_dll.createLabel_dll(window, text.encode('utf-8'), row, column)

ButtonCallback = CFUNCTYPE(None)

_global_callbacks = []

def createButton(window, text, callback, row, column):
    callback_c = ButtonCallback(callback)
    _global_callbacks.append(callback_c)
    return mygui_dll.createButton_dll(window, text.encode('utf-8'), callback_c, row, column)

def createEntry(window, text, row, column):
    return mygui_dll.createEntry_dll(window, text.encode('utf-8'), row, column)

def clearText(hwnd):
    return mygui_dll.clearText_dll(hwnd)

def getText(hwnd):
    text = mygui_dll.getText_dll(hwnd)
    return text.decode('utf-8')

def setText(hwnd, text):
    mygui_dll.setText_dll(hwnd, text.encode('utf-8'))

def destroyElement(hwnd):
    ctypes.windll.user32.DestroyWindow(hwnd)

def run():
    msg = ctypes.wintypes.MSG()
    while True:
        ret = ctypes.windll.user32.GetMessageW(ctypes.pointer(msg), None, 0, 0)
        if ret == 0:
            break
        ctypes.windll.user32.TranslateMessage(ctypes.pointer(msg))
        ctypes.windll.user32.DispatchMessageW(ctypes.pointer(msg))
