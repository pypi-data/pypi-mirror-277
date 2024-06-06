# ObjectTrainer

ObjectTrainer is a Python package designed to simplify the process of training YOLO (You Only Look Once) models for object detection tasks. With ObjectTrainer, users can easily train YOLO models using custom datasets and split their data into training, validation, and testing sets. The package provides classes for both model training and data splitting, allowing users to efficiently manage their training pipeline. Additionally, ObjectTrainer includes functionality for saving the best-performing model weights, making it easy to deploy trained models for inference tasks.

## Features

- Train YOLO models with custom datasets
- Split datasets into training, validation, and testing sets
- Save best-performing model weights for deployment

## Installation

You can install ObjectTrainer using pip:

```bash
pip install ObjectTrainer
````

## Usage

## Training a YOLO Model

```python
from ObjectTrainer import YOLO_trainer

# Initialize YOLO Trainer with absolute data.yaml folder path and absolute destination folder path for best weights
trainer = YOLO_trainer(Data_yaml_fold_path='path/to/data.yaml', Best_Weight_dest='path/to/destination', epochs=50)

# Run the full training process
trainer.run_full_training()
```

### Splitting Data

```python
from ObjectTrainer import data_splitter

# Initialize Data Splitter with absolute data folder path, destination folder path, and number of classes
splitter = data_splitter(data_folder='path/to/data', dest_fold='path/to/destination', no_classes=3)

# Run the full data splitting process
splitter.run_full_split()
```

## License

Model Trainer is licensed under the MIT License. See the [LICENSE](https://github.com/Rathoreatri03/Model_Trainer/blob/main/LICENSE) file for details.

## Support

For support, please open an issue on our [GitHub repository](https://github.com/Rathoreatri03/Model_Trainer/issues).
```

This Markdown-formatted README includes the updated usage instructions with the new single-method calls for training and data splitting, making it easy for users to follow and implement.