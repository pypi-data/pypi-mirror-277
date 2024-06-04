import os
import cv2
import timm
import site
import torch
import torch.nn as nn
import torch.nn.functional as F
from PIL import Image
from torchvision import transforms as T

def load_prebuilt_model():
    """
    Load prebuilt watermark model
    """
    model = timm.create_model('efficientnet_b3a', pretrained=True, num_classes=2)
    model.classifier = nn.Sequential(
        nn.Linear(in_features=1536, out_features=625),
        nn.ReLU(),
        nn.Dropout(p=0.3),
        nn.Linear(in_features=625, out_features=256),
        nn.ReLU(),
        nn.Linear(in_features=256, out_features=2),
    )
    site_packages_dir = site.getusersitepackages()
    zip_path = os.path.join(site_packages_dir, 'ArtSnake')
    resume_name = 'watermark_model_v1.pt'
    model_path = os.path.join(zip_path, resume_name)
    state_dict = torch.load(model_path)
    model.load_state_dict(state_dict)
    model.eval()
    return model

def load_prebuilt_transform():
    """
    Load prebuilt image transformation
    """
    return T.Compose([
        T.Resize((256, 256)),
        T.ToTensor(),
        T.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])


def detect_watermark_wrapper(func, img):
    """
    Wrapper function for detecting watermarks
    """
    return func(img)


def watermark_proba_prebuilt_from_opencv(img):
    """
    Returns the probability of an image being a watermarked.\n
    Use None for model and preprocessing to use the prebuilt model and preprocessing function.\n
    The preprocessing function should take an image and return a PyTorch tensor.
    """
    
    model = load_prebuilt_model()
    preprocessing = load_prebuilt_transform()

    # Load the image and apply preprocessing
    img = preprocessing(Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)))
    batch = torch.stack([img])

    # Use GPU if available
    if torch.cuda.is_available():
        model.cuda()
        batch = batch.cuda()

    # Perform prediction
    with torch.no_grad():
        pred = model(batch)
        syms = F.softmax(pred, dim=1).detach().cpu().numpy().tolist()
        for sym in syms:
            water_sym, clear_sym = sym
    return water_sym


def watermark_proba_from_path(image_path, model=None, preprocessing=None):
    """
    Returns the probability of an image being a watermarked.\n
    Use None for model and preprocessing to use the prebuilt model and preprocessing function.\n
    The preprocessing function should take an image and return a PyTorch tensor.
    """
    if model is None:
        model = load_prebuilt_model()
    if preprocessing is None:
        preprocessing = load_prebuilt_transform()

    # Load the image and apply preprocessing
    img = preprocessing(Image.open(image_path).convert('RGB'))
    batch = torch.stack([img])

    # Use GPU if available
    if torch.cuda.is_available():
        model.cuda()
        batch = batch.cuda()

    # Perform prediction
    with torch.no_grad():
        pred = model(batch)
        syms = F.softmax(pred, dim=1).detach().cpu().numpy().tolist()
        for sym in syms:
            water_sym, clear_sym = sym
            if water_sym > clear_sym:
                print(f"{image_path}: Watermarked, probability: {water_sym}")
            else:
                print(f"{image_path}: Clear, probability: {clear_sym}")
    return water_sym


def watermark_proba_from_dir(directory, model=None, preprocessing=None):
    """
    Returns the probability of an image being a watermarked.
    Use None for model and preprocessing to use the prebuilt model and preprocessing function.\n
    The preprocessing function should take an image and return a PyTorch tensor.
    """
    # Predict images in the specified directory
    for filename in os.listdir(directory):
        image_path = os.path.join(directory, filename)
        if os.path.isfile(image_path) and filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            watermark_proba_from_path(image_path, model, preprocessing)

if __name__ == '__main__':
    image_path = "example.jpg"
    watermark_proba_from_path(image_path)
