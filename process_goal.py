from PIL import Image
import os

# Path to the GENERATED image
path = '/Users/CraveAsia/.gemini/antigravity/brain/54ecfb3b-778d-4848-922b-504f0f3a57ea/goal_post_modern_1768525707213.png'
output_path = '/Users/CraveAsia/.gemini/antigravity/scratch/aliens_vs_malaysians/assets/goal_v3.png'

print(f"Processing {path}...")
try:
    img = Image.open(path)
    img = img.convert("RGBA")
    datas = img.getdata()
    
    # Target Background Color (Black for generated images)
    bg_r, bg_g, bg_b = 0, 0, 0
    
    print(f"Target Removal Color: R={bg_r} G={bg_g} B={bg_b}")
    
    tolerance = 30 # Tighter tolerance for black
    new_data = []
    
    for item in datas:
        r, g, b = item[0], item[1], item[2]
        
        # Check strict black/near-black
        if r < tolerance and g < tolerance and b < tolerance:
            new_data.append((0, 0, 0, 0)) # Fully Transparent
        else:
            new_data.append(item)
            
    img.putdata(new_data)
    img.save(output_path, "PNG")
    print(f"Successfully processed and saved to {output_path}")

except Exception as e:
    print(f"Error: {e}")
