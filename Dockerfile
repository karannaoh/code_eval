FROM gcc:4.9
WORKDIR /usr/
COPY run.sh /usr/run.sh
RUN chmod +x /usr/run.sh
CMD ["/usr/run.sh"]
