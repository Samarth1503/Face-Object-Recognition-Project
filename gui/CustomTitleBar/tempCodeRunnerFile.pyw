
def changex_on_hovering(event):
    global close_button
    close_button['bg']='red'    
    
def returnx_to_normalstate(event):
    global close_button
    close_button['bg']=RGRAY
    
def change_size_on_hovering(event):
    global expand_button
    expand_button['bg']=LGRAY
    
def return_size_on_hovering(event):
    global expand_button
    expand_button['bg']=RGRAY
    
def changem_size_on_hovering(event):
    global minimize_button
    minimize_button['bg']=LGRAY
    
def returnm_size_on_hovering(event):
    global minimize_button
    minimize_button['bg']=RGRAY
    
def get_pos(event):
    if root.maximized == False:
        xwin = root.winfo_x()
        ywin = root.winfo_y()
        startx = event.x_root
        starty = event.y_root
        ywin = ywin - starty
        xwin = xwin - startx

        def move_window(event):
            root.config(cursor="fleur")
            root.geometry(f'+{event.x_root + xwin}+{event.y_root + ywin}')

        def release_window(event):
            root.config(cursor="arrow")
            
        title_bar.bind('<B1-Motion>', move_window)
        title_bar.bind('<ButtonRelease-1>', release_window)
        title_bar_title.bind('<B1-Motion>', move_window)
        title_bar_title.bind('<ButtonRelease-1>', release_window)
    else:
        expand_button.config(text=" 🗖 ")
        root.maximized = not root.maximized