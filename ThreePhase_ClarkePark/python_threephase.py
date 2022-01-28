import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation


t0=0 #Starting time (s)
t_end=2 #Ending time (s)
dt=0.005 #Time interval (s)
Vm=50 #Amplitude of signals (V)
f=1 #Frequency of signals (Hz). Because of animation purposes it is 1 Hz

t=np.arange(t0,t_end+dt,dt) #Time array 0-2 seconds

#Creating three phase system
phase1=Vm*np.sin(2*np.pi*t*f) 
phase2=Vm*np.sin(2*np.pi*t-(2*np.pi/3)*f)
phase3=Vm*np.sin(2*np.pi*t+(2*np.pi/3)*f)
phases=phase1+phase2+phase3

##ANIMATION PART##

frame_amount=len(t) #Number of frames is equal to len(t) because we have that much array length for signals.

def update_plot(num): #Function for updating each singals values from their arrays to the current frame.

    phase1_ref.set_data(t[0:num],phase1[0:num])
    phase2_ref.set_data(t[0:num],phase2[0:num])
    phase3_ref.set_data(t[0:num],phase3[0:num])
    phase1_2_ref.set_data(t[0:num],phase1[0:num])
    phase2_2_ref.set_data(t[0:num],phase2[0:num])
    phase3_2_ref.set_data(t[0:num],phase3[0:num])

    

    return phase1_ref,phase2_ref,phase3_ref, phase1_2_ref,phase2_2_ref, phase3_2_ref

#Creating main figure for animation
fig=plt.figure(figsize=(16,9),dpi=120,facecolor=(0.8,0.8,0.8)) #Main figure
gs=gridspec.GridSpec(2,3) #Number and the order of the subplots

#Subplot 1 (Phase 1)
ax0=fig.add_subplot(gs[1,0],facecolor=(0.9,0.9,0.9))
phase1_ref,=ax0.plot([],[],'r',linewidth=2)
plt.xlim(0,t[-1])
plt.ylim(-60,60)
plt.xticks(np.arange(t[0],t[-1]+dt,t[-1]/10))
plt.xlabel('Amplitude (V)')
plt.ylabel('Time (s)')
plt.title('Phase 1')
plt.grid(True)

#Subplot 2 (Phase 2)
ax1=fig.add_subplot(gs[1,1],facecolor=(0.9,0.9,0.9))
phase2_ref,=ax1.plot([],[],'g',linewidth=2)
plt.xlim(0,t[-1])
plt.ylim(-60,60)
plt.xticks(np.arange(t[0],t[-1]+dt,t[-1]/10))
plt.xlabel('Amplitude (V)')
plt.ylabel('Time (s)')
plt.title('Phase 2')
plt.grid(True)

#Subplot 3 (Phase 3)
ax2=fig.add_subplot(gs[1,2],facecolor=(0.9,0.9,0.9))
phase3_ref,=ax2.plot([],[],'b',linewidth=2)
plt.xlim(0,t[-1])
plt.ylim(-60,60)
plt.xticks(np.arange(t[0],t[-1]+dt,t[-1]/10))
plt.xlabel('Amplitude (V)')
plt.ylabel('Time (s)')
plt.title('Phase 3')
plt.grid(True)

#Subplot 4 (Three Phase System)
ax3=fig.add_subplot(gs[0,:],facecolor=(0.9,0.9,0.9))
phase1_2_ref,=ax3.plot([],[],'r',linewidth=2,label='Phase 1')
phase2_2_ref,=ax3.plot([],[],'g',linewidth=2,label='Phase 2')
phase3_2_ref,=ax3.plot([],[],'b',linewidth=2,label='Phase 3')
plt.xlim(0,t[-1])
plt.ylim(-60,60)
plt.xticks(np.arange(t[0],t[-1]+dt,t[-1]/10))
plt.xlabel('Amplitude (V)')
plt.ylabel('Time (s)')
plt.title('Three Phase System')
plt.legend(loc='upper right',fontsize='small')
plt.grid(True)


threephase_ani=animation.FuncAnimation(fig,update_plot,frames=frame_amount,interval=20,repeat=True,blit=True)
plt.show()

##FIXED PLOTS##

#Subplot 1 (Three Phase System)
plt.subplot(211)
plt.plot(t,phase1,'r',linewidth=2,label='Phase 1')
plt.plot(t,phase2,'g',linewidth=2,label='Phase 2')
plt.plot(t,phase3,'b',linewidth=2,label='Phase 3')
plt.xlim(0,t[-1])
plt.ylim(-60,60)
plt.xticks(np.arange(t[0],t[-1]+dt,t[-1]/10))
plt.xlabel('Time (s)')
plt.ylabel('Amplitude (V)')
plt.title('Three Phase System')
plt.legend(loc='upper right',fontsize='small')
plt.grid(True)

#Subplot 2 (Phase 1)
plt.subplot(2,3,4)
plt.plot(t,phase1,'r',linewidth=2)
plt.xlim(0,t[-1])
plt.ylim(-60,60)
plt.xticks(np.arange(t[0],t[-1]+dt,t[-1]/10))
plt.xlabel('Time (s)')
plt.ylabel('Amplitude (V)')
plt.title('Phase 1')
plt.grid(True)

#Subplot 3 (Phase 2)
plt.subplot(2,3,5)
plt.plot(t,phase2,'g',linewidth=2)
plt.xlim(0,t[-1])
plt.ylim(-60,60)
plt.xticks(np.arange(t[0],t[-1]+dt,t[-1]/10))
plt.xlabel('Time (s)')
plt.ylabel('Amplitude (V)')
plt.title('Phase 2')
plt.grid(True)

#Subplot 4 (Phase 3)
plt.subplot(2,3,6)
plt.plot(t,phase3,'b',linewidth=2)
plt.xlim(0,t[-1])
plt.ylim(-60,60)
plt.xticks(np.arange(t[0],t[-1]+dt,t[-1]/10))
plt.xlabel('Time (s)')
plt.ylabel('Amplitude (V)')
plt.title('Phase 3')
plt.grid(True)

plt.show()







