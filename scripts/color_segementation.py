"""
Author: Hari Krishna
Github: tvharikrishna
Linkedin: www.linkedin.com/in/tvharikrishna
"""



import cv2
import numpy as np
import os

class ColorSpaceProcessor:
    """
    A class to process an image in different color spaces and extract specified colors.
    """

    def __init__(self, image_path, save_path):
        """
        Initialize the processor with the image path and save path.

        :param image_path: Path to the image file.
        :param save_path: Path where the processed images will be saved.
        """
        self.image_path = image_path
        self.save_path = save_path
        self.frame = cv2.imread(image_path)
        if self.frame is None:
            raise FileNotFoundError("Image not found at provided path.")
        self.color_ranges = {

            # Filter out blue color and range
            'blue_lower': ([90, 150, 150], [130, 255, 255]),  
            'blue_upper': ([80, 150, 150], [100, 255, 255]),

            # Filter out green color
            'green': ([67, 200, 200], [87, 255, 255]),

            # Filter out yellow color
            'yellow': ([17, 132, 200], [37, 232, 255]),

            # Filter out red color
            'red_lower': ([0, 202, 185], [15, 255, 255]),
            'red_upper': ([160, 202, 185], [179, 255, 255])
        }

    def process_color_space(self, colorcode):
        """
        Process the image to extract the specified color and save the results.

        :param colorcode: The color to be extracted from the image.
        """
        # Convert to different color spaces
        gray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
        hsv = cv2.cvtColor(self.frame, cv2.COLOR_BGR2HSV)

        # Ensure the save path exists
        if not os.path.exists(self.save_path):
            os.makedirs(self.save_path)

        # Apply color filter based on the colorcode
        mask = self.apply_color_filter(hsv, colorcode)

        filtered = cv2.bitwise_and(self.frame, self.frame, mask=mask)

        # Save all frames without text
        self.save_image(self.frame, '1.Original_Image.png')
        self.save_image(gray, '2.Grayscale_Image.png')
        self.save_image(hsv, '3.HSV_Image.png')
        self.save_image(mask, '4.Threshold_Image.png')
        self.save_image(filtered, f'{colorcode}_Filtered_Color_Image.png')

        cv2.destroyAllWindows()

    def apply_color_filter(self, hsv, colorcode):
        """
        Apply the color filter based on the specified colorcode.

        :param hsv: The HSV representation of the image.
        :param colorcode: The color to be filtered.
        :return: The mask after applying the color filter.
        """
        if colorcode in ['blue', 'red']:
            lower1, upper1 = self.color_ranges[f'{colorcode}_lower']
            lower2, upper2 = self.color_ranges[f'{colorcode}_upper']
            mask1 = cv2.inRange(hsv, np.array(lower1, dtype="uint8"), np.array(upper1, dtype="uint8"))
            mask2 = cv2.inRange(hsv, np.array(lower2, dtype="uint8"), np.array(upper2, dtype="uint8"))
            return cv2.bitwise_or(mask1, mask2)
        else:
            lower, upper = self.color_ranges[colorcode]
            return cv2.inRange(hsv, np.array(lower, dtype="uint8"), np.array(upper, dtype="uint8"))

    def save_image(self, image, save_name):
        """
        Save the given image with the specified filename.

        :param image: The image to be saved.
        :param save_name: The filename for the saved image.
        """
        cv2.imwrite(os.path.join(self.save_path, save_name), image)


if __name__ == "__main__":
    # Path to your Image
    image_path = 'scripts/data/original_Image.png'
    
    # Directory to save the images
    save_path = 'scripts/generated_images'
    
    # Create an instance of ColorSpaceProcessor
    processor = ColorSpaceProcessor(image_path, save_path)
    
    # Enter the color that you want to filter out
    processor.process_color_space('red')