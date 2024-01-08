from os import walk
import pygame

def import_folder(path,rescale):
    """Importiert alle Bilder aus einem Ordner und gibt sie als Liste zurück."""
    surface_list = []
    
    for _, __, img_files in walk(path):
        for img in img_files:
            full_path = path +'/' + img
            img_surface = pygame.image.load(full_path).convert_alpha()
            img_surface = pygame.transform.scale(img_surface,rescale)
            surface_list.append(img_surface)
    
    return surface_list