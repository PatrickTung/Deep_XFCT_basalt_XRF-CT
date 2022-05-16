# Deep_XFCT_basalt_XRF-CT

The files included are:

1) A Jupyter notebook that applies bilateral filtering and k-means clustering. Intended for use with X-ray flouresence elemental maps.
2) A Dragonfly ORS macro (written as python code) that registers images and resamples the labelled clustered images into the geometry of a target micro-CT image. Followed by conversion into a Multi-ROI and then back into an image to be used for deep learning segmentation training data.
3) The remaining are files for the Segmentation Wizard from Dragonfly ORS, including the the trained model and training parameters.
