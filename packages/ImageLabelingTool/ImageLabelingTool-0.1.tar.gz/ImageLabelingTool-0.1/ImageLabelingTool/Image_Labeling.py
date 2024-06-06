import cv2
import keyboard
import time
import random
import os

class ImageLabeling:
    def __init__(self):
        self.frames = []  # List to store frames
        self.current_frame_index = 0
        self.rect_start = (0, 0)
        self.rect_end = (0, 0)
        self.drawing = False
        self.rectangles = []  # List to store tuples of (rectangle, class_name)
        self.frame_cache = []
        self.frame_index = 0
        self.class_names = {}  # Dictionary to store class names and corresponding rectangles
        self.class_colors = {}  # Dictionary to store class names and corresponding colors
        self.last_selected_class = None  # Variable to store the last selected class name
        self.annotation_changed = False

        self.F_width = 640
        self.F_height = 480

    # -------------------- Input Method --------------------#

    def choose_input(self):
        """
            Allows the user to choose between camera input or video input.
            Returns:
                cap (cv2.VideoCapture): Video capture object.
            """
        while True:
            print("-----------------------------------------------------------------------------------")
            decision = input("Enter '0' for the camera and '1' for video input: ")
            if decision == '0':
                cap = cv2.VideoCapture(0)
                cap.set(3, self.F_width)
                cap.set(4, self.F_height)
                return cap
            elif decision == '1':
                print("-----------------------------------------------------------------------------------")
                video_path = input("Enter the absolute path to the video:")
                print("-----------------------------------------------------------------------------------")
                cap = cv2.VideoCapture(video_path)
                return cap
            else:
                print("Error Occurs!!!\nWrong input!! Please Choose correct option either '0' or '1'")

    # -------------------- Drawing Bbox --------------------#
    def draw_rectangle(self, event, x, y, flags, param):
        """
        Callback function for mouse events to draw rectangles on the image.
        Args:
            event: The mouse event type.
            x: The x-coordinate of the mouse event.
            y: The y-coordinate of the mouse event.
            flags: Additional flags.
            param: Additional parameters.
        """
        if event == cv2.EVENT_LBUTTONDOWN:
            self.drawing = True
            self.rect_start = (x, y)
            self.rect_end = (x, y)
        elif event == cv2.EVENT_MOUSEMOVE:
            if self.drawing:
                self.rect_end = (x, y)
        elif event == cv2.EVENT_LBUTTONUP:
            self.drawing = False
            self.rect_end = (x, y)
            # Scale and append the bounding box coordinates
            scaled_bbox = ((min(self.rect_start[0], self.rect_end[0]), min(self.rect_start[1], self.rect_end[1])),
                           (max(self.rect_start[0], self.rect_end[0]), max(self.rect_start[1], self.rect_end[1])))
            class_name = self.get_class_name()

            self.rectangles.append((scaled_bbox, class_name))

            self.class_names[class_name].append(scaled_bbox)
            self.last_selected_class = class_name
            self.rect_start = (0, 0)
            self.rect_end = (0, 0)

            if not self.drawing:
                self.annotation_changed = True
        elif event == cv2.EVENT_RBUTTONDOWN:
            if self.rectangles:
                last_rectangle = self.rectangles.pop()
                last_class_name = last_rectangle[1]
                self.class_names[last_class_name].remove(last_rectangle[0])
                self.annotation_changed = True
                frame_to_show = self.frame_cache[self.frame_index].copy()
                for rect, class_name in self.rectangles:
                    scaled_rect = ((int(rect[0][0]), int(rect[0][1])),
                                   (int(rect[1][0]), int(rect[1][1])))
                    color = self.class_colors[class_name]
                    cv2.rectangle(frame_to_show, scaled_rect[0], scaled_rect[1], color, 2)
                cv2.imshow('Draw Rectangle', frame_to_show)

    # -------------------- Boundary Box Normalizer --------------------#
    def scale_bbox(self, bbox, img_width, img_height):
        """
        Normalize bounding box coordinates to [0, 1] range.
        Args:
            bbox: Tuple containing the top-left and bottom-right coordinates of the bounding box.
            img_width: Width of the image.
            img_height: Height of the image.
        Returns:
            Tuple: Normalized bounding box coordinates.
        """
        x_min, y_min = bbox[0]
        x_max, y_max = bbox[1]
        scaled_x_min = min(x_min, x_max) / img_width
        scaled_y_min = min(y_min, y_max) / img_height
        scaled_x_max = max(x_min, x_max) / img_width
        scaled_y_max = max(y_min, y_max) / img_height
        return ((scaled_x_min, scaled_y_min), (scaled_x_max, scaled_y_max))

    # -------------------- Loading Class Names --------------------#
    def load_class_names(self, file_path):
        """
        Load class names from a text file.
        Args:
            file_path (str): Path to the text file containing class names.
        """
        if os.path.isfile(file_path):
            with open(file_path, 'r') as f:
                lines = f.readlines()
                self.class_names = {line.strip(): [] for line in lines}

    # -------------------- Getting Class Name --------------------#
    def get_class_name(self):
        """
        Prompt the user to enter a class name for the rectangle.
        Returns:
            str: The selected class name.
        """
        if not self.class_colors:  # Check if class_colors is empty, if so, initialize it
            self.class_colors = {class_name: self.get_random_color() for class_name in self.class_names}
        if self.class_names:
            self.print_class_names()
            class_name_option = input(
                "Enter the class name option for the rectangle ('C' for continue, 'N' for new, 'S' for select): ").upper()
            print("-----------------------------------------------------------------------------------")

            if class_name_option == 'N':
                class_name = input("Enter the new class name for the rectangle: ")
                self.class_names[class_name] = []
                self.class_colors[class_name] = self.get_random_color()  # Assign a random color to the new class
                self.last_selected_class = class_name
                print("-----------------------------------------------------------------------------------")

            elif class_name_option == 'C':
                if self.last_selected_class is not None:
                    class_name = self.last_selected_class
                else:
                    class_name = input("No previous class name selected. Enter the new class name for the rectangle: ")
                self.last_selected_class = class_name
                print("-----------------------------------------------------------------------------------")

            elif class_name_option == 'S':
                index = input("Enter the index of the class name to select from above list: ")
                class_name = list(self.class_names.keys())[int(index)]
                self.last_selected_class = class_name
                print("-----------------------------------------------------------------------------------")

            else:
                print("Invalid option. Please try again.")
                print("-----------------------------------------------------------------------------------")
                while True:
                    class_name_option = input(
                        "Enter the class name option for the rectangle ('C' for continue, 'N' for new, 'S' for select): ").upper()
                    print("-----------------------------------------------------------------------------------")
                    if class_name_option in ['C', 'N', 'S']:
                        break
                    else:
                        print("Invalid option. Please try again.")
                        print("-----------------------------------------------------------------------------------")

        else:
            class_name = input("No class names available. Enter the new class name for the rectangle: ")
            print("-----------------------------------------------------------------------------------")
            self.class_names[class_name] = []
            self.class_colors[class_name] = self.get_random_color()  # Assign a random color to the new class
            self.last_selected_class = class_name
        return class_name

    # -------------------- Printing Class Names --------------------#
    def print_class_names(self):
        """
        Prints the available class names.
        """
        print("Class Names:")
        for i, class_name in enumerate(self.class_names):
            print(f"{i}: {class_name}")

    # -------------------- Saving Class Names --------------------#
    def save_class_names(self, file_path):
        """
        Save class names to a text file.
        Args:
            file_path (str): Path to the text file where class names will be saved.
        """
        with open(file_path, 'w') as f:
            for class_name in self.class_names.keys():
                f.write(f"{class_name}\n")
        print("Class names saved successfully.")
        print("-----------------------------------------------------------------------------------")

    # -------------------- Random Color Generator --------------------#
    def get_random_color(self):
        """
        Generates a random color.
        Returns:
            Tuple: RGB values of the random color.
        """
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # -------------------- Saving Annotations --------------------#
    def save_annotations_yolo(self, file_path):
        """
        Save annotations in YOLO format to a text file.
        Args:
            file_path (str): Path to the text file where annotations will be saved.
        """
        with open(file_path, 'w') as f:
            for idx, (class_name, class_rectangles) in enumerate(self.class_names.items()):
                for rectangle in class_rectangles:
                    x_min, y_min = rectangle[0]
                    x_max, y_max = rectangle[1]
                    scaled_bbox = self.scale_bbox(((x_min, y_min), (x_max, y_max)), self.F_width, self.F_height)
                    x_center = (scaled_bbox[0][0] + scaled_bbox[1][0]) / 2
                    y_center = (scaled_bbox[0][1] + scaled_bbox[1][1]) / 2
                    width = scaled_bbox[1][0] - scaled_bbox[0][0]
                    height = scaled_bbox[1][1] - scaled_bbox[0][1]
                    f.write(f"{idx} {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}\n")
        print("-----------------------------------------------------------------------------------")
        print("Annotations saved successfully.")
        print("-----------------------------------------------------------------------------------")
        self.class_names = {key: [] for key in self.class_names}

    # -------------------- Main Loop --------------------#
    def run(self):
        """
        Main loop of the image labeling tool.
        """
        self.frame_index = 0
        cap = self.choose_input()
        out_path = input("Enter the absolute path for the output folder: ")
        self.load_class_names(f'{out_path}/classes.txt')

        print("Press 'space' to capture the next frame. Press 'ESC' to exit.")
        print("Press and hold the right arrow key to fast forward.")
        print("Press and hold the left arrow key to rewind.")
        print("-----------------------------------------------------------------------------------")

        while True:
            if self.frame_index < len(self.frame_cache):
                img = self.frame_cache[self.frame_index]
            else:
                success, img = cap.read()
                if not success:
                    print("Failed to capture image or end of video reached")
                    break
                img = cv2.resize(img, (self.F_width, self.F_height))
                self.frame_cache.append(img)

            cv2.imshow('frame', img)

            while True:
                if keyboard.is_pressed('space'):
                    self.frame_index += 1
                    break

                if keyboard.is_pressed('right'):
                    self.frame_index += 1
                    if self.frame_index >= len(self.frame_cache):
                        success, img = cap.read()
                        if success:
                            img = cv2.resize(img, (self.F_width, self.F_height))
                            self.frame_cache.append(img)
                            cv2.imshow('frame', img)
                        else:
                            print("Failed to capture image or end of video reached")
                            self.frame_index -= 1
                    else:
                        cv2.imshow('frame', self.frame_cache[self.frame_index])
                    time.sleep(0)

                if keyboard.is_pressed('left'):
                    self.frame_index = max(0, self.frame_index - 1)
                    cv2.imshow('frame', self.frame_cache[self.frame_index])
                    time.sleep(0.01)

                if keyboard.is_pressed('enter'):
                    print("-----------------------------------------------------------------------------------")
                    print("Use left mouse button to draw rectangles.")
                    print("Right-click to redraw the last drawn rectangle.")
                    print("Press 'ESC' to exit.")
                    print("-----------------------------------------------------------------------------------")

                    current_frame = self.frame_cache[self.frame_index].copy()

                    self.rectangles = []  # Create a new empty list for the rectangles

                    cv2.namedWindow('Draw Rectangle')
                    cv2.setMouseCallback('Draw Rectangle', self.draw_rectangle)

                    while True:
                        frame_to_show = current_frame.copy()
                        for rect, class_name in self.rectangles:
                            scaled_rect = ((int(rect[0][0]), int(rect[0][1])),
                                           (int(rect[1][0]), int(rect[1][1])))
                            color = self.class_colors[class_name]
                            cv2.rectangle(frame_to_show, scaled_rect[0], scaled_rect[1], color, 2)
                        if self.drawing:
                            cv2.rectangle(frame_to_show, self.rect_start, self.rect_end, (0, 255, 0), 2)

                        cv2.imshow('Draw Rectangle', frame_to_show)
                        key2 = cv2.waitKey(1) & 0xFF
                        if key2 == 27:
                            break
                    if self.annotation_changed:
                        timestamp = time.strftime("%Y%m%d%H%M%S")
                        self.save_annotations_yolo(f"{out_path}/{timestamp}.txt")

                        cv2.imwrite(f"{out_path}/{timestamp}.jpg", self.frame_cache[self.frame_index])  # Save the last frame

                        self.annotation_changed = False

                    cv2.destroyWindow('Draw Rectangle')

                if cv2.waitKey(1) & 0xFF == 27:
                    self.save_class_names(f'{out_path}/classes.txt')
                    cap.release()
                    cv2.destroyAllWindows()
                    exit()

if __name__ == "__main__":
    image_labeling = ImageLabeling()
    image_labeling.run()
