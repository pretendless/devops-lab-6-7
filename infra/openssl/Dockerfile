FROM ubuntu:latest as build

RUN apt update
RUN apt install -y libpcre3 libpcre3-dev perl zlib1g zlib1g-dev libssl-dev gcc g++ make wget

RUN cd /tmp && \
    wget https://www.openssl.org/source/openssl-3.0.8.tar.gz && \
    tar -xvf openssl-3.0.8.tar.gz && \
    mv ./openssl-3.0.8 ./openssl

WORKDIR /tmp/openssl

RUN ./config -static \
        --prefix=/usr/local/openssl \
	    --openssldir=/usr/local/openssl && \
    make -j24 && \
    make install
RUN strip /usr/local/openssl/bin/openssl


FROM scratch

COPY --from=build /usr/local/openssl /usr/local/openssl
