from PIL import Image, ImageDraw, ImageFont
import os

def create_bpms_icon(size, filename):
    """Create BPMS branded icon"""
    # Ensure directory exists
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    # Create image with blue background
    img = Image.new('RGB', (size, size), color='#0d6efd')
    draw = ImageDraw.Draw(img)
    
    # Draw outer circle border (convert to integer)
    outer_width = int(size * 0.03)
    draw.ellipse((int(size*0.05), int(size*0.05), int(size*0.95), int(size*0.95)), 
                 outline='white', width=outer_width)
    
    # Draw inner circle (convert to integer)
    inner_width = int(size * 0.02)
    draw.ellipse((int(size*0.12), int(size*0.12), int(size*0.88), int(size*0.88)), 
                 fill='#0d6efd', outline='white', width=inner_width)
    
    # Draw "BP" text
    try:
        # Try to use a system font
        font = ImageFont.truetype("arial.ttf", size//3)
    except:
        # Fallback to default font
        font = ImageFont.load_default()
    
    # Center the text
    text = "BP"
    # Get text bounding box
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    x = (size - text_width) // 2
    y = (size - text_height) // 2 - 5
    draw.text((x, y), text, fill='white', font=font)
    
    # Save the image
    img.save(filename)
    print(f"✅ Created: {filename}")

# Create icons
create_bpms_icon(192, 'suppliers/static/images/icon-192x192.png')
create_bpms_icon(512, 'suppliers/static/images/icon-512x512.png')

print("\n🎉 BPMS Portal icons created successfully!")
print("📁 Location: suppliers/static/images/")