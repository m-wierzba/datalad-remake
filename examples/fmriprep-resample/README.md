# Use case: resample a BOLD image onto a target space

This example demonstrates how to run a simple Python [script](https://hub.datalad.org/mslw/fmriprep-resampling) to reproduce fMRIPrep's preprocessed BOLD image (projected onto a target space) from the raw image, ancillary fMRIPrep derivatives, and related metadata. All dependencies for the script are provided by an fMRIPrep singularity container. The singularity container used in this example is `bids-fmriprep--24.1.0` and comes from the [ReproNim containers collection](https://github.com/ReproNim/containers).

The example comprises the following files:
- `fmriprep-resample` template
- `input.txt` input specification
- `output.txt` output specification
- `parameter.txt` parameters

## Requirements

This example requires Singularity.

Please note, that there is no need to install fMRIPrep. The singularity container will be automatically retrieved from the ReproNim containers collection.

## How to install

Install `datalad-remake` extension, as described [here](https://github.com/datalad/datalad-remake/tree/main?tab=readme-ov-file#installation).

## How to use

It is assumed that you have a local copy of the `datalad-remake` project in your `$HOME` directory. If this not the case, adjust the path below:

```
EXAMPLE=$HOME/datalad-remake/examples/fmriprep-resample
```

### Clone example dataset

To run the example, you'll need a raw BIDS dataset that has been minimally preprocessed with fMRIPrep. For a complete list of data dependencies, please refer to [this](https://github.com/datalad/datalad-remake/blob/main/examples/fmriprep-resample/input.txt) specification.

For convenience, a ready-made dataset containing all inputs required for running the example can be obtained like so:

```bash
> cd $HOME
> datalad clone https://hub.datalad.org/example my-project
> cd my-project
> datalad get -n data/ds001734
> datalad get -n derivatives/ds001734
```

The dataset is organized in a modular way. It contains raw BIDS data (`data/ds001734`), as well as fMRIPrep derivative data (`derivatives/ds001734`). Also, it includes the `resample.py` script, as well as the software container that will be needed for running the script (`code/containers`).

The resulting dataset structure is as follows:

```
my-project
├── code
│   ├── containers
│   ├── make
│   └── resample.py
├── data
│   └── ds001734
└── derivatives
    └── ds001734
```

### Configure (or enable) special remote

Configure the dataset in which you want to collect the results of the (re)computation, in this case `derivatives/ds001734` subdataset.

```bash
> cd $HOME/my-project/derivatives/ds001734
```

If you're working with the ready-made example dataset, you are good to go. The `datalad-remake` special remote is already enabled. You can verify that by running:

```bash
> datalad siblings
```

If you're working with your own dataset, make sure to configure a `datalad-remake` special remote:

```bash
> git annex initremote datalad-remake type=external externaltype=datalad-remake \
encryption=none allow-untrusted-execution=true autoenable=true
```

### Add template

Place the `fmriprep-resample` template in the `.datalad/make/methods` of the root dataset:

```bash
> cd $HOME/my-project
> cp $EXAMPLE/fmriprep-resample .datalad/make/methods/fmriprep-resample
> datalad save -m "Add a make method"
```

Place the `input.txt`, `output.txt` and `parameter.txt` files in the root dataset. These files do not have to be tracked in git history, so no `datalad save` is required at this point.

```bash
> mkdir -p code/make/fmriprep-resample
> cp $EXAMPLE/*.txt ./code/make/fmriprep-resample/
```

### Execute (re)computation

To test the example, run:

```bash
> cd $HOME/my-project
> datalad make \
-I code/make/fmriprep-resample/input.txt \
-O code/make/fmriprep-resample/output.txt \
-P code/make/fmriprep-resample/parameter.txt \
--allow-untrusted-execution fmriprep-resample
```