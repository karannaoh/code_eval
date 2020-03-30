FROM gcc:4.9
WORKDIR /usr/src/
COPY run.sh /usr/run.sh
RUN chmod +x /usr/run.sh
CMD ["/usr/run.sh"]
