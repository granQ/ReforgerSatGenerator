from PIL import Image, ImageDraw, ImageFilter, ImageOps

Image.MAX_IMAGE_PIXELS = None

layers = [
  'Asphalt_01',
  'BeachGrass_01',
  'Cobblestone_01_Wave',
  'Concrete_01',
  'Concrete_02',
  'Crop_Field_01',
  'Crop_Field_02',
  'Debris_Rock_01',
  'default',
  'Dirt_01',
  'Dirt_02',
  'ForestConiferous_01_Base',
  'ForestConiferous_02',
  'ForestDeciduous_01_Base',
  'ForestDeciduous_02',
  'Grass_01',
  'Grass_02',
  'Grass_03',
  'Heather_01',
  'MountainGrass_01',
  'Pebbles_01',
  'Pebbles_02',
  'Rock_01',
  'SeaBed_01'
]
tiled = True
blur = True
backgroundColor = '#405d34'

base_folder = 'p:/ReforgerSatGenerator'
textures_folder = f'{base_folder}/groundtexture'
masks_folder = f'{base_folder}/mask_export'

output_image = Image.open(f'{base_folder}/mask_export/Asphalt_01.png')
output_image = Image.new(mode="RGB", size=output_image.size, color='#00004c')

for layer in layers:
  if(tiled):
    groundtexture_image = Image.open(f'{textures_folder}/{layer}.jpg')
    bg_w, bg_h = groundtexture_image.size
    texture_w, texture_h = output_image.size
    texture_image = Image.new('RGB', (texture_w,texture_h))
    for i in range(0, texture_w, bg_w):
      for j in range(0, texture_h, bg_h):
        texture_image.paste(groundtexture_image, (i, j))
  else:
    texture_image = Image.open(f'{textures_folder}/{layer}.jpg').resize(output_image.size)
  if(blur):
    texture_image = texture_image.filter(ImageFilter.GaussianBlur(radius = 2))
  mask_image = Image.open(f'{masks_folder}/{layer}.png')
  mask_inverted_image = ImageOps.invert(mask_image)
  
  output_image = Image.composite(output_image, texture_image, mask_inverted_image)

output_image.save(f'{base_folder}/satellite.png', quality=95)
