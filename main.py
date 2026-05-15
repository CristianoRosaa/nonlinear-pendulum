## Analytical Solution from Literature ##

import numpy as np
import matplotlib.pyplot as plt

l = 1; g = 9.81; m = 1; theta0 = np.pi; theta01 = 1; 
E = 2*m*g*l*(np.sin(theta0/2))**2
E0 = 2*m*g*l

theta = np.arange(-5,5,0.01)

def theta_dot(theta,theta0,a):
    f = 2*(((np.sin(theta0/2))**2 - (np.sin(theta/2))**2  + a)**0.5)
    return f

Theta = []
for i in range(len(theta)):
    t = theta_dot(theta[i],theta0,0)
    Theta.append(t)

Theta_minus = []
for j in range(len(theta)):
    Theta_minus.append(-Theta[j])

Theta1 = []
for i in range(len(theta)):
    t = theta_dot(theta[i],theta01,0)
    Theta1.append(t)

Theta1_minus = []
for j in range(len(theta)):
    Theta1_minus.append(-Theta1[j])

Theta2 = []
for i in range(len(theta)):
    t = theta_dot(theta[i],theta0,1)
    Theta2.append(t)

Theta2_minus = []
for j in range(len(theta)):
    Theta2_minus.append(-Theta2[j])


##  Euler Method Implementation ##


# Time array for plotting:
t = np.arange(0,24,10**-2)


def euler_method(x0,v0,tf,dt):
  
  """
  Simulates the nonlinear pendulum using Euler's method.
  
  """

  g = 9.81; l = 10
  w = np.sqrt(g/l)

  def a(x,w):
    a = -(w**2)*np.sin(x)
    return(a)

  pos = []; vel = [] 

  for t in np.arange(0,tf,dt):
    x0 += v0*dt
    pos.append(x0)
    v0 += a(x0,w)*dt
    vel.append(v0)
  return(pos,vel)

## Runge Kutta 2nd order implementation ##


def runge_kutta_2(x,v,tf,dt):
  
  """
  Simulates the nonlinear pendulum using Runge-Kutta 2nd order method.
  
  """

  def a(x,w):
    return  -(w**2)*np.sin(x)
  g = 9.81; l = 10
  w = np.sqrt(g/l)
  T=[]; X=[]; V=[]
  T.append(0); X.append(x); V.append(v)
  for i in np.arange(0,tf,dt):
    xi = x + v*dt/2
    vi = v + a(x,w)*dt/2
    x = xi + vi*dt
    v = vi + a(xi,w)*dt
    T.append(i); X.append(x); V.append(v)
  return (T,X,V)

## Figures ##

def fig_analytic():
    fig = plt.figure(figsize=(10,5))
    plt.plot(theta,Theta,c='blue',label='$E = E_0$')
    plt.plot(theta,Theta_minus,c='blue')
    plt.plot(theta,Theta1,c='red',label='$E < E_0$')
    plt.plot(theta,Theta1_minus,c='red')
    plt.plot(theta,Theta2,c='green',label='$E > E_0$')
    plt.plot(theta,Theta2_minus,c='green')
    plt.xlabel(r'$\theta$')
    plt.ylabel(r'$\frac{\dot{\theta}}{\sqrt{g/l}}$')
    plt.legend()
    plt.grid()
    plt.savefig("images/analytic_phase_diagram.png", dpi=200)
    plt.close()


def fig_euler_position():
    fig = plt.figure(figsize=(10,5))
    plt.plot(t,euler_method(0.1,0,24,10**-2)[0],label="$\Theta$=5,37°")
    plt.plot(t,euler_method(0.5,0,24,10**-2)[0],label="$\Theta$=28,65°")
    plt.plot(t,euler_method(1,0,24,10**-2)[0],label="$\Theta$=57,30°")
    plt.xlabel("t (s)")
    plt.ylabel("x (m)")
    plt.title("Posição x Tempo")
    plt.legend()
    plt.grid()
    plt.savefig("images/euler_position_time.png", dpi=200)
    plt.close()


