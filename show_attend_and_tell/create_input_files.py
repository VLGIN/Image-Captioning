from utils import create_input_files

if __name__ == '__main__':
    # Create input files (along with word map)
    create_input_files(dataset='VizWiz',
                       karpathy_json_path='caption_dataset/VizWiz.json',
                       image_folder='/content/drive/MyDrive/PROJECT_3/dataset',
                       captions_per_image=5,
                       min_word_freq=5,
                       output_folder='input_for_model/',
                       max_len=50)
