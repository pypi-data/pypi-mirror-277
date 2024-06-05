import chess
import chess.svg
from IPython.display import display
import ipywidgets as wg
from .observable import ObservableStr

def show_fen(fen: str, size: int):
  board = chess.Board(fen)
  return chess.svg.board(board=board, size=size)

class Board:
    
  def __init__(self, fen: ObservableStr, *, size: int = 512):
    super().__init__()
    self.fen = fen.value
    self.size = size
    self.svg = show_fen(self.fen, self.size)
    self.html = wg.HTML(value=self.svg)
    def callback(fen: str):
      self.svg = show_fen(fen, self.size)
      self.html.value = self.svg
    fen.observe(callback)
        
  def __call__(self):
    return self.html
  
  def _repr_svg_(self):
    return self.svg

  def _ipython_display_(self):
    display(self.svg)
