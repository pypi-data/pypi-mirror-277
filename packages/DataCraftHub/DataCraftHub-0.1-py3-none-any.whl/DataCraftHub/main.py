import os
import random
import time
import shutil
import cv2 as cv

def rename_and_copy_with_incremental_index(source_folder,destination_folder,rename_text, start_index):
    files = os.listdir(source_folder)

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    for i , file_name in enumerate(files):

        if file_name.endswith(".jpg") or file_name.endswith(".png") or file_name.endswith(".jpeg"):
            new_file_name = f"{rename_text}_{start_index+1}.jpg"

            src_file_path = os.path.join(source_folder,file_name)
            dst_file_path = os.path.join(destination_folder,new_file_name)

            while os.path.exists(dst_file_path):
                start_index+=1
                new_file_name = f"{rename_text}_{start_index+1}.jpg"
                dst_file_path = os.path.join(destination_folder,new_file_name)
            
            start_index += 1

            shutil.copyfile(src_file_path,dst_file_path)
            print(f"save {file_name} to {new_file_name} in {destination_folder} folder")

def extract_and_save_cropped_images(input_folder,output_folder,roi):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(input_folder):
        if filename.endswith(".jpg"):
            image_path = os.path.join(input_folder, filename)
            image = cv.imread(image_path)
            img2 = image[roi[1]:roi[1]+roi[3],roi[0]:roi[0]+roi[2]]

            output_path = os.path.join(output_folder, filename)
            cv.imwrite(output_path, img2)

def split_dataset_into_partitioned_sets(dataset_dir, output_dir, split_ratio=(0.8, 0.1, 0.1)):

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    classes = [folder for folder in os.listdir(dataset_dir) if os.path.isdir(os.path.join(dataset_dir, folder))]
    
    train_dir = os.path.join(output_dir, 'train')
    val_dir = os.path.join(output_dir, 'val')
    test_dir = os.path.join(output_dir, 'test')
    
    for directory in [train_dir, val_dir, test_dir]:
        if not os.path.exists(directory):
            os.makedirs(directory)

    for cls in classes:
        images = os.listdir(os.path.join(dataset_dir, cls))
        random.shuffle(images)
        
        train_split = int(len(images) * split_ratio[0])
        val_split = int(len(images) * (split_ratio[0] + split_ratio[1]))
        
        for i, image in enumerate(images):
            src_path = os.path.join(dataset_dir, cls, image)
            if i < train_split:
                dest_path = os.path.join(train_dir, cls, image)
            elif i < val_split:
                dest_path = os.path.join(val_dir, cls, image)
            else:
                dest_path = os.path.join(test_dir, cls, image)
            os.makedirs(dest_path, exist_ok=True)
            shutil.copy(src_path, dest_path)
    
    return output_dir

def generate_text_files_for_images(image_directory,label_directory,text):
    os.makedirs(label_directory, exist_ok=True)

    for filename in os.listdir(image_directory):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            txt_filename = os.path.splitext(filename)[0] + '.txt'

            text_content = f'{text}'

            with open(os.path.join(label_directory, txt_filename), 'w') as txt_file:
                txt_file.write(text_content)

    print("Text files created successfully.")

def split_dataset_with_associated_labels(dataset_dir, output_dir, split_ratio=(0.8, 0.1, 0.1)):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    train_dir = os.path.join(output_dir, 'train')
    val_dir = os.path.join(output_dir, 'val')
    test_dir = os.path.join(output_dir, 'test')

    for directory in [train_dir, val_dir, test_dir]:
        if not os.path.exists(directory):
            os.makedirs(directory)

    images_dir = os.path.join(dataset_dir, 'images')
    labels_dir = os.path.join(dataset_dir, 'labels')

    images = os.listdir(images_dir)
    random.shuffle(images)
    
    train_split = int(len(images) * split_ratio[0])
    val_split = int(len(images) * (split_ratio[0] + split_ratio[1]))
    
    for i, image_name in enumerate(images):
        image_path = os.path.join(images_dir, image_name)
        label_path = os.path.join(labels_dir, image_name.replace('.jpg', '.txt'))

        if os.path.exists(image_path) and os.path.exists(label_path):
        
            if i < train_split:
                dest_dir = train_dir
            elif i < val_split:
                dest_dir = val_dir
            else:
                dest_dir = test_dir
            
            dest_images_dir = os.path.join(dest_dir, 'images')
            dest_labels_dir = os.path.join(dest_dir, 'labels')
            os.makedirs(dest_images_dir, exist_ok=True)
            os.makedirs(dest_labels_dir, exist_ok=True)
            
            shutil.copy(image_path, os.path.join(dest_images_dir, image_name))
            shutil.copy(label_path, os.path.join(dest_labels_dir, image_name.replace('.jpg', '.txt')))

        
    return output_dir

def split_video_into_frames(video_path, output_folder):
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    cap = cv.VideoCapture(video_path)

    frame_count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame_count += 1
        frame_path = os.path.join(output_folder, f"frame_{frame_count}.jpg")
        cv.imwrite(frame_path, frame)

    cap.release()

