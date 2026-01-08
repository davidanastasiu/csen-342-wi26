# csen-342-wi26
Repository for CSEN 342, Deep Learning, Santa Clara University, Winter 2026

## Preliminaries

I suggest creating a conda environment for examples in this class. All examples in this repo will use the Santa Clara University HPC, so commands are designed to work in that environment. You may need to update paths depending on your current project directory. Use the command below to create and activate the environment, followed by installing some necessary packages.

```bash
module load Anaconda3
conda create --name 342wi26 python=3.9 -y
conda activate 342wi26
conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia -y
python -m pip install matplotlib scipy pandas scikit-learn seaborn jupyter
python -m ipykernel install --user --name 342wi26
```

The last command ads your newly created conda environment to Jupyter so that you can use it from the Jupyter Hub environment. Next time you connect to Jupyter Hub, you will now see a new `342wi26` kernel available for using in jupyter or ipython notebooks. You can thus use this environment both in notebooks and in batch scripts or interactively on the command line.

## Examples

I will be adding notebooks or scripts in the `tutorials` directory to showcase some of the concepts we will discuss in class.
