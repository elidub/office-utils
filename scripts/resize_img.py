import os
from PIL import Image

def resize_and_place_on_black(image_path, output_path, resize_factor):
    # Open the image
    original_image = Image.open(image_path)

    org_width, org_height = org_size = original_image.size
    new_width, new_height = int(org_width / resize_factor), int(org_height / resize_factor)

    # Resize the image
    resized_image = original_image.resize((new_width, new_height))

    # Create a black background image
    black_background = Image.new("RGB", org_size, "black")
    

    # Paste the resized image onto the black background
    black_background.paste(resized_image, ((org_width-new_width)// 2, (org_height-new_height) // 2))

    # Save the result
    black_background.save(output_path)

if __name__ == '__main__':
    # Example usage
    fig_dir = os.path.join(os.path.expanduser('~'), 'Pictures')
    input_image_path = os.path.join(fig_dir, 'ararat.jpeg')
    output_image_path = os.path.join(fig_dir, 'ararat_smalll.jpg')

    resize_and_place_on_black(input_image_path, output_image_path, resize_factor = 2.)

    print('Done!')
