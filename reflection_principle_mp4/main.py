import numpy as np
import os
import matplotlib.pyplot as plt
from matplotlib import animation

# animation function.  This is called sequentially
def animate(i, line1, line2, line3):
    t = [0,  1,  2,  3, 4, 5, 6, 7, 8,  9, 10]
    y = [0, -1, -2, -1, 0, \
         1+(1-1)*np.cos(np.pi*i/180), \
         1+(2-1)*np.cos(np.pi*i/180), \
         1+(1-1)*np.cos(np.pi*i/180), \
         1+(0-1)*np.cos(np.pi*i/180), \
         1+(-1-1)*np.cos(np.pi*i/180), \
         1+(0-1)*np.cos(np.pi*i/180)]     
    line1.set_data(t, y)
    
    t2 = [5, 6, 7, 8, 9, 10]
    y2 = [1, 1, 1, 1, 1,  1]
    line2.set_data(t2, y2)
    
    t3 = [5, 6, 7, 8,  9, 10]
    y3 = [1, 2, 1, 0, -1,  0]    
    line3.set_data(t3, y3)
        
    return line1, line2, line3

def main():
    # First set up the figure, the axis, and the plot element we want to animate
    fig = plt.figure()
    ax = plt.axes(xlim=(-1, 11), ylim=(-4, 4))
    line1, = ax.plot([], [], '-o'); line1.set_data([], [])
    line2, = ax.plot([], [], '--r'); line2.set_data([], [])
    line3, = ax.plot([], [], '--o', alpha=0.5); line3.set_data([], [])
    ax.grid(True)

    # call the animator.  
    # We've chosen a 180 frame animation with a 20ms delay between frames.
    # blit=True means only re-draw the parts that have changed.
    anim = animation.FuncAnimation(fig, 
                                   animate, fargs=(line1, line2, line3), 
                                   frames=180, interval=20, blit=True)

    # save the animation as an mp4.  
    # This requires ffmpeg or mencoder to be installed.

    # https://www.videosurveillance.com/tech/frame-rate.asp
    # 30 fps means the camera captured 30 frames in a single second of video

    # The extra_args ensure that the x264 codec is used, so that
    # the video can be embedded in html5.  
    # You may need to adjust this for your system: for more information, see
    # http://matplotlib.sourceforge.net/api/animation_api.html
    os.makedirs("./video",exist_ok=True)
    anim.save('./video/reflection_principle.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

    plt.show()

if __name__ == "__main__":
    main()