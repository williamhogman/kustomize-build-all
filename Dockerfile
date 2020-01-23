FROM lyft/kustomizer:v3.1.0

RUN apk add --update \
        python3

COPY main.py /
ENTRYPOINT ["/main.py"]    
