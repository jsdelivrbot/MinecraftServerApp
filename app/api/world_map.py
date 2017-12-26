from app import app
from flask import Response, jsonify
from app.utilities.map_renderer import MinecraftWorldMapToImageGenerator

# todo: need to create config file to point to
images_path = '/opt/minecraft/server/mapcrafts'
jar_file_path = '/opt/minecraft/server/TMCMR/TMCMR.jar'
region_dir = '/opt/minecraft/server/world/region'

image_generator = MinecraftWorldMapToImageGenerator(
    jar_executable_path=jar_file_path,
    region_dir=region_dir,
    output_dir=images_path,
)


@app.route('/api/get_world_map', methods=['GET'])
def get_world_map():
    try:
        image_tiles = image_generator.get_tile_images()
        return Response(jsonify(image_tiles), 200)

    except Exception as error:
        return Response('get_world_map error, {}'.format(error), 404)


@app.route('/api/refresh_world_map', methods=['POST'])
def refresh_world_map():
    try:
        image_generator.create_image()
        return Response(200)
    except Exception as error:
        return Response('create_world_map error, {}'.format(error), 404)
