# https://uwekorn.com/2021/03/01/deploying-conda-environments-in-docker-how-to-do-it-right.html
FROM condaforge/miniforge3:4.11.0-0

# https://docs.docker.com/engine/reference/builder/#using-arg-variables
ARG USERNAME

ENV USERNAME=${USERNAME:-"user"}

ARG USERID

ENV USERID=${USERID:-"1000"}

ARG GROUPNAME

ENV GROUPNAME=${GROUPNAME:-"group"}

ARG GROUPID

ENV GROUPID=${GROUPID:-"1000"}

# https://docs.docker.com/engine/reference/builder/#environment-replacement
# RUN echo ${USERNAME} ${GROUPNAME}
# RUN echo ${USERID} ${GROUPID}

# https://stackoverflow.com/questions/67968543/docker-unable-to-find-user-no-matching-entries-in-passwd-file-for-openjdk11
RUN addgroup --system ${GROUPNAME} --gid ${GROUPID}
RUN adduser --system ${USERNAME} -uid ${USERID} --ingroup ${GROUPNAME}

# https://stackoverflow.com/questions/48507140/docker-docker-error-response-from-daemon-linux-spec-user-unable-to-find-user
USER ${USERNAME}:${GROUPNAME}

WORKDIR /usr/jupyter-diagrams

COPY environment.build.yml .

RUN ["conda", "env", "create", "-f", "environment.build.yml"]

# https://stackoverflow.com/questions/55123637/activate-conda-environment-in-docker
SHELL ["conda", "run", "--no-capture-output", "-n", "yfiles_jupyter_graphs_build", "/bin/bash", "-c"]

# https://pythonspeed.com/articles/activate-conda-dockerfile/
CMD  ["conda", "run", "--no-capture-output", "-n", "yfiles_jupyter_graphs_build", "python",  "-m", "build"]
