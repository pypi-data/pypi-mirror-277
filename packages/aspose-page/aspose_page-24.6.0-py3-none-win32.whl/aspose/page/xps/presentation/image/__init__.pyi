import aspose.page
import aspose.pydrawing
import datetime
import decimal
import io
import uuid
from typing import Iterable

class BmpSaveOptions(aspose.page.eps.device.ImageSaveOptions):
    '''Class for XPS-as-BMP saving options.'''
    
    def __init__(self):
        '''Creates new instance of options.'''
        ...
    
    @property
    def page_numbers(self) -> list[int]:
        ...
    
    @page_numbers.setter
    def page_numbers(self, value: list[int]):
        ...
    
    @property
    def text_rendering_hint(self) -> aspose.pydrawing.Text.TextRenderingHint:
        ...
    
    @text_rendering_hint.setter
    def text_rendering_hint(self, value: aspose.pydrawing.Text.TextRenderingHint):
        ...
    
    @property
    def interpolation_mode(self) -> aspose.pydrawing.Drawing2D.InterpolationMode:
        ...
    
    @interpolation_mode.setter
    def interpolation_mode(self, value: aspose.pydrawing.Drawing2D.InterpolationMode):
        ...
    
    @property
    def image_size(self) -> aspose.pydrawing.Size:
        ...
    
    @image_size.setter
    def image_size(self, value: aspose.pydrawing.Size):
        ...
    
    ...

class ImageDevice(aspose.page.Device):
    '''Class incapsulating image composing device.'''
    
    @overload
    def __init__(self):
        '''Creates the new instance.'''
        ...
    
    @overload
    def __init__(self, page_size: aspose.pydrawing.Size):
        '''Creates the new instance with specified media size.
        
        :param page_size: The size of the device output media.'''
        ...
    
    @overload
    def open_page(self, title: str) -> bool:
        '''Starts a new page with the specifies title.
        
        :param title: The title.
        :returns: ``True`` if started page is to be output (it's number is contained in PageNumbers save options).
                  ``False``, otherwise.'''
        ...
    
    @overload
    def open_page(self, width: float, height: float) -> bool:
        '''Starts a new page with the specified width and height.
        
        :param width: The width of the page.
        :param height: The height of the page.
        :returns: ``True`` if started page is to be output (it's number is contained in PageNumbers save options).
                  ``False``, otherwise.'''
        ...
    
    def init_page_numbers(self) -> None:
        '''Initializes numbers of pages to output.'''
        ...
    
    def close_page(self) -> None:
        '''Accomplishes the page.'''
        ...
    
    def update_page_parameters(self, device: aspose.page.IMultiPageDevice) -> None:
        '''Updates the current page parameters.
        
        :param device: The multipage device.'''
        ...
    
    def open_partition(self) -> None:
        '''Starts a new document partition.'''
        ...
    
    def close_partition(self) -> None:
        '''Accomplished the document partition.'''
        ...
    
    @property
    def result(self) -> list[list[bytes]]:
        '''Returns the resulting images byte arrays.
        The first dimension is for inner documents
        and the second one is for pages within inner documents.'''
        ...
    
    @property
    def current_page_number(self) -> int:
        '''Returns the absolute number of the current page within the document.'''
        ...
    
    @property
    def current_relative_page_number(self) -> int:
        '''Returns the relative number of the current page within the current partition.'''
        ...
    
    ...

class ImageSaveOptions(aspose.page.SaveOptions):
    '''Basic class for XPS-as-image saving options.'''
    
    @property
    def page_numbers(self) -> list[int]:
        '''Gets/sets the array of numbers of pages to convert.'''
        ...
    
    @page_numbers.setter
    def page_numbers(self, value: list[int]):
        ...
    
    @property
    def resolution(self) -> float:
        '''Gets/sets the image resolution.'''
        ...
    
    @resolution.setter
    def resolution(self, value: float):
        ...
    
    @property
    def smoothing_mode(self) -> aspose.pydrawing.Drawing2D.SmoothingMode:
        '''Gets/sets the smoothing mode.'''
        ...
    
    @smoothing_mode.setter
    def smoothing_mode(self, value: aspose.pydrawing.Drawing2D.SmoothingMode):
        ...
    
    @property
    def text_rendering_hint(self) -> aspose.pydrawing.Text.TextRenderingHint:
        '''Gets/sets the text rendering hint.'''
        ...
    
    @text_rendering_hint.setter
    def text_rendering_hint(self, value: aspose.pydrawing.Text.TextRenderingHint):
        ...
    
    @property
    def interpolation_mode(self) -> aspose.pydrawing.Drawing2D.InterpolationMode:
        '''Gets/sets the interpolation mode.'''
        ...
    
    @interpolation_mode.setter
    def interpolation_mode(self, value: aspose.pydrawing.Drawing2D.InterpolationMode):
        ...
    
    @property
    def image_size(self) -> aspose.pydrawing.Size:
        '''Gets/sets the size of the output images in pixels.'''
        ...
    
    @image_size.setter
    def image_size(self, value: aspose.pydrawing.Size):
        ...
    
    ...

