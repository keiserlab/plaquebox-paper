# Interpretable Classification of Alzheimer's Disease Pathologies with a Convolutional Neural Network Pipeline
## bioRxiv 454793
## DOI: https://doi.org/10.1101/454793
## Zenodo Data Available at: https://doi.org/10.5281/zenodo.1470797
This repository accompanies the publication above. Specifically, we include Jupyter notebooks to reproduce all image preprocessing and processing, training of convolutional neural networks, confidence visualizations, and saliency maps. The available code is provided as-is, and does not constitute a full-fledged software package for analysis.

## Systems requirements

This code repository was developed on Linux CentOS 7 and Ubuntu 18 and has not been tested on on other systems (Windows, MacOS).

Code requires the following Python packages:
```
python                    3.6.5                hc3d631a_2  
ipython                   6.4.0                    py36_0  
jupyter                   1.0.0                    py36_4  
matplotlib                2.2.2            py36h0e671d2_1  
numpy                     1.14.3           py36hcd700cb_1  
pandas                    0.23.0           py36h637b7d7_0  
scikit-learn              0.19.1           py36h7aa7ec6_0     
scikit-image              0.13.1           py36h14c3975_1    
scipy                     1.1.0            py36hfc37229_0  
pytorch                   0.3.0            py35_cuda8.0.61_cudnn7.0.3hb362f6e_4    pytorch
torchvision               0.2.1                    py36_1    pytorch   
libopencv                 3.4.1                h1a3b859_1   
opencv                    3.4.1            py36h6fd60c2_2  
py-opencv                 3.4.1            py36h0676e08_1  
pyvips                    2.1.2                     <pip>
tqdm                      4.23.4                   py36_0
```

In addition, libvips (version 8.2.2-1) was used in this study for handling of whole slide images. The open-source python package pyvips is a wrapper for libvips ((https://jcupitt.github.io/libvips/), which can be installed in Linux with the following:

```
sudo apt-get install libvips
```

### Hardware Requirements

Graphics Cards for Deep Learning - All deep learning models were trained using 4 X NVIDIA 1080 GPUs. As indicated above, PyTorch requires CUDA 8.0 and cuDNN 7.0 for compatibility.

## Installation guide
We recommend creating a new Anaconda (https://www.anaconda.com/) environment with the dependencies above.

This repository can be cloned directly through:

```
git clone https://github.com/keiserlab/plaquebox-paper.git
```

## Demo


## Instructions for use



