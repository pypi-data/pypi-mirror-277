FROM quay.io/jupyter/minimal-notebook

USER root

RUN sudo add-apt-repository ppa:ubuntugis/ppa && \
    sudo apt-get update && \
    sudo apt-get install gdal-bin && \
    sudo apt-get install libgdal-dev

RUN sudo apt install graphviz

RUN python -m pip install --upgrade pip

RUN python -m pip install naturf

