import yaml
import random
import os
import string
import tempfile
import sys
from lib.generate_tiles import render_tiles

CONFIG_FILE = './config/config.yaml'

def get_config():
    with open(CONFIG_FILE) as f:
        return yaml.load(f, Loader=yaml.Loader)


def get_zoom_options(config, zoom):
    for options_item in config['scale']:
        zoom_range = options_item['zoom']
        zoom_list = range(zoom_range[0], zoom_range[1] + 1)

        if zoom in zoom_list:
            return options_item


def build_replace_map(db, options):
    replace_map = {}
    for values in [db, options]:
        for key in values:
            replace_map[key] = str(values[key])

    return replace_map


def generate_temp_filename():
    file = tempfile.NamedTemporaryFile()

    return file.name


def generate_map_file(tmpl, db, options):
    file = open(tmpl)
    content = file.read()
    file.close()

    replace_map = build_replace_map(db, options)

    for key in replace_map:
        content = content.replace('%%%s%%' % key.upper(), replace_map[key])

    output_filename = generate_temp_filename()
    output_file = open(output_filename, 'w')
    output_file.write(content)
    output_file.close()

    return output_filename


def render(zoom_min, zoom_max, output_dir):
    file = tempfile.NamedTemporaryFile()

    config = get_config()

    bbox = config['map']['bbox']
    db = config['db']

    for zoom in range(zoom_min, zoom_max + 1):
        zoom_options = get_zoom_options(config, zoom)

        map_template = zoom_options['template']
        map_file = generate_map_file(map_template, db, {
            'dir': os.getcwd()
        })

        print 'Rendering zoom ', zoom, '...'
        render_tiles(bbox, map_file, output_dir, zoom, zoom)


if __name__ == '__main__':
    [_, zoom_min, zoom_max, output_dir] = sys.argv

    render(int(zoom_min), int(zoom_max), output_dir)
