from PIL import Image, ImageDraw

# Define flag dimensions
width, height = 450, 300

# Create a white background
flag = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(flag)

# Draw saffron stripe
draw.rectangle([0, 0, width, height // 3], fill="#FF9933")

# Draw white stripe
draw.rectangle([0, height // 3, width, 2 * height // 3], fill="white")

# Draw green stripe
draw.rectangle([0, 2 * height // 3, width, height], fill="#138808")

# Draw Ashoka Chakra
chakra_radius = min(width, height) // 6
draw.ellipse(
    [
        width // 2 - chakra_radius,
        height // 2 - chakra_radius,
        width // 2 + chakra_radius,
        height // 2 + chakra_radius,
    ],
    outline="#000080",
    width=chakra_radius // 15,
)

# Draw 24 spokes
for i in range(24):
    angle = i * (360 / 24)
    x1 = (
        width // 2 + chakra_radius * 0.85 * -1
        if i % 2 == 0
        else width // 2 + chakra_radius * 0.85 * -1.25
    )
    y1 = height // 2
    x2 = width // 2 + chakra_radius * 0.85 * -0.25
    y2 = height // 2
    draw.line([(x1, y1), (x2, y2)], fill="#000080", width=chakra_radius // 30)

# Save the flag image
flag.save("indian_flag.png")
flag.show()