class JpegSaveOptions(aspose.page.eps.device.ImageSaveOptions):
    '''Class for XPS-as-JPEG saving options.'''
    
    def __init__(self):
        '''Creates new instance of options.'''
        ...
    
    @property
    def page_numbers(self) -> list[int]:
        ...
    
    @page_numbers.setter
    def page_numbers(self, value: list[int]):
        ...
    
    @property
    def text_rendering_hint(self) -> aspose.pydrawing.Text.TextRenderingHint:
        ...
    
    @text_rendering_hint.setter
    def text_rendering_hint(self, value: aspose.pydrawing.Text.TextRenderingHint):
        ...
    
    @property
    def interpolation_mode(self) -> aspose.pydrawing.Drawing2D.InterpolationMode:
        ...
    
    @interpolation_mode.setter
    def interpolation_mode(self, value: aspose.pydrawing.Drawing2D.InterpolationMode):
        ...
    
    @property
    def image_size(self) -> aspose.pydrawing.Size:
        ...
    
    @image_size.setter
    def image_size(self, value: aspose.pydrawing.Size):
        ...
    
    ...

class PngSaveOptions(aspose.page.eps.device.ImageSaveOptions):
    '''Class for XPS-as-PNG saving options.'''
    
    def __init__(self):
        '''Creates new instance of options.'''
        ...
    
    @property
    def page_numbers(self) -> list[int]:
        ...
    
    @page_numbers.setter
    def page_numbers(self, value: list[int]):
        ...
    
    @property
    def text_rendering_hint(self) -> aspose.pydrawing.Text.TextRenderingHint:
        ...
    
    @text_rendering_hint.setter
    def text_rendering_hint(self, value: aspose.pydrawing.Text.TextRenderingHint):
        ...
    
    @property
    def interpolation_mode(self) -> aspose.pydrawing.Drawing2D.InterpolationMode:
        ...
    
    @interpolation_mode.setter
    def interpolation_mode(self, value: aspose.pydrawing.Drawing2D.InterpolationMode):
        ...
    
    @property
    def image_size(self) -> aspose.pydrawing.Size:
        ...
    
    @image_size.setter
    def image_size(self, value: aspose.pydrawing.Size):
        ...
    
    ...

class TiffSaveOptions(aspose.page.eps.device.ImageSaveOptions):
    '''Class for XPS-as-TIFF saving options.'''
    
    def __init__(self):
        '''Creates new instance of options.'''
        ...
    
    @property
    def page_numbers(self) -> list[int]:
        ...
    
    @page_numbers.setter
    def page_numbers(self, value: list[int]):
        ...
    
    @property
    def text_rendering_hint(self) -> aspose.pydrawing.Text.TextRenderingHint:
        ...
    
    @text_rendering_hint.setter
    def text_rendering_hint(self, value: aspose.pydrawing.Text.TextRenderingHint):
        ...
    
    @property
    def interpolation_mode(self) -> aspose.pydrawing.Drawing2D.InterpolationMode:
        ...
    
    @interpolation_mode.setter
    def interpolation_mode(self, value: aspose.pydrawing.Drawing2D.InterpolationMode):
        ...
    
    @property
    def image_size(self) -> aspose.pydrawing.Size:
        ...
    
    @image_size.setter
    def image_size(self, value: aspose.pydrawing.Size):
        ...
    
    @property
    def multipage(self) -> bool:
        '''Gets/sets the flag that defines if multiple images
        should be saved in a single multipage TIFF file.'''
        ...
    
    @multipage.setter
    def multipage(self, value: bool):
        ...
    
    ...

