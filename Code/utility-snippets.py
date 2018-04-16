{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[9, 4, 4], [0, 11, 12], [1, 2, 10]]\n",
      "[[9, 4, 4, 15, 15, 9], [0, 11, 12, 12, 15, 6], [1, 2, 10, 8, 14, 5]]\n"
     ]
    }
   ],
   "source": [
    "import random\n",
    "\n",
    "#comprehensive method to get a matrice filled with random numbers\n",
    "rand_mat = [[random.randint(i,i+10) for i in range(3)] for j in range(3)]\n",
    "print(rand_mat)\n",
    "\n",
    "#simple method to get a matrice filled with random numbers\n",
    "for i in range(3):\n",
    "    for j in range(3):\n",
    "        rand_num = random.randint(5,15)\n",
    "        rand_mat[i].append(rand_num)\n",
    "print(rand_mat)\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
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
   "version": "3.6.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
