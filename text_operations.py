def cut(textbox):
    textbox.event_generate("<<Cut>>")

def copy(textbox):
    textbox.event_generate("<<Copy>>")

def paste(textbox):
    textbox.event_generate("<<Paste>>")
