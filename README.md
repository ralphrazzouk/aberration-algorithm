# Aberration Algorithm

This algorithm is designed for detecting when seismic activity begins on the Moon and Mars.


## Installation


## Interactive Example with Documentation
The link [example.ipynb](https://github.com/ralphrazzouk/aberration-algorithm/blob/master/example.ipynb) directs you to a Jupyter notebook that runs throught the basics, accompanied by documentation that breaks down how to use the model we developed.

## Models
### Classical Models
- Short-Term Average / Long-Term Average
### Machine Learning Models
- Darts
- ScikitLearn
- PyTorch

## Paper
Linked below is the paper we wrote alongside our development of the code that describes the model and different approaches to the challenge.

## Data Format
The data was provided by the [Space Apps 2024 Seismic Detection Data Packet](https://wufs.wustl.edu/SpaceApps/data/space_apps_2024_seismic_detection.zip).

The training and testing data, for both the Moon and Mars, where given in `.csv` and `.mseed` files, so we made sure that our model works well at taking both as input. Additionally, our model can accept `hdf5` and `numpy` data.

## Training
### Moon
The training data for the Moon can be found at

### Mars
The training data for Mars can be found at



## Testing
### Moon
The testing data for the Moon can be found at

### Mars
The testing data for Mars can be found at



## Notes


## References