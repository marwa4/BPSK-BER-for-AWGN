
import numpy as np
import matplotlib.pyplot as plt
import numpy.random as nr
from scipy.stats import norm


BlockLength = 10000000 # transmitted symbols
SNRdB = np.arange(1.0,14.1) # SNR range in dB
BER = np.zeros(SNRdB.size) # Initializaiton of the BER vector
SNR = 10**(SNRdB/10)
Sym = 2*nr.randint(2,size=BlockLength)-1


noise = nr.normal(0.0,1.0,BlockLength)

for itersnrdB in range(SNRdB.size):
    Txbits = np.sqrt(SNR[itersnrdB])*Sym
    Rxbits = Txbits+noise
    Decbits = 2*(Rxbits>0)-1
    BER[itersnrdB] = BER[itersnrdB]+np.sum(Decbits!=Sym)

BER = BER/BlockLength

plt.yscale('log')
plt.plot(SNRdB, BER, 'go')
plt.plot(SNRdB, 1-norm.cdf(np.sqrt(SNR)),'r-')
plt.grid(1,which = 'both')
plt.suptitle('BER for AWGN')
plt.xlabel('SNR (dB)')
plt.ylabel('BER')
plt.legend(['Experiments', 'Theory'])
plt.show()
