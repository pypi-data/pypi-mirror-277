from setuptools import setup, find_packages

with open("README.md", 'r') as f:
    description = f.read()

setup(
    name="DataCraftHub",
    version = '0.1',
    packages=find_packages(),
    install_requies = [
        "numpy",
        "os",
        "time",
        "opencv-python",
        "random",
        "shutil",
    ],
    entry_points = {
        "console_scripts" : [
            "rename_and_copy_with_incremental_index = DataCraftHub:rename_and_copy_with_incremental_index",
            "extract_and_save_cropped_images = DataCraftHub:extract_and_save_cropped_images",
            "split_dataset_into_partitioned_sets = DataCraftHub:split_dataset_into_partitioned_sets",
            "split_dataset_with_associated_labels = DataCraftHub:split_dataset_with_associated_labels",
            "split_video_into_frames = DataCraftHub:split_video_into_frames",
            "generate_text_files_for_images = DataCraftHub:generate_text_files_for_images",

        ],
    },
    long_description=description,
    long_description_content_type='text/markdown',
)