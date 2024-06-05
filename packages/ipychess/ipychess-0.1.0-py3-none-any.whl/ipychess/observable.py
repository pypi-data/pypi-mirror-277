from typing import Callable
from traitlets import HasTraits, Unicode

class ObservableStr(HasTraits):
  """What trailets should've had in the first place. A freaking observable value."""
  value = Unicode()
  def __init__(self, value: str):
    self.value = value
  def observe(self, callback: Callable[[str], None]):
    def _callback(change):
      callback(change['new'])
    super().observe(_callback, names='value')