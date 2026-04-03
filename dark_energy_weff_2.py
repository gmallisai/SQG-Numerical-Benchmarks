import numpy as np
import matplotlib.pyplot as plt

# --- SQG Cosmological Parameters ---
# Time evolution (arbitrary units, from early universe to late universe)
t = np.linspace(0, 10, 500)

# Stabilization Score Q_S(t): Logistic growth from 0 to 1
# Represents the network finding its optimal error-correcting phase
k = 1.2      # Rate of stabilization
t_0 = 5.0    # Transition epoch
Q_S = 1.0 / (1.0 + np.exp(-k * (t - t_0)))

# Effective Equation of State (w_eff)
# Driven purely by the macroscopic deficit (1 - Q_S) and the saturation limit
w_eff = -Q_S 

# --- Visualization ---
fig, ax1 = plt.subplots(figsize=(10, 6))
fig.suptitle('SQG Cosmology: Dark Energy from Stabilization Flow', fontsize=15, fontweight='bold')

# Axis 1: Stabilization Score (Q_S)
color1 = '#1f77b4'
ax1.set_xlabel('Cosmological Time / Stabilization Evolution', fontsize=12)
ax1.set_ylabel('Stabilization Score $Q_S(t)$', color=color1, fontsize=12)
line1 = ax1.plot(t, Q_S, color=color1, lw=3, label='Stabilization Phase $Q_S(t)$')
ax1.tick_params(axis='y', labelcolor=color1)
ax1.set_ylim(0, 1.1)
ax1.axhline(1.0, color='gray', linestyle=':', lw=2, alpha=0.6, label='Einsteinian Saturated Limit ($Q_S=1$)')

# Axis 2: Equation of State (w_eff)
ax2 = ax1.twinx()
color2 = '#d62728'
ax2.set_ylabel('Effective Equation of State $w_{eff}$', color=color2, fontsize=12)
line2 = ax2.plot(t, w_eff, color=color2, linestyle='--', lw=3, label='$w_{eff}$ (Dynamical Flow)')
ax2.tick_params(axis='y', labelcolor=color2)
ax2.set_ylim(-1.2, 0.2)
ax2.axhline(-1.0, color='black', linestyle=':', lw=2, label='Asymptotic Dark Energy ($w=-1$)')

# Combine legends
lines = line1 + line2
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc='center right', fontsize=10)

plt.grid(True, alpha=0.2)
plt.tight_layout()
plt.savefig('dark_energy_flow.png', dpi=300)
print("Saved plot as 'dark_energy_flow.png'")
plt.show()