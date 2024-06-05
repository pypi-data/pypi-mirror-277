import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
from PIL import Image
from lang_sam import LangSAM
import torch
import matplotlib.pyplot as plt
import cv2
import numpy as np
from PIL import Image
import os
from sklearn.decomposition import PCA
from scipy.ndimage import rotate
import cv2
import os
import numpy as np

def process_video(video_files, video_path, output_path, initial_point=(500, 600)):
    for i in video_files:
        cap = cv2.VideoCapture(os.path.join(video_path, i))    
        print(os.path.join(video_path, i))

        # Take first frame
        ret, old_frame = cap.read()
        old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)
        
        # Set the initial tracking point
        p0 = np.array([[list(initial_point)]], dtype=np.float32)

        if not os.path.exists(output_path):
            os.makedirs(output_path)

        # Define the codec and create a VideoWriter object
        fourcc = cv2.VideoWriter_fourcc(*'mp4v') 
        out = cv2.VideoWriter(os.path.join(output_path, f'{i.split(".")[0]}.mp4'), fourcc, 30.0, (old_frame.shape[1], old_frame.shape[0]))
        
        while True:
            ret, frame = cap.read()
            
            # Break the loop if the frame can't be read
            if not ret:
                break
        
            frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
            # Calculate optical flow using Farneback method
            flow = cv2.calcOpticalFlowFarneback(old_gray, frame_gray, None, 0.5, 3, 15, 3, 5, 1.2, 0)
        
            # Update the tracking point
            p0 += flow[int(p0[0,0,1]), int(p0[0,0,0])]
        
            # Draw the tracking point
            a, b = map(int, p0[0,0])
            frame = cv2.circle(frame, (a, b), 5, (0, 0, 255), -1)  # Red color
        
            # Write the frame into the file 'output.mp4'
            out.write(frame)
        
            # Now update the previous frame
            old_gray = frame_gray.copy()

        # Release the VideoCapture and VideoWriter objects and close all windows
        cap.release()
        out.release()

def get_angle(input_matrix):
    coordinate_array = np.array(np.where(input_matrix > 0)).T
    pca_analysis = PCA(n_components=2).fit(coordinate_array)
    angle_values = np.arctan2(pca_analysis.components_[:,1], pca_analysis.components_[:,0])
    angle_values = np.rad2deg(angle_values)
    angle_values = np.mod(angle_values, 180)
    if abs(90 - angle_values[0]) < 30:
        chosen_angle = angle_values[0]
    else:
        chosen_angle = angle_values[1]
    return 90 - chosen_angle

def slope_and_intercept(input_line):
    point1_x, point1_y, point2_x, point2_y = input_line
    calculated_slope = (point2_x - point1_x) / (point2_y - point1_y)
    calculated_intercept = point1_x - (calculated_slope * point1_y)
    return calculated_slope, calculated_intercept

def line_getter(input_slope, input_intercept, input_shape):
    coordinate_x1 = int(input_intercept)
    coordinate_y1 = 0
    coordinate_x2 = int(input_slope * input_shape[0] + input_intercept)
    coordinate_y2 = input_shape[0]
    return coordinate_x1, coordinate_y1, coordinate_x2, coordinate_y2

def boundry_locator(input_res, input_pca_angle):
    shape_dimensions = input_res.shape
    high_percent_inliers = 0.60
    low_percent_inliers = 0.50
    depth_mask_filtered = (input_res > 0) * 1
    rotated_depth_mask_filtered = rotate(depth_mask_filtered * 1, input_pca_angle, reshape=False)
    image = rotated_depth_mask_filtered
    initial_row = 0
    final_row = 0
    for i in range(image.shape[0]):
        column = image[i,:]
        if np.any(column):
            initial_row = i
            break
    for i in range(image.shape[0]-1, -1, -1):
        column = image[i,:]
        if np.any(column):
            final_row = i
            break
   
    difference = final_row - initial_row
    rotated_depth_mask_filtered = (np.abs(rotated_depth_mask_filtered) > 0.00) * 1
    left_boundary = 0
    for j in range(shape_dimensions[1]):
        count_values = np.bincount(rotated_depth_mask_filtered[:, j])
        if len(count_values) < 2:
            continue
        if count_values[1] / difference > high_percent_inliers:
            left_boundary = j
            break
    for j in range(left_boundary - 1, -1, -1):
        count_values = np.bincount(rotated_depth_mask_filtered[:, j])
        if len(count_values) < 2:
            continue
        if count_values[1] / difference < low_percent_inliers:
            left_boundary = j + 1
            break


    right_boundary = 0
    for j in range(shape_dimensions[1] - 1, -1, -1):
        count_values = np.bincount(rotated_depth_mask_filtered[:, j])
        if len(count_values) < 2:
            continue
        if count_values[1] / difference > high_percent_inliers:
            right_boundary = j
            break

    for j in range(right_boundary, shape_dimensions[1]):
        count_values = np.bincount(rotated_depth_mask_filtered[:, j])
        if len(count_values) < 2:
            continue
        if count_values[1] / difference < low_percent_inliers:
            right_boundary = j - 1
            break
    return left_boundary, right_boundary

