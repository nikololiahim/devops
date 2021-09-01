# Github Actions Best Practices

1. Keep your Actions minimal
2. Don’t install dependencies unnecessarily
3. Never hardcode secrets
4. Limit environment variables to the narrowest possible scope
5. Ensure every repository contains a CI/CD workflow
6. Store authors in Action metadata to promote code ownership
7. Don’t use self-hosted runners in a public repository

# Jenkins Best Practices

1. Forwarding a Docker socket to Jenkins container to avoid a 'docker-in-docker' situation
