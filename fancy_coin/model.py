import matplotlib.pyplot as plt
import numpy as np
import PIL
import urllib.request as request

class FancyCoin:
    def __init__(self, p=0.5):
        """
        p         : probability of head
        """
        self.p = p

    def run_MC(self, num_steps=5, seed=None):
        """
        num_steps : number of coin flips to make a sample path
        seed      : seed of random number generator
        """
        if seed is not None:
            np.random.seed(seed)

        url_head = "https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/US_Half_Dollar_Obverse_2015.png/154px-US_Half_Dollar_Obverse_2015.png"
        img_head = np.array(PIL.Image.open(request.urlopen(url_head)))

        url_tail = "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2d/US_50_Cent_Rev.png/154px-US_50_Cent_Rev.png"
        img_tail = np.array(PIL.Image.open(request.urlopen(url_tail)))

        fig, axes = plt.subplots(nrows=1, ncols=num_steps, figsize=(3*num_steps,3))
        for i in range(num_steps):
            if np.random.uniform() > 1 - self.p:
                axes[i].imshow(img_head)
            else:
                axes[i].imshow(img_tail)
            axes[i].axis('off')
        plt.show()


def main():
    obj = FancyCoin()
    obj.run_MC(num_steps=5, seed=0)

if __name__ == "__main__":
    main()