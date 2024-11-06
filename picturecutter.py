from PIL import Image
import os

def cut_image_into_pieces(input_image_path, output_dir, rows=4, cols=4):
    # Open the input image
    image = Image.open(input_image_path)
    
    # Get the dimensions of the image
    width, height = image.size
    
    # Calculate the width and height of each piece
    piece_width = width // cols
    piece_height = height // rows
    
    # Make the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Loop through each row and column to extract and save the pieces
    piece_number = 0
    for row in range(rows):
        for col in range(cols):
            # Calculate the box to crop the image
            left = col * piece_width
            upper = row * piece_height
            right = left + piece_width
            lower = upper + piece_height
            
            # Crop the image to get the piece
            piece = image.crop((left, upper, right, lower))
            
            # Save the piece with the appropriate name
            piece_filename = f"piece_{row}_{col}.png"
            piece.save(os.path.join(output_dir, piece_filename))
            print(f"Saved: {piece_filename}")
    
    print(f"Finished cutting the image into {rows}x{cols} pieces.")

# Example usage
input_image_path = 'input_image.png'  # Path to your input image
output_dir = 'output_pieces'          # Directory to save the pieces
cut_image_into_pieces(input_image_path, output_dir)
