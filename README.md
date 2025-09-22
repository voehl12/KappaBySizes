# KappaBySizes: Gravitational Lensing and Galaxy Size Distributions Tutorial

An educational tutorial series for students learning about gravitational lensing, kappa mapping, and galaxy size distribution analysis.

## Overview

This repository contains a comprehensive tutorial series designed to teach students the fundamentals of:

1. **Power Spectrum to Kappa Map Generation** - Understanding how cosmic structure power spectra generate gravitational lensing convergence (kappa) maps
2. **Galaxy Catalogues and Lensing** - Working with galaxy catalogues and applying gravitational lensing effects
3. **Size Distribution Analysis** - Comparing galaxy size distributions between small sky patches and full surveys to understand convergence
4. **Redshift Distributions** - Extracting and analyzing redshift distributions from galaxy catalogues

## Tutorial Structure

### Notebook 1: Power Spectrum to Kappa Map Generation
- Introduction to gravitational lensing theory
- Power spectrum fundamentals
- Generating kappa maps from power spectra
- Visualization and interpretation

### Notebook 2: Galaxy Catalogues and Lensing
- Working with galaxy catalogue data
- Applying lensing transformations
- Shape and size modifications due to lensing
- Observational effects

### Notebook 3: Size Distribution Analysis and Convergence
- Galaxy size measurement techniques
- Comparing distributions: small patches vs. full survey
- Statistical convergence analysis
- Bias identification and mitigation

### Notebook 4: Redshift Distributions from Catalogues
- Extracting redshift information from catalogues
- Photometric vs. spectroscopic redshifts
- Creating and analyzing redshift distributions
- Impact on lensing analysis

## Getting Started

### Prerequisites
- Python 3.8+
- Jupyter Notebook or JupyterLab
- Basic knowledge of Python, NumPy, and Matplotlib

### Installation

1. Clone this repository:
```bash
git clone https://github.com/voehl12/KappaBySizes.git
cd KappaBySizes
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Launch Jupyter:
```bash
jupyter notebook
```

4. Start with `01_power_spectrum_to_kappa.ipynb`

## Dependencies

The tutorials use standard scientific Python packages:
- `numpy` - Numerical computations
- `matplotlib` - Plotting and visualization
- `scipy` - Scientific computing utilities
- `astropy` - Astronomical data handling
- `healpy` - HEALPix map operations
- `jupyter` - Interactive notebook environment

## Learning Objectives

By completing these tutorials, students will:

- Understand the theoretical foundation of gravitational lensing
- Know how to generate and manipulate kappa maps from power spectra
- Be able to work with realistic galaxy catalogue data
- Understand statistical challenges in size distribution analysis
- Learn about redshift measurement techniques and their limitations
- Gain practical experience with astronomical data analysis tools

## Contributing

This tutorial series is designed for educational purposes. If you find errors or have suggestions for improvements, please open an issue or submit a pull request.

## License

This educational material is provided under the MIT License for free use in academic and educational contexts.