def fig_euler_velocity_position():
    fig = plt.figure(figsize=(10,5))
    plt.plot(euler_method(0.1,0,24,10**-3)[0],euler_method(0.1,0,24,10**-3)[1],label="$\Theta$=5,37°")
    plt.plot(euler_method(0.5,0,24,10**-3)[0],euler_method(0.5,0,24,10**-3)[1],label="$\Theta$=28,65°")
    plt.plot(euler_method(1,0,24,10**-3)[0],euler_method(1,0,24,10**-3)[1],label="$\Theta$=57,30°")
    plt.plot(euler_method(3*np.pi,-0.1,24,10**-3)[0],euler_method(3*np.pi,-0.1,24,10**-3)[1],label="$\Theta$=180°")
    plt.plot(euler_method(-3*np.pi,0.1,24,10**-3)[0],euler_method(-3*np.pi,0.1,24,10**-3)[1],label="$\Theta$=-180°")
    plt.xlabel(r"$\theta$")
    plt.ylabel(r"$\dot{\theta}$")
    plt.legend()
    plt.grid()
    plt.savefig("images/euler_velocity_position.png", dpi=200)
    plt.close()


def fig_runge_kutta_2_velocity_position():
    fig = plt.figure(figsize=(10,5))
    plt.plot(runge_kutta_2(0.1,0,24,10**-3)[1],runge_kutta_2(0.1,0,24,10**-3)[2],c='blue',label="$\Theta$=5,37°")
    plt.plot(runge_kutta_2(0.5,0,24,10**-3)[1],runge_kutta_2(0.5,0,24,10**-3)[2],c='orange',label="$\Theta$=28,65")
    plt.plot(runge_kutta_2(1,0,24,10**-3)[1],runge_kutta_2(1,0,24,10**-3)[2],c='green',label="$\Theta$=57,30°")
    plt.plot(runge_kutta_2(3*np.pi,-0.1,24,10**-3)[1],runge_kutta_2(3*np.pi,-0.1,24,10**-3)[2],c='black',label="$\Theta$=180°")
    plt.plot(runge_kutta_2(-3*np.pi,0.1,24,10**-3)[1],runge_kutta_2(-3*np.pi,0.1,24,10**-3)[2],c='purple',label="$\Theta$=-180°")
    plt.xlim(-10,10)
    plt.xlabel(r"$\theta$")
    plt.ylabel(r"$\dot{\theta}$")
    plt.legend()
    plt.grid()
    plt.savefig("images/runge_kutta_2_velocity_position.png", dpi=200)
    plt.close()

# Figure Runge KUTTA 2nd order - comparation of different time steps:

def fig_runge_kutta_2_time_steps():
    fig = plt.figure(figsize=(10,5))
    plt.plot(runge_kutta_2(0.1,0,24,10**-2)[0],runge_kutta_2(0.1,0,24,10**-2)[1],color="black",label="$\Delta t = 10^{-2}$")
    plt.plot(runge_kutta_2(0.1,0,24,10**-3)[0],runge_kutta_2(0.1,0,24,10**-3)[1],color="blue",label="$\Delta t = 10^{-3}$")
    plt.plot(runge_kutta_2(0.1,0,24,10**-4)[0],runge_kutta_2(0.1,0,24,10**-4)[1],color="red",label="$\Delta t = 10^{-4}$")
    plt.xlabel("t (s)")
    plt.ylabel(r"$\theta$")
    plt.legend()
    plt.grid()
    plt.savefig("images/runge_kutta_2_time_steps.png", dpi=200)
    plt.close()


if __name__ == "__main__":
    fig_analytic()
    fig_euler_position()
    fig_euler_velocity_position()
    fig_runge_kutta_2_velocity_position()
    fig_runge_kutta_2_time_steps()