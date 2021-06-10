import matplotlib.pyplot as plt

# Figure 1.1
def figure_1_1():
    fig, (ax1, ax2) = plt.subplots(ncols=2, subplot_kw={'xlim':[-3,5], 'ylim':[-3,5], })
    
    # ax1
    ax1.axline((0,-1), (2,3))
    ax1.axline((0,5), (5,0))
    ax1.spines['left'].set_position('zero')
    ax1.spines['right'].set_color('none')
    ax1.spines['bottom'].set_position('zero')
    ax1.spines['top'].set_color('none')
    ax1.set_title('(A)\n', fontsize=16)
    
    ax2.arrow(0,0, -1,1, head_width=0.3, length_includes_head=True, color='green')
    ax2.arrow(0,0, 2,1, head_width=0.3, length_includes_head=True, color='purple')

    ax2.arrow(-1,1, -1,1, head_width=0.3, length_includes_head=True)
    ax2.arrow(-2,2, -1,1, head_width=0.3, length_includes_head=True)

    ax2.arrow(2,1, 2,1, head_width=0.3, length_includes_head=True)

    ax2.arrow(-3,3, 4,2, linestyle='-.', lw=2, head_width=0.3, length_includes_head=True, color='gray')
    ax2.arrow(4,2, -3,3, linestyle='-.', lw=2, head_width=0.3, length_includes_head=True, color='gray')
    ax2.arrow(0,0, 1,5, linestyle='--', lw=1, head_width=0.3, length_includes_head=True)
    ax2.spines['left'].set_position('zero')
    ax2.spines['right'].set_color('none')
    ax2.spines['bottom'].set_position('zero')
    ax2.spines['top'].set_color('none')
    ax2.set_title('(B)\n', fontsize=16)

# Figure 1.4
def figure_1_4():
    fig, (ax1, ax2, ax3, ax4) = plt.subplots(ncols=4)
    
    # Figure A
    ax1.set_xlim(-2,5)
    ax1.set_ylim(0,5)
    ax1.set_title('(A)\n', fontsize=16)
    
    ax1.axline((0,0), (5,3))
    ax1.axline((4,0), (0,3))
    ax1.axline((6,0), (0,5))
    ax1.set_xlabel('Two parallel')
     
    # Figure B
    ax2.set_xlim(-2,5)
    ax2.set_ylim(0,5)
    ax2.set_title('(B)\n', fontsize=16)
    
    ax2.axline((0,1), (5,1))
    ax2.axline((-1,1), (5,4))
    ax2.axline((4,1), (0,4))   
    ax2.set_xlabel('No intersection')
    
    # Figure C
    ax3.set_xlim(-2,5)
    ax3.set_ylim(0,5)
    ax3.set_title('(C)\n', fontsize=16)
    ax3.set_xlabel('Line of intersection')
    
    ax3.axline((0,2.5), (5,2.5))
    ax3.axline((0,0), (5,5))
    ax3.axline((0,5), (5,0))  
    
    # Figure D
    ax4.set_xlim(-2,5)
    ax4.set_ylim(0,5)
    ax4.set_title('(D)\n', fontsize=16)
    
    ax4.axline((3,0), (0,4))
    ax4.axline((4,0), (0,5))
    ax4.axline((5,0), (0,6))
    ax4.set_xlabel('All parallel')
    
    plt.tight_layout()
