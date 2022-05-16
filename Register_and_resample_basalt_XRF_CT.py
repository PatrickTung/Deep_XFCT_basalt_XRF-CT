"""


:author: Patrick Tung
:contact: 
:email: patrick.tung@unsw.edu.au
:organization: University of New South Wales
:address: 
:copyright: 
:date: May 16 2022 13:32
:dragonflyVersion: 2022.1.0.1231
:UUID: 7c2e9cded4c711ec9852a4bb6d607461
"""

__version__ = '1.0.3'

# Action log Mon May 16 13:34:30 2022

# Macro name: Register_and_resample_basalt_XRF_CT

# ********** BEGIN MACRO ********** #
"""
Register a mobile dataset with a fixed dataset.

:name: register
:execution: execute

:param fixedChannel: reference dataset (fixed in space).
:type fixedChannel: ORSModel.ors.Channel
:param mobileChannel: mobile dataset.
:type mobileChannel: ORSModel.ors.Channel
:param useScale: if True, the scale factor will be used.
:type useScale: bool
:param useRotation: if True, the rotation factor will be used.
:type useRotation: bool
:param useTranslation: if True, the translation factor will be used.
:type useTranslation: bool
:param xScaleInitial: initial value for the scale factor in the X direction
:type xScaleInitial: float
:param yScaleInitial: initial value for the scale factor in the Y direction
:type yScaleInitial: float
:param zScaleInitial: initial value for the scale factor in the Z direction
:type zScaleInitial: float
:param xRotationInitial: initial value for the rotation factor in the X direction
:type xRotationInitial: float
:param yRotationInitial: initial value for the rotation factor in the Y direction
:type yRotationInitial: float
:param zRotationInitial: initial value for the rotation factor in the Z direction
:type zRotationInitial: float
:param xTranslationInitial: initial value for the translation factor in the X direction
:type xTranslationInitial: float
:param yTranslationInitial: initial value for the translation factor in the Y direction
:type yTranslationInitial: float
:param zTranslationInitial: initial value for the translation factor in the Z direction
:type zTranslationInitial: float
:param xScaleSmallest: final value for the scale factor in the X direction
:type xScaleSmallest: float
:param yScaleSmallest: final value for the scale factor in the Y direction
:type yScaleSmallest: float
:param zScaleSmallest: final value for the scale factor in the Z direction
:type zScaleSmallest: float
:param xRotationSmallest: final value for the rotation factor in the X direction
:type xRotationSmallest: float
:param yRotationSmallest: final value for the rotation factor in the Y direction
:type yRotationSmallest: float
:param zRotationSmallest: final value for the rotation factor in the Z direction
:type zRotationSmallest: float
:param xTranslationSmallest: final value for the translation factor in the X direction
:type xTranslationSmallest: float
:param yTranslationSmallest: final value for the translation factor in the Y direction
:type yTranslationSmallest: float
:param zTranslationSmallest: final value for the translation factor in the Z direction
:type zTranslationSmallest: float
:param nearestInterpolationMethod: if True, the nearest interpolation method will be used; if False, the linear interpolation will be used.
:type nearestInterpolationMethod: bool
:param mutualInfoRegistrationMethod: if True, the mutual information registration algorithm will be used; if False, the SSD registration algorithm will be used.
:type mutualInfoRegistrationMethod: bool
:param xSampling: sampling in the X direction for the similarity metric
:type xSampling: int
:param ySampling: sampling in the Y direction for the similarity metric
:type ySampling: int
:param zSampling: sampling in the Z direction for the similarity metric
:type zSampling: int
:param mask: Visual Shape 3D or ROI that mask pixels of fixed dataset to make a scored registration.
:type mask: ORSModel.ors.ROI, ORSModel.ors.VisualShape3D
:param useMultiScale: Use a multiscale step in the registration
:type useMultiScale: bool

:return transformationMatrix: transformation matrix to go from the original location of the mobile dataset to the final location of the mobile dataset
:rtype transformationMatrix: ORSModel.ors.Matrix4x4
:return metricSimilarity: value of the similarity obtained by the registration
:rtype metricSimilarity: float
"""

# ----- BEGIN INPUT ARGUMENT DEFINITION ----- #
useScale = True

useRotation = True

useTranslation = True

xScaleInitial = 0.1

yScaleInitial = 0.1

zScaleInitial = 0.1

xRotationInitial = 0.174533

yRotationInitial = 0.174533

zRotationInitial = 0.174533

xTranslationInitial = 0.0024885000000000003

yTranslationInitial = 0.0024885000000000003

zTranslationInitial = 0.0024885000000000003

xScaleSmallest = 0.001

yScaleSmallest = 0.001

zScaleSmallest = 0.001

xRotationSmallest = 0.00872665

yRotationSmallest = 0.00872665

zRotationSmallest = 0.00872665

xTranslationSmallest = 9.875000000000001e-06

yTranslationSmallest = 9.875000000000001e-06

zTranslationSmallest = 9.875000000000001e-06

