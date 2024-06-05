FROM python:3.10
RUN useradd -m jupyter
EXPOSE 8888

RUN apt update && apt install -y lsof

# Install Python requirements
RUN pip install --upgrade --no-cache-dir hatch pip

# Install project requirements
WORKDIR /tmp
RUN wget https://github.com/RuleWorld/bionetgen/releases/download/BioNetGen-2.9.2/BioNetGen-2.9.2-linux.tar.gz && \
    tar -xzf BioNetGen-2.9.2-linux.tar.gz && \
    mv BioNetGen-2.9.2 /usr/local/share/BioNetGen && \
    rm BioNetGen-2.9.2-linux.tar.gz

WORKDIR /opt/stochkit
ENV STOCHKIT_HOME=/opt/stochkit
RUN git clone https://github.com/StochSS/StochKit.git /opt/stochkit
RUN bash ./install.sh
ENV PATH=$PATH:$STOCHKIT_HOME/bin

COPY --chown=1000:1000 . /jupyter/
RUN chown -R 1000:1000 /jupyter
RUN pip install -e /jupyter

# Switch to non-root user. It is crucial for security reasons to not run jupyter as root user!
USER jupyter
WORKDIR /jupyter

# Service
CMD ["python", "-m", "beaker_kernel.server.main", "--ip", "0.0.0.0"]
