# KappaBySizes: Student Tutorial

A comprehensive tutorial series for understanding galaxy size distributions and convergence mapping in weak gravitational lensing.

## Overview

This tutorial teaches students how to use galaxy size distributions to determine convergence maps - a key technique in weak gravitational lensing studies. Students will learn to forward model the effects of gravitational lensing on galaxy sizes and develop estimators to recover convergence information from observational data.

## Learning Objectives

By completing this tutorial series, students will understand:

1. **Fundamental Concepts**: What convergence maps represent and how gravitational lensing affects galaxy sizes
2. **Data Generation**: How to create realistic galaxy catalogues using GalSBI
3. **Cosmological Modeling**: How to work with redshift distributions and generate power spectra
4. **Forward Modeling**: How to simulate the effects of convergence on galaxy size distributions
5. **Statistical Analysis**: How to build estimators to recover convergence from size distribution comparisons
6. **Advanced Modeling**: Differences between Gaussian and lognormal models for κ (kappa)

## Tutorial Structure

### Tutorial 1: Basic Concepts (`intro.ipynb`)
- Introduction to convergence maps and weak lensing
- Working with HEALPix maps and healpy functions
- Understanding galaxy size distributions
- Visualizing the effects of gravitational lensing

### Tutorial 2: Galaxy Catalogue Generation (`02_catalogue_generation.ipynb`)
- Using GalSBI to generate realistic galaxy catalogues
- Understanding galaxy properties (positions, redshifts, sizes)
- Working with survey masks and sky coverage

### Tutorial 3: Redshift Distributions (`03_redshift_distributions.ipynb`)
- Extracting and modeling redshift distributions
- Using Gaussian Mixture Models for redshift binning
- Understanding the relationship between redshift and lensing efficiency

### Tutorial 4: Cosmological Power Spectra (`04_power_spectra.ipynb`)
- Setting up cosmological models with pyccl
- Generating convergence power spectra
- Creating convergence maps from power spectra
- Understanding correlation lengths and angular scales

### Tutorial 5: Forward Modeling (`05_forward_modeling.ipynb`)
- Applying convergence effects to galaxy sizes
- Comparing original vs. lensed size distributions
- Understanding the magnification effect: `lensed_size = original_size * (1 + κ)`
- Visualizing the spatial correlation between galaxies and convergence

### Tutorial 6: Building Estimators (`06_estimator_development.ipynb`)
- Developing methods to recover convergence from size distributions
- Comparing local (per-pixel) vs. regional (nearest neighbors) approaches
- Statistical techniques for convergence estimation
- Validation and error analysis

## Prerequisites

Students should have basic knowledge of:
- Python programming
- NumPy and matplotlib
- Basic statistics and probability
- Astronomical coordinate systems
- Elementary understanding of cosmology and general relativity

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/voehl12/KappaBySizes.git
   cd KappaBySizes
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Start Jupyter:
   ```bash
   jupyter notebook
   ```

## Data Files

- `catalogue.npy`: Pre-generated galaxy catalogue for quick start
- `cl_kappa.txt`: Convergence power spectrum data
- Additional data files will be generated as you work through the tutorials

## Key Concepts Covered

### Convergence (κ)
The convergence κ represents the projected density contrast along the line of sight. It affects galaxy sizes through:
```
observed_size = intrinsic_size × (1 + κ)
```

### Size Distributions
Galaxy size distributions provide information about:
- Intrinsic galaxy properties
- Effects of gravitational lensing
- Local matter density (convergence)

### Estimation Strategy
The tutorial develops an estimator based on:
1. Comparing local galaxy size sub-distributions to the global distribution
2. The global distribution remains relatively unchanged by lensing (averaging effect)
3. Local variations reveal convergence information

## Advanced Topics

- Lognormal vs. Gaussian models for convergence
- Non-linear effects in strong lensing regimes  
- Survey systematics and observational effects
- Cross-correlation with other probes

## Further Reading

- Bartelmann & Schneider (2001): "Weak gravitational lensing"
- Kilbinger (2015): "Cosmology with cosmic shear"
- Modern weak lensing surveys: DES, KiDS, HSC, Euclid, LSST

## Contributing

This tutorial is designed for educational purposes. If you find errors or have suggestions for improvements, please open an issue or submit a pull request.

## License

This educational material is provided under an open license for academic and educational use.