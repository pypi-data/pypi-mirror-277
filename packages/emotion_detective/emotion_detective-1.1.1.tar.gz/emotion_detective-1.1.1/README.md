
# Emotion Detective

## Overview

This NLP project provides functions to analyze emotions in video or audio files. It offers a comprehensive set of tools to detect and analyze emotions at a sentence level, producing valuable insights into the emotional content of multimedia sources. It includes a package with all necessary functions, two pipelines -- one for training the NLP model and one for inference, and Sphinx documentation.

## Installation

To install the package and its dependencies, use the following pip command:

```bash
pip install emotion_detective
```

#### Additional Dependencies

The package also requires to have the following dependencies installed on your system. To install the additional dependencies, refer to the installation documentation linked below:

- [Rust](https://www.rust-lang.org/tools/install)
- [Cuda Toolkit](https://developer.nvidia.com/cuda-downloads)

## Usage

### Package

To use the package in your Python code, import it as follows:

```python
import emotion_detective
```

[Provide a brief overview of the main functionalities of your package and how users can use them.]

### Pipelines

#### Training Pipeline

The training pipeline in this NLP project is the training pipeline for an emotion classification model. This pipeline executes the following steps:

1. **Data Loading**: It loads the input data from the specified file path, including text data and emotion labels.

2. **Class Balancing**: It balances the dataset to ensure equal representation of all emotion classes.

3. **Spelling Correction**: It corrects spelling mistakes in the text data.

4. **Text Preprocessing**: It preprocesses the text data, including tokenization and encoding.

5. **Model Training and Evaluation**: It trains and evaluates a RoBERTa-based emotion classification model using the preprocessed data, specified learning rate, batch size, number of epochs, and patience for early stopping.

6. **Model Saving**: It saves the trained model to the specified directory with the given name.

This pipeline takes the following parameters:
- `file_path`: Path to the file containing the input data.
- `text_column`: Name of the column in the DataFrame containing text data.
- `emotion_column`: Name of the column in the DataFrame containing emotion labels.
- `mapped_emotion_column`: Name of the column in the DataFrame containing mapped emotion labels.
- `input_id_column`: Name of the column in the DataFrame containing input IDs.
- `learning_rate`: Learning rate for the optimizer.
- `batch_size`: Batch size for training and validation DataLoaders.
- `num_epochs`: Number of epochs to train the model.
- `patience`: Patience for early stopping.
- `model_dir`: Directory where the trained model will be saved.
- `model_name`: Name to use when saving the trained model.

Upon completion, this pipeline does not return any value but logs the completion status.

#### Inference Pipeline

The first pipeline in this NLP project is the inference pipeline for emotion detection from video and audio files. This pipeline performs the following steps:

1. **Data Ingestion**: It ingests the input audio (mp3) or video file (mp4). If the input is a video file, it converts it to audio format and saves it to the specified output path.

2. **Data Preprocessing**: It transcribes and translates the audio using NLP techniques.

3. **Model Loading**: It loads the pre-trained NLP model specified by the `model_path`.

4. **Prediction**: It utilizes the loaded model to predict emotions from the transcribed sentences.

5. **Logging**: It logs the program's execution process, including information, warnings, and errors, to a log file (`logs/emotion_detective.txt`) and the console.

The pipeline takes the following parameters:
- `input_path`: Path to the input audio or video file.
- `output_audio_path` (optional): Path to save the transcribed audio file, required only when the input is a video file.  Ensure the file extension is .mp3.
- `model_path` (optional): Path to the saved NLP model, defaulting to "roberta-base".
- `batch_size` (optional): Batch size used for model prediction, defaulting to 32.

The pipeline returns a DataFrame containing transcribed sentences, predicted emotions, their values, and probabilities.

#### Pipeline Overview

![Visualisation of the pipeline](data/docs/pipelines.png)

### Sphinx Documentation

[Provide instructions on how to generate and access Sphinx documentation for your project.]

## Examples

[Include code examples or usage scenarios to demonstrate how to use your package and pipelines.]

## License

## Credits

Amy Suneeth, Martin Vladimirov, Andrea Tosheva, Kacper Janczyk, Rebecca Borski

## Contact

[Provide contact information for users to reach out to you for questions, feedback, or support.]
