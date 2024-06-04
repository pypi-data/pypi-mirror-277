from typing import Sequence, TypedDict
from jaxtyping import Float, Int
from torch import Tensor, nn
import torch
import numpy as np
from .._loss import segmented_loss
from ... import uci
from .decode import argmax_ucis
from ..metrics import accuracy, consecutive_eq

def loss(
  logits: Float[Tensor, 'batch seq_len 36'],
  labels: Int[Tensor, 'batch seq_len 5'], *,
  ce_loss: nn.CrossEntropyLoss = nn.CrossEntropyLoss(ignore_index=-100)
) -> Float[Tensor, '']:
  losses = segmented_loss(logits, labels, loss=ce_loss, ends=[8, 16, 24, 32, 36])
  return sum(l for l in losses if not torch.isnan(l)) # type: ignore
  # nan may happen if all promotion labels are -100 (which is quite likely)

def metrics(sample_logits: Float[Tensor, 'L 5'], true_ucis: Sequence[str]) -> uci.Metrics:
  pred_ucis = argmax_ucis(sample_logits)
  return uci.metrics(uci_labs=true_ucis, uci_preds=pred_ucis[0])

class BatchMetrics(TypedDict):
  acc: float
  seq_acc: float
  consecutive_correct: float
  from_sq_acc: float
  to_sq_acc: float

def pt_metrics(y_pred: Int[Tensor, 'B L 5'], y_true: Int[Tensor, 'B L 5'], *, ignore_idx: int = -100) -> BatchMetrics:
  y_pred = y_pred.clone()
  y_pred[y_true == ignore_idx] = ignore_idx
  consecutive_mean = float(np.mean([consecutive_eq(p, l) for p, l in zip(y_pred, y_true)]))
  return BatchMetrics(
    acc=accuracy(y_pred, y_true).item(),
    seq_acc=consecutive_mean / y_true.size(1),
    consecutive_correct=consecutive_mean,
    from_sq_acc=accuracy(y_pred[:, :, :2], y_true[:, :, :2]).item(),
    to_sq_acc=accuracy(y_pred[:, :, 2:4], y_true[:, :, 2:4]).item(),
  )