def canvas_rotated_boundary(input_left_boundary, input_right_boundary, input_pca_angle, input_shape):
    left_boundary_canvas = np.zeros(input_shape, dtype=np.uint8)
    right_boundary_canvas = np.zeros(input_shape, dtype=np.uint8)

    left_boundary_canvas[:,input_left_boundary] = 255
    right_boundary_canvas[:,input_right_boundary] = 255

    rotated_left_boundary_canvas = rotate(left_boundary_canvas * 1, -input_pca_angle, reshape=False)
    rotated_right_boundary_canvas = rotate(right_boundary_canvas * 1, -input_pca_angle, reshape=False)

    left_top_point = (0,0)
    left_bottom_point = (0,0)
    for i in range(rotated_left_boundary_canvas.shape[0]):
        column_values = np.where(rotated_left_boundary_canvas[i,:] > 0)[0]
        if column_values.size > 0:
            left_top_point = (column_values[0], i)
            break
    for i in range(rotated_left_boundary_canvas.shape[0] - 1, -1, -1):
        column_values = np.where(rotated_left_boundary_canvas[i,:] > 0)[0]
        if column_values.size > 0:
            left_bottom_point = (column_values[0], i)
            break
    left_line = (left_top_point[0], left_top_point[1], left_bottom_point[0], left_bottom_point[1])

    right_top_point = (0,0)
    right_bottom_point = (0,0)
    for i in range(rotated_right_boundary_canvas.shape[0]):
        column_values = np.where(rotated_right_boundary_canvas[i,:] > 0)[0]
        if column_values.size > 0:
            right_top_point = (column_values[0], i)
            break
    for i in range(rotated_right_boundary_canvas.shape[0] - 1, -1, -1):
        column_values = np.where(rotated_right_boundary_canvas[i,:] > 0)[0]
        if column_values.size > 0:
            right_bottom_point = (column_values[0], i)
            break
    right_line = (right_top_point[0], right_top_point[1], right_bottom_point[0], right_bottom_point[1])

    slope_left, intercept_left = slope_and_intercept(left_line)
    slope_right, intercept_right = slope_and_intercept(right_line)

    new_x1, new_y1 ,new_x2, new_y2 = line_getter(slope_left, intercept_left, input_shape)
    new_x3, new_y3 ,new_x4, new_y4 = line_getter(slope_right, intercept_right, input_shape)

    left_canvas = np.zeros(input_shape, dtype=np.uint8)
    cv2.line(left_canvas, (new_x1, new_y1), (new_x2, new_y2), (255, 255, 255), 2)
    right_canvas = np.zeros(input_shape, dtype=np.uint8)
    cv2.line(right_canvas, (new_x3, new_y3), (new_x4, new_y4), (255, 255, 255), 2)
    return left_canvas, right_canvas, slope_left, intercept_left, slope_right, intercept_right

def borders_to_segmented_images(seg_img,img):
    enh_image = seg_img
    gray_img = cv2.cvtColor(enh_image, cv2.COLOR_BGR2GRAY)
    mask = gray_img > 0
    mask = mask.astype(np.uint8) * 255
    theta = get_angle(mask)
    lb, rb = boundry_locator(mask, theta)
    canvas_left, canvas_right,slope1,intercept1,slope2,intercept2 = canvas_rotated_boundary(lb, rb, theta, mask.shape)
    single_canvas = cv2.bitwise_or(canvas_left, canvas_right)
    single_canvas_rgb = cv2.cvtColor(single_canvas, cv2.COLOR_GRAY2BGR)
    borders_in_image = cv2.bitwise_or(single_canvas_rgb, img)
    return borders_in_image,slope1,intercept1,slope2,intercept2

def borders_to_original_images(img):
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, binary_img = cv2.threshold(gray_img, 160, 255, cv2.THRESH_BINARY)
    mask = binary_img > 0
    mask = mask.astype(np.uint8) * 255
    theta = get_angle(mask)
    lb, rb = boundry_locator(mask, theta)
    canvas_left, canvas_right,slope1,intercept1,slope2,intercept2 = canvas_rotated_boundary(lb, rb, theta, mask.shape)
    single_canvas = cv2.bitwise_or(canvas_left, canvas_right)
    single_canvas_rgb = cv2.cvtColor(single_canvas, cv2.COLOR_GRAY2BGR)
    borders_in_image = cv2.bitwise_or(single_canvas_rgb, img)
    return borders_in_image,slope1,intercept1,slope2,intercept2

def border_lines_cap(video_files, video_path, output_path, text_prompt="Identify and segment the image to isolate any tree trunks present. If multiple tree trunks are detected, focus on segmenting only the largest one. There will atleast one tree trunk in every image", model=LangSAM()):
    for im in video_files:
        cap = cv2.VideoCapture(os.path.join(video_path, im))
        i = 0
        while(cap.isOpened()):
            ret, frame = cap.read()
            if ret == False:
                break

            image_rgb = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

            masks, boxes, phrases, logits = model.predict(image_rgb, text_prompt)
            masks_np = [mask.squeeze().cpu().numpy() for mask in masks]
            fin_img = None

            if len(masks_np) != 0 and len(masks_np[0][:]) != 0:
                seg_img = image_rgb*np.stack([masks_np[0][:]]*3, axis=-1)
                fin_img,slope1,intercept1,slope2,intercept2 = borders_to_segmented_images(seg_img,frame)
                print("slope left:",slope1, "intercept left:",intercept1,"slope right:",slope2,"intercept right:",intercept2)
            else:
                fin_img,slope1,intercept1,slope2,intercept2 = borders_to_original_images(frame)
                print("slope left:",slope1, "intercept left:",intercept1,"slope right:",slope2,"intercept right:",intercept2)

            if not os.path.exists(os.path.join(output_path,im.split(".")[0])):
                os.makedirs(os.path.join(output_path,im.split(".")[0]))

            cv2.imwrite(os.path.join(output_path,im.split(".")[0],f"frame{i}.jpg"),fin_img)
            i += 1
            plt.imshow(fin_img)
            plt.show()
        cap.release()

def create_video(image_folder, output_file):
    command = f"ffmpeg -r 30 -i {image_folder}/frame%01d.jpg -vcodec mpeg4 -y {output_file}"
    os.system(command)