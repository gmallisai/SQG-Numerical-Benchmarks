import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def compute_spectral_dimension(G, t_vals):
    """Computes the spectral dimension ds(t) via the Heat Kernel trace."""
    # Normalized Laplacian Matrix (analogous to the Code Hamiltonian)
    L = nx.normalized_laplacian_matrix(G).toarray()
    evals = np.linalg.eigvalsh(L)
    
    # Remove 0 eigenvalues to avoid numerical instability at t -> infinity
    evals = evals[evals > 1e-10] 
    
    ds_vals = []
    for t in t_vals:
        P_t = np.sum(np.exp(-t * evals))
        dP_dt = -np.sum(evals * np.exp(-t * evals))
        # d_s(t) = -2 * t * P'(t) / P(t)
        ds = -2 * t * (dP_dt / P_t)
        ds_vals.append(ds)
        
    return np.array(ds_vals)

def run_simulation():
    print("Initializing SQG Spectral Flow Simulation...")
    # 1. IR Regime: Stabilized Code (High Q_S, 4D Macroscopic Spacetime)
    size = 5
    G_IR = nx.grid_graph(dim=(size, size, size, size))

    # 2. UV Regime: Unstable Code (Low Q_S, Defect-heavy phase)
    # Simulate percolation by removing logical edges (Stabilizer Deficit)
    G_UV = G_IR.copy()
    edges = list(G_UV.edges())
    np.random.seed(42)
    np.random.shuffle(edges)
    
    # Remove 60% of connections
    G_UV.remove_edges_from(edges[:int(0.6 * len(edges))])
    # Keep the largest connected giant component
    G_UV = G_UV.subgraph(max(nx.connected_components(G_UV), key=len)).copy()

    # Diffusion Scale (t)
    t_vals = np.logspace(-1, 1.2, 50) 

    print("Computing Spectral Dimensions...")
    ds_IR = compute_ds(G_IR, t_vals)
    ds_UV = compute_ds(G_UV, t_vals)

    # --- Visualization ---
    plt.figure(figsize=(9, 6))
    plt.plot(t_vals, ds_IR, 'b-', lw=3, label='High $Q_S$ (Stabilized 4D IR)')
    plt.plot(t_vals, ds_UV, 'r--', lw=3, label='Low $Q_S$ (Defect-Heavy UV)')
    
    plt.axhline(4, color='k', linestyle=':', lw=2, label='Macroscopic 4D Limit')
    plt.axhline(2, color='gray', linestyle=':', lw=2, label='UV Quantum Limit (CDT Match)')
    
    plt.xscale('log')
    plt.ylim(0, 4.5)
    plt.title('SQG Dimensionality Flow: Corrected Spectral Dimension $d_s(t)$', fontsize=14, fontweight='bold')
    plt.xlabel('Diffusion Scale $t$ (Random Walk Steps)', fontsize=12)
    plt.ylabel('Effective Spectral Dimension $d_s$', fontsize=12)
    plt.legend(loc='lower right', fontsize=11)
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('spectral_dimension_flow.png', dpi=300)
    print("Saved -> spectral_dimension_flow.png")
    
if __name__ == "__main__":
    # Fallback definition for local function call
    compute_ds = compute_spectral_dimension
    run_simulation()