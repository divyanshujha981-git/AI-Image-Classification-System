
**AI-Powered Image Classification System** is a deep learning project built using a Convolutional Neural Network (CNN) trained on the CIFAR-10 dataset. It classifies images into 10 categories using a custom 6-layer CNN architecture.

------------------------------------------------------------------------

## 🚀 Features

-   📊 **Image Classification** -- Predicts one of the 10 CIFAR-10
    categories
-   🧠 **Custom CNN Architecture** -- Includes convolution layers, batch
    normalization, ReLU, and dropout
-   ⚙️ **Complete Training Pipeline** -- Preprocessing, training,
    validation, and testing
-   📈 **Performance Metrics** -- Accuracy, loss, confusion matrix,
    precision, recall, F1-score
-   🎥 **Demo Video Included** -- Overview of training and model
    behavior
-   📓 **Jupyter Notebook** -- Contains full model code and training
    workflow

------------------------------------------------------------------------

## 🧠 Dataset: CIFAR-10

-   **60,000 images** (32×32 pixels)
    -   50,000 for training\
    -   10,000 for testing\
-   Images were:\
    ✔️ Merged and shuffled\
    ✔️ Normalized (0.0 -- 1.0)\
    ✔️ Split into training, validation, and testing sets

------------------------------------------------------------------------

## 🏗️ Model Architecture

The CNN consists of:

-   🔹 **6 Convolutional Layers** -- Extract visual features\
-   🔹 **Batch Normalization** -- Stable and faster training\
-   🔹 **ReLU Activation** -- Adds non-linearity\
-   🔹 **Dropout (0.3)** -- Reduces overfitting\
-   🔹 **Fully Connected Layers** -- Perform final classification\
-   🔹 **Softmax Output** -- Predicts probabilities for 10 classes

------------------------------------------------------------------------

## 📊 Model Performance

-   **Training Accuracy:** 0.79\
-   **Validation Accuracy:** 0.78\
-   **Training Loss:** 0.60\
-   **Validation Loss:** 0.63

Generated outputs include:\
- ✔️ Confusion Matrix\
- ✔️ Accuracy & Loss Graphs\
- ✔️ Precision, Recall, F1-score

------------------------------------------------------------------------

## 📷 Demo Images

<img width="1916" height="900" alt="Screenshot 2025-12-03 120658" src="https://github.com/user-attachments/assets/ba9e64d6-cdd8-492c-80c2-a069409d0f79" />

<img width="1919" height="891" alt="Screenshot 2025-12-03 120711" src="https://github.com/user-attachments/assets/9f197a9a-3e43-476c-923f-b339ba4a00d2" />

<img width="1918" height="896" alt="Screenshot 2025-12-03 120737" src="https://github.com/user-attachments/assets/386375aa-41ef-451a-b486-20fb7f73e1c4" />

<img width="1915" height="897" alt="Screenshot 2025-12-03 120751" src="https://github.com/user-attachments/assets/dbbe5ccb-dc2a-40cf-a881-9bbfad20da73" />

<img width="1919" height="898" alt="Screenshot 2025-12-03 120809" src="https://github.com/user-attachments/assets/2c09d1c5-e3b6-4b39-bb14-4359e926aba4" />

<img width="1919" height="898" alt="Screenshot 2025-12-03 120819" src="https://github.com/user-attachments/assets/77f74e82-170e-4ed4-b7be-79a7a79e6cc5" />

------------------------------------------------------------------------

## 📌 Future Enhancements

-   Data augmentation\
-   Using advanced architectures like ResNet\
-   Deploying the model using Streamlit or Flask\
-   Real-time image prediction demo
