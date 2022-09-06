{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "3b0aed30",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Welcome to Computer Quiz\n",
      "DO you want to play ?yes|no :yes\n",
      "Okay! Let's play\n",
      "who is father of Python is  ?gudio van rossum\n",
      "Correct!\n",
      "what does RAM stands for ?random access memory\n",
      "Correct!\n",
      "what does PSU stands for ?power \n",
      "Incorrect !\n",
      "what does CPU stands for ?central processing unit\n",
      "Correct!\n",
      "You Got 3 Questions Correct\n",
      "You Got 75.0 %.\n"
     ]
    }
   ],
   "source": [
    "print(\"Welcome to Computer Quiz\")\n",
    "\n",
    "playing = input('DO you want to play ?yes|no :')\n",
    "\n",
    "if playing.lower() != 'yes':\n",
    "    quit()\n",
    "print('Okay! Let\\'s play') \n",
    "score = 0\n",
    "\n",
    "answer = input(\"who is father of Python is  ?\").lower() \n",
    "if answer =='gudio van rossum':\n",
    "    print('Correct!')\n",
    "    score += 1\n",
    "else:\n",
    "    print('Incorrect !')\n",
    "answer = input(\"what does RAM stands for ?\").lower() \n",
    "if answer =='random access memory':\n",
    "    print('Correct!')\n",
    "    score += 1\n",
    "else:\n",
    "    print('Incorrect !')\n",
    "answer = input(\"what does PSU stands for ?\").lower() \n",
    "if answer =='power supply':\n",
    "    print('Correct!')\n",
    "    score += 1\n",
    "else:\n",
    "    print('Incorrect !')\n",
    "answer = input(\"what does CPU stands for ?\").lower() \n",
    "if answer =='central processing unit':\n",
    "    print('Correct!')\n",
    "    score += 1\n",
    "else:\n",
    "    print('Incorrect !')\n",
    "    \n",
    "print(\"You Got\",str(score),\"Questions Correct\")\n",
    "print(\"You Got\",str(score/4 *100),\"%.\")\n",
    "\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ba32283e",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
