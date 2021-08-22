# Docker Best Practices

[Don't install unnecessary packages](
https://docs.docker.com/develop/develop-images/dockerfile_best-practices/#dont-install-unnecessary-packages
) - this is why I decided to split `requirements.txt` into `requirements/prod.txt` and `requirements/dev.txt` and use
just `requirements/prod.txt` for the Docker image

[exclude with .dockerinore](
https://docs.docker.com/develop/develop-images/dockerfile_best-practices/#exclude-with-dockerignore
) - in order to minimize build context I created a `.dockerignore` file that excludes all the files that are irrelevant
in production environment

[Minimize the number of layers](
https://docs.docker.com/develop/develop-images/dockerfile_best-practices/#dont-install-unnecessary-packages
) - the previous practice allowed me to reduce the number of `COPY` instructions. Also, running all the command within
one `RUN` instruction allowed me to minimize the number of `RUN` instructions.

# `Dockerfile` linter
I used the linter that comes with [Pycharm](https://www.jetbrains.com/pycharm/).