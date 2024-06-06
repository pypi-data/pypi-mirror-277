import numpy as np
import sidpy
from skimage.restoration import inpaint

def crop_image(dataset: sidpy.Dataset, corners: np.ndarray) -> sidpy.Dataset:
    """
    Crops an image according to the corners given in the format of matplotlib.widget.RectangleSelector.

    Parameters
    ----------
    dataset: sidpy.Dataset
        An instance of sidpy.Dataset representing the image to be cropped.
    corners: np.ndarray
        A 1D array of length 4 containing the corners of the rectangular region to be cropped.
        The order of the corners should be (x1, y1, x2, y2).

    Returns
    -------
    sidpy.Dataset
        A new instance of sidpy.Dataset representing the cropped image.

    Raises
    ------
    ValueError
        If dataset is not an instance of sidpy.Dataset or if dataset is not an image dataset.
        If corners parameter is not of correct shape or size.

    """
    if not isinstance(dataset, sidpy.Dataset):
        raise ValueError('Input dataset is not an instance of sidpy.Dataset')
    if not dataset.data_type.name == 'IMAGE':
        raise ValueError('Only image datasets are supported at this point')
    
    if corners.shape != (4,):
        raise ValueError('Input corners parameter should have shape (4,) but got shape {0}'.format(corners.shape))
    if corners[2]-corners[0] <= 0 or corners[3]-corners[1] <= 0:
        raise ValueError('Invalid input corners parameter')
    
    pixel_size = np.array([dataset.x[1]-dataset.x[0], dataset.y[1]-dataset.y[0]])
    corners /= pixel_size
    
    selection = np.stack([np.min(corners[:2])+0.5, np.max(corners[2:])+0.5]).astype(int)

    cropped_dset = dataset.like_data(dataset[selection[0, 0]:selection[1, 0], selection[0, 1]:selection[1, 1]])
    cropped_dset.title = 'cropped_' + dataset.title
    cropped_dset.source = dataset.title
    cropped_dset.metadata = {'crop_dimension': selection, 'original_dimensions': dataset.shape}
    
    return cropped_dset

def flatten_image(sid_dset, order=1, flatten_axis = 'row', method = 'line_fit'):
    """
    Flattens an image according to the method chosen. Used heavily for AFM/STM images

    Parameters
    ----------
    dataset: sidpy.Dataset
        An instance of sidpy.Dataset representing the image to be flattened.
    order: integer, 
        Optional, default = 1. Ordfor the polynomial fit.
    flatten_axis: string, 
        Optional, default = 'row'. Axis along which to flatten the image.
    method: string, 
        Optional, default = 'line_fit'. Method to use for flattening the image.

    Returns
    -------
    sidpy.Dataset
        A new instance of sidpy.Dataset representing the flattened image.
    """
    #TODO: lots of cleanup in this function required...
    new_sid_dset = sid_dset.copy()
    assert len(new_sid_dset._axes) == 2, "Dataset must be 2-D for this function"
    assert new_sid_dset.data_type == sidpy.DataType.IMAGE, "Dataset must IMAGE for this function"
    #check the spatial dimensions, flatten along each row
    if flatten_axis == 'row':
        num_pts = sid_dset.shape[0] #this is hard coded, it shouldn't be
    elif flatten_axis == 'col':
        num_pts = sid_dset.shape[1] #this is hard coded, but it shouldn't be
    else:
        raise ValueError("Gave flatten axis of {} but only 'row', 'col' are allowed".format(flatten_axis))
    
    data_flat = np.zeros(sid_dset.shape) #again this should be the spatial (2 dimensional) part only
    print(sid_dset.shape, num_pts)
    if method == 'line_fit':
        for line in range(num_pts):
            if flatten_axis=='row':
                line_data = np.array(sid_dset[:])[line,:]
            elif flatten_axis=='col':
                line_data = np.array(sid_dset[:])[:,line]
            p = np.polyfit(np.arange(len(line_data)), line_data,order)
            lin_est = np.polyval(p,np.arange(len(line_data)))
            new_line = line_data - lin_est
            data_flat[line] = new_line
    elif method == 'plane_fit':
        #TODO: implement plane fit
        pass
    else:
        raise ValueError("Gave method of {} but only 'line_fit', 'plane_fit' are allowed".format(method))
   
    new_sid_dset[:] = data_flat 
    
    return new_sid_dset


def inpaint_image(sid_dset, mask = None, channel = None):
    """Inpaints a sparse image, given a mask.

    Args:
        sid_dset (_type_): sidpy Dataset with two dimensions being of spatial or reciprocal type
        mask (np.ndarry) : mask [0,1] same shape as sid_dset. If providing a sidpy dataset and mask is in the metadata dict, 
        then this entry is optional
        channel (int): (optional) for multi-channel datasets, provide the channel to in-paint
    """
    if len(sid_dset.shape)==2:
        image_data = np.array(sid_dset).squeeze()
    elif len(sid_dset.shape)==3:
        image_dims = []
        selection = []
        for dim, axis in sid_dset._axes.items():
            if axis.dimension_type in [sidpy.DimensionType.SPATIAL, sidpy.DimensionType.RECIPROCAL]:
                selection.append(slice(None))
                image_dims.append(dim)
            else:
                if channel is None:
                    channel=0
                selection.append(slice(channel, channel+1))

        image_data = np.array(sid_dset[tuple(selection)]).squeeze()
    if mask is None:
        mask_data = sid_dset.metadata["mask"]
        mask = np.copy(mask_data)
        mask[mask==1] = -1
        mask[mask==0] = 1
        mask[mask==-1] = 0
        
  
    inpainted_data = inpaint.inpaint_biharmonic(image_data, mask)
    
    #convert this into a sidpy dataset
    data_set = sidpy.Dataset.from_array(inpainted_data, name='inpainted_image')
    data_set.data_type = 'image'  # supported

    data_set.units = sid_dset.units
    data_set.quantity = sid_dset.quantity

    data_set.set_dimension(0, sid_dset.get_dimension_by_number(image_dims[0])[0])
    data_set.set_dimension(1, sid_dset.get_dimension_by_number(image_dims[1])[0])

    data_set.metadata["mask"] = mask
    import skimage
    skimage_version = skimage.__version__
    data_set.metadata["inpainting"] = 'Biharmonic method from Skimage {}'.format(skimage_version)

    return data_set
    
    