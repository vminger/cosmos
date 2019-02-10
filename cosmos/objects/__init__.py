# Copyright 2019 PandoraGo Co.,LTD.
# All Rights Reserved.
#
# Tony 2019/2/5: Add base object.  


def register_all():
    # NOTE(Tony): You must make sure your object gets imported in this
    # function in order for it to be registered by services.
    __import__('cosmos.objects.half_plus_two')
