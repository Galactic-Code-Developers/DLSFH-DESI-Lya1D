# Analysis

- `DESI_allz_profile_chi2_logspace.csv`
  Profiled likelihood scan output used to generate the Δχ²(Ξ0) curve.
  If you regenerate scans, keep the same column naming convention:
  one column containing `Xi0` and one column containing `chi2`.

- `make_chi2_plot.py`
  Utility to produce `figures/chi2_vs_Xi0.pdf` from the scan CSV.
