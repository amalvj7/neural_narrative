{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "9e0e3932-44e6-4e75-ad0a-a60793c59572",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "5538aeff-8e9f-4df0-9200-7f859c150da9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Epoch 0: Cost = 111.66666666666667, b = 0.2, m = 0.8166666666666668\n",
      "Epoch 100: Cost = 0.5342873401160694, b = 1.339778329300845, m = 2.387793668244803\n",
      "Epoch 200: Cost = 0.2571632313800838, b = 1.8481840887259684, m = 2.2690405295020555\n",
      "Epoch 300: Cost = 0.12377783003332864, b = 2.200901953709994, m = 2.1866528838450576\n",
      "Epoch 400: Cost = 0.059576756465295755, b = 2.445607860306259, m = 2.1294946122510163\n",
      "Epoch 500: Cost = 0.0286754898673648, b = 2.6153780553198094, m = 2.0898397831129194\n",
      "Epoch 600: Cost = 0.013802089403983099, b = 2.7331599246495557, m = 2.062328358604843\n",
      "Epoch 700: Cost = 0.0066432229334763135, b = 2.8148737304309663, m = 2.043241692619528\n",
      "Epoch 800: Cost = 0.003197516669550752, b = 2.871564510542364, m = 2.0299998912606765\n",
      "Epoch 900: Cost = 0.0015390290156504782, b = 2.910895007009953, m = 2.0208130954440477\n",
      "Epoch 1000: Cost = 0.0007407655864846235, b = 2.938181418474874, m = 2.014439550403666\n",
      "Epoch 1100: Cost = 0.0003565453597948745, b = 2.9571119766295766, m = 2.010017761001506\n",
      "Epoch 1200: Cost = 0.0001716124451657724, b = 2.970245474689927, m = 2.0069500457201097\n",
      "Epoch 1300: Cost = 8.260051779307777e-05, b = 2.9793571326712556, m = 2.004821749640898\n",
      "Epoch 1400: Cost = 3.9757288774087215e-05, b = 2.9856785491581057, m = 2.0033451966412574\n",
      "Epoch 1500: Cost = 1.913598186667069e-05, b = 2.990064173210512, m = 2.0023208049778787\n",
      "Epoch 1600: Cost = 9.210532541149304e-06, b = 2.993106797971758, m = 2.0016101103531305\n",
      "Epoch 1700: Cost = 4.433214364577098e-06, b = 2.9952176869415195, m = 2.0011170500640807\n",
      "Epoch 1800: Cost = 2.1337951431685626e-06, b = 2.9966821633697065, m = 2.000774978462338\n",
      "Epoch 1900: Cost = 1.0270384733455162e-06, b = 2.997698176641573, m = 2.0005376586389456\n"
     ]
    }
   ],
   "source": [
    "def gradient_descent( x , y , lr  , epochs ):\n",
    "    m = 0.0 \n",
    "    b  = 0.0\n",
    "\n",
    "    n  = len(y)\n",
    "\n",
    "    for epoch in range(epochs):\n",
    "        y_predict = m*x + b\n",
    "        error = y - y_predict\n",
    "        cost  = np.mean(error**2)\n",
    "\n",
    "        dm = -2*np.mean(error*x)\n",
    "        db = -2*np.mean(error)\n",
    "\n",
    "        b = b - db*lr\n",
    "        m = m - dm*lr\n",
    "\n",
    "        # Optional: Print cost every 100 iterations to monitor progress\n",
    "        if epoch % 100 == 0:\n",
    "            print(f\"Epoch {epoch}: Cost = {cost}, b = {b}, m = {m}\")\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    x  = np.array([1 , 2 ,3  , 4 ,5,6])\n",
    "    y  = np.array([5 , 7 , 9 ,11, 13, 15])\n",
    "\n",
    "    gradient_descent(x , y  , 0.01 , 2000)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a752190e-9adf-4eeb-b6e7-f6fa71e2df92",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3.10",
   "language": "python",
   "name": "python310"
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
   "version": "3.10.11"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
