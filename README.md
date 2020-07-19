mtDNA sequences are in the `data/34-mammals` directory.  Along with natural mtDNA, there are some randomly synthesized data, prefixed with `randgen`.  There is also a chimera sequence in `random/chimeras`.

This tutorial assumes you are running in a Linux environment. 

To setup the environment, you'll first need to create a virtualenv and install the `python-Levenshtein` library.
```
virtualenv -p python3.8 venv
source venv/bin/activate
pip install -r requirements.txt
```

Now, you can run the `stats.py` script to compare sequences:
```
python code/stats.py data/34-mammals/human data/34-mammals/chimpanzee
# Results
transitions 0.036430037426053365
a<->t 0.0021514629948364886
g<->c 0.0013067400275103163
a<->c|g<->t 0.0020825787758058673
```

To create a random sequence from the nucleotide distribution of a given sequence, you can do the following:
```
python code/randgen.py data/34-mammals/human > data/34-mammals/randgen_human
```
