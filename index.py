from PIL import Image, ImageDraw, ImageFont
import os

def create_volleyball_meme(expectation_image_path, reality_image_path, output_path="CSELEC3_3A_CalisoRhetteLendle_Activity1.png"):
    
    canvas_width = 1000
    canvas_height = 600
    
    img_width = 450
    img_height = 350
    
    canvas = Image.new('RGB', (canvas_width, canvas_height), 'white')
    draw = ImageDraw.Draw(canvas)
    
    try:
        title_font = ImageFont.truetype("arial.ttf", 48)
        label_font = ImageFont.truetype("arial.ttf", 36)
    except:
        try:
            title_font = ImageFont.truetype("Arial Bold.ttf", 48)
            label_font = ImageFont.truetype("Arial Bold.ttf", 36)
        except:
            title_font = ImageFont.load_default()
            label_font = ImageFont.load_default()
    
    title = "INTRAMURALS"
    title_bbox = draw.textbbox((0, 0), title, font=title_font)
    title_width = title_bbox[2] - title_bbox[0]
    title_x = (canvas_width - title_width) // 2
    draw.text((title_x, 30), title, fill='black', font=title_font)
    
    try:
        expectation_img = Image.open(expectation_image_path)
        expectation_img = expectation_img.resize((img_width, img_height), Image.Resampling.LANCZOS)
    except Exception as e:
        print(f"Error loading expectation image: {e}")
        expectation_img = Image.new('RGB', (img_width, img_height), 'lightgray')
        placeholder_draw = ImageDraw.Draw(expectation_img)
        placeholder_draw.text((img_width//2-50, img_height//2-10), "IMAGE NOT FOUND", fill='black')
    
    try:
        reality_img = Image.open(reality_image_path)
        reality_img = reality_img.resize((img_width, img_height), Image.Resampling.LANCZOS)
    except Exception as e:
        print(f"Error loading reality image: {e}")
        reality_img = Image.new('RGB', (img_width, img_height), 'lightgray')
        placeholder_draw = ImageDraw.Draw(reality_img)
        placeholder_draw.text((img_width//2-50, img_height//2-10), "IMAGE NOT FOUND", fill='black')
    
    expectation_x = 25
    reality_x = canvas_width - img_width - 25
    image_y = 120
    
    canvas.paste(expectation_img, (expectation_x, image_y))
    canvas.paste(reality_img, (reality_x, image_y))
    
    draw.rectangle([expectation_x-2, image_y-2, expectation_x+img_width+2, image_y+img_height+3], 
                  outline='white', width=3) 
    draw.rectangle([reality_x-2, image_y-2, reality_x+img_width+2, image_y+img_height+3], 
                  outline='white', width=3)
    
    expectation_label = "EXPECTATION"
    reality_label = "REALITY"
    
    exp_bbox = draw.textbbox((0, 0), expectation_label, font=label_font)
    exp_width = exp_bbox[2] - exp_bbox[0]
    exp_x = expectation_x + (img_width - exp_width) // 2
    
    real_bbox = draw.textbbox((0, 0), reality_label, font=label_font)
    real_width = real_bbox[2] - real_bbox[0]
    real_x = reality_x + (img_width - real_width) // 2
    
    label_y = image_y + img_height + 30

    draw.text((exp_x, label_y), expectation_label, fill='black', font=label_font)
    draw.text((real_x, label_y), reality_label, fill='black', font=label_font)
    
    canvas.save(output_path, 'PNG', quality=95)
    print(f"Meme saved as: {output_path}")
    
    return canvas

def main():
    
    possible_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.gif']
    
    expectation_path = None
    reality_path = None
    
    for ext in possible_extensions:
        if os.path.exists(f'expectation{ext}'):
            expectation_path = f'expectation{ext}'
            break
    
    for ext in possible_extensions:
        if os.path.exists(f'reality{ext}'):
            reality_path = f'reality{ext}'
            break
    
    if not expectation_path or not reality_path:
        print("Could not find 'expectation' and 'reality' images.")
        print("Available images in current directory:")
        for file in os.listdir('.'):
            if any(file.lower().endswith(ext) for ext in possible_extensions):
                print(f"  - {file}")
        
        expectation_path = input("Enter path to expectation image (or press Enter to use default): ").strip()
        reality_path = input("Enter path to reality image (or press Enter to use default): ").strip()
        
        if not expectation_path:
            expectation_path = "expectation.jpg"
        if not reality_path:
            reality_path = "reality.jpg"
    
    try:
        create_volleyball_meme(expectation_path, reality_path)
        print("\nSuccess! Your volleyball intramurals meme has been created!")
    except Exception as e:
        print(f"Error creating meme: {e}")

if __name__ == "__main__":
    main()