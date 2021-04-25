import pypokedex
import PIL.Image, PIL.ImageTk
import tkinter as tk
import urllib3
from io import BytesIO


window = tk.Tk ()
window.geometry("1280x720")
window.title("Ghanem PokeDex")
window.config(padx=10, pady=10)


title_label = tk.Label(window, text="PokeDex")
title_label.config(font=("Arial, 32"))
title_label.pack (padx=10, pady=10)


pokemon_image = tk.Label(window)
pokemon_image.pack(padx=10, pady=10)


pokemon_info =tk.Label(window)
pokemon_info.config(font=("Arial, 20"))
pokemon_info.pack(padx=10, pady=10)


pokemon_types =tk.Label(window)
pokemon_types.config(font=("Arial, 20"))
pokemon_types.pack(padx=10, pady=10)

pokemon_height = tk.Label(window)
pokemon_height.config(font=("Arial, 20"))
pokemon_height.pack(padx=10, pady=10)

pokemon_weight = tk.Label(window)
pokemon_weight.config(font=("Arial, 20"))
pokemon_weight.pack(padx=10, pady=10)


pokemon_base = tk.Label(window)
pokemon_base.config(font=("Arial, 20"))
pokemon_base.pack(padx=10, pady=10)




def load_pokemon():
    pokemon = pypokedex.get(name=text_id_name.get(1.0 , "end-1c"))

    http = urllib3.PoolManager()
    response = http.request('GET', pokemon.sprites.front.get('default'))
    image = PIL.Image.open(BytesIO(response.data))
    
    img = PIL.ImageTk.PhotoImage(image)
    pokemon_image.config(image=img)
    pokemon_image.image = img

    pokemon_info.config(text=f"{pokemon.dex} - {pokemon.name}".title())
    pokemon_types.config(text= " - ".join(([t for t in pokemon.types])).title())

    pokemon_height.config(text=f"Height:{pokemon.height} dm")
    pokemon_weight.config(text=f"Weight:{pokemon.weight} hg")
    pokemon_base.config(text= f"Stats: {pokemon.base_stats}")


label_id_name = tk.Label(window,text="ID or NAME")
label_id_name.config(font=("Arial, 20"))
label_id_name.pack(padx=10, pady=10)


text_id_name = tk.Text(window,height=1)
text_id_name.config(font=("Arial, 20"))
text_id_name.pack(padx=10, pady=10)


btn_load = tk.Button(window, text="Load Pokemon", command=load_pokemon)
btn_load.config(font=("Arial, 20"))
btn_load.pack(padx=10, pady=10)

window.mainloop()