nearestInterpolationMethod = False

mutualInfoRegistrationMethod = True

xSampling = 2

ySampling = 2

zSampling = 1

mask = None

useMultiScale = False

# ----- END INPUT ARGUMENT DEFINITION ----- #
# Interface method
transformationMatrix, metricSimilarity = OrsChannelRegistration.register(fixedChannel=fixedChannel,
                                                                         mobileChannel=mobileChannel,
                                                                         useScale=useScale,
                                                                         useRotation=useRotation,
                                                                         useTranslation=useTranslation,
                                                                         xScaleInitial=xScaleInitial,
                                                                         yScaleInitial=yScaleInitial,
                                                                         zScaleInitial=zScaleInitial,
                                                                         xRotationInitial=xRotationInitial,
                                                                         yRotationInitial=yRotationInitial,
                                                                         zRotationInitial=zRotationInitial,
                                                                         xTranslationInitial=xTranslationInitial,
                                                                         yTranslationInitial=yTranslationInitial,
                                                                         zTranslationInitial=zTranslationInitial,
                                                                         xScaleSmallest=xScaleSmallest,
                                                                         yScaleSmallest=yScaleSmallest,
                                                                         zScaleSmallest=zScaleSmallest,
                                                                         xRotationSmallest=xRotationSmallest,
                                                                         yRotationSmallest=yRotationSmallest,
                                                                         zRotationSmallest=zRotationSmallest,
                                                                         xTranslationSmallest=xTranslationSmallest,
                                                                         yTranslationSmallest=yTranslationSmallest,
                                                                         zTranslationSmallest=zTranslationSmallest,
                                                                         nearestInterpolationMethod=nearestInterpolationMethod,
                                                                         mutualInfoRegistrationMethod=mutualInfoRegistrationMethod,
                                                                         xSampling=xSampling,
                                                                         ySampling=ySampling,
                                                                         zSampling=zSampling,
                                                                         mask=mask,
                                                                         useMultiScale=useMultiScale)

# ----- BEGIN RETURNED VALUES DEFINITION ----- #
# transformationMatrix = orsMatrix(1.0015482132287294, -0.0054413261403525254, 0, 5.2415448708352476e-05, 0.0054626546143213559, 0.99763775274704836, 0, -2.791176900341307e-05, 0, 0, 0.99999999999999989, 0, 0, 0, 0, 0.99999999999999989)

# metricSimilarity = 1.12115476176262

# ----- END RETURNED VALUES DEFINITION ----- #
# ********** END MACRO ********** #

# ********** BEGIN MACRO ********** #
"""
Creates a new instance of class Progress

:name: __new__
:execution: execute

:return aProgress: the created instance of class Progress
:rtype aProgress: ORSModel.ors.Progress
"""

# Interface method
aProgress = Progress(logging=True)

# ----- BEGIN RETURNED VALUES DEFINITION ----- #
# aProgress = orsObj('145F4F1FE995443587122AE2D8D3A6B9CxvProgress')

# ----- END RETURNED VALUES DEFINITION ----- #
# ********** END MACRO ********** #

# ********** BEGIN MACRO ********** #
"""
:name: startWorkingProgressWithID
:execution: execute

:param aProgress: 
:type aProgress: ORSModel.ors.Progress
:param iID: 
:type iID: int
:param bCancellable: 
:type bCancellable: bool
"""

# ----- BEGIN INPUT ARGUMENT DEFINITION ----- #
iID = 45

bCancellable = True

# ----- END INPUT ARGUMENT DEFINITION ----- #
# Interface method
aProgress.startWorkingProgressWithID(iID=iID,
                                     bCancellable=bCancellable,
                                     logging=True)

# ********** END MACRO ********** #

# ********** BEGIN MACRO ********** #
"""
Creates a new MultiROI where each pixel is contained in the label matching the dataset value at that location

:name: createMultiROIFromDataset
:execution: execute

:param dataset: a dataset
:type dataset: ORSModel.ors.Channel
:param multiROI: multiROI output object. May be None.
:type multiROI: ORSModel.ors.MultiROI
:param aProgress: progress object
:type aProgress: ORSModel.ors.Progress

:return aMultiROI: new MultiROI
:rtype aMultiROI: ORSModel.ors.MultiROI
"""

# ----- BEGIN INPUT ARGUMENT DEFINITION ----- #
multiROI = None

# ----- END INPUT ARGUMENT DEFINITION ----- #
# Interface method
aMultiROI = DatasetHelper.createMultiROIFromDataset(dataset=dataset,
                                                    multiROI=multiROI,
                                                    IProgress=aProgress)

# ----- BEGIN RETURNED VALUES DEFINITION ----- #
# aMultiROI = orsObj('4FB9759004764AF5827AF048FC8A7AB0CxvLabeledMultiROI')

# ----- END RETURNED VALUES DEFINITION ----- #
# ********** END MACRO ********** #

# ********** BEGIN MACRO ********** #
"""
:name: deleteObject
:execution: execute

:param aProgress: 
:type aProgress: ORSModel.ors.Managed
"""

