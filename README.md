# Text-to-Image_Stable-Diffusion
##  Features
-  **Stable Diffusion v1.5** integration
-  CustomTkinter-based modern GUI
-  Automatic device selection (CPU/GPU)
-  Prompt-to-image generation with adjustable inference steps
-  Save generated images locally with prompt-based filenames
-  Responsive UI with threaded generation
  # How It Works
## User Input
- Enter a text prompt into the GUI.

## Model Initialization
- Loads runwayml/stable-diffusion-v1-5 using StableDiffusionPipeline.

## Image Generation
- Generates an image using latent diffusion in ~15 inference steps.

## Display & Save
- Renders the image in a 512x512 canvas and allows saving as PNG.
## Configurations
- Inference steps (num_inference_steps=15)
- Output image resolution (default: 512x512)
- Save location (default: local directory)
## Output
![image](https://github.com/user-attachments/assets/6ec43670-ca60-4074-8a4a-869108820d8e)
