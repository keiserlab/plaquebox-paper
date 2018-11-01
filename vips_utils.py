import os

import numpy as np
import matplotlib.pyplot as plt
import pyvips as Vips

NP_DTYPE_TO_VIPS_FORMAT = {
        np.dtype('int8'): Vips.BandFormat.CHAR,
        np.dtype('uint8'): Vips.BandFormat.UCHAR,
        np.dtype('int16'): Vips.BandFormat.SHORT,
        np.dtype('uint16'): Vips.BandFormat.USHORT,
        np.dtype('int32'): Vips.BandFormat.INT,
        np.dtype('float32'): Vips.BandFormat.FLOAT,
        np.dtype('float64'): Vips.BandFormat.DOUBLE
    }

VIPS_FORMAT_TO_NP_DTYPE = {v:k for k, v in NP_DTYPE_TO_VIPS_FORMAT.items()}

def array_vips(vips_image, verbose=False):
    # dtype = np.dtype('u{}'.format(vips_image.BandFmt.bit_length() + 1))
    dtype = VIPS_FORMAT_TO_NP_DTYPE[vips_image.format]
    if verbose:
        print(dtype, vips_image.height, vips_image.width, vips_image.bands)
    return (np.fromstring(vips_image.write_to_memory(), dtype=dtype) #np.uint8)
             .reshape(vips_image.height, vips_image.width, vips_image.bands))

def show_vips(vips_image, ax=plt, show=True, verbose=False):
    if not isinstance(vips_image, Vips.Image):
        return -1
    
    im_np = array_vips(vips_image)
    if verbose:
        print(im_np.shape)
    if vips_image.bands == 1:
        ax.imshow(im_np.squeeze()/np.max(im_np), cmap=plt.get_cmap('gist_ncar'))
    elif vips_image.bands == 2:
        im_np = im_np[:,:,1]
        ax.imshow(im_np/np.max(im_np), cmap=plt.get_cmap('gray'))
    else:
        ax.imshow(im_np)
    if show:
        plt.show()
    
def image_fields_dict(im_with_fields):
    return {k:im_with_fields.get(k) 
            for k in im_with_fields.get_fields() 
            if im_with_fields.get_typeof(k)}
# from https://github.com/jcupitt/libvips/blob/master/doc/Examples.md

NP_DTYPE_TO_VIPS_FORMAT = {
        np.dtype('int8'): Vips.BandFormat.CHAR,
        np.dtype('uint8'): Vips.BandFormat.UCHAR,
        np.dtype('int16'): Vips.BandFormat.SHORT,
        np.dtype('uint16'): Vips.BandFormat.USHORT,
        np.dtype('int32'): Vips.BandFormat.INT,
        np.dtype('float32'): Vips.BandFormat.FLOAT,
        np.dtype('float64'): Vips.BandFormat.DOUBLE
    }

VIPS_FORMAT_TO_NP_DTYPE = {v:k for k, v in NP_DTYPE_TO_VIPS_FORMAT.items()}

def array_vips(vips_image, verbose=False):
    # dtype = np.dtype('u{}'.format(vips_image.BandFmt.bit_length() + 1))
    dtype = VIPS_FORMAT_TO_NP_DTYPE[vips_image.format]
    if verbose:
        print(dtype, vips_image.height, vips_image.width, vips_image.bands)
    return (np.fromstring(vips_image.write_to_memory(), dtype=dtype) #np.uint8)
             .reshape(vips_image.height, vips_image.width, vips_image.bands)).squeeze()

def show_vips(vips_image, ax=plt, show=True, verbose=False):
    if not isinstance(vips_image, Vips.Image):
        return -1
    
    im_np = array_vips(vips_image)
    if verbose:
        print(im_np.shape)
    if vips_image.bands == 1:
        ax.imshow(im_np/np.max(im_np), cmap=plt.get_cmap('gist_ncar'))
    elif vips_image.bands == 2:
        im_np = im_np[:,:,1]
        ax.imshow(im_np/np.max(im_np), cmap=plt.get_cmap('gray'))
    else:
        ax.imshow(im_np)
    if show:
        plt.show()
    
def image_fields_dict(im_with_fields):
    return {k:im_with_fields.get(k) 
            for k in im_with_fields.get_fields() 
            if im_with_fields.get_typeof(k)}

def save_and_tile(image_to_segment, output_dir, tile_size=1536):
    basename = os.path.basename(image_to_segment.filename)
    base_dir_name = os.path.join(output_dir, basename.split('.svs')[0])
    if not os.path.exists(base_dir_name):
        os.makedirs(base_dir_name)
    Vips.Image.dzsave(image_to_segment, base_dir_name,
                        layout='google',
                        suffix='.jpg[Q=90]',
                        tile_size=tile_size,
                        depth='one',
                        properties=True)
    return None