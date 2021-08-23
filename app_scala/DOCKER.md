# Dockerfile for Scala-Play application

I didn't write the `Dockerfile` manually for the scala application. Instead I used the `sbt-docker-plugin` that
generated the Dockerfile for me. If you run:

```shell
sbt docker:stage
```

then you will be able to see to the Dockerfile produced by this plugin. For now, it looks something like this:

```dockerfile
FROM openjdk:8 as stage0
LABEL snp-multi-stage="intermediate"
LABEL snp-multi-stage-id="6871562c-056f-47ef-9ed7-64019d532eeb"
WORKDIR /opt/docker
COPY opt /opt
USER root
RUN ["chmod", "-R", "u=rwX,g=rwX", "/opt/docker"]
RUN ["chmod", "u+x,g+x", "/opt/docker/bin/app_scala"]

FROM openjdk:8
LABEL MAINTAINER="m.olokin@innopolis.university"
USER root
RUN id -u demiourgos728 1>/dev/null 2>&1 || (( getent group 0 1>/dev/null 2>&1 || ( type groupadd 1>/dev/null 2>&1 && groupadd -g 0 root || addgroup -g 0 -S root )) && ( type useradd 1>/dev/null 2>&1 && useradd --system --create-home --uid 1001 --gid 0 demiourgos728 || adduser -S -u 1001 -G root demiourgos728 ))
WORKDIR /opt/docker
COPY --from=stage0 --chown=demiourgos728:root /opt/docker /opt/docker
EXPOSE 9000
USER 1001:0
ENTRYPOINT ["/opt/docker/bin/app_scala"]
CMD []
```

As you can see, it already adheres to some of the Docker's best practices, like:

- multi-stage builds
- creating a dedicated OS-user for a container
- special labels to provide more information about the image
