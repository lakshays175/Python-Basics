from random import shuffle
def shuffle_list(my_list):
  shuffle(my_list)
  return (my_list)

def player_guess():
  guess= ''

  while guess not in ('0','1','2'):
    guess= input("Enter a guess: ")
  return int(guess)

def check(shuffle_list,guess):
  if shuffle_list[guess]== 'O':
      print("O Tusi Sahi ho! Agla bande noon aan do!")
  else:
    print("Tuhano kuch aanda hein nhi! Agli baar try kar kanjar")
    print(shuffle_list)
    guess= player_guess()
    check(shuffle_list,guess)


#Initial list
my_list=['','O','']
#shuffle_list
mixed_list= shuffle_list(my_list)

#user_guess
guess = player_guess()

#check guess
check(mixed_list,guess)