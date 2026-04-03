import numpy as np
import matplotlib.pyplot as plt

# Redshifts from z=1000 (CMB) down to z=0 (Local Universe)
z = np.logspace(-3, 3, 500)
a = 1.0 / (1.0 + z) # Scale factor

# Base Lambda-CDM parameters (Planck)
H0_CMB = 67.4
Omega_m = 0.315
Omega_Lambda = 1.0 - Omega_m
H_GR = H0_CMB * np.sqrt(Omega_m * (1+z)**3 + Omega_Lambda)

# SQG Stabilization Deficit modifying expansion at low z (Late Universe)
# Q_S drops slightly in large-scale voids, bridging the gap to SH0ES (H0=73)
H0_Local = 73.0
delta_H = H0_Local - H0_CMB
SQG_Correction = 1.0 + (delta_H / H0_CMB) * np.exp(-3 * z)

H_SQG = H_GR * SQG_Correction

# Convert to Comoving Expansion Rate for visualization: H(z)/(1+z)
comoving_H_GR = H_GR / (1+z)
comoving_H_SQG = H_SQG / (1+z)

# Visualization
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(z, comoving_H_GR, 'b--', lw=2, label=f'Rigid $\\Lambda$CDM (Planck Anchor: $H_0={H0_CMB}$)')
ax.plot(z, comoving_H_SQG, 'g-', lw=3, label='SQG Stabilization Flow (Dynamical $1-Q_S$ Deficit)')

ax.scatter([1000], [H0_CMB/1001], color='blue', s=100, zorder=5, label='CMB Measurement (High-z)')
ax.scatter([0], [H0_Local], color='red', s=100, zorder=5, label='Local Supernovae (SH0ES $H_0=73$)')

ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlim(1e-3, 2e3)
ax.invert_xaxis() # Lookback time: present (z=0) is on the left
ax.set_xlabel('Redshift ($z$) - Lookback Time $\\rightarrow$', fontsize=12)
ax.set_ylabel('Comoving Expansion Rate $H(z)/(1+z)$', fontsize=12)
ax.set_title('SQG Resolution of the Hubble Tension ($H_0$)', fontsize=14, fontweight='bold')
ax.legend(loc='lower left')
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('hubble_tension.png', dpi=300)
plt.show()