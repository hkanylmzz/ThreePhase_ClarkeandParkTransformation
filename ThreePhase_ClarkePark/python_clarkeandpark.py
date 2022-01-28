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

#In order to use in Clarke transformation new variables are assigned.
ia=phase1
ib=phase2
ic=phase3

#Clarke Transform (Iabc -> Iab)
ialpha=2/3*(ia-0.5*ib-0.5*ic)
ibeta=2/3*((np.sqrt(3)/2)*ib-(np.sqrt(3)/2)*ic)

#Park Transform (Iab -> Idq)
wt=2*np.pi*f*t
delta=0 #Changing delta is direct effect on id and iq. Can be adjusted for desired id and iq
theta=wt+delta
id=np.cos(theta)*ialpha+np.sin(theta)*ibeta
iq=-np.sin(theta)*ialpha+np.cos(theta)*ibeta

##ANIMATION PART##

frame_amount=len(t) #Number of frames is equal to len(t) because we have that much array length for signals.

def update_plot(num): #Function for updating each singals values from their arrays to the current frame.

    phase1_ref.set_data(t[0:num],phase1[0:num])
    phase2_ref.set_data(t[0:num],phase2[0:num])
    phase3_ref.set_data(t[0:num],phase3[0:num])

    ialpha_ref.set_data(t[0:num],ialpha[0:num])
    ibeta_ref.set_data(t[0:num],ibeta[0:num])

    id_ref.set_data(t[0:num],id[0:num])
    iq_ref.set_data(t[0:num],iq[0:num])

    return phase1_ref,phase2_ref,phase3_ref,ialpha_ref,ibeta_ref,id_ref,iq_ref

#Creating main figure for animation
fig=plt.figure(figsize=(16,9),dpi=120,facecolor=(0.8,0.8,0.8)) #Main figure
gs=gridspec.GridSpec(3,1)  #Number and the order of the subplots

#Subplot 1 (Three Phase System)
ax0=fig.add_subplot(gs[0,0],facecolor=(0.9,0.9,0.9))
phase1_ref,=ax0.plot([],[],'r',linewidth=2,label='Phase 1')
phase2_ref,=ax0.plot([],[],'g',linewidth=2,label='Phase 2')
phase3_ref,=ax0.plot([],[],'b',linewidth=2,label='Phase 3')
plt.xlim(0,t[-1])
plt.ylim(-100,100)
plt.xticks(np.arange(t[0],t[-1]+dt,t[-1]/10))
plt.xlabel('Time (s)')
plt.ylabel('Amplitude (V)')
plt.title('Three Phase System')
plt.legend(loc='upper right',fontsize='small')
plt.grid(True)

#Subplot 2 (Clarke Transform (Iabc -> Iab))
ax1=fig.add_subplot(gs[1,0],facecolor=(0.9,0.9,0.9))
ialpha_ref,=ax1.plot([],[],'r',linewidth=2,label='ialpha')
ibeta_ref,=ax1.plot([],[],'b',linewidth=2,label='ibeta')
plt.xlim(0,t[-1])
plt.ylim(-100,100)
plt.xticks(np.arange(t[0],t[-1]+dt,t[-1]/10))
plt.xlabel('Time (s)')
plt.ylabel('Amplitude (V)')
plt.title('Clarke Transform (Iabc -> Iab)')
plt.legend(loc='upper right',fontsize='small')
plt.grid(True)

#Subplot 2 (Park Transform (Iab -> Idq))
ax2=fig.add_subplot(gs[2,0],facecolor=(0.9,0.9,0.9))
id_ref,=ax2.plot([],[],'r',linewidth=2,label='id')
iq_ref,=ax2.plot([],[],'b',linewidth=2,label='iq')
plt.xlim(0,t[-1])
plt.ylim(-100,100)
plt.xticks(np.arange(t[0],t[-1]+dt,t[-1]/10))
plt.xlabel('Time (s)')
plt.ylabel('Amplitude (V)')
plt.title('Park Transform (Iab -> Idq)')
plt.legend(loc='upper right',fontsize='small')
plt.grid(True)


clarkepark_ani=animation.FuncAnimation(fig,update_plot,frames=frame_amount,interval=20,repeat=True,blit=True)
plt.show()

##FIXED PLOTS##

#Subplot 1 (Three Phase System)
plt.subplot(3,1,1)
plt.plot(t,phase1,'r',linewidth=2,label='Phase 1')
plt.plot(t,phase2,'g',linewidth=2,label='Phase 2')
plt.plot(t,phase3,'b',linewidth=2,label='Phase 3')
plt.xlim(0,t[-1])
plt.ylim(-100,100)
plt.xticks(np.arange(t[0],t[-1]+dt,t[-1]/10))
plt.xlabel('Time (s)')
plt.ylabel('Amplitude (V)')
plt.title('Three Phase System')
plt.legend(loc='upper right',fontsize='small')
plt.grid(True)

#Subplot 2 (Clarke Transform (Iabc -> Iab))
plt.subplot(3,1,2)
plt.plot(t,ialpha,'r',linewidth=2,label='ialpha')
plt.plot(t,ibeta,'b',linewidth=2,label='ibeta')
plt.xlim(0,t[-1])
plt.ylim(-100,100)
plt.xticks(np.arange(t[0],t[-1]+dt,t[-1]/10))
plt.xlabel('Time (s)')
plt.ylabel('Amplitude (V)')
plt.title('Clarke Transform (Iabc -> Iab)')
plt.legend(loc='upper right',fontsize='small')
plt.grid(True)

#Subplot 2 (Park Transform (Iab -> Idq))
plt.subplot(3,1,3)
plt.plot(t,id,'r',linewidth=2,label='id')
plt.plot(t,iq,'b',linewidth=2,label='iq')
plt.xlim(0,t[-1])
plt.ylim(-100,100)
plt.xticks(np.arange(t[0],t[-1]+dt,t[-1]/10))
plt.xlabel('Time (s)')
plt.ylabel('Amplitude (V)')
plt.title('Park Transform (Iab -> Idq)')
plt.legend(loc='upper right',fontsize='small')
plt.grid(True)

plt.show()



