import aspose.page
import aspose.pydrawing
import datetime
import decimal
import io
import uuid
from typing import Iterable

class ImageDevice(aspose.page.Device):
    '''This class encapsulates rendering of document to image.'''
    
    @overload
    def __init__(self):
        '''Initializes new instance of :class:`ImageDevice`.'''
        ...
    
    @overload
    def __init__(self, size: aspose.pydrawing.Size):
        '''Initializes new instance of :class:`ImageDevice` with specified size of a page.
        
        :param size: Page size.'''
        ...
    
    @overload
    def __init__(self, image_format: aspose.pydrawing.Imaging.ImageFormat):
        '''Initializes new instance of :class:`ImageDevice` with specified image format.
        
        :param image_format: Format of the image.'''
        ...
    
    @overload
    def __init__(self, size: aspose.pydrawing.Size, image_format: aspose.pydrawing.Imaging.ImageFormat):
        '''Initializes new instance of :class:`ImageDevice` with specified size of a page and image format.
        
        :param size: Page size.
        :param image_format: Format of the image.'''
        ...
    
    @overload
    def open_page(self, title: str) -> bool:
        '''Makes necessary preparation of the device before page rendering.
        
        :param title: The page title.
        :returns: Always true.'''
        ...
    
    @overload
    def open_page(self, width: float, height: float) -> bool:
        '''Makes necessary preparation of the device before each page rendering.
        
        :param width: A width of the page.
        :param height: A height of the page.
        :returns: Always true.'''
        ...
    
    def init_page_numbers(self) -> None:
        '''Initializes numbers of pages to output.'''
        ...
    
    def close_page(self) -> None:
        '''Makes necessary preparation of the device after page has been rendered.'''
        ...
    
    def update_page_parameters(self, device: aspose.page.IMultiPageDevice) -> None:
        '''Updates page parameters from other multi-paged device.
        
        :param device: Another instance of the same device.'''
        ...
    
    @property
    def current_page_number(self) -> int:
        '''Current page number.'''
        ...
    
    @property
    def images_bytes(self) -> list[bytes]:
        '''Returns resulting images in bytes, one byte array for one page.'''
        ...
    
    TRANSPARENT: str
    
    BACKGROUND: str
    
    BACKGROUND_COLOR: str
    
    PAGE_SIZE: str
    
    PAGE_MARGINS: str
    
    ORIENTATION: str
    
    FIT_TO_PAGE: str
    
    EMBED_FONTS: str
    
    EMIT_WARNINGS: str
    
    EMIT_ERRORS: str
    
    PRODUCER: str
    
    ...

