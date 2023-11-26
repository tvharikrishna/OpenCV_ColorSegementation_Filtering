import cv2
import numpy as np
import os

def color_spaces(colorcode: str, image_path: str, save_path: str):

    # Load the image
    frame = cv2.imread(image_path)

    if frame is None:
        print('Image not found')
        return

    # Define color ranges for filtering with expanded blue range
    color_ranges = {
        'blue_lower': ([90, 150, 150], [130, 255, 255]),  
        'blue_upper': ([80, 150, 150], [100, 255, 255]),

        'green': ([67, 200, 200], [87, 255, 255]),

        'yellow': ([17, 132, 200], [37, 232, 255]),

        'red_lower': ([0, 202, 185], [15, 255, 255]),
        'red_upper': ([160, 202, 185], [179, 255, 255])
    }

    # Convert to different color spaces
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Ensure the save path exists
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    # Function to save images without adding text
    def save_image(image, save_name):
        cv2.imwrite(os.path.join(save_path, save_name), image)

    # Apply color filter based on the colorcode
    if colorcode == 'blue':
        # For blue, we need to combine two ranges
        lower_blue1, upper_blue1 = color_ranges['blue_lower']
        lower_blue2, upper_blue2 = color_ranges['blue_upper']
        lower_blue1 = np.array(lower_blue1, dtype="uint8")
        upper_blue1 = np.array(upper_blue1, dtype="uint8")
        lower_blue2 = np.array(lower_blue2, dtype="uint8")
        upper_blue2 = np.array(upper_blue2, dtype="uint8")
        mask1 = cv2.inRange(hsv, lower_blue1, upper_blue1)
        mask2 = cv2.inRange(hsv, lower_blue2, upper_blue2)
        mask = cv2.bitwise_or(mask1, mask2)
    elif colorcode == 'red':
        # For red, we need to combine two ranges
        lower_red1, upper_red1 = color_ranges['red_lower']
        lower_red2, upper_red2 = color_ranges['red_upper']
        lower_red1 = np.array(lower_red1, dtype="uint8")
        upper_red1 = np.array(upper_red1, dtype="uint8")
        lower_red2 = np.array(lower_red2, dtype="uint8")
        upper_red2 = np.array(upper_red2, dtype="uint8")
        mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
        mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
        mask = cv2.bitwise_or(mask1, mask2)
    else:
        # For other colors, use the single range
        lower, upper = color_ranges[colorcode]
        lower = np.array(lower, dtype="uint8")
        upper = np.array(upper, dtype="uint8")
        mask = cv2.inRange(hsv, lower, upper)

    filtered = cv2.bitwise_and(frame, frame, mask=mask)

    # Save all frames without text
    save_image(frame, '1.Original_Image.png')
    save_image(gray, '2.Grayscale_Image.png')
    save_image(hsv, '3.HSV_Image.png')
    save_image(mask, '4.Threshold_Image.png')
    save_image(filtered, colorcode + '_Filtered_Color_Image.png')

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":

    # Path to your Image
    image_path = 'data\original_Image.png'  # Replace with the actual path to your image
    
    # Directory to save the images
    save_path = 'generated_images' # Replace with the actual path to your save directory
    
    # Enter the color that you want to filter out 
    color_spaces('red', image_path, save_path)  # Use 'green' as the colorcode to test the green segmentation