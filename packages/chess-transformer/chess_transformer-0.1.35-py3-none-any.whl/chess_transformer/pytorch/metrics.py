from jaxtyping import Float
from torch import Tensor
import torch

def elementwise_eq(x: Float[Tensor, '*B L N'], y: Float[Tensor, '*B L N']) -> Float[Tensor, '*B L']:
  """Elementwise equality"""
  return (x == y).all(dim=-1)

def accuracy(y_pred: Float[Tensor, '*B L N'], y_true: Float[Tensor, '*B L N']) -> Float[Tensor, 'L']:
  """Proportion of equal elements, averaged across samples"""
  return torch.mean(elementwise_eq(y_pred, y_true).float())

def intra_accuracy(y_pred: Float[Tensor, '*B L N'], y_true: Float[Tensor, '*B L N']) -> Float[Tensor, '']:
  """Average accuracy within sequence elements (dimension N)"""
  return torch.mean((y_pred == y_true).float())

def consecutive_eq(y_pred: Float[Tensor, 'L *N'], y_true: Float[Tensor, 'L *N']) -> int:
  """Number of consecutive equal elements"""
  eq = elementwise_eq(y_pred, y_true)
  i_min = eq.int().argmin()
  return y_pred.size(0) if bool(torch.min(eq[i_min])) else i_min.item() # type: ignore
  # if all elements are equal (minimum is True), return the number of elements