class ImageSaveOptions(aspose.page.SaveOptions):
    '''This class contains options necessary for managing image saving process.'''
    
    @overload
    def __init__(self):
        '''Initializes a new instance of the :class:`ImageSaveOptions` class with default values
        for flags  (true) and  (false).'''
        ...
    
    @overload
    def __init__(self, image_format: aspose.page.drawing.imaging.ImageFormat):
        '''Initializes a new instance of the :class:`ImageSaveOptions` with
        with specified image format.
        
        :param image_format: The format of the image.'''
        ...
    
    @overload
    def __init__(self, size: aspose.page.drawing.Size):
        '''Initializes a new instance of the :class:`ImageSaveOptions` with
        with specified size of the image.
        
        :param size: The image size.'''
        ...
    
    @overload
    def __init__(self, size: aspose.page.drawing.Size, image_format: aspose.page.drawing.imaging.ImageFormat):
        '''Initializes a new instance of the :class:`ImageSaveOptions` with
        with specified size of the image and image format.
        
        :param size: The image size.
        :param image_format: The format of the image.'''
        ...
    
    @overload
    def __init__(self, image_format: aspose.page.drawing.imaging.ImageFormat, supress_errors: bool):
        '''Initializes a new instance of the :class:`ImageSaveOptions` with
        with specified image format.
        
        :param image_format: The format of the image.
        :param supress_errors: Specifies whether errors must be suppressed or not.
                               If true suppressed errors are added to  list.'''
        ...
    
    @overload
    def __init__(self, size: aspose.page.drawing.Size, supress_errors: bool):
        '''Initializes a new instance of the :class:`ImageSaveOptions` with
        with specified size.
        
        :param size: The image size.
        :param supress_errors: Specifies whether errors must be suppressed or not.
                               If true suppressed errors are added to  list.'''
        ...
    
    @overload
    def __init__(self, size: aspose.page.drawing.Size, image_format: aspose.page.drawing.imaging.ImageFormat, supress_errors: bool):
        '''Initializes a new instance of the :class:`ImageSaveOptions` with
        with specified size of the image and image format.
        
        :param size: The image size.
        :param image_format: The format of the image.
        :param supress_errors: Specifies whether errors must be suppressed or not.
                               If true suppressed errors are added to  list.'''
        ...
    
    @overload
    def __init__(self, supress_errors: bool):
        '''Initializes a new instance of the :class:`ImageSaveOptions` with
        default value for flag  (false).
        
        :param supress_errors: Specifies whether errors must be suppressed or not.
                               If true suppressed errors are added to  list.'''
        ...
    
    @property
    def smoothing_mode(self) -> aspose.page.drawing.drawing2d.SmoothingMode:
        '''Gets/sets the smoothing mode for rendering image.'''
        ...
    
    @smoothing_mode.setter
    def smoothing_mode(self, value: aspose.page.drawing.drawing2d.SmoothingMode):
        ...
    
    @property
    def resolution(self) -> float:
        '''Gets/sets the image resolution.'''
        ...
    
    @resolution.setter
    def resolution(self, value: float):
        ...
    
    @property
    def image_format(self) -> aspose.page.drawing.imaging.ImageFormat:
        '''Gets/sets an image format for resulting image.'''
        ...
    
    @image_format.setter
    def image_format(self, value: aspose.page.drawing.imaging.ImageFormat):
        ...
    
    ...

class PdfDevice(aspose.page.Device):
    '''This class encapsulates rendering of document to PDF.'''
    
    @overload
    def __init__(self, ros: io.BytesIO):
        '''Initializes new instance of :class:`PdfDevice` with output stream.
        
        :param ros: Output stream.'''
        ...
    
    @overload
    def __init__(self, ros: io.BytesIO, size: aspose.pydrawing.Size):
        '''Initializes new instance of :class:`PdfDevice` with output stream and specified size of a page.
        
        :param ros: Output stream.
        :param size: Page size.'''
        ...
    
    @overload
    def open_page(self, title: str) -> bool:
        '''Makes necessary preparation of the device before page rendering.
        
        :param title: The page title.
        :returns: Always true.'''
        ...
    
    @overload
    def open_page(self, width: float, height: float) -> bool:
        '''Makes necessary preparation of the device before each page rendering.
        
        :param width: A width of the page.
        :param height: A height of the page.
        :returns: Always true.'''
        ...
    
    def init_page_numbers(self) -> None:
        '''Initializes numbers of pages to output.'''
        ...
    
    def close_page(self) -> None:
        '''Makes necessary preparation of the device after page has been rendered.'''
        ...
    
    def update_page_parameters(self, device: aspose.page.IMultiPageDevice) -> None:
        '''Updates page parameters from other multi-paged device.
        
        :param device: Another instance of the same device.'''
        ...
    
    @property
    def current_page_number(self) -> int:
        '''Current page number.'''
        ...
    
    @property
    def output_stream(self) -> io.BytesIO:
        '''Specifies or returns an output stream.'''
        ...
    
    @output_stream.setter
    def output_stream(self, value: io.BytesIO):
        ...
    
    VERSION: str
    
    VERSION5: str
    
    TRANSPARENT: str
    
    BACKGROUND: str
    
    BACKGROUND_COLOR: str
    
    PAGE_SIZE: str
    
    PAGE_MARGINS: str
    
    ORIENTATION: str
    
    FIT_TO_PAGE: str
    
    EMBED_FONTS: str
    
    EMBED_FONTS_AS: str
    
    COMPRESS: str
    
    WRITE_IMAGES_AS: str
    
    AUTHOR: str
    
    TITLE: str
    
    SUBJECT: str
    
    KEYWORDS: str
    
    EMIT_WARNINGS: str
    
    EMIT_ERRORS: str
    
    ...

