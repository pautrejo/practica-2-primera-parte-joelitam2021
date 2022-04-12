FROM palmoreck/kale_certs:0.6.1
USER root

RUN pip install --quiet "git+https://github.com/optimizacion-2-2022-gh-classroom/practica-2-primera-parte-joelitam2021"

VOLUME ["/shared_volume"]

WORKDIR /

ENV NB_PREFIX myurl

ENTRYPOINT ["/usr/local/bin/jupyter", "lab", "--ip=0.0.0.0", "--no-browser", "--allow-root", "--LabApp.allow_origin='*'", "--LabApp.base_url=myurl"]
