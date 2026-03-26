"""
Generate an animated terminal GIF for the GitHub README
This script creates frame-by-frame animation of the terminal commands
"""

from PIL import Image, ImageDraw, ImageFont
import os

# Configuration
OUTPUT_PATH = "assets/terminal-animation.gif"
FRAME_DURATION = 80  # milliseconds per frame
WIDTH, HEIGHT = 1000, 600
BG_COLOR = (30, 30, 30)  # Dark background
BORDER_COLOR = (102, 126, 234)  # Blue-purple
TEXT_COLOR = (0, 255, 0)  # Neon green
PROMPT_COLOR = (102, 126, 234)  # Blue-purple for $
OUTPUT_COLOR = (255, 255, 255)  # White
TAG_COLOR = (255, 107, 107)  # Red for >
SUCCESS_COLOR = (0, 255, 0)  # Green for ✓
GOLD_COLOR = (255, 215, 0)  # Gold for name

# Font setup
try:
    # Try to use a monospace font
    font_large = ImageFont.truetype("C:\\Windows\\Fonts\\consolas.ttf", 18)
    font_small = ImageFont.truetype("C:\\Windows\\Fonts\\consolas.ttf", 16)
except:
    # Fallback to default font
    font_large = ImageFont.load_default()
    font_small = ImageFont.load_default()

frames = []

