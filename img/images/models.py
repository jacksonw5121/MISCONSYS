# -*- coding: utf-8 -*-

#============================================#
#                                            #
#   Model to define the Database Schema by.  #
#                                            #
#          Author: davidkroell               #
#         Version: 0.0.1                     #
#                                                                                                              #
#============================================#

from __future__ import unicode_literals
from django.db import models


#-------------------------
#    Image entity
#
# Attributes:
#    - img_id:   Image id using primary Key
#    - img_path: Absolute path of the image file.
#    - lon:      longitude that the image was taken at.
#    - latitude: latitude that the image was taken at.
#-------------------------
class Image(models.Model):
    img_photo = models.ImageField(default="default.img", 
                                  blank=True, null=True, upload_to="images/unprocessed_%Y%m%d%H%M%S")
    
    img_path  = models.CharField(max_length=50)
    lon       = models.DecimalField(max_digits=9, decimal_places=6)
    lat       = models.DecimalField(max_digits=9, decimal_places=6)



#-------------------------
#    Targets entity
#
# Attributes:
#    - target_id:          The primary key for target information.
#    - img_path:           The absolute path of the image on that storage system.
#    - shape_choices:      The possible shapes the target could be.
#    - shape_color:        The possible colors the target could be.
#    - alphanumeric_color: The color of the letter in the shape.
#    - alphanumeric:       The character letter appearing in the shape.
#-------------------------
class Target(models.Model):
    image     = models.ForeignKey(Image, on_delete=models.CASCADE)
    
    SHAPE_CHOICES = (
        ('circle', 'Circle'),
        ('star', 'Star'),
        ('square', 'Square'),
        ('triangle', 'Triangle'),
        ('pentagon', 'Pentagon'),
        ('quarter_circle', 'Quarter-Circle'),
        ('semicircle', 'Semi-Circle'),
        ('trapezoid', 'Trapezoid'),
        ('heptagon', 'Heptagon'),
        ('hexagon', 'Hexagon'),
        ('star', 'Star'),
        ('cross', 'Cross')
    )

    shape_choices = models.CharField(max_length=15, choices=SHAPE_CHOICES, default="circle")
    
    COLORS = (
        ('white', 'White'),
        ('black', 'Black'),
        ('grey', 'Grey'),
        ('red', 'Red'),
        ('blue', 'Blue'),
        ('orange', 'Orange'),
        ('green', 'Green'),
        ('yellow', 'Yellow'),
        ('purple', 'Purple'),
        ('brown', 'Brown')
    )
    
    shape_color = models.CharField(max_length=10, choices=COLORS, default="white")
    
    alphanumeric = models.CharField(max_length=1)
    alphanumeric_color = models.CharField(max_length=10, choices=COLORS, default="white")

    DIRECTION = (
        ('ne', 'North East'),
        ('n', 'North'),
        ('nw', 'North West'),
        ('w', 'West'),
        ('sw', 'South West'),
        ('s', 'South'),
        ('se', 'South East'),
        ('e', 'East'),
    )

    direction = models.CharField(max_length=20, choices=DIRECTION, default='ne')
    
