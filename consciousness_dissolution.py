import numpy as np
import matplotlib.pyplot as plt

def simulate_boundary_dissolution():
    print("Simulating Conscious Agent Boundary and Global Entanglement...")
    
    # Time steps of the experience (simulation timeline)
    t = np.linspace(0, 100, 1000)
    
    # Point of the boundary dissolution event
    t_trigger = 40.0
    
    # 1. Local Stabilizer Boundary (Illusionary Boundary Strength)
    # Starts high (isolation). Collapses at t_trigger.
    boundary_strength = np.where(t < t_trigger, 
                                 1.0, 
                                 np.exp(-(t - t_trigger) / 5.0))
    
    # 2. Quantum Entanglement Entropy with the Universe (S_EE)
    # While the boundary is high, entanglement is low (the agent is isolated).
    # When the boundary falls, the system unifies with the Bulk (Global Integration).
    S_max = 10.0 # Maximal thermal entanglement (The Universe)
    S_EE = np.where(t < t_trigger,
                    0.5 + 0.05 * np.sin(t), # Small daily fluctuations of perception
                    S_max - (S_max - 0.5) * np.exp(-(t - t_trigger) / 8.0))
    
    # 3. Local Complexity (Local Self-Referential Processing)
    # The default mode network stops processing the isolated "self".
    local_processing = np.where(t < t_trigger,
                                8.0 + np.cos(t*2),
                                8.0 * np.exp(-(t - t_trigger) / 3.0))

    # --- Visualization ---
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)
    fig.suptitle('SQG Topology of Consciousness: Boundary Dissolution & Global Entanglement', fontsize=15, fontweight='bold')

    # Top Plot: The Illusionary Boundary and Local Processing
    ax1.plot(t, boundary_strength, 'r-', lw=3, label='Local Stabilizer Boundary (Illusionary Firewall)')
    ax1.plot(t, local_processing / 10.0, 'orange', lw=2, linestyle='--', label='Local Self-Referential Processing')
    ax1.axvline(t_trigger, color='black', linestyle=':', lw=2, label='Dissolution Event (Boundary Drops)')
    ax1.set_ylabel('Boundary / Processing Strength', fontsize=12)
    ax1.legend(loc='upper right')
    ax1.grid(True, alpha=0.3)
    ax1.fill_between(t, 0, boundary_strength, color='red', alpha=0.1)

    # Bottom Plot: Merging with the Universe (Integration)
    ax2.plot(t, S_EE, 'b-', lw=3, label='Entanglement Entropy with the Bulk (S_EE)')
    ax2.axvline(t_trigger, color='black', linestyle=':', lw=2)
    ax2.axhline(S_max, color='gray', linestyle='--', lw=2, label='Maximal Entanglement (Total Integration)')
    ax2.set_xlabel('Time (Simulation Steps)', fontsize=12)
    ax2.set_ylabel('Entanglement Entropy (S_EE)', fontsize=12)
    ax2.legend(loc='lower right')
    ax2.grid(True, alpha=0.3)
    ax2.fill_between(t, 0, S_EE, color='blue', alpha=0.1)

    plt.tight_layout()
    plt.savefig('boundary_dissolution_entanglement.png', dpi=300)
    print("Saved -> boundary_dissolution_entanglement.png")
    plt.show()

if __name__ == "__main__":
    simulate_boundary_dissolution()