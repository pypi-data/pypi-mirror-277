import cv2
import matplotlib.pyplot as plt
from skimage.measure import label, regionprops
import pandas as pd
import numpy as np

def imgtotempmat(image_path, min_temperature, max_temperature):
    # Read the thermal RGB image
    image = cv2.imread(image_path)

    # Convert the RGB image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Calculate the temperature matrix
    temperature_matrix = (gray_image / 255.0) * (max_temperature - min_temperature) + min_temperature

    # Display the original image and the temperature matrix
    plt.figure(figsize=(10, 10))

    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title('Original Image')

    plt.subplot(1, 2, 2)
    plt.imshow(temperature_matrix, cmap='jet', vmin=min_temperature, vmax=max_temperature)
    plt.colorbar()
    plt.title('Temperature Matrix')

    # Print the temperature matrix
    print('Temperature Matrix:')
    print(temperature_matrix)

    plt.show()





def detect_temperature_regions(image_path, min_temperature, max_temperature, detection_temperature, output_excel_path):
    # Read the thermal RGB image
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Image at path '{image_path}' could not be loaded.")
    
    # Convert the RGB image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Calculate the temperature matrix
    temperature_matrix = (gray_image / 255.0) * (max_temperature - min_temperature) + min_temperature
    
    # Detect regions with temperature greater than or equal to the detection temperature
    detection_mask = temperature_matrix >= detection_temperature
    
    # Label connected regions in the detection mask
    labeled_regions = label(detection_mask)
    
    # Get bounding boxes for each detected region
    region_props = regionprops(labeled_regions)
    
    # Extract bounding boxes
    bounding_boxes = [prop.bbox for prop in region_props]
    
    # Filter out smaller boxes that are contained within larger boxes
    filtered_boxes = []
    for i in range(len(bounding_boxes)):
        contained = False
        bb1 = bounding_boxes[i]
        for j in range(len(bounding_boxes)):
            if i != j:
                bb2 = bounding_boxes[j]
                if bb1[0] >= bb2[0] and bb1[1] >= bb2[1] and bb1[2] <= bb2[2] and bb1[3] <= bb2[3]:
                    contained = True
                    break
        if not contained:
            filtered_boxes.append(bb1)
    
    # Display the original image with filtered bounding boxes around detected regions
    fig, ax = plt.subplots(1, 2, figsize=(12, 6))
    
    ax[0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    ax[0].set_title('Original Image with Detection Bounding Boxes')
    for box in filtered_boxes:
        minr, minc, maxr, maxc = box
        rect = plt.Rectangle((minc, minr), maxc - minc, maxr - minr, fill=False, edgecolor='red', linewidth=2)
        ax[0].add_patch(rect)
    ax[0].axis('off')
    
    # Display the temperature matrix with colormap
    cax = ax[1].imshow(temperature_matrix, cmap='jet', vmin=min_temperature, vmax=max_temperature)
    ax[1].set_title('Temperature Matrix')
    fig.colorbar(cax, ax=ax[1])
    
    plt.show()
    
    # Save the temperature matrix to an Excel file
    temperature_df = pd.DataFrame(temperature_matrix)
    temperature_df.to_excel(output_excel_path, index=False, header=False)
    print(f'Temperature matrix saved to {output_excel_path}')
