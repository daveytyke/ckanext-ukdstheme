# encoding: utf-8

'''plugin.py

'''
import random
import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

def get_bg_css():
    return random.randint(1,10)

class UKDSThemePlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.ITemplateHelpers)
    # Declare that this class implements IConfigurer.
    plugins.implements(plugins.IConfigurer)

    def update_config(self, config):

        # Add this plugin's templates dir to CKAN's extra_template_paths, so
        # that CKAN will use this plugin's custom templates.
        # 'templates' is the path to the templates dir, relative to this
        # plugin.py file.
        toolkit.add_template_directory(config, 'templates')
        toolkit.add_public_directory(config, 'public')
        toolkit.add_resource('assets', 'ukdstheme')
        toolkit.add_resource('assets', 'civic')

    # ITemplateHelpers

    def get_helpers(self):
        return {'get_bg_css': get_bg_css}
