import numpy as np
import matplotlib.pyplot as plt

def simulate_dark_energy_flow():
    print("Simulating SQG Cosmological Flow...")
    # Cosmological Time (Arbitrary Units)
    t = np.linspace(0, 10, 500)

    # The Universe tries to stabilize, but expansion acts as a friction.
    # Q_S flows from near 0 (Chaos) and saturates asymptotically at ~0.85
    Q_s = 0.85 - 0.75 * np.exp(-0.8 * t)

    # Hubble Expansion Rate:
    # Composed of regular matter dilution and the permanent Stabilizer Deficit
    H_matter = 2.0 * np.exp(-1.2 * t)
    H_deficit = 0.6 * (1.0 - Q_s) # The Deficit acts as Vacuum Energy!
    H_total = H_matter + H_deficit

    # Calculate the Effective Equation of State: w_eff = -1 - (2/3) * (dH/dt) / H^2
    dH_dt = np.gradient(H_total, t)
    w_eff = -1.0 - (2.0 / 3.0) * (dH_dt / (H_total**2))

    # --- Visualization ---
    fig, ax1 = plt.subplots(figsize=(10, 6))
    fig.suptitle('Emergence of Dark Energy via SQG Stabilization Flow', fontsize=15, fontweight='bold')

    # Plot Q_S (Stabilization Score)
    color1 = '#005b96'
    ax1.set_xlabel('Cosmological Time / Thermalization', fontsize=12)
    ax1.set_ylabel('Stabilization Score $Q_S(t)$', color=color1, fontsize=12, fontweight='bold')
    ax1.plot(t, Q_s, color=color1, lw=3, label='Stabilization Flow $Q_S(t)$')
    ax1.tick_params(axis='y', labelcolor=color1)
    ax1.set_ylim(0, 1.0)
    ax1.axhline(1.0, color='gray', linestyle=':', lw=2, alpha=0.6, label='Perfect Einsteinian Saturation')

    # Twin axis for w_eff
    ax2 = ax1.twinx()
    color2 = '#d9534f'
    ax2.set_ylabel('Effective Eq. of State $w_{eff}$', color=color2, fontsize=12, fontweight='bold')
    ax2.plot(t, w_eff, color=color2, linestyle='--', lw=3, label='Dynamical $w_{eff}$ (Dark Energy Limit)')
    ax2.axhline(-1, color='black', linestyle=':', lw=2, label='Rigid Cosmological Constant ($w=-1$)')
    ax2.tick_params(axis='y', labelcolor=color2)
    ax2.set_ylim(-1.2, 0.5)

    # Combine legends
    lines_1, labels_1 = ax1.get_legend_handles_labels()
    lines_2, labels_2 = ax2.get_legend_handles_labels()
    ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc='upper right', fontsize=11)

    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig('cosmology_dark_energy.png', dpi=300)
    print("Saved -> cosmology_dark_energy.png")

if __name__ == "__main__":
    simulate_dark_energy_flow()