import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
import threading
import torch
from diffusers import StableDiffusionPipeline


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


print("Loading Stable Diffusion model... This may take a while.")
model_id = "runwayml/stable-diffusion-v1-5"
device = "cuda" if torch.cuda.is_available() else "cpu"

pipe = StableDiffusionPipeline.from_pretrained(
    model_id,
    torch_dtype=torch.float16 if device == "cuda" else torch.float32,
    safety_checker=None,
)
pipe = pipe.to(device)
pipe.enable_attention_slicing()


app = ctk.CTk()
app.geometry("540x700")
app.title("Stable Diffusion Text to Image")


canvas = tk.Canvas(app, width=512, height=512, bg="black", highlightthickness=0)
canvas.place(x=14, y=140)


prompt_input = ctk.CTkEntry(app, width=512, height=40, placeholder_text="Enter prompt here...")
prompt_input.place(x=14, y=50)


status_label = ctk.CTkLabel(app, text="")
status_label.place(x=14, y=100)


tk_img = None
generated_image = None


def generate_image():
    global tk_img, generated_image

    prompt = prompt_input.get()
    if not prompt.strip():
        status_label.configure(text="Please enter a prompt.", text_color="red")
        return

    status_label.configure(text="Generating image, please wait...", text_color="white")
    app.update_idletasks()

    try:

        image = pipe(prompt, num_inference_steps=15).images[0]
        generated_image = image


        tk_img = ImageTk.PhotoImage(image)
        canvas.delete("all")
        canvas.create_image(0, 0, anchor=tk.NW, image=tk_img)

        status_label.configure(text="Image generated successfully!", text_color="green")
    except Exception as e:
        status_label.configure(text=f"Error: {str(e)}", text_color="red")


def threaded_generate():

    threading.Thread(target=generate_image, daemon=True).start()


def save_image():
    global generated_image
    if generated_image is None:
        status_label.configure(text="No image to save!", text_color="red")
        return

    filename = prompt_input.get().strip().replace(" ", "_") or "image"
    try:
        generated_image.save(f"{filename}.png")
        status_label.configure(text=f"Image saved as {filename}.png", text_color="green")
    except Exception as e:
        status_label.configure(text=f"Error saving image: {str(e)}", text_color="red")



generate_button = ctk.CTkButton(app, text="Generate Image", command=threaded_generate, width=120, height=40)
generate_button.place(x=100, y=600)

save_button = ctk.CTkButton(app, text="Save Image", command=save_image, width=120, height=40)
save_button.place(x=320, y=600)

app.mainloop()




