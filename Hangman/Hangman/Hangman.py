word = "konya"
word2 = "_____"


list1 = list(word)
list2 = list(word2)

list3 = list()


tries =5
print("Let's play hangman! I have a word for you! ")
print("Here is the word:")


print(word2)

while tries >=0:
    ch = input("What is the letter or word you thinking?")
    if(len(ch)==1) and ch.isalpha():
        if ch in list3:
            print(f"You have already guessed {ch}")    
        elif ch in word:
            k = int(word.index(ch))
            list2[k] = list1[k]
            print(''.join(list2))
            list3.append(ch)
        elif ch not in word:
            tries-=1 
            list3.append(ch)
            print(f"{ch} is not found.")
    if len(ch)==len(word):
        if ch==word:
            print("Congratulations! You guessed the word!")
            break
        else:
            tries-=1
            print("Wrong word :(")
    if list1==list2:
        print("Congratulations! You guessed the word!")
        break
    if tries==0:
        print(f"You lose :( The word was {word}")
        break
        
      