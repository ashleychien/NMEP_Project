"""
Configuration for the generate module
"""

#-----------------------------------------------------------------------------#
# Flags for running on CPU
#-----------------------------------------------------------------------------#
FLAG_CPU_MODE = True

#-----------------------------------------------------------------------------#
# Paths to models and biases
#-----------------------------------------------------------------------------#
paths = dict()

# Skip-thoughts
paths['skmodels'] = './models/'
paths['sktables'] = './tables/'

# Decoder
paths['decmodel'] = './storyteller/romance.npz'
paths['dictionary'] = './storyteller/romance_dictionary.pkl'

# Image-sentence embedding
paths['vsemodel'] = './storyteller/coco_embedding.npz'

# VGG-19 convnet
paths['vgg'] = './models/vgg/vgg19.pkl'
paths['pycaffe'] = './caffe-run/python'
paths['vgg_proto_caffe'] = './models/vgg/VGG_ILSVRC_19_layers_deploy.prototxt'
paths['vgg_model_caffe'] = './models/vgg/VGG_ILSVRC_19_layers.caffemodel'

# VIST training stories-in-sequence
paths['stories-in-sequence'] = './storyteller/vist_train_stories_in_sequence.txt'

# Biases
paths['negbias'] = './storyteller/caption_style.npy'
paths['posbias'] = './storyteller/romance_style.npy'
