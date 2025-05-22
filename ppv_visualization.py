

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# === Step 1: Define Fixed Sensitivity ===
SENSITIVITY = 0.99  # Constant for this simulation

# === Step 2: Define prevalence and specificity ranges ===
prevalence_range = np.logspace(-5, np.log10(0.5), 100)  # From 0.001% to 50%
specificity_levels = [0.99, 0.999, 0.9999, 0.99999]  # Increasingly strict tests

# === Step 3: Calculate PPV for each combination ===
results = []

for spec in specificity_levels:
    for prev in prevalence_range:
        # Bayes' Theorem
        p_positive = SENSITIVITY * prev + (1 - spec) * (1 - prev)
        ppv = (SENSITIVITY * prev) / p_positive
        results.append({
            "Prevalence (%)": prev * 100,
            "Specificity": f"{spec:.4f}",
            "PPV (%)": ppv * 100
        })

# Convert results to DataFrame
df = pd.DataFrame(results)

# === Step 4: Plotting the results ===
plt.figure(figsize=(10, 6))
for spec in df["Specificity"].unique():
    df_sub = df[df["Specificity"] == spec]
    plt.plot(df_sub["Prevalence (%)"], df_sub["PPV (%)"], label=f"Specificity: {spec}")

plt.xscale('log')
plt.xlabel("Prevalence (%)")
plt.ylabel("Positive Predictive Value (PPV, %)")
plt.title("PPV vs Prevalence under Varying Specificity (Sensitivity = 99%)")
plt.grid(True, which="both", ls="--", linewidth=0.5)
plt.legend(title="Test Specificity")
plt.tight_layout()
plt.savefig("ppv_plot.png")
plt.show()
