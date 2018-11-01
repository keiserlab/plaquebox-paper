# Modified from OpenCV Implementation
# https://github.com/Peter554/StainTools/blob/master/staintools/reinhard_color_normalizer.py

import pyvips as Vips

class Reinhard(object):
    """
    A stain normalization object for PyVips.
    fits a reference PyVips image,
    transforms a PyVips Image.
    Can also be initialized with precalculated
    means and stds (in LAB colorspace)
    """

    def __init__(self, target_means=None, target_stds=None):
        self.target_means = target_means
        self.target_stds  = target_stds

    def fit(self, target): 
        """
        target is a PyVips Image object
        """
        means, stds = self.get_mean_std(target)
        self.target_means = means
        self.target_stds  = stds
    
    def transform(self, image):
        L, A, B = self.lab_split(image)
        means, stds = self.get_mean_std(image)
        norm1 = ((L - means[0]) * (self.target_stds[0] / stds[0])) + self.target_means[0]
        norm2 = ((A - means[1]) * (self.target_stds[1] / stds[1])) + self.target_means[1]
        norm3 = ((B - means[2]) * (self.target_stds[2] / stds[2])) + self.target_means[2]
        return self.merge_to_rgb(norm1, norm2, norm3)
    
    def lab_split(self, img):
        img_lab = img.colourspace("VIPS_INTERPRETATION_LAB")
        L, A, B = img_lab.bandsplit()[:3]
        return L, A, B
        
    def get_mean_std(self, image):
        L, A, B = self.lab_split(image)
        m1, sd1 = L.avg(), L.deviate()
        m2, sd2 = A.avg(), A.deviate()
        m3, sd3 = B.avg(), B.deviate()
        means = m1, m2, m3
        stds  = sd1, sd2, sd3
        self.image_stats = means, stds
        return means, stds
    
    def merge_to_rgb(self, L, A, B):
        img_lab = L.bandjoin([A,B])
        img_rgb = img_lab.colourspace('VIPS_INTERPRETATION_sRGB')
        return img_rgb