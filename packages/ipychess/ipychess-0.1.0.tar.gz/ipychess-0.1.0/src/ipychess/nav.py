from typing import Callable
from traitlets import Int, HasTraits
import ipywidgets as wg
from IPython.display import display

class Nav(HasTraits):
  index = Int()
  
  def __init__(self, num_moves):
    super().__init__()
    self.num_moves = num_moves
    self.index = 0
    
    self.left_btn = wg.Button(description='⟵')
    self.right_btn = wg.Button(description='⟶')
    self.index_input = wg.BoundedIntText(
      value=0, min=0, max=num_moves-1, description='Move'
    )
    
    self.left_btn.on_click(self.on_left)
    self.right_btn.on_click(self.on_right)
    self.index_input.observe(self.on_index, names='value')
    
  def on_left(self, b):
    if self.index > 0:
      self.index -= 1
      self.index_input.value = self.index
    
  def on_right(self, b):
    if self.index < self.num_moves - 1:
      self.index += 1
      self.index_input.value = self.index
    
  def on_index(self, change):
    self.index = change['new']

  def observe(self, callback: Callable[[int], None]):
    """Observe the current index"""
    def _callback(change):
      callback(change['new'])
    super().observe(_callback, names='index')
    
  def __call__(self):
    return wg.HBox([self.left_btn, self.index_input, self.right_btn])
  
  def _ipython_display_(self):
    display(self())