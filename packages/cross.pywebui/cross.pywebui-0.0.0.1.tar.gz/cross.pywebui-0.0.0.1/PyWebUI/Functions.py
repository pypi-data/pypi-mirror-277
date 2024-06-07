from PyWebUI.Constants import *
from PyWebUI.utilities import util4code as u4c
def add_key_event(func, key: str) -> None:
    """Adds an event during key presses.

    Args:
        func (function): The function to be run when key is pressed. No parameters required.
        *args (tuple): tuple can be any length. This contains the keys being pressed at once.
    """
    
    modifiers = [] # contains modifier keys
    regulars = [] # contains regular keys
    # differentiates modifiers and regular keys
    if key in MODIFIERS:
        modifiers.append(key)
    else:
        regulars.append(key)
    KeyPressEvent(func = func,
                    modifier_keys = modifiers,
                    regular_keys = regulars)
    
class KeyPressEvent:
    all_key_events = []
    def __init__(self, func, modifier_keys=[], regular_keys=[]):
        self.modifier_keys = modifier_keys
        self.regular_keys = regular_keys
        self.func = func
        KeyPressEvent.all_key_events.append(self)
        print(KeyPressEvent.all_key_events)

    def run(self,*args,**kwargs):
        if PLATFORM == 'Windows':
            self._run_for_windows(*args)
        else:
            self._run_for_android(*args)

    def _run_for_windows(self, event,*args):
        from PyQt5.QtCore import Qt
        mod_keys_equiv = []
        reg_keys_equiv = []
        for mod_key in self.modifier_keys:
            mod_keys_equiv.append(KEY_MAPPING[mod_key][0]) # first index belongs to windows
        for reg_key in self.regular_keys:
            reg_keys_equiv.append(KEY_MAPPING[reg_key][0]) # first index belongs to windows
        # get key name from constants, exculding Qt.
        reg_key_pressed = all([event.key() == getattr(Qt, key[3:]) for key in reg_keys_equiv]) if len(reg_keys_equiv)>0 else True
      
        if reg_key_pressed:
            try:
                self.func()
            except Exception as e:
                u4c.show_error()
             
    def _run_for_android(self, event):
        pass