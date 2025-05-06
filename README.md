
# EmojiWave – Real-Time Hand Gesture Recognition with Emoji Feedback

## 📋 Project Overview

**EmojiWave** is a web application that uses computer vision to detect hand gestures in real-time. It then translates these gestures into corresponding emojis using a custom-trained Convolutional Neural Network (CNN). The app leverages **Streamlit** for an interactive user experience, enabling users to either upload an image or use their webcam for real-time gesture recognition.

## 🚀 Key Features
- **Real-time emoji feedback:** Detects hand gestures via webcam or uploaded images and displays corresponding emojis.
- **Interactive experience:** Fun and personal interaction without the need for touch or voice inputs.
- **Portable deployment:** Easily deployed via Docker for seamless use across different environments.
- **Live Demo:** Try EmojiWave in here (https://emojiwaveapp.streamlit.app/)

## 🔧 Tech Stack
- **Python**
- **TensorFlow** (for deep learning)
- **OpenCV** (for computer vision)
- **Streamlit** (for interactive web interface)
- **Jupyter / Google Colab** (for model development)
- **Docker** (for containerized deployment)
- **VS Code** (for development)

## 📸 How It Works
1. **Upload an image** or use your **webcam** for gesture recognition.
2. The system processes the image, detecting hand gestures.
3. The recognized gesture is matched to an emoji and displayed on the screen.

# Project Structure

``` plaintext

EmojiWave/
├── __pycache__/
├── fast.py                     # FastAPI application server
├── model.py                    # Contains the model architecture
├── preprocess.py               # Data preprocessing functions
├── notebooks/                  # Jupyter notebooks
│   ├── final_model_acc99.h5    # Final trained model with 99% accuracy
│   ├── Baseline_Model.ipynb    # Notebook for baseline model training
│   ├── EDA.ipynb               # Exploratory Data Analysis notebook
│   ├── PreProcess.ipynb        # Notebook for data preprocessing
│   ├── Best_Model.ipynb        # Notebook for fine-tuning the best model
│   └── plots/                  # Directory for storing plots
│       ├── baseline_model.jpeg  # Visualization of baseline model results
│       └── best_model.jpeg      # Visualization of best model results
├── streamlit_app/              # Directory for Streamlit application
│   ├── pages/                  # Subdirectory for app pages
│   ├── EmojiWave-unscreen-1.gif # GIF logo
│   └── Home.py                 # Main home page of the Streamlit app
├── requirements.txt            # List of project dependencies
├── .gitignore                  # Files and directories to be ignored by Git
└── README.md                   # project documentation
```


## 💻 How to Run the Project Locally

To run the app on your local machine, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/moalb08/EmojiWave.git
   ```

2. Install required dependencies:
   ```bash
   cd EmojiWave
   pip install -r requirements.txt
   ```

3. Launch the app using Streamlit:
   ```bash
   streamlit run streamlit_app/app.py
   ```

---

## 👥 Acknowledgments

Shoutout to my incredible team for making EmojiWave happen:

- [**Noura Alzahrani**](https://github.com/Nourii-24)
- [**Norah Alharbi**](https://github.com/NourahNH)
- [**Amal Alahmadi**](https://github.com/amal-Stu)
- [**Yousif Alnasser**](https://github.com/ai-yousif)
