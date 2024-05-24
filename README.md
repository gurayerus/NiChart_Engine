# **NiChart<sup>Engine</sup>** 

A software library designed to calculate **NiChart** pre-trained models and reference distributions from the [NiChart reference dataset](https://neuroimagingchart.com/components/#Reference%20Dataset) [<sup>1</sup>](#f1). **NiChart<sup>Engine</sup>** includes tools for [image processing](https://neuroimagingchart.com/components/#Image%20Processing), [data harmonization](https://neuroimagingchart.com/components/#Harmonization), [machine learning](https://neuroimagingchart.com/components/#Machine%20Learning), and centile calculation. **NiChart<sup>Engine</sup>** utilizes [Snakemake](https://snakemake.github.io) workflows to define multi-step image processing and data analytics pipelines.

![Workflow Diagram](docs/NiChart_Flowchart_Level1A.png)

## Installation

Install **NiChart<sup>Engine</sup>** within a conda environment using the following command:

```console
pip install NiChart_Engine
```

## Usage

Users can apply **NiChart<sup>Engine</sup>** workflows to their data with just a few simple steps:

1. Copy Data: Transfer your data to the designated location within the project directory.
2. Edit Configuration File: Make any necessary adjustments to the configuration file as specified by the package documentation.
3. Run Workflow: Execute the Snakemake workflow to initiate the analysis.

## Contents:

- NiChart_Data:

Workflows for consolidation of initial clinical, demographic and scanner data.

- NiChart_ImageProcessing:

Workflows for application of image processing pipelines (sMRI, DTI and/or fMRI).

- NiChart_MLAnalytics:

Workflows for application of harmonization, machine learning and centile calculation steps to calculate reference models and data distributions.

## Contributing

We welcome contributions from the community! If you have bug fixes, improvements, or new features, please consider creating a pull request. Before submitting a pull request, please:

- Ensure your code adheres to the existing code style and formatting.
- Include clear documentation for your changes.
- Write unit tests for any new functionality.

## License

This project is licensed under the [License Name] license. Please refer to the LICENSE file for the full license text. (Replace [License Name] with the actual license used by your project, such as MIT, Apache, or BSD)


## Contact

For any inquiries, please contact guray.erus@pennmedicine.upenn.edu. (Last Updated: 5/19/2024)