def create_base_image():
    """Create a base image with the terminal border"""
    img = Image.new('RGB', (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    
    # Draw border
    border_width = 3
    draw.rectangle(
        [(40, 30), (WIDTH - 40, HEIGHT - 30)],
        outline=BORDER_COLOR,
        width=border_width
    )
    
    return img, draw

def draw_text(draw, x, y, text, color, font):
    """Draw text at specified position"""
    draw.text((x, y), text, fill=color, font=font)

def add_frame(frames, img):
    """Add a frame to the animation"""
    frames.append(img.copy())

# ========== FRAME SEQUENCE ==========

# Frame 1: Empty terminal
img, draw = create_base_image()
add_frame(frames, img)

# Frames 2-9: Type "$ whoami" character by character
whoami_cmd = "$ whoami"
for i in range(len(whoami_cmd) + 1):
    img, draw = create_base_image()
    cmd_text = whoami_cmd[:i]
    draw.text((70, 70), cmd_text, fill=TEXT_COLOR, font=font_large)
    # Draw cursor
    draw.rectangle([(70 + len(cmd_text) * 11, 70), (75 + len(cmd_text) * 11, 92)], fill=TEXT_COLOR)
    add_frame(frames, img)

# Frames: Show whoami output (hold for a few frames)
for _ in range(3):
    img, draw = create_base_image()
    draw.text((70, 70), "$ whoami", fill=TEXT_COLOR, font=font_large)
    draw.text((70, 120), "Newtan Ananda Gopal Mukhopadhyay", fill=GOLD_COLOR, font=font_large)
    add_frame(frames, img)

# Frames: Type "$ cat interests.txt" character by character
cat_cmd = "$ cat interests.txt"
for i in range(len(cat_cmd) + 1):
    img, draw = create_base_image()
    draw.text((70, 70), "$ whoami", fill=TEXT_COLOR, font=font_large)
    draw.text((70, 120), "Newtan Ananda Gopal Mukhopadhyay", fill=GOLD_COLOR, font=font_large)
    cmd_text = cat_cmd[:i]
    draw.text((70, 170), cmd_text, fill=TEXT_COLOR, font=font_large)
    # Draw cursor
    draw.rectangle([(70 + len(cmd_text) * 11, 170), (75 + len(cmd_text) * 11, 192)], fill=TEXT_COLOR)
    add_frame(frames, img)

# Frames: Show interests box appearing line by line
interests_lines = [
    "> System Design Enthusiast",
    "> Algorithm Optimization Expert",
    "> Distributed Systems Builder",
    "> Problem Solver | Mentor | Learner"
]

for num_lines in range(len(interests_lines) + 1):
    img, draw = create_base_image()
    draw.text((70, 70), "$ whoami", fill=TEXT_COLOR, font=font_large)
    draw.text((70, 120), "Newtan Ananda Gopal Mukhopadhyay", fill=GOLD_COLOR, font=font_large)
    draw.text((70, 170), "$ cat interests.txt", fill=TEXT_COLOR, font=font_large)
    
    # Draw box
    box_y = 210
    draw.rectangle([(80, box_y), (920, box_y + 140)], outline=BORDER_COLOR, width=2)
    
    # Draw interests lines
    for idx in range(num_lines):
        line_y = box_y + 20 + (idx * 28)
        draw.text((100, line_y), interests_lines[idx], fill=OUTPUT_COLOR, font=font_small)
    
    add_frame(frames, img)

# Hold on full interests box
for _ in range(3):
    img, draw = create_base_image()
    draw.text((70, 70), "$ whoami", fill=TEXT_COLOR, font=font_large)
    draw.text((70, 120), "Newtan Ananda Gopal Mukhopadhyay", fill=GOLD_COLOR, font=font_large)
    draw.text((70, 170), "$ cat interests.txt", fill=TEXT_COLOR, font=font_large)
    
    box_y = 210
    draw.rectangle([(80, box_y), (920, box_y + 140)], outline=BORDER_COLOR, width=2)
    
    for idx in range(len(interests_lines)):
        line_y = box_y + 20 + (idx * 28)
        draw.text((100, line_y), interests_lines[idx], fill=OUTPUT_COLOR, font=font_small)
    
    add_frame(frames, img)

# Frames: Type "$ npm run build-dreams" character by character
npm_cmd = "$ npm run build-dreams"
for i in range(len(npm_cmd) + 1):
    img, draw = create_base_image()
    draw.text((70, 70), "$ whoami", fill=TEXT_COLOR, font=font_large)
    draw.text((70, 120), "Newtan Ananda Gopal Mukhopadhyay", fill=GOLD_COLOR, font=font_large)
    draw.text((70, 170), "$ cat interests.txt", fill=TEXT_COLOR, font=font_large)
    
    box_y = 210
    draw.rectangle([(80, box_y), (920, box_y + 140)], outline=BORDER_COLOR, width=2)
    
    for idx in range(len(interests_lines)):
        line_y = box_y + 20 + (idx * 28)
        draw.text((100, line_y), interests_lines[idx], fill=OUTPUT_COLOR, font=font_small)
    
    cmd_text = npm_cmd[:i]
    draw.text((70, 380), cmd_text, fill=TEXT_COLOR, font=font_large)
    # Draw cursor
    draw.rectangle([(70 + len(cmd_text) * 11, 380), (75 + len(cmd_text) * 11, 402)], fill=TEXT_COLOR)
    add_frame(frames, img)

# Frames: Show npm output appearing line by line
build_output = [
    "🚀 Building scalable solutions...",
    "✓ System architectures designed",
    "✓ Algorithms optimized",
    "✓ Impact created at scale"
]

for num_lines in range(len(build_output) + 1):
    img, draw = create_base_image()
    draw.text((70, 70), "$ whoami", fill=TEXT_COLOR, font=font_large)
    draw.text((70, 120), "Newtan Ananda Gopal Mukhopadhyay", fill=GOLD_COLOR, font=font_large)
    draw.text((70, 170), "$ cat interests.txt", fill=TEXT_COLOR, font=font_large)
    
    box_y = 210
    draw.rectangle([(80, box_y), (920, box_y + 140)], outline=BORDER_COLOR, width=2)
    
    for idx in range(len(interests_lines)):
        line_y = box_y + 20 + (idx * 28)
        draw.text((100, line_y), interests_lines[idx], fill=OUTPUT_COLOR, font=font_small)
    
    draw.text((70, 380), "$ npm run build-dreams", fill=TEXT_COLOR, font=font_large)
    
    # Draw output lines
    output_y = 420
    for idx in range(num_lines):
        draw.text((100, output_y + (idx * 28)), build_output[idx], fill=OUTPUT_COLOR, font=font_small)
    
    add_frame(frames, img)

# Hold on complete terminal
for _ in range(5):
    img, draw = create_base_image()
    draw.text((70, 70), "$ whoami", fill=TEXT_COLOR, font=font_large)
    draw.text((70, 120), "Newtan Ananda Gopal Mukhopadhyay", fill=GOLD_COLOR, font=font_large)
    draw.text((70, 170), "$ cat interests.txt", fill=TEXT_COLOR, font=font_large)
    
    box_y = 210
    draw.rectangle([(80, box_y), (920, box_y + 140)], outline=BORDER_COLOR, width=2)
    
    for idx in range(len(interests_lines)):
        line_y = box_y + 20 + (idx * 28)
        draw.text((100, line_y), interests_lines[idx], fill=OUTPUT_COLOR, font=font_small)
    
    draw.text((70, 380), "$ npm run build-dreams", fill=TEXT_COLOR, font=font_large)
    
    output_y = 420
    for idx in range(len(build_output)):
        draw.text((100, output_y + (idx * 28)), build_output[idx], fill=OUTPUT_COLOR, font=font_small)
    
    add_frame(frames, img)

# ========== SAVE GIF ==========

# Create assets directory if it doesn't exist
os.makedirs("assets", exist_ok=True)

# Save as animated GIF
frames[0].save(
    OUTPUT_PATH,
    save_all=True,
    append_images=frames[1:],
    duration=FRAME_DURATION,
    loop=0,  # Loop forever
    optimize=False
)

print(f"✓ Animated GIF created successfully: {OUTPUT_PATH}")
print(f"✓ Total frames: {len(frames)}")
print(f"✓ Duration per frame: {FRAME_DURATION}ms")
print(f"✓ Total animation time: {len(frames) * FRAME_DURATION / 1000:.1f} seconds")
