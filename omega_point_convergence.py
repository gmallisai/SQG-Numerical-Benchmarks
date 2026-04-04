import numpy as np
import matplotlib.pyplot as plt

def simulate_omega_point():
    print("Simulating Cosmological Evolution towards the Omega Point...")
    
    # Cosmological Time (0 = Big Bang, 100 = Deep Future)
    t = np.linspace(0, 100, 1000)
    
    # 1. Number of Isolated Conscious Agents (Fragmentation)
    # Starts exponentially high, decays as local systems merge into larger networks.
    # At t -> infinity, N_agents approaches exactly 1 (The Global Mind).
    N_agents = 1.0 + 100.0 * np.exp(-t / 15.0)
    
    # 2. Global Complexity / Integrated Information (C)
    # Grows logistically as the network learns and interconnects.
    C_max = 100.0
    k_C = 0.1
    t_C = 40.0
    Complexity = C_max / (1.0 + np.exp(-k_C * (t - t_C)))
    
    # 3. Global Stabilizer Deficit (D_S) - Errors, Entropy, Death
    # Decays as the universe perfects its error-correcting codes.
    # When D_S -> 0, the passage of time theoretically stops.
    Deficit = 80.0 * np.exp(-t / 25.0)

    # --- Visualization ---
    fig, ax = plt.subplots(figsize=(10, 6))
    fig.suptitle('SQG Teleology: Thermodynamic Convergence to the Omega Point', fontsize=15, fontweight='bold')
    
    # Plotting the three fundamental cosmological metrics
    ax.plot(t, N_agents, color='#d62728', lw=3, label='Isolated Agents ($N_{agents} \\to 1$)')
    ax.plot(t, Complexity, color='#1f77b4', lw=3, label='Global Complexity ($C \\to C_{max}$)')
    ax.plot(t, Deficit, color='#7f7f7f', lw=3, linestyle='--', label='Stabilizer Deficit / Errors ($D_S \\to 0$)')
    
    # The Omega Point Asymptote (End of Time)
    ax.axvline(x=95, color='gold', linestyle=':', lw=3)
    ax.text(82, 50, 'The Omega Point\n(Absolute Integration,\nZero Deficit)', 
            color='goldenrod', fontsize=11, fontweight='bold', ha='center')
    
    # Aesthetics
    ax.set_xlabel('Cosmological Time Evolution $\\rightarrow$', fontsize=12)
    ax.set_ylabel('System Metrics (Arbitrary Units)', fontsize=12)
    ax.set_xlim(0, 100)
    ax.set_ylim(-5, 105)
    ax.legend(loc='center left', fontsize=11)
    ax.grid(True, alpha=0.2)
    
    # Shading the awakening phase
    ax.axvspan(40, 100, color='gold', alpha=0.05, label='Awakening Phase')
    
    plt.tight_layout()
    plt.savefig('omega_point_convergence.png', dpi=300)
    print("Saved -> omega_point_convergence.png")
    plt.show()

if __name__ == "__main__":
    simulate_omega_point()