class PdfSaveOptions(aspose.page.SaveOptions):
    '''This class contains input and output streams and other options necessary for managing conversion process.'''
    
    @overload
    def __init__(self):
        '''Initializes a new instance of the :class:`PdfSaveOptions` class with default values
        for flags  (true) and  (false).'''
        ...
    
    @overload
    def __init__(self, supress_errors: bool):
        '''Initializes a new instance of the :class:`PdfSaveOptions` class with default values for flag  (false).
        
        :param supress_errors: Specifies whether errors must be suppressed or not.
                               If true suppressed errors are added to  list.'''
        ...
    
    @overload
    def __init__(self, size: aspose.page.drawing.Size):
        '''Initializes a new instance of the :class:`PdfSaveOptions` with
        with specified size of the page.
        
        :param size: The page size.'''
        ...
    
    @overload
    def __init__(self, supress_errors: bool, size: aspose.page.drawing.Size):
        '''Initializes a new instance of the :class:`PdfSaveOptions` class with default values for flag  (false) and with specified size of the page.
        
        :param supress_errors: Specifies whether errors must be suppressed or not.
                               If true suppressed errors are added to  list.
        :param size: The page size.'''
        ...
    
    ...

class PsSaveOptions(aspose.page.SaveOptions):
    '''This class contains options necessary for managing process of converting document to PostScript (PS) or Encapsulated PostScript (EPS) file.'''
    
    @overload
    def __init__(self):
        '''Initializes a new instance of the :class:`PsSaveOptions` class with default values
        for flags  (true) and  (false).'''
        ...
    
    @overload
    def __init__(self, supress_errors: bool):
        '''Initializes a new instance of the :class:`PsSaveOptions` class with default values for flag  (false).
        
        :param supress_errors: Specifies whether errors must be suppressed or not.
                               If true suppressed errors are added to  list.'''
        ...
    
    @property
    def save_format(self) -> aspose.page.eps.device.PsSaveFormat:
        '''The save format of resulting file.'''
        ...
    
    @save_format.setter
    def save_format(self, value: aspose.page.eps.device.PsSaveFormat):
        ...
    
    @property
    def page_size(self) -> aspose.page.drawing.Size:
        '''The size of the page.'''
        ...
    
    @page_size.setter
    def page_size(self, value: aspose.page.drawing.Size):
        ...
    
    @property
    def margins(self) -> aspose.page.Margins:
        '''The margins of the page.'''
        ...
    
    @margins.setter
    def margins(self, value: aspose.page.Margins):
        ...
    
    @property
    def background_color(self) -> aspose.page.drawing.Color:
        '''The background color.'''
        ...
    
    @background_color.setter
    def background_color(self, value: aspose.page.drawing.Color):
        ...
    
    @property
    def transparent(self) -> bool:
        '''Indicates if background is transparent.'''
        ...
    
    @transparent.setter
    def transparent(self, value: bool):
        ...
    
    @property
    def embed_fonts(self) -> bool:
        '''Indicates whether to embed used fonts in PS document.'''
        ...
    
    @embed_fonts.setter
    def embed_fonts(self, value: bool):
        ...
    
    @property
    def embed_fonts_as(self) -> str:
        '''A type of font in which to embed fonts in PS document.'''
        ...
    
    @embed_fonts_as.setter
    def embed_fonts_as(self, value: str):
        ...
    
    ...

class PsSaveFormat:
    '''This enumeration contains available options of saving format. It can be PS or EPS.
    EPS is used for only 1-paged documents while PS file can contain any number of pages.'''
    
    PS: int
    EPS: int

