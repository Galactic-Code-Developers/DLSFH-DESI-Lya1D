#!/usr/bin/env python3
"""Generate Δχ²(Ξ0) from a profiled likelihood scan CSV.

Expected CSV columns:
- one column containing 'Xi0' (e.g. 'Xi0_hMpc2')
- one column containing 'chi2' (e.g. 'chi2_log')

Usage:
  python analysis/make_chi2_plot.py --scan analysis/DESI_allz_profile_chi2_logspace.csv --out figures/chi2_vs_Xi0.pdf
"""
import argparse
import pandas as pd
import matplotlib.pyplot as plt

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--scan", required=True, help="Path to likelihood scan CSV")
    ap.add_argument("--out", required=True, help="Output PDF path")
    args = ap.parse_args()

    df = pd.read_csv(args.scan)

    xi_col = None
    for c in df.columns:
        if "Xi0" in c:
            xi_col = c
            break
    if xi_col is None:
        raise ValueError("Could not find a column containing 'Xi0'.")

    chi_col = None
    for c in df.columns:
        if "chi2" in c.lower():
            chi_col = c
            break
    if chi_col is None:
        raise ValueError("Could not find a column containing 'chi2'.")

    chi2_min = df[chi_col].min()
    df["Delta_chi2"] = df[chi_col] - chi2_min

    plt.figure()
    plt.plot(df[xi_col], df["Delta_chi2"])
    plt.axhline(1.0, linestyle="--")
    plt.axhline(4.0, linestyle="--")
    plt.xlabel(r"$\Xi_0\;[h^{-2}\,\mathrm{Mpc}^2]$")
    plt.ylabel(r"$\Delta\chi^2$")
    plt.title(r"DESI Ly$\alpha$ 1D Constraint on DLSFH Transport")
    plt.tight_layout()
    plt.savefig(args.out)
    plt.close()

if __name__ == "__main__":
    main()
