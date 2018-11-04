import time

def boil_udon():
  print('  うどんを茹でます。')
  time.sleep(3)
  print('  うどんが茹であがりました。')

def make_tuyu():
  print('  ツユをつくります。')
  time.sleep(2)
  print('  ツユができました。')

print('うどんを作ります。')
boil_udon()
make_tuyu()
print('盛り付けます。')
print('うどんができました。')
