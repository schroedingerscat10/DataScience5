FROM ubuntu:22.04
LABEL maintainer="Sarah Haeger sarah.haeger@uni-goettingen.de>"

RUN apt-get update 
# Install essential Ubuntu packages
RUN apt-get update && apt-get install -y \
    python3.9 \
    python3-pip

# Install essential Python packages
RUN python3 -m pip --no-cache-dir install \
    pandas \
    jupyter \
    jupyterlab \
    numpy \
    matplotlib \
    seaborn

# Export port for Jupyter Notebook
EXPOSE 8888

WORKDIR /notebooks

# By default start running jupyter notebook
CMD jupyter lab --no-browser --ip 0.0.0.0 --port 8888 --allow-root /notebooks


