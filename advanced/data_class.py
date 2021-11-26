from dataclasses immport dataclass # astuple, asdict

@dataclass(frozen = True, order = True)
class Comment:
  id: int
  text: str
    
def main():
  comment = Comment(1, "I just subscribed!")
  print(comment)                # Comment(id = 1, text = 'I just subscribed!')
  
  # print(astuple(comment))     -- (1, 'I just subscribed!'
  # print(asdict(comment))      -- {'id': 1, 'text': 'I just subscribed'}
  # pprint(inspect.getmembers(Comment, inspect.isfunction))
  
  
 if __name__ == '__main__':
  main()
 