# Interface method
aProgress.deleteObject(logging=True)

# ********** END MACRO ********** #

# ********** BEGIN MACRO ********** #
"""
Sets an object as representable and notifies the Dragonfly UI of a new available object

:name: publish
:execution: execute

:param aMultiROI: 
:type aMultiROI: ORSModel.ors.Managed
"""

# Interface method
aMultiROI.publish(logging=True)

# ********** END MACRO ********** #

# ********** BEGIN MACRO ********** #
"""
Resamples a new dataset using another structured grid

:name: copyStructuredGridIntoAnotherShape
:execution: execute

:param aMultiROI: the structured grid to resample
:type aMultiROI: ORSModel.ors.StructuredGrid
:param mobileChannel: the structured grid having the shape of reference
:type mobileChannel: ORSModel.ors.StructuredGrid
:param newTitle: the title of the new dataset
:type newTitle: str

:return derivedDataset: a new resampled dataset
:rtype derivedDataset: ORSModel.ors.StructuredGrid
"""

# ----- BEGIN INPUT ARGUMENT DEFINITION ----- #
newTitle = 'tomo_closeTo2_mask_Labels (as Multi-ROI) (Resampled)'

# ----- END INPUT ARGUMENT DEFINITION ----- #
# Interface method
derivedDataset = OrsDerivedDataset.copyStructuredGridIntoAnotherShape(sourceStructuredGrid=aMultiROI,
                                                                      referenceStructureGrid=mobileChannel,
                                                                      newTitle=newTitle)

# ----- BEGIN RETURNED VALUES DEFINITION ----- #
# derivedDataset = orsObj('0AC3D25DE56E4137B3052CAC7A896E6ECxvLabeledMultiROI')

# ----- END RETURNED VALUES DEFINITION ----- #
# ********** END MACRO ********** #

# ********** BEGIN MACRO ********** #
"""
Sets an object as representable and notifies the Dragonfly UI of a new available object

:name: publish
:execution: execute

:param derivedDataset: 
:type derivedDataset: ORSModel.ors.Managed
"""

# Interface method
derivedDataset.publish(logging=True)

# ********** END MACRO ********** #

# ********** BEGIN MACRO ********** #
"""
Creates a new instance of class Progress

:name: __new__
:execution: execute

:return aProgress_2: the created instance of class Progress
:rtype aProgress_2: ORSModel.ors.Progress
"""

# Interface method
aProgress_2 = Progress(logging=True)

# ----- BEGIN RETURNED VALUES DEFINITION ----- #
# aProgress_2 = orsObj('23EEBA8CD5234D60A7076EFAA40CAE80CxvProgress')

# ----- END RETURNED VALUES DEFINITION ----- #
# ********** END MACRO ********** #

# ********** BEGIN MACRO ********** #
"""
:name: startWorkingProgressWithID
:execution: execute

:param aProgress_2: 
:type aProgress_2: ORSModel.ors.Progress
:param iID_2: 
:type iID_2: int
:param bCancellable_2: 
:type bCancellable_2: bool
"""

# ----- BEGIN INPUT ARGUMENT DEFINITION ----- #
iID_2 = 78

bCancellable_2 = True

# ----- END INPUT ARGUMENT DEFINITION ----- #
# Interface method
aProgress_2.startWorkingProgressWithID(iID=iID_2,
                                       bCancellable=bCancellable_2,
                                       logging=True)

# ********** END MACRO ********** #

# ********** BEGIN MACRO ********** #
"""
Creates a new dataset where the value at each pixel is the label in the MultiROI

:name: createDatasetFromMultiROI
:execution: execute

:param derivedDataset: a MultiROI
:type derivedDataset: ORSModel.ors.MultiROI
:param aProgress_2: progress object
:type aProgress_2: ORSModel.ors.Progress

:return dataset_2: new dataset
:rtype dataset_2: ORSModel.ors.Channel
"""

# Interface method
dataset_2 = DatasetHelper.createDatasetFromMultiROI(aMultiROI=derivedDataset,
                                                    IProgress=aProgress_2)

# ----- BEGIN RETURNED VALUES DEFINITION ----- #
# dataset_2 = orsObj('BF621B341ED14C33B9554D1976809DB6CxvChannel')

# ----- END RETURNED VALUES DEFINITION ----- #
# ********** END MACRO ********** #

# ********** BEGIN MACRO ********** #
"""
:name: deleteObject
:execution: execute

:param aProgress_2: 
:type aProgress_2: ORSModel.ors.Managed
"""

# Interface method
aProgress_2.deleteObject(logging=True)

# ********** END MACRO ********** #

# ********** BEGIN MACRO ********** #
"""
Sets an object as representable and notifies the Dragonfly UI of a new available object

:name: publish
:execution: execute

:param dataset_2: 
:type dataset_2: ORSModel.ors.Managed
"""

# Interface method
dataset_2.publish(logging=True)

# ********** END MACRO ********** #

