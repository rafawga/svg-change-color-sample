import xml.etree.ElementTree as ET

def is_green(color):
    """Check if a given hex color code is a shade of green."""
    if color.startswith('#') and len(color) == 7:
        r = int(color[1:3], 16)
        g = int(color[3:5], 16)
        b = int(color[5:7], 16)
        # A simple heuristic: green values are significantly higher than red and blue
        return g > r and g > b
    return False

def change_green_to_color(svg_path, new_color, output_path):
    # Load the SVG file
    tree = ET.parse(svg_path)
    root = tree.getroot()

    # Iterate over all elements and modify green colors to the new color
    for element in root.iter():
        fill = element.get('fill')
        stroke = element.get('stroke')

        # Check and change fill color if it is a shade of green
        if fill and is_green(fill.lower()):
            element.set('fill', new_color)  # Change to the new color

        # Check and change stroke color if it is a shade of green
        if stroke and is_green(stroke.lower()):
            element.set('stroke', new_color)  # Change to the new color

    # Save the modified SVG
    tree.write(output_path)
    print(f"Modified SVG saved at: {output_path}")

# Paths for the input and output SVG files
svg_path = "C:/Users/rafaw/Downloads/Certificate.svg"  # Replace with the path to your input SVG
output_path = "C:/Users/rafaw/Downloads/CertificateMOdifeed.svg"  # Replace with the path for the modified output SVG

# Variable to set the desired replacement color (e.g., blue)
new_color = "#8a16b8"  # Change this to the color you want to use

# Call the function to change green shades to the chosen color
change_green_to_color(svg_path, new_color, output_path)
