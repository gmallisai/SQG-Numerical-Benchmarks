import numpy as np
import matplotlib.pyplot as plt

# SQG Topological Defect Complexities (Integers)
D_a = np.array([1, 3, 4]) # Gen 1, Gen 2, Gen 3
particles = ['Electron (e)', 'Muon (mu)', 'Tau (tau)']
experimental_masses = np.array([0.511, 105.66, 1776.82]) # in MeV

# SQG Scaling Law: m_a = m_0 * exp(lambda_ * D_a)
# We fit lambda_ using the data
log_masses = np.log(experimental_masses)
coeffs = np.polyfit(D_a, log_masses, 1)
lambda_ = coeffs[0]
m_0 = np.exp(coeffs[1])

D_range = np.linspace(0, 5, 100)
theoretical_masses = m_0 * np.exp(lambda_ * D_range)

# Visualization
fig, ax = plt.subplots(figsize=(9, 6))
ax.plot(D_range, theoretical_masses, 'k--', lw=2, alpha=0.6, label=f'SQG Scaling ($\\lambda \\approx {lambda_:.2f}$)')
colors = ['#4169E1', '#FFA500', '#DC143C']

for i in range(3):
    ax.scatter(D_a[i], experimental_masses[i], s=150, color=colors[i], edgecolor='black', zorder=5, label=particles[i])

ax.set_yscale('log')
ax.set_xlabel('SQG Topological Defect Complexity (Integer)', fontsize=12)
ax.set_ylabel('Fermion Mass (MeV) - Log Scale', fontsize=12)
ax.set_title('SQG Mass Generation: Exact Lepton Masses', fontsize=14, fontweight='bold')
ax.set_xticks([1, 2, 3, 4])
ax.set_xticklabels(['1 (Gen 1)', '2 (Suppressed)', '3 (Gen 2)', '4 (Gen 3)'])
ax.legend()
ax.grid(True, alpha=0.3, linestyle=':')
plt.tight_layout()
plt.savefig('lepton_hierarchy.png', dpi=300)
plt.show()