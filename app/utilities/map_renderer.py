#! /usr/bin/python

# Minecraft map image generator is provided by the following resources:
# https://github.com/TOGoS/TMCMR/
# http://www.nuke24.net/projects/TMCMR/

import subprocess
import shlex

# todo: alot of these class var can be moved to config files I feel like


class MinecraftWorldMapToImageGenerator(object):
    def __init__(self, jar_executable_path, region_dir, output_dir):
        """
        :param jar_executable_path:
        :param region_dir: (str) explicit file path for minecraft world dir
        :param output_dir: (str) explicit path for image dest
        """
        self.jar_path = jar_executable_path
        self.region_dir = region_dir
        self.output_dir = output_dir

    def create_image(self):
        """
        Creates minecraft world image into a series of .png images
        :return: (bool)
        """
        command = 'sudo java -jar {jar_path} -create-big-image {region_dir} -o {output_dir}'.format(
            jar_path=self.jar_path,
            region_dir=self.region_dir,
            output_dir=self.output_dir,
        )

        process = subprocess.Popen(
            shlex.split(command),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=False,
        )

        stdout, stderr = process.communicate()
        if stderr:
            print('Error occurred when trying to create world image.')
            return False
        return True


    # comment: Do not need this.
    def get_tile_images(self):
        """
        :return: (arr) tiles
        """
        command = 'ls {output_dir}'.format(
            output_dir=self.output_dir,
        )

        process = subprocess.Popen(
            shlex.split(command),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=False,
        )

        stdout, stderr = process.communicate()
        if stderr:
            return False

        return [tile for tile in stdout.split() if 'png' in tile]

    def crop_image(self):
        """
        One downside of using TMCMR is that it leaves a ton of transparency pixels
        that need to be cropped out
        :return:
        """
        # Use PIL (pillow) for python image manipulation
        # get image
        # Start from top, find where transparent pixels end
        # Start from bottom, find where transparent pixels end
        # Start from midpt of top and bottom, from left find where transparent pixels end
        # Start from midpt of top and bottom, from right find where transparent pixels end

        # crop image based on coords
        # save image
        pass
