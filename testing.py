import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask

#qr = qrcode.make('Hello World')
#qr.save('myQr.png')

qr = qrcode.QRCode(
    version=4,
    box_size=15, 
    border=9
)


data = 'https://relaymile.com'
qr.add_data(data)
qr.make(fit=True)
img_1 = qr.make_image(image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer())
img_2 = qr.make_image(image_factory=StyledPilImage, color_mask=RadialGradiantColorMask())
img_1.save('test.png')
img_2.save('test2.png')