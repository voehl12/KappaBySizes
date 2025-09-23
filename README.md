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

### Tutorial 1: Basic Concepts (`01_intro_basic_concepts.ipynb`)
- Introduction to convergence maps and weak lensing theory
- Working with HEALPix maps and healpy functions
- Understanding galaxy size distributions and catalogs
- Forward modeling: applying lensing effects to galaxy sizes
- Visualizing correlations between galaxies and convergence

### Tutorial 2: Galaxy Catalogue Generation (`02_catalogue_generation.ipynb`)
- Using GalSBI to generate realistic galaxy catalogues
- Working with survey masks and sky coverage strategies
- Batch processing for large-scale catalogue generation
- Quality validation and data management best practices
- Understanding galaxy properties and coordinate systems

### Tutorial 3: Redshift Distributions and Cosmology (`03_redshift_distributions.ipynb`)
- Extracting and analyzing redshift distributions from catalogues
- Using Gaussian Mixture Models for redshift binning
- Setting up cosmological models with PyCC
- Computing angular power spectra for different redshift bins
- Understanding lensing efficiency and cross-bin correlations

### Tutorial 4: Power Spectra and Convergence Maps (`04_power_spectra_and_maps.ipynb`)
- Analyzing convergence power spectra and their properties
- Generating Gaussian random convergence fields with healpy
- Implementing lognormal fields for realistic non-Gaussianity
- Comprehensive map validation and quality assessment
- Preparing convergence maps for forward modeling

### Tutorial 5: Forward Modeling and Estimators (`05_forward_modeling_estimators.ipynb`)
- Complete forward modeling pipeline from theory to practice
- Building convergence estimators using statistical approaches
- Implementing pixel-based, nearest-neighbor, and sliding window methods
- Validating estimator performance against true convergence
- Understanding the complete KappaBySizes methodology

### Legacy Files
- `intro.ipynb`: Original introduction notebook (kept for reference)
- `catalogue_gen.ipynb`: Original catalogue generation notebook (content split into new tutorials)

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