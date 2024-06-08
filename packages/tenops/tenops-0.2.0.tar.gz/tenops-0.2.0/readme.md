# Ten(sor) Op(eration)s

The basic idea behind this repository is to allow for seamlessly switching between libraries like numpy, pytorch, and tensorflow by checking the input types and returning the proper function for use in some operation.

## Installation
Installation can be done over pip
```
pip install tenops
```

Note that for the library to work you'll need to have at least one of the following libraries installed:
- numpy
- torch
- tensorflow

## Usage

Functions work like regular functions, one just needs to pass in the object and the function will identify the corresponding module and use the appropriate function:

```
>>> import torch, numpy, tensorflow as tf
>>> from tenops.special import exp
>>> exp(numpy.array([0]))
array([1.])
>>> exp(torch.tensor([0]))
tensor([1.])
>>> exp(tf.constant([0.]))
<tf.Tensor: shape=(1,), dtype=float32, numpy=array([1.], dtype=float32)>
```

One can also just specify the module using the `default` parameter rather than typecasting directly (note that this requires that the specified library is installed):

```
>>> from tenops.special import exp
>>> exp([0], default="numpy")
array([1.])
>>> exp([0], default="torch")
tensor([1.])
>>> exp([0.], default="tensorflow")
<tf.Tensor: shape=(1,), dtype=float32, numpy=array([1.], dtype=float32)>
```


## Development

[Poetry](https://python-poetry.org/docs/) is used to manage